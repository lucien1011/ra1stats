from inputData import orig,mixedMuons,afterAlphaT,afterAlphaT_b,mixedMuons_b,mixedMuons_b_sets,mixedMuons_b_sets_aT

class selection(object) :
    '''Each key appearing in samplesAndSignalEff is used in the likelihood;
    the corresponding value determines whether signal efficiency is considered for that sample.'''

    def __init__(self, name = "", note = "", samplesAndSignalEff = {}, data = None,
                 alphaTMinMax = (None, None), nbTag = None, bTagLower = None,
                 fZinvIni = 0.5, AQcdIni = 1.0e-2, zeroQcd = False,
                 universalSystematics = False, universalKQcd = False) :
        for item in ["name", "note", "samplesAndSignalEff", "data",
                     "alphaTMinMax","nbTag", "bTagLower",
                     "fZinvIni", "AQcdIni", "zeroQcd",
                     "universalSystematics", "universalKQcd"] :
            setattr(self, item, eval(item))

def alphaT_slices(systMode = 1) :
    selections = [
        selection(name = "55",
                  note = "#alpha_{T}>0.55",
                  alphaTMinMax = ("55", None),
                  samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                  data = afterAlphaT.data_55_v1( systMode = systMode ),
                  universalSystematics = True,
                  universalKQcd = True,
        ),
        selection(name = "53",
                  note = "0.53<#alpha_{T}<0.55",
                  alphaTMinMax = ("53", "55"),
                  samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                  data = afterAlphaT.data_53_v1( systMode = systMode ),
        ),
        selection(name = "52",
                  note = "0.52<#alpha_{T}<0.53",
                  alphaTMinMax = ("52", "53"),
                  samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                  data = afterAlphaT.data_52_v1( systMode = systMode ),
        ),
    ]
    return selections
 
def btag(systMode = 1) :
    selections = selection(name = "55b_mixed",
                           note = "#geq1 b-tag",
                           alphaTMinMax = ("55", None),
                           samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                           data = mixedMuons_b.data_55_v1( systMode = systMode ),
                           bTagLower = "0",
                           universalSystematics = True,
                           universalKQcd = True,
                          )
    return selections

def alphaT_0btags(systMode = 1) :
    selections = selection(name = "55_0b",
                           note = "0 b-tags (w/ #alpha_{T})",
                           alphaTMinMax = ("55", None),
                           samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                           data = mixedMuons_b_sets_aT.data_55_0btag( systMode = systMode ),
                           nbTag = "0",
                           universalSystematics = True,
                           universalKQcd = True,
                          )
    return selections

def noAlphaT_0btags(systMode = 1) :
    selections = selection(name = "55_0b",
                           note = "0 b-tags",
                           alphaTMinMax = ("55", None),
                           samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                           data = mixedMuons_b_sets.data_55_0btag( systMode = systMode ),
                           nbTag = "0",
                           universalSystematics = True,
                           universalKQcd = True,
                          )
    return selections

def btags_1_2_gt2(systMode = 1) :
    selections = [
        selection(name = "55_1b",
                  note = "1 b-tag",
                  alphaTMinMax = ("55", None),
                  samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                  data = mixedMuons_b_sets.data_55_1btag( systMode = systMode ),
                  nbTag = "1",
                  fZinvIni = 0.25,
                  AQcdIni = 0.0,
        ),
        selection(name = "55_2b",
                  note = "2 b-tags",
                  alphaTMinMax = ("55", None),
                  samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                  data = mixedMuons_b_sets.data_55_2btag( systMode = systMode ),
                  nbTag = "2",
                  fZinvIni = 0.1,
                  AQcdIni = 0.0,
        ),
        selection(name = "55_gt2b",
                  note = "#geq3 b-tags",
                  alphaTMinMax = ("55", None),
                  #samplesAndSignalEff = {"had":True, "muon":True, "phot":False, "mumu":False},
                  samplesAndSignalEff = {"had":True, "muon":True, "mumu":False},
                  data = mixedMuons_b_sets.data_55_gt2btag( systMode = systMode ),
                  bTagLower = "2",
                  fZinvIni = 0.1,
                  AQcdIni = 0.0,
        )
    ]

    return selections
