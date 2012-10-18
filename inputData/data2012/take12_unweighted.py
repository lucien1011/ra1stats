from data import data
import utils

def common1(x) :
    x._lumi = {
        "mumu"  : 1.139e+04,
        "muon"  : 1.139e+04,
        "mcPhot": 1.157e+04,
        "phot"  : 1.157e+04,
        "mcHad" : 5.125e+03,
        "had"   : 5.125e+03,
        "mcMuon": 1.139e+04,
        "mcMumu": 1.139e+04,
	}

    x._triggerEfficiencies = {
        "hadBulk":       (1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000),
        "had":           (0.870, 0.986, 0.994, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000),
        "muon":          (0.880, 0.880, 0.880, 0.880, 0.880, 0.880, 0.880, 0.880, 0.880, 0.880),
        "phot":          (1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000),
        "mumu":          (0.950, 0.960, 0.960, 0.970, 0.970, 0.970, 0.980, 0.980, 0.980, 0.980),
        }

    x._htBinLowerEdges = ( 275.0, 325.0, 375.0, 475.0, 575.0, 675.0, 775.0, 875.0, 975.0, 1.075e+03, )
    x._htMaxForPlot    = 1.175e+03
    x._htMeans         = ( 298.0, 348.0, 416.0, 517.0, 617.0, 719.0, 819.0, 1044.,   0.0,       0.0, )

    x._observations["nPhot"] = tuple([None, None]+list(x._observations["nPhot"][2:]))

    uncs = {"btagUncert": 0.035, "lumi": 0.06, "deadEcal": 0.03, "lepVetoes": 0.025, "jesjer": 0.025, "pdf": 0.10} # SMS other than T1, T2
    uncs["btagUncert"] = 0.12 #T1, T2, cMSSM tb10 only
    return utils.quadSum(uncs.values())

def common(x) :
    lumiLikeValue = common1(x)

    systBins = tuple([0]*4+[1]*2+[2]*2)
    name = x.__class__.__name__
    if "ge2j" in name :
        systMagnitudes = (0.10, 0.20, 0.60)
        x._observations["nHadBulk"] = (630453600, 286166200, 209611400, 69777150, 26101500, 20182300, 4745175, 4776350, 0, 0)
    elif "le3j" in name :
        systMagnitudes = (0.15, 0.30, 0.50)
        x._observations["nHadBulk"] = (487992800, 202369400, 134976100, 36965375, 12292400,  8301900, 1925125, 1768325, 0, 0)
    elif "ge4j" in name :
        systMagnitudes = (0.25, 0.35, 0.70)
        x._observations["nHadBulk"] = (142460800,  83796800,  74635300, 32811775, 13809100, 11880400, 2820050, 3008025, 0, 0)

    if "ge4b" in name :
        x._mergeBins = (0, 1, 2, 2, 2, 2, 2, 2, 2, 2)
        systMagnitudes = (0.25,)
        systBins = (0, 0, 0)
    else :
        if "0b" in name :
            x._mergeBins = (0, 1, 2, 3, 4, 5, 6, 7, 7, 7)
        else :
            x._mergeBins = (0, 1, 2, 3, 4, 5, 6, 7, 7, 7)
            #x._mergeBins = (0, 1, 2, 3, 4, 5, 6, 6, 6, 6)
            #systBins = tuple([0]*4+[1]*2+[2]*1)

    x._systBins = {
        "sigmaLumiLike": [0]*len(systBins),
        "sigmaPhotZ": systBins,
        "sigmaMuonW": systBins,
        "sigmaMumuZ": systBins,
        }

    x._fixedParameters = {
        "sigmaLumiLike": tuple([lumiLikeValue]*1),
        "sigmaPhotZ": systMagnitudes,
        "sigmaMuonW": systMagnitudes,
        "sigmaMumuZ": systMagnitudes,
        "k_qcd_nom":2.96e-2,
        "k_qcd_unc_inp":utils.quadSum([0.61e-2, 0.463e-2])
        }

