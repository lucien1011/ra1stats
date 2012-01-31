from inputData import orig,mixedMuons,afterAlphaT,afterAlphaT_b

class selection(object) :
    def __init__(self, name = "", samplesAndSignalEff = {}, data = None, alphaTMinMax = (None, None),
                 universalSystematics = False, universalKQcd = False) :
        for item in ["name", "samplesAndSignalEff", "data", "alphaTMinMax",
                     "universalSystematics", "universalKQcd"] :
            setattr(self, item, eval(item))

class spec(dict) :
    def __init__(self, simpleOneBin = False, qcdSearch = False) :
        self._selections = []
        self.load()

        #for compatibility; to be rewritten
        d = self

        if simpleOneBin :
            assert False
            d["simpleOneBin"] = {"b":3.0}
            key = max(d["alphaT"].keys())
            d["alphaT"] = {key: {"samples": [("had", True)]} }
        else :
            d["simpleOneBin"] = {}
    
        d["selections"] = self.selections()
        d["REwk"] = ["", "Linear", "FallingExp", "Constant"][0]
        d["RQcd"] = ["Zero", "FallingExp", "FallingExpA"][1]
        d["nFZinv"] = ["All", "One", "Two"][2]
        d["qcdSearch"] = qcdSearch
        d["constrainQcdSlope"] = True
    
    def selections(self) :
        return self._selections

    def add(self, sel = None) :
        self._selections.append(sel)

    def load(self) :
        self.add(selection(name = "55",
                           samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                           data = afterAlphaT.data_55_v1(),
                           #universalSystematics = True,
                           #universalKQcd = True,
                           )
                 )
        #self.add(selection(name = "53",
        #                   samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
        #                   data = afterAlphaT.data_53_v1(),
        #                   )
        #         )
        #self.add(selection(name = "52",
        #                   samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
        #                   data = afterAlphaT.data_52_v1(),
        #                   )
        #         )

        #self.add(selection(name = "55b",
        #                   samplesAndSignalEff = {"had":True, "muon":True, "mumu":False},
        #                   data = afterAlphaT_b.data_55_v1(),
        #                   )
        #         )
        #
        #self.add(selection(name = "2010",
        #                   samplesAndSignalEff = {"had":True, "muon":True, "phot":False},
        #                   data = inputData.data2010(),
        #                   )
        #         )