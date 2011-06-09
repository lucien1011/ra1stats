from data import data,scaled,excl

class data2011(data) :
    def _fill(self) :
        isExcl =                         (    1,     1,     0,     0,     0,     0,     0,     1)

        self._htBinLowerEdges =          (275.0, 325.0, 375.0, 475.0, 575.0, 675.0, 775.0, 875.0)
        self._htMaxForPlot = 975.0

        self._mergeBins = None
        self._constantMcRatioAfterHere = (    0,     0,     1,     0,     0,     0,     0,     0)
        
        #self._mergeBins =                (    0,     1,     2,     3,     3,     4,     4,     4)
        #self._constantMcRatioAfterHere = (    0,     0,     1,     0,     0)

        self._lumi = {
            "had":     248.,
            "hadBulk": 189.,
            
            "muon":    244., #mu dataset (pt>25)
            "mcMuon":  248.,
            "mcTtw":   248.,
            
            "phot":    164.6,
            "mcPhot":  164.6,
            "mcZinv":  164.6,
            }
        self._htMeans = (     297.51,      347.25,      415.57,  516.2 , 617.17, 717.72, 818.33, 919.08)
        self._observations = {
            "nHadBulk":scaled(( 9.047e+06,   3.793e+06,   2.623e+06,  823968, 289401, 112899,  48118,  65098), self.lumi()["had"]/self.lumi()["hadBulk"]),
            "nHad":      excl((       164,          83,          77,      21,      8,      1,      0,      0), isExcl),
           #"nHad":           (       164,          83,          56,      13,      7,      2,      1,      1), #fix last three bins to SM exp.
            "nPhot":     excl((       142,          57,          43,      12,      2,      2,      2,      0), isExcl),
           #"nMuon":          (       177,          77,          13,      10,      4,      0,      0,      0), #183/pb
            "nMuon":          (        76,          30,          37,      15,      5,      1,      0,      0), #244/pb
            }
        ep = 0.01        
        self._mcExpectations = {
           #"mcMuon":         scaled((198.17,  100.06,   16.78,   4.82,   2.08,   1.13,   0.11, 0.02), self.lumi()["muon"]/self.lumi()["mcMuon"]), #189/pb
            "mcMuon":         scaled(( 81.87,   30.35,   21.44,   6.73,   2.52,   1.48,   0.10, 0.03), self.lumi()["muon"]/self.lumi()["mcMuon"]), #248/pb
           #"mcTtw":          scaled((  74.4,   27.82,   19.26,   7.17,   1.24,   1.05,   0.52, 0.55), self.lumi()["had" ]/self.lumi()["mcTtw" ]), #189/pb
            "mcTtw":          scaled(( 94.94,   34.01,   22.75,   8.48,   1.35,   1.31,   0.62, 0.17), self.lumi()["had" ]/self.lumi()["mcTtw"] ), #248/pb
            "mcPhot":    excl(scaled((   110,      37,      28,      9,      4,    0.8,    0.5,   ep), self.lumi()["phot"]/self.lumi()["mcPhot"]), isExcl),
            "mcZinv":    excl(scaled((    39,      16,      18,      9,    1.7, ep+0.4,    0.4,   ep), self.lumi()["had"] /self.lumi()["mcZinv"]), isExcl),
            }
        self._mcStatError = {
            "mcPhotErr":      scaled((    10,       3,       3,      1,      1,    0.5,    0.4,    1), self.lumi()["phot"]/self.lumi()["mcPhot"]),
            "mcZinvErr":      scaled((     4,       3,       3,      2,    0.9,    0.4,    0.4,    1), self.lumi()["had"] /self.lumi()["mcZinv"]),
            }
        self._fixedParameters = {
            "sigmaLumi":  0.04,
            "sigmaPhotZ": 0.40,
            "sigmaMuonW": 0.30,
            }
        # (3% ECAL, 2.5% vetoes, 2.5% JES and JER + the lumi uncert.) PDF uncertainties we used 10%.
        
class data2010(data) :
    def _fill(self) :
        self._htBinLowerEdges =          (250.0, 300.0, 350.0, 450.0)
        self._mergeBins = None
        self._constantMcRatioAfterHere = (    0,     0,     0,     0)
        self._htMaxForPlot = 600.0
        self._lumi = {
            "had":     35.0,
            "hadBulk": 35.0,
            
            "muon":    35.0,
            "mcMuon":  35.0,
            "mcTtw":   35.0,
            
            "phot":    35.0,
            "mcPhot":  35.0,
            "mcZinv":  35.0,
            }
        self._htMeans = ( 265.0,  315.0,  375.0,  475.0) #place-holder values
        self._observations = {
            "nHadBulk": (844459, 331948, 225649, 110034),
            "nHad":     (    33,     11,      8,      5),
            "nPhot":    (    24,      4,      6,      1),
            "nMuon":    (    13,      5,      5,      2),
            }
        self._mcExpectations = {
            "mcMuon": (  12.2,    5.2,    4.1,    1.9  ),
            "mcTtw":  (  10.5,    4.47,   3.415,  1.692),
            "mcPhot": (  22.4,    7.0,    4.4,    2.1  ),
            "mcZinv": (   8.1,    3.9,    2.586,  1.492),
            }
        self._mcStatError = {}
        self._fixedParameters = {
            "sigmaLumi":  0.04,
            "sigmaPhotZ": 0.40,
            "sigmaMuonW": 0.30,
            }
