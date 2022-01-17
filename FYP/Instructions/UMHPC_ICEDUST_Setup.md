# How to build ICEDUST on UMHPC

Before we proceed, please make sure that you have added the SSH key for your UMHPC account to Gitlab.

## Checkout ICEDUST packages

1. Log in to umhpc by replacing `<username>` with your registered account username:

```
ssh -XY <username>@umhpc.dicc.um.edu.my
```

2. Load a recent version of git:
```
module load git/git-2.32.0
```

3. We will be checking out ICEDUST in your `/scratch` space and later build it there. 
Go to your `/scratch/<username>` directory and make the directory where you will 
checkout ICEDUST from Gitlab:

```bash
cd /home/user/$USER
mkdir -p ./comet/icedust/
cd ./comet/icedust/
```

4. Checkout the following repositories from Gitlab:

```bash
git lfs install
git lfs clone --depth 1 git@gitlab.in2p3.fr:comet/ICEDUST_externals_source_LFS.git
git clone git@gitlab.in2p3.fr:comet/ICEDUST_packages.git  
```

Next, we download the `150630_Phase-I_opt` field map as per the instruction in this Gitlab wiki (https://gitlab.in2p3.fr/comet/ICEDUST_packages/-/wikis/FieldMap-Installation):

```bash
mkdir ICEDUST_fieldmaps
cd ICEDUST_fieldmaps
git archive --format=tar.gz --remote=ssh://git@gitlab.in2p3.fr/comet/ICEDUST_fieldmaps.git master -- 150630_Phase-I_opt > fieldmap.tar.gz
tar -xf fieldmap.tar.gz
rm fieldmap.tar.gzc
cd ..
```

## Build ICEDUST with a batch job

Building ICEDUST for the first time can be very time consuming. Rather than login into an interactive node for now, we will a 
submit batch script to SLURM with the instructions for the batch job to follow in order to build ICEDUST. 

1. Make a bash file called `ICEDUSTCompile.sh` and copy (and paste) every line below into the bash file:

```bash
#!/bin/bash -l
 
#SBATCH --partition=cpu-epyc
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err
#SBATCH --mem=16G
#SBATCH --ntasks=8
#SBATCH --nodes=1

#
# setup an env variable which points to icedust directory
#
export ICEDUSTDIR=/home/user/$USER/comet/icedust

#
# load some necessary modules
#
module load git/git-2.32.0
module load cmake/cmake-3.21.0

#
# Build external packages first
#
echo -e "\n"
echo "==============================="
echo "Building External Packages"
echo "==============================="
echo -e "\n"
cd $ICEDUSTDIR
mkdir ext_build
cd ext_build
cmake -DBUILD_ROOT6=ON ../ICEDUST_externals_source_LFS
make -j8

#
# Then build ICEDUST  
#
echo -e "\n"
echo "==============================="
echo "Building ICEDUST"
echo "==============================="
echo -e "\n"
cd $ICEDUSTDIR
mkdir build
cd build
cmake -DBUILD_ROOT6=ON ../ICEDUST_packages
make -j8
make install

echo -e "\n"
echo "ICEDUST Built"
```

2. Change the permission of the bash file by doing the following:

```bash
chmod +x ./ICEDUSTCompile.sh
```

3. Send the batch job:

```
sbatch ICEDUSTCompile.sh
```

4. Check that your batch job is in the batch job queue by typing `squeue`
