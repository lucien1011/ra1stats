import common

def scaled(t, factor) :
    return tuple([factor*item for item in t])

simple = common.signal(xs = 1.0, label = "signal")
simple.insert("test", {
        "effSimple": (1.0, ),
        })

t1_1 = common.signal(xs = 0.0243547, label = "T1 m_{gl} = 1.0 TeV; m_{LSP} = 0.4 TeV (xs = 24 fb)")
t1_1.insert("0b_ge4j", {"effHad":[0.000000, 0.000200, 0.000800, 0.005200, 0.013100, 0.024600, 0.032000, 0.065700],})
t1_1.insert("0b_le3j", {"effHad":[0.000600, 0.000800, 0.002100, 0.004000, 0.007800, 0.010700, 0.007300, 0.008000],})
t1_1.insert("1b_ge4j", {"effHad":[0.000100, 0.000000, 0.000000, 0.001100, 0.001100, 0.002200, 0.003200, 0.006000],})
t1_1.insert("1b_le3j", {"effHad":[0.000000, 0.000000, 0.000200, 0.000300, 0.000700, 0.000400, 0.000200, 0.000100],})
t1_1.insert("2b_ge4j", {"effHad":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000200, 0.000400],})
t1_1.insert("2b_le3j", {"effHad":[0.000000, 0.000000, 0.000000, 0.000000, 0.000100, 0.000000, 0.000000, 0.000000],})
t1_1.insert("3b_ge4j", {"effHad":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],})
t1_1.insert("3b_le3j", {"effHad":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],})
t1_1.insert("ge4b_ge4j",{"effHad":[0.000000, 0.000000, 0.000000],})

