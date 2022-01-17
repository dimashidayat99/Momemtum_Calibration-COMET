void RunMacro(std::string macroName, std::string inFilePath, std::string outFilePath) {
  gROOT->SetBatch(1);
  gSystem->Load("$OAEVENTROOT/lib/liboaEvent.so");
  gSystem->Load("$OAGEOMINFOROOT/lib/liboaGeomInfo.so");

  std::string macro;
  macro = macroName+"(\""+inFilePath+"\",\""+outFilePath+"\")";

  TInterpreter::EErrorCode code;
  int ret = gInterpreter->ExecuteMacro(macro.c_str(), &code);
  if (code != 0) {
    std::cerr << "Error: couldn't interpret macro." << std::endl;
    return code;
  }
  return ret;
}
