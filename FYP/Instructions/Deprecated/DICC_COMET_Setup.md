## How to build ICEDUST using a specific tag

Starting from your own `$HOME` directory, make the following directory:

```bash
mkdir -p icedust_tags/mc5a02
cd icedust_tags/mc5a02
```
then we checkout the following repositories:
```bash
git lfs install
git lfs clone --depth 1 git@gitlab.in2p3.fr:comet/ICEDUST_externals_source_LFS.git
git clone --branch mc5a02 git@gitlab.in2p3.fr:comet/ICEDUST_packages.git  
```
What we had just done here was to clone `ICEDUST_packages` then checkout `mc5a02` tag. Next, we'll build the packages.
We'll start with the external packages needed by ICEDUST first:
```bash
mkdir ext_build
cd ext_build
cmake -DBUILD_ROOT6=ON ../ICEDUST_externals_source_LFS
make -j8
cd $HOME/icedust_tags/mc5a02
```
and then, we build the ICEDUST framework:
```bash
mkdir build
cd build
cmake -DBUILD_ROOT6=ON ../ICEDUST_packages
make -j8
make install
cd $HOME/icedust_tags/mc5a02
```
Next, we download the `150630_Phase-I_opt` fieldd map as like in this wiki (https://gitlab.in2p3.fr/comet/ICEDUST_packages/-/wikis/FieldMap-Installation):

```bash
mkdir ICEDUST_fieldmaps
cd ICEDUST_fieldmaps
git archive --format=tar.gz --remote=ssh://git@gitlab.in2p3.fr/comet/ICEDUST_fieldmaps.git master -- 150630_Phase-I_opt > fieldmap.tar.gz
tar -xf fieldmap.tar.gz
rm fieldmap.tar.gz
cd $HOME/icedust_tags/mc5a02
```

To download this `basic_studies` package,

```bash
cd $HOME/icedust_tags/mc5a02/ICEDUST_install
git clone git@gitlab.in2p3.fr:nurfikri89/basic_studies.git
cd basic_studies
```

then change the path to your work directory in `setupICEDUST_DICC.sh`.

Some relevant links:
- https://gitlab.in2p3.fr/comet/ICEDUST_packages/-/wikis/Tutorial