class data_0b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 287.0, 198.2, 109.8, 51.44, 26.24, 10.82, 5.717, 4.442, ) ,
		"mcHad"              :   ( 504.2, 200.2, 159.9, 105.1, 48.87, 24.15, 10.57, 4.517, 2.003, 2.277, ) ,
		"mcTtw"              :   ( 312.6, 124.5, 102.9, 65.06, 28.65, 14.3, 5.7, 2.786, 1.113, 1.193, ) ,
		"mcMuon"             :   ( 1.478e+03, 756.6, 829.8, 640.5, 347.1, 183.3, 98.0, 55.17, 30.01, 44.02, ) ,
		"mcZinv"             :   ( 191.6, 75.73, 57.0, 40.08, 20.22, 9.849, 4.869, 1.731, 0.8908, 1.083, ) ,
		"mcMumu"             :   ( 130.7, 63.71, 52.44, 48.36, 35.13, 21.94, 11.18, 2.253, 1.407, 6.046, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 34.01, 11.84, 19.89, 9.06, 6.881, 4.873, 3.754, 2.585, 2.2, 2.512, ) ,
		"mcMumuErr"          :   ( 10.9, 7.593, 6.804, 6.555, 5.629, 4.473, 3.21, 1.394, 0.9359, 2.348, ) ,
		"mcHadErr"           :   ( 16.03, 3.677, 2.9, 2.231, 1.427, 1.104, 0.6652, 0.447, 0.2783, 0.2999, ) ,
		"mcZinvErr"          :   ( 2.786, 1.688, 1.299, 0.9754, 0.686, 0.4805, 0.3359, 0.1998, 0.1436, 0.1568, ) ,
		"mcTtwErr"           :   ( 15.79, 3.267, 2.593, 2.007, 1.251, 0.9944, 0.5741, 0.3998, 0.2384, 0.2556, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 14.59, 11.42, 8.382, 5.749, 4.1, 2.627, 1.907, 1.679, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 308.0, 213.0, 99.0, 50.0, 24.0, 11.0, 3.0, 3.0, ) ,
		"nHad"               :   ( 441.0, 218.0, 171.0, 113.0, 57.0, 25.0, 5.0, 4.0, 6.0, 4.0, ) ,
		"nMuon"              :   ( 1.383e+03, 644.0, 636.0, 444.0, 260.0, 147.0, 59.0, 34.0, 18.0, 36.0, ) ,
		"nMumu"              :   ( 126.0, 46.0, 55.0, 56.0, 32.0, 11.0, 7.0, 4.0, 2.0, 2.0, ) ,
	}

        common(self)


class data_0b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 2.55e+03, 869.7, 288.4, 112.4, 42.58, 21.5, 4.801, 5.433, ) ,
		"mcHad"              :   ( 2.689e+03, 1.223e+03, 878.1, 266.1, 89.61, 31.07, 12.68, 5.537, 2.048, 2.241, ) ,
		"mcTtw"              :   ( 1.295e+03, 587.4, 428.5, 122.4, 37.39, 11.8, 5.379, 2.392, 0.5302, 0.9371, ) ,
		"mcMuon"             :   ( 1.075e+04, 5.991e+03, 5.743e+03, 2.386e+03, 1.019e+03, 476.9, 249.7, 132.0, 65.06, 103.6, ) ,
		"mcZinv"             :   ( 1.393e+03, 636.0, 449.6, 143.7, 52.22, 19.27, 7.299, 3.145, 1.518, 1.304, ) ,
		"mcMumu"             :   ( 1.194e+03, 707.8, 664.8, 264.3, 124.5, 55.81, 27.31, 11.47, 6.592, 11.46, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 86.08, 37.79, 33.27, 20.1, 13.3, 9.081, 6.507, 4.67, 3.138, 4.057, ) ,
		"mcMumuErr"          :   ( 34.29, 26.38, 25.58, 16.13, 11.1, 7.444, 5.258, 3.371, 2.415, 3.404, ) ,
		"mcHadErr"           :   ( 22.72, 9.174, 7.017, 3.488, 1.96, 1.132, 0.7428, 0.496, 0.2728, 0.314, ) ,
		"mcZinvErr"          :   ( 7.44, 4.893, 3.643, 1.894, 1.139, 0.6937, 0.4265, 0.2799, 0.1938, 0.1796, ) ,
		"mcTtwErr"           :   ( 21.47, 7.76, 5.997, 2.929, 1.596, 0.8945, 0.6081, 0.4095, 0.192, 0.2576, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 44.08, 24.46, 14.05, 8.796, 5.385, 3.821, 1.815, 1.921, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 2.601e+03, 854.0, 252.0, 94.0, 35.0, 11.0, 6.0, 4.0, ) ,
		"nHad"               :   ( 2.855e+03, 1.296e+03, 878.0, 241.0, 71.0, 25.0, 4.0, 8.0, 5.0, 2.0, ) ,
		"nMuon"              :   ( 9.698e+03, 5.039e+03, 4.653e+03, 1.808e+03, 779.0, 294.0, 150.0, 77.0, 55.0, 61.0, ) ,
		"nMumu"              :   ( 1.336e+03, 708.0, 623.0, 205.0, 120.0, 44.0, 21.0, 14.0, 6.0, 6.0, ) ,
	}

        common(self)


