#include "StandardHypoTestInvDemo.cxx"

void cls(RooWorkspace *wspace = 0, int nPoints = 1, double poiMin = 0.0, double poiMax = 0.0, int nToys = 1) {
  RooStats::HypoTestInvTool hypoTestInvTool;
  hypoTestInvTool.SetParameter("PlotHypoTestResult", false);
  hypoTestInvTool.SetParameter("WriteResult", false);
  hypoTestInvTool.SetParameter("Optimize", true);
  hypoTestInvTool.SetParameter("UseVectorStore", true);
  hypoTestInvTool.SetParameter("GenerateBinned", false);
  hypoTestInvTool.SetParameter("UseProof", false);
  hypoTestInvTool.SetParameter("Rebuild", false);
  hypoTestInvTool.SetParameter("NWorkers", 1);
  hypoTestInvTool.SetParameter("NToyToRebuild", 100);
  hypoTestInvTool.SetParameter("PrintLevel", 0);
  hypoTestInvTool.SetParameter("InitialFit", -1);
  hypoTestInvTool.SetParameter("RandomSeed", -1);
  hypoTestInvTool.SetParameter("NToysRatio", 2);
  hypoTestInvTool.SetParameter("MaxPOI", -1.0);
  hypoTestInvTool.SetParameter("MassValue", "");
  hypoTestInvTool.SetParameter("MinimizerType", "");
  hypoTestInvTool.SetParameter("ResultFileName", "");

  RooStats::HypoTestInverterResult* result;
  result = hypoTestInvTool.RunInverter(wspace, //RooWorkspace * w,
				       "modelConfig", "", //const char * modelSBName, const char * modelBName,
				       "dataName", 0, 3, //const char * dataName, int type,  int testStatType,
				       true, nPoints, poiMin, poiMax, //bool useCLs, int npoints, double poimin, double poimax,
				       nToys, //int ntoys,
				       true, //bool useNumberCounting = false,
				       ""); //const char * nuisPriorName = 0);
  
  hypoTestInvTool.AnalyzeResult( result, 0, 3, true, nPoints, "lulz.root" );
}

int drive(char* fileName) {
  TFile f(fileName);
  RooWorkspace *wspace = (RooWorkspace*)f.Get("Workspace");
  cls(wspace, 2, 0.0, 3.0, 5);
  f.Close();
  return 0;
}

int main(int argc, char** argv) {
  if (argc<2) {
    std::cout << "Usage: " << argv[0] << " root-file" << std::endl;
    return 1;
  }
  return drive(argv[1]);
}