t1bbbb_1 = common.signal(xs = 0.0101744, label = "T1bbbb m_{gl} = 1.1 TeV; m_{LSP} = 0.5 TeV (xs = 10 fb)")
t1bbbb_1.insert("0b_ge4j", {"effHad" :[0.000000, 0.000000, 0.000000, 0.000200, 0.000300, 0.001000, 0.000400, 0.001400],
                            "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]})
t1bbbb_1.insert("0b_le3j", {"effHad" :[0.000000, 0.000100, 0.000300, 0.000300, 0.000800, 0.000600, 0.000200, 0.000500],
                            "effMuon":[0.000000, 0.000000, 0.000100, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]})
t1bbbb_1.insert("1b_ge4j", {"effHad" :[0.000000, 0.000000, 0.000500, 0.000600, 0.002700, 0.003700, 0.004200, 0.010000],
                            "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]})
t1bbbb_1.insert("1b_le3j", {"effHad" :[0.000300, 0.000800, 0.001900, 0.002200, 0.003200, 0.002600, 0.002100, 0.001800],
                            "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]})
t1bbbb_1.insert("2b_ge4j", {"effHad" :[0.000000, 0.000100, 0.000400, 0.002800, 0.007300, 0.010900, 0.010000, 0.019000],
                            "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]})
t1bbbb_1.insert("2b_le3j", {"effHad" :[0.000100, 0.000300, 0.001800, 0.004100, 0.005700, 0.004900, 0.003200, 0.004400],
                            "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]})
t1bbbb_1.insert("3b_ge4j", {"effHad" :[0.000000, 0.000100, 0.000600, 0.002500, 0.006800, 0.011200, 0.010100, 0.021400],
                            "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]})
t1bbbb_1.insert("3b_le3j", {"effHad" :[0.000000, 0.000200, 0.001200, 0.002300, 0.003800, 0.002800, 0.002200, 0.002000],
                            "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]})
t1bbbb_1.insert("ge4b_ge4j",{"effHad":[0.000000, 0.000000, 0.017600],
                             "effMuon":[0.000000, 0.000000, 0.000000]})

t2bb_2 = common.signal(xs = 0.0486, label = ["#lower[0.35]{#splitline{SM + SUSY Model D}{(m_{sbottom} = 500 GeV, m_{LSP} = 150 GeV)}}",
                                             "T2bb m_{sbottom} = 500 GeV; m_{LSP} = 150 GeV (xs = 49 fb)"][0])
t2bb_2.insert("55_0b", {
        "effHad": [0.003599, 0.004056, 0.007274, 0.004042, 0.002711, 0.000908, 0.000688, 0.000195],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t2bb_2.insert("55_1b", {
        "effHad": [0.013004, 0.017577, 0.029381, 0.019993, 0.008749, 0.003636, 0.001679, 0.001369],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t2bb_2.insert("55_2b", {
        "effHad": [0.013788, 0.017518, 0.032410, 0.019653, 0.007640, 0.004892, 0.001398, 0.001219],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t2bb_2.insert("55_gt2b", {
        "effHad": [0.000000, 0.000123, 0.000618, 0.001586, 0.001702, 0.000179, 0.000156, 0.000228],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })

t1 = common.signal(xs = 0.0651, label = ["#lower[0.35]{#splitline{SM + SUSY Model A}{(m_{gluino} = 800 GeV, m_{LSP} = 200 GeV)}}",
                                         "T1 m_{gluino} = 800 GeV; m_{LSP} = 200 GeV (xs = 65 fb)"][0])
t1.insert("55_0b", {
    "effHad": [0.000200, 0.001200, 0.005500, 0.013000, 0.028600, 0.040800, 0.035300, 0.040400],
    })
t1.insert("55_1b", {
    "effHad": [0.000000, 0.000000, 0.000200, 0.000800, 0.001000, 0.001900, 0.002200, 0.002700],
    })
t1.insert("55_2b", {
    "effHad": [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000300],
    })
t1.insert("55_gt2b", {
    "effHad": [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000100, 0.000000, 0.000000],
    })

t1tttt_2012 = common.signal(xs=0.0243547, label="T1tttt m_{gluino} = 1000 GeV; m_{LSP} = 200GeV (xs = 24 fb)")
t1tttt_2012.insert( "55_0b", {
        "effHad": [0.000000, 0.000000, 0.000082, 0.000439, 0.000505, 0.000805, 0.000505, 0.001351],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t1tttt_2012.insert( "55_1b", {
        "effHad": [0.000000, 0.000101, 0.000223, 0.001161, 0.001688, 0.003061, 0.002830, 0.006204],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t1tttt_2012.insert( "55_2b", {
        "effHad": [0.000000, 0.000037, 0.000418, 0.001075, 0.002313, 0.003854, 0.004511, 0.010442],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t1tttt_2012.insert( "55_gt2b", {
        "effHad": [0.000000, 0.000000, 0.000155, 0.000893, 0.002082, 0.002905, 0.005776, 0.014815],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })

ttch = "t#bar{t} #tilde{#chi}^{0}"
t1ttttLabel = "#tilde{g}#tilde{g} #rightarrow %s %s"%(ttch, ttch)
t1tttt_2012_2 = common.signal(xs=0.157399, label = "#lower[0.35]{#splitline{SM + SUSY  ( %s )}{(m_{gluino} = 800 GeV, m_{LSP} = 100 GeV)}}"%t1ttttLabel)
t1tttt_2012_2.insert( "55_0b", {
        "effHad": [0.000040, 0.000000, 0.000189, 0.000429, 0.001074, 0.000405, 0.000323, 0.000367],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t1tttt_2012_2.insert( "55_1b", {
        "effHad": [0.000121, 0.000224, 0.000694, 0.001554, 0.002514, 0.002789, 0.001555, 0.001644],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t1tttt_2012_2.insert( "55_2b", {
        "effHad": [0.000119, 0.000131, 0.000575, 0.001417, 0.003898, 0.003822, 0.003127, 0.003162],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t1tttt_2012_2.insert( "55_gt2b", {
        "effHad": [0.000000, 0.000000, 0.000165, 0.001438, 0.002540, 0.003726, 0.003030, 0.003359],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })

t1tttt_2012_23 = common.signal(xs=0.157399, label = "#lower[0.35]{#splitline{SM + SUSY  ( %s )}{(m_{gluino} = 800 GeV, m_{LSP} = 100 GeV)}}"%t1ttttLabel)
t1tttt_2012_23.insert( "55_0b", {
        "effHad": [0.000040, 0.000000, 0.000189, 0.000429, 0.001074, 0.000405, 0.000323, 0.000367],
        "effMuon":[0.000050, 0.000000, 0.000150, 0.000200, 0.000200, 0.000150, 0.000150, 0.000150],
        })
t1tttt_2012_23.insert( "55_1b", {
        "effHad": [0.000121, 0.000224, 0.000694, 0.001554, 0.002514, 0.002789, 0.001555, 0.001644],
        "effMuon":[0.000200, 0.000150, 0.000450, 0.000800, 0.001050, 0.000650, 0.000550, 0.000450],
        })
t1tttt_2012_23.insert( "55_2b", {
        "effHad": [0.000119, 0.000131, 0.000575, 0.001417, 0.003898, 0.003822, 0.003127, 0.003162],
        "effMuon":[0.000000, 0.000100, 0.000400, 0.001100, 0.001550, 0.001500, 0.000600, 0.000900],
        })
t1tttt_2012_23.insert( "55_gt2b", {
        "effHad": [0.000000, 0.000000, 0.000165, 0.001438, 0.002540, 0.003726, 0.003030, 0.003359],
        "effMuon":[0.000000, 0.000000, 0.000100, 0.000450, 0.000900, 0.001000, 0.000500, 0.001150],
        })

t1tttt_2012_3 = common.signal(xs=0.157399, label = "#lower[0.35]{#splitline{SM + SUSY  ( %s )}{(m_{gluino} = 800 GeV, m_{LSP} = 100 GeV)}}"%t1ttttLabel)
t1tttt_2012_3.insert( "55_0b", {
        "effHad": [0.000000, 0.000000, 0.000250, 0.000350, 0.001050, 0.000400, 0.000350, 0.000400],
        "effMuon":[0.000050, 0.000000, 0.000150, 0.000200, 0.000200, 0.000150, 0.000150, 0.000150],
        })
t1tttt_2012_3.insert( "55_1b", {
        "effHad": [0.000150, 0.000200, 0.000900, 0.001550, 0.002350, 0.003250, 0.001750, 0.001900],
        "effMuon":[0.000200, 0.000150, 0.000450, 0.000800, 0.001050, 0.000650, 0.000550, 0.000450],
        })
t1tttt_2012_3.insert( "55_2b", {
        "effHad": [0.000200, 0.000150, 0.000550, 0.001750, 0.004250, 0.004000, 0.002950, 0.003300],
        "effMuon":[0.000000, 0.000100, 0.000400, 0.001100, 0.001550, 0.001500, 0.000600, 0.000900],
        })
t1tttt_2012_3.insert( "55_gt2b", {
        "effHad": [0.000000, 0.000000, 0.000200, 0.001150, 0.002450, 0.003450, 0.002650, 0.003250],
        "effMuon":[0.000000, 0.000000, 0.000100, 0.000450, 0.000900, 0.001000, 0.000500, 0.001150],
        })