class data_1b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 50.95, 34.16, 21.13, 9.445, 4.545, 1.929, 1.033, 0.8108, ) ,
		"mcHad"              :   ( 275.8, 110.4, 88.97, 52.01, 22.22, 8.893, 3.68, 1.749, 0.8972, 0.8048, ) ,
		"mcTtw"              :   ( 241.3, 96.7, 78.26, 44.35, 18.35, 7.111, 2.738, 1.402, 0.7297, 0.5833, ) ,
		"mcMuon"             :   ( 1.433e+03, 755.2, 809.5, 586.4, 302.0, 146.2, 74.54, 40.36, 21.4, 27.0, ) ,
		"mcZinv"             :   ( 34.5, 13.73, 10.71, 7.655, 3.871, 1.782, 0.942, 0.3468, 0.1675, 0.2215, ) ,
		"mcMumu"             :   ( 33.49, 15.27, 16.48, 14.31, 8.747, 4.695, 2.179, 0.6469, 0.8849, 1.144, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 18.64, 13.75, 14.88, 13.57, 10.08, 7.221, 5.171, 3.653, 2.791, 3.152, ) ,
		"mcMumuErr"          :   ( 4.453, 1.525, 2.56, 1.756, 1.979, 0.7309, 0.5927, 0.4159, 0.5637, 0.3362, ) ,
		"mcHadErr"           :   ( 5.72, 3.659, 3.391, 2.615, 1.727, 1.006, 0.6471, 0.4347, 0.3239, 0.2598, ) ,
		"mcZinvErr"          :   ( 1.037, 0.6266, 0.4959, 0.3547, 0.2123, 0.1232, 0.1042, 0.05962, 0.05666, 0.04819, ) ,
		"mcTtwErr"           :   ( 5.626, 3.605, 3.354, 2.59, 1.714, 0.9987, 0.6387, 0.4305, 0.3189, 0.2553, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 4.248, 2.52, 1.955, 1.594, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 57.0, 45.0, 16.0, 12.0, 10.0, 1.0, 1.0, 1.0, ) ,
		"nHad"               :   ( 229.0, 91.0, 84.0, 26.0, 26.0, 4.0, 5.0, 3.0, 1.0, 0.0, ) ,
		"nMuon"              :   ( 1.373e+03, 612.0, 592.0, 444.0, 203.0, 108.0, 55.0, 17.0, 10.0, 21.0, ) ,
		"nMumu"              :   ( 31.0, 14.0, 21.0, 15.0, 11.0, 3.0, 2.0, 4.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_1b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 272.6, 94.37, 33.84, 12.07, 5.463, 2.646, 0.4952, 0.6155, ) ,
		"mcHad"              :   ( 497.9, 225.0, 158.7, 43.14, 13.57, 4.276, 1.577, 0.6265, 0.2571, 0.2584, ) ,
		"mcTtw"              :   ( 338.2, 151.9, 107.0, 26.18, 7.407, 2.096, 0.7479, 0.2835, 0.06286, 0.1068, ) ,
		"mcMuon"             :   ( 2.693e+03, 1.548e+03, 1.415e+03, 500.2, 195.4, 82.41, 38.65, 18.87, 12.33, 14.01, ) ,
		"mcZinv"             :   ( 159.7, 73.16, 51.72, 16.96, 6.165, 2.181, 0.8291, 0.343, 0.1943, 0.1516, ) ,
		"mcMumu"             :   ( 165.6, 96.14, 91.77, 34.02, 16.39, 6.04, 2.219, 1.146, 1.425, 0.8857, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 17.02, 13.02, 12.28, 6.811, 4.078, 2.508, 1.866, 1.219, 0.7744, 0.9319, ) ,
		"mcMumuErr"          :   ( 6.475, 4.443, 4.562, 2.051, 1.834, 1.27, 0.1736, 0.1585, 0.3353, 0.1204, ) ,
		"mcHadErr"           :   ( 4.58, 3.028, 2.461, 1.103, 0.5276, 0.2848, 0.1235, 0.07244, 0.0177, 0.02619, ) ,
		"mcZinvErr"          :   ( 1.401, 0.8671, 0.6383, 0.3159, 0.1735, 0.1085, 0.0596, 0.03949, 0.01727, 0.02619, ) ,
		"mcTtwErr"           :   ( 4.36, 2.901, 2.377, 1.057, 0.4983, 0.2633, 0.1082, 0.06073, 0.003859, 0.0, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 6.703, 2.65, 2.054, 0.6512, 0.9722, 0.7683, 0.0, 0.0, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 307.0, 101.0, 27.0, 9.0, 5.0, 2.0, 1.0, 0.0, ) ,
		"nHad"               :   ( 509.0, 213.0, 153.0, 42.0, 9.0, 4.0, 1.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 2.662e+03, 1.434e+03, 1.223e+03, 413.0, 154.0, 51.0, 27.0, 12.0, 7.0, 7.0, ) ,
		"nMumu"              :   ( 184.0, 99.0, 102.0, 42.0, 18.0, 6.0, 2.0, 4.0, 0.0, 1.0, ) ,
	}

        common(self)


class data_2b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 7.229, 3.461, 3.198, 1.255, 0.32, 0.141, 0.0778, 0.05818, ) ,
		"mcHad"              :   ( 122.7, 48.61, 39.04, 22.25, 9.169, 3.607, 1.184, 0.7253, 0.3462, 0.2539, ) ,
		"mcTtw"              :   ( 117.8, 46.79, 37.33, 21.21, 8.712, 3.385, 1.07, 0.6816, 0.3301, 0.2354, ) ,
		"mcMuon"             :   ( 934.5, 490.8, 513.5, 363.1, 187.3, 84.57, 41.2, 22.98, 10.94, 13.39, ) ,
		"mcZinv"             :   ( 4.927, 1.813, 1.705, 1.036, 0.4572, 0.222, 0.1145, 0.04378, 0.0161, 0.01854, ) ,
		"mcMumu"             :   ( 12.47, 5.383, 8.014, 6.438, 3.102, 1.315, 0.4191, 0.2822, 0.4589, 0.1559, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 9.982, 7.275, 7.291, 6.082, 4.368, 2.852, 1.983, 1.507, 1.02, 1.086, ) ,
		"mcMumuErr"          :   ( 2.044, 1.526, 1.827, 1.716, 0.8576, 0.3178, 0.1655, 0.141, 0.6031, 0.1081, ) ,
		"mcHadErr"           :   ( 2.228, 1.402, 1.23, 0.9083, 0.5749, 0.3759, 0.1863, 0.1823, 0.108, 0.08636, ) ,
		"mcZinvErr"          :   ( 0.3608, 0.2016, 0.1925, 0.1173, 0.07064, 0.04912, 0.03403, 0.02208, 0.0, 0.0, ) ,
		"mcTtwErr"           :   ( 2.199, 1.387, 1.215, 0.9007, 0.5706, 0.3727, 0.1831, 0.1809, 0.108, 0.08636, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 1.899, 0.9842, 1.19, 0.6758, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 14.0, 13.0, 5.0, 1.0, 2.0, 1.0, 0.0, 1.0, ) ,
		"nHad"               :   ( 103.0, 38.0, 41.0, 32.0, 10.0, 3.0, 0.0, 0.0, 0.0, 1.0, ) ,
		"nMuon"              :   ( 823.0, 415.0, 388.0, 271.0, 146.0, 66.0, 25.0, 10.0, 3.0, 4.0, ) ,
		"nMumu"              :   ( 9.0, 7.0, 4.0, 7.0, 3.0, 1.0, 0.0, 0.0, 0.0, 2.0, ) ,
	}

        common(self)


class data_2b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 19.37, 5.167, 2.496, 0.6991, 0.5225, 0.1359, 0.01683, 0.02303, ) ,
		"mcHad"              :   ( 93.65, 42.27, 30.73, 7.304, 1.962, 0.5689, 0.1592, 0.02936, 0.02903, 0.01018, ) ,
		"mcTtw"              :   ( 79.18, 35.71, 26.38, 5.842, 1.511, 0.3964, 0.09606, 0.01492, 0.00318, 0.004301, ) ,
		"mcMuon"             :   ( 933.9, 532.9, 473.0, 153.2, 56.0, 20.53, 8.325, 3.691, 2.027, 1.961, ) ,
		"mcZinv"             :   ( 14.47, 6.568, 4.344, 1.462, 0.4509, 0.1725, 0.06318, 0.01444, 0.02585, 0.005882, ) ,
		"mcMumu"             :   ( 36.07, 16.84, 16.56, 6.539, 3.23, 0.5414, 0.189, 0.1085, 0.2552, 0.02126, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 8.031, 5.955, 5.615, 3.129, 1.948, 1.118, 0.7014, 0.464, 0.3501, 0.2756, ) ,
		"mcMumuErr"          :   ( 2.959, 2.081, 2.204, 1.493, 1.052, 0.2584, 0.1614, 0.07845, 0.2357, 0.1059, ) ,
		"mcHadErr"           :   ( 1.54, 0.9803, 0.8512, 0.402, 0.2006, 0.09862, 0.05267, 0.01459, 0.02018, 0.008137, ) ,
		"mcZinvErr"          :   ( 0.536, 0.3593, 0.2542, 0.1358, 0.06953, 0.04267, 0.02896, 0.007768, 0.01975, 0.005132, ) ,
		"mcTtwErr"           :   ( 1.444, 0.9121, 0.8124, 0.3784, 0.1881, 0.0889, 0.04399, 0.01235, 0.00415, 0.006314, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 2.85, 1.193, 0.9336, 0.527, 0.3337, 0.09853, 0.03941, 0.04258, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 33.0, 7.0, 1.0, 2.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 107.0, 53.0, 24.0, 5.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 876.0, 451.0, 403.0, 120.0, 31.0, 7.0, 3.0, 3.0, 1.0, 0.0, ) ,
		"nMumu"              :   ( 44.0, 26.0, 15.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_3b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.4376, 0.1484, 0.1598, 0.09059, 0.01196, 0.005511, 0.003224, 0.002039, ) ,
		"mcHad"              :   ( 13.89, 5.405, 4.45, 2.792, 1.253, 0.5315, 0.1572, 0.1201, 0.05296, 0.04189, ) ,
		"mcTtw"              :   ( 13.63, 5.327, 4.333, 2.742, 1.23, 0.5109, 0.152, 0.1176, 0.05167, 0.04108, ) ,
		"mcMuon"             :   ( 109.7, 56.47, 58.83, 42.64, 25.92, 12.17, 5.701, 3.506, 1.737, 1.716, ) ,
		"mcZinv"             :   ( 0.2532, 0.07743, 0.1173, 0.05006, 0.02281, 0.02062, 0.005245, 0.002538, 0.001291, 0.0008104, ) ,
		"mcMumu"             :   ( 0.674, 0.5181, 0.4852, 0.2312, 0.2263, 0.1582, 0.03543, 0.04779, 0.1589, 0.001889, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 0.7518, 0.5494, 0.5593, 0.4697, 0.3944, 0.2655, 0.1646, 0.1381, 0.09879, 0.0647, ) ,
		"mcMumuErr"          :   ( 0.07184, 0.09391, 0.07504, 0.03637, 0.04294, 0.02643, 0.008833, 0.01531, 0.04798, 0.0, ) ,
		"mcHadErr"           :   ( 0.1676, 0.1073, 0.09866, 0.07963, 0.05463, 0.03666, 0.01735, 0.01955, 0.0099, 0.007625, ) ,
		"mcZinvErr"          :   ( 0.01424, 0.006875, 0.01051, 0.004376, 0.002993, 0.003062, 0.0009449, 0.0009499, 0.0, 0.0, ) ,
		"mcTtwErr"           :   ( 0.167, 0.107, 0.09809, 0.07951, 0.05455, 0.03653, 0.01732, 0.01952, 0.0099, 0.007625, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.1034, 0.03729, 0.04587, 0.04212, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 13.0, 1.0, 0.0, 1.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 84.0, 48.0, 48.0, 31.0, 18.0, 11.0, 6.0, 1.0, 1.0, 0.0, ) ,
		"nMumu"              :   ( 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_3b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.362, 0.08496, 0.05439, 0.003376, 0.009723, 0.003069, 0.0001878, 0.0002843, ) ,
		"mcHad"              :   ( 4.471, 1.939, 1.488, 0.3073, 0.07657, 0.0243, 0.004471, 0.0006529, 0.000254, 0.0001466, ) ,
		"mcTtw"              :   ( 4.08, 1.822, 1.364, 0.2839, 0.06865, 0.01928, 0.003347, 0.0003873, 7.879e-05, 7.047e-05, ) ,
		"mcMuon"             :   ( 47.54, 26.69, 22.85, 6.719, 2.589, 0.9835, 0.3255, 0.1661, 0.08118, 0.06313, ) ,
		"mcZinv"             :   ( 0.391, 0.1167, 0.1239, 0.02332, 0.007924, 0.005019, 0.001124, 0.0002655, 0.0001752, 7.615e-05, ) ,
		"mcMumu"             :   ( 0.7707, 0.4973, 0.4185, 0.08188, 0.09621, 0.02403, 0.005367, 0.005621, 0.03056, 0.0001491, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 0.3615, 0.2771, 0.2514, 0.1255, 0.08507, 0.04812, 0.02559, 0.01957, 0.01411, 0.006926, ) ,
		"mcMumuErr"          :   ( 0.0538, 0.05507, 0.04045, 0.01466, 0.03228, 0.005262, 0.002764, 0.004194, 0.02729, 0.0, ) ,
		"mcHadErr"           :   ( 0.06671, 0.04503, 0.04118, 0.01814, 0.008474, 0.004461, 0.001556, 0.0, 0.0001206, 0.0, ) ,
		"mcZinvErr"          :   ( 0.01033, 0.006113, 0.006993, 0.002185, 0.001267, 0.00142, 0.0004671, 0.0, 0.0001206, 0.0, ) ,
		"mcTtwErr"           :   ( 0.06591, 0.04461, 0.04058, 0.018, 0.008379, 0.004228, 0.001484, 0.0, 0.0, 0.0, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.06506, 0.0236, 0.02319, 0.0, 0.005843, 0.0, 0.0, 0.0, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 6.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 48.0, 29.0, 20.0, 8.0, 3.0, 0.0, 1.0, 0.0, 0.0, 0.0, ) ,
		"nMumu"              :   ( 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_ge4b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.009084, 0.002597, 0.002513, 0.002976, 0.0002697, 0.000128, 8.251e-05, 3.46e-05, ) ,
		"mcHad"              :   ( 0.5011, 0.1861, 0.1719, 0.1405, 0.07243, 0.035, 0.01024, 0.009621, 0.004688, 0.004086, ) ,
		"mcTtw"              :   ( 0.4962, 0.1851, 0.164, 0.1396, 0.07198, 0.03458, 0.01013, 0.009559, 0.004602, 0.004066, ) ,
		"mcMuon"             :   ( 3.826, 1.873, 2.099, 1.846, 1.447, 0.7285, 0.3992, 0.2262, 0.1205, 0.1167, ) ,
		"mcZinv"             :   ( 0.004812, 0.001069, 0.007934, 0.0009294, 0.0004487, 0.000424, 0.0001103, 6.168e-05, 8.588e-05, 1.962e-05, ) ,
		"mcMumu"             :   ( 0.009096, 0.01289, 0.008272, 0.003271, 0.006338, 0.0081, 0.00139, 0.003374, 0.0286, 2.832e-05, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 0.03132, 0.02204, 0.02876, 0.03251, 0.03491, 0.02161, 0.04215, 0.01235, 0.01033, 0.008656, ) ,
		"mcMumuErr"          :   ( 0.001038, 0.002587, 0.001281, 0.0005168, 0.001529, 0.001938, 0.0004797, 0.001545, 0.02206, 1.304e-05, ) ,
		"mcHadErr"           :   ( 0.008749, 0.004884, 0.006061, 0.008156, 0.004248, 0.003493, 0.001688, 0.002208, 0.001473, 0.001353, ) ,
		"mcZinvErr"          :   ( 0.001054, 0.0001111, 0.0002688, 0.0001078, 7.506e-05, 0.0001246, 3.073e-05, 2.997e-05, 7.62e-05, 5.253e-06, ) ,
		"mcTtwErr"           :   ( 0.008685, 0.004883, 0.006055, 0.008155, 0.004247, 0.003491, 0.001687, 0.002208, 0.001471, 0.001353, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.002613, 0.0008662, 0.0007564, 0.001758, 9.52e-05, 5.547e-05, 4.824e-05, 1.608e-05, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 1.0, 1.0, 0.0, 1.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMumu"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_ge4b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.0, 0.000225, 0.0003028, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcHad"              :   ( 0.00583, 0.002323, 0.0007302, 3.996e-05, 0.0, 2.466e-05, 4.345e-06, 0.0, 0.0, 0.0, ) ,
		"mcTtw"              :   ( 0.004626, 0.0007998, 0.0006456, 2.36e-05, 0.0, 5.241e-06, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcMuon"             :   ( 0.03102, 0.01781, 0.009517, 0.002121, 0.001152, 0.0003092, 0.0003512, 0.0001731, 0.0001619, 0.0, ) ,
		"mcZinv"             :   ( 0.001203, 0.001524, 8.454e-05, 1.636e-05, 0.0, 1.942e-05, 4.345e-06, 0.0, 0.0, 0.0, ) ,
		"mcMumu"             :   ( 0.0004732, 0.0002692, 0.0001083, 7.637e-07, 0.0003924, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 0.002882, 0.00212, 0.001291, 0.0005332, 0.0004283, 0.0002187, 0.0002028, 0.0001426, 0.0001619, 0.0, ) ,
		"mcMumuErr"          :   ( 0.0003611, 0.0001846, 7.658e-05, 7.637e-07, 0.0003924, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcHadErr"           :   ( 0.001202, 0.001459, 0.0002383, 2.628e-05, 0.0, 2.012e-05, 4.344e-06, 0.0, 0.0, 0.0, ) ,
		"mcZinvErr"          :   ( 0.001024, 0.001435, 4.968e-05, 1.157e-05, 0.0, 1.942e-05, 4.344e-06, 0.0, 0.0, 0.0, ) ,
		"mcTtwErr"           :   ( 0.0006304, 0.000263, 0.0002331, 2.36e-05, 0.0, 5.241e-06, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.0, 0.0002251, 0.0003028, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMumu"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)