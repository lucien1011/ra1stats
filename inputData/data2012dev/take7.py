from configuration.units import fb
from data import data
import utils


def common1(x) :
    x._lumi =  	{
		"mumu"               :   19.15/fb,
		"muon"               :   19.15/fb,
		"mcPhot"             :   19.18/fb,
		"mcHad"              :   18.33/fb,
		"mcTtw"              :   18.33/fb,
		"had"                :   18.33/fb,
		"mcMuon"             :   19.15/fb,
		"mcZinv"             :   18.33/fb,
		"mcMumu"             :   19.15/fb,
		"phot"               :   19.18/fb,
                }

    x._triggerEfficiencies = {
        #"hadBulk":       (0.666, 0.745, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000),
        "hadBulk":       (1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000),
        "muon":          (0.880, 0.880, 0.880, 0.880, 0.880, 0.880, 0.880, 0.880, 0.880, 0.880, 0.880),
        "phot":          (1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000),
        "mumu":          (0.949, 0.952, 0.950, 0.956, 0.953, 0.954, 0.958, 0.959, 0.962, 0.974, 0.953),
        
                }
    x._htBinLowerEdges = ( 200.0, 275.0, 325.0, 375.0, 475.0, 575.0, 675.0, 775.0, 875.0, 975.0, 1075.0)
    x._htMaxForPlot    = 1175.0
    x._htMeans         = ( 235.2, 297.5, 347.5, 416.4, 517.3, 618.4, 716.9, 819.9, 919.0, 1019.0, 1289.0)
    

    iPhot = 3
    x._observations["nPhot"] = tuple([None]*iPhot + list(x._observations["nPhot"][iPhot:]))


def common(x) :
    common1(x)

    systBins = tuple([0]*2 + [1]*3 + [2]*1 + [3]*2 + [4]*3)
#    systBins = tuple([0,1,2,3,3,4,4,5,5,6,6])
    name = x.__class__.__name__


    if "le3j" in name :
        systMagnitudes = (0.05, 0.05, 0.10, 0.20, 0.30)  # tmp
#        systMagnitudes = (0.05, 0.05, 0.05, 0.10, 0.10, 0.20, 0.30)  # tmp
        x._triggerEfficiencies["had"] = (0.816, 0.901, 0.988, 0.994, 1.000, .994, 1.000, 1.000, 1.000, 1.000, 1.000)
        x._observations["nHadBulk"] = (3.4067318E09, 8.317453E08, 3.29919975E08, 2.74138825E08, 8.507427E07,   
                                       2.8887025E07, 1.09110E07, 4.6215E06, 2.07715E06, 1.031125E06, 1.20755E06)

    elif "ge4j" in name :
        systMagnitudes = (0.05, 0.10, 0.10, 0.20, 0.30)  # dtmp
        #systMagnitudes = (0.05, 0.05, 0.05, 0.10, 0.10, 0.20, 0.30)  # tmp
        x._triggerEfficiencies["had"] = (0.665, 0.666, 0.971, 0.988, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000)
        x._observations["nHadBulk"] = (6.60088E07, 1.400533E08, 5.2689525E07, 4.8204025E07, 3.35079E07,
                                       1.582655E07, 7.279475E06, 3.46345E06, 1.732725E06, 8.9562E05, 1.142775E06)

    if "ge4b" in name :
        x._mergeBins = (0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3)
        systMagnitudes = (0.25,)
        systBins = (0, 0, 0, 0)
    else :
        x._mergeBins = None

    x._systBins = {
        "sigmaPhotZ": systBins,
        "sigmaMuonW": systBins,
        "sigmaMumuZ": systBins,
        }

    x._fixedParameters = {
        "sigmaPhotZ": systMagnitudes,
        "sigmaMuonW": systMagnitudes,
        "sigmaMumuZ": systMagnitudes,
        "k_qcd_nom":2.96e-2,
        "k_qcd_unc_inp":utils.quadSum([0.61e-2, 0.463e-2])
        #"k_qcd_unc_inp":utils.quadSum([2.5*0.61e-2, 2.5*0.463e-2])
        }

class data_0b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.0, 459.3, 339.1, 184.6, 83.28, 42.12, 18.56, 8.659, 10.78, ) ,
		"mcTtw"              :   ( 271.0, 1474.0, 529.5, 414.8, 255.2, 113.5, 43.2, 22.51, 8.681, 4.644, 6.478, ) ,
		"mcHad"              :   ( 400.1, 2153.0, 803.0, 638.1, 420.6, 198.9, 82.3, 40.01, 17.09, 8.787, 10.77, ) ,
		"mcMuon"             :   ( 894.6, 3042.0, 1432.0, 1540.0, 1165.0, 649.4, 344.3, 187.9, 100.1, 58.03, 79.37, ) ,
		"mcZinv"             :   ( 129.0, 678.9, 273.5, 223.3, 165.4, 85.42, 39.1, 17.5, 8.412, 4.143, 4.288, ) ,
		"mcMumu"             :   ( 66.23, 228.0, 109.2, 107.6, 93.91, 55.98, 31.64, 17.47, 9.463, 6.129, 9.175, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 24.72, 34.72, 16.83, 17.28, 11.03, 7.989, 5.888, 4.401, 3.143, 2.398, 2.817, ) ,
		"mcMumuErr"          :   ( 4.971, 6.86, 4.481, 1.993, 1.545, 1.269, 0.8563, 0.656, 0.4653, 0.3689, 0.4718, ) ,
		"mcZinvErr"          :   ( 3.833, 7.873, 4.719, 3.13, 1.97, 1.374, 0.9063, 0.6054, 0.4219, 0.2946, 0.3006, ) ,
		"mcHadErr"           :   ( 12.41, 19.22, 9.694, 7.614, 5.538, 3.572, 2.208, 1.615, 0.9792, 0.7136, 0.8731, ) ,
		"mcTtwErr"           :   ( 11.8, 17.53, 8.467, 6.941, 5.176, 3.297, 2.013, 1.497, 0.8836, 0.6499, 0.8198, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.0, 11.18, 8.926, 6.511, 4.332, 3.077, 2.083, 1.414, 1.596, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 395.0, 267.0, 146.0, 75.0, 29.0, 13.0, 6.0, 7.0, ) ,
		"nHad"               :   ( 282.0, 1786.0, 720.0, 614.0, 451.0, 231.0, 91.0, 29.0, 18.0, 14.0, 11.0, ) ,
		"nMuon"              :   ( 717.0, 2322.0, 1011.0, 1080.0, 728.0, 462.0, 227.0, 112.0, 79.0, 40.0, 44.0, ) ,
		"nMumu"              :   ( 60.0, 188.0, 76.0, 93.0, 81.0, 39.0, 18.0, 8.0, 8.0, 3.0, 2.0, ) ,
	}

        common(self)


class data_0b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.0, 4274.0, 1459.0, 524.8, 201.8, 74.26, 31.83, 18.02, 15.14, ) ,
		"mcTtw"              :   ( 1.285e+04, 5928.0, 2521.0, 1733.0, 480.9, 145.8, 48.3, 18.78, 9.127, 3.647, 2.389, ) ,
		"mcHad"              :   ( 2.407e+04, 1.12e+04, 4928.0, 3577.0, 1084.0, 359.1, 125.8, 50.89, 22.91, 9.738, 7.769, ) ,
		"mcMuon"             :   ( 5.247e+04, 2.026e+04, 1.12e+04, 1.05e+04, 4263.0, 1817.0, 848.4, 424.4, 226.8, 125.8, 181.5, ) ,
		"mcZinv"             :   ( 1.122e+04, 5274.0, 2407.0, 1844.0, 602.9, 213.3, 77.45, 32.11, 13.79, 6.091, 5.381, ) ,
		"mcMumu"             :   ( 5655.0, 2291.0, 1294.0, 1246.0, 543.2, 238.9, 116.9, 60.04, 31.88, 16.68, 28.3, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 177.0, 68.72, 42.17, 38.59, 21.82, 14.29, 9.707, 6.894, 5.006, 3.742, 4.451, ) ,
		"mcMumuErr"          :   ( 46.47, 13.76, 8.823, 7.101, 3.654, 2.407, 1.654, 1.188, 0.9192, 0.6356, 0.8172, ) ,
		"mcZinvErr"          :   ( 37.12, 21.48, 13.68, 8.663, 3.721, 2.197, 1.315, 0.8459, 0.5562, 0.3708, 0.3499, ) ,
		"mcHadErr"           :   ( 71.62, 38.48, 23.8, 17.09, 8.188, 4.534, 2.609, 1.62, 1.118, 0.7233, 0.5979, ) ,
		"mcTtwErr"           :   ( 61.25, 31.92, 19.47, 14.73, 7.294, 3.965, 2.254, 1.382, 0.9694, 0.621, 0.4849, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.0, 34.37, 18.86, 11.34, 6.988, 4.211, 2.781, 2.076, 1.946, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 3720.0, 1170.0, 411.0, 137.0, 45.0, 20.0, 11.0, 10.0, ) ,
		"nHad"               :   ( 2.058e+04, 1.027e+04, 4708.0, 3320.0, 945.0, 288.0, 107.0, 39.0, 17.0, 13.0, 10.0, ) ,
		"nMuon"              :   ( 4.335e+04, 1.596e+04, 8410.0, 7646.0, 2962.0, 1302.0, 506.0, 262.0, 124.0, 75.0, 95.0, ) ,
		"nMumu"              :   ( 5174.0, 2077.0, 1137.0, 1027.0, 402.0, 184.0, 82.0, 39.0, 21.0, 11.0, 12.0, ) ,
	}

        common(self)


class data_1b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.0, 80.12, 58.59, 32.1, 16.27, 8.043, 3.598, 1.862, 1.796, ) ,
		"mcTtw"              :   ( 172.3, 1087.0, 425.0, 325.4, 189.9, 76.67, 28.5, 11.47, 6.2, 2.877, 2.464, ) ,
		"mcHad"              :   ( 189.8, 1190.0, 468.2, 361.7, 216.0, 90.29, 36.19, 15.0, 7.737, 3.653, 3.136, ) ,
		"mcMuon"             :   ( 826.5, 3008.0, 1543.0, 1652.0, 1195.0, 637.8, 307.5, 156.8, 82.48, 43.44, 55.18, ) ,
		"mcZinv"             :   ( 17.42, 102.7, 43.17, 36.3, 26.14, 13.62, 7.697, 3.53, 1.537, 0.7761, 0.6724, ) ,
		"mcMumu"             :   ( 16.1, 57.88, 26.41, 30.03, 27.92, 14.03, 8.524, 4.909, 2.036, 1.611, 2.435, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 10.21, 18.77, 13.61, 13.91, 11.77, 8.475, 5.839, 4.103, 2.962, 2.087, 2.452, ) ,
		"mcMumuErr"          :   ( 1.228, 2.419, 1.276, 1.304, 1.292, 0.7689, 0.6399, 0.5451, 0.2305, 0.25, 0.3341, ) ,
		"mcZinvErr"          :   ( 0.7433, 1.662, 1.001, 0.6712, 0.4113, 0.2842, 0.2173, 0.1497, 0.09533, 0.0614, 0.05703, ) ,
		"mcHadErr"           :   ( 4.44, 11.15, 6.92, 5.99, 4.559, 2.833, 1.743, 1.042, 0.8319, 0.4873, 0.436, ) ,
		"mcTtwErr"           :   ( 4.377, 11.02, 6.847, 5.953, 4.54, 2.819, 1.729, 1.031, 0.8264, 0.4834, 0.4323, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.0, 2.504, 2.031, 1.442, 0.9891, 0.7039, 0.5047, 0.3533, 0.3312, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 90.0, 57.0, 35.0, 18.0, 7.0, 2.0, 2.0, 3.0, ) ,
		"nHad"               :   ( 131.0, 844.0, 437.0, 353.0, 193.0, 69.0, 20.0, 23.0, 6.0, 2.0, 3.0, ) ,
		"nMuon"              :   ( 637.0, 2238.0, 999.0, 1034.0, 725.0, 336.0, 177.0, 84.0, 38.0, 13.0, 28.0, ) ,
		"nMumu"              :   ( 12.0, 60.0, 25.0, 35.0, 25.0, 16.0, 3.0, 2.0, 4.0, 0.0, 2.0, ) ,
	}

        common(self)


class data_1b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.0, 431.6, 146.0, 49.39, 22.83, 7.792, 3.49, 2.063, 1.658, ) ,
		"mcTtw"              :   ( 2608.0, 1447.0, 639.0, 438.7, 98.76, 24.1, 8.569, 2.58, 1.253, 0.4549, 0.3303, ) ,
		"mcHad"              :   ( 3523.0, 1940.0, 868.9, 617.0, 157.0, 43.63, 16.88, 5.983, 2.737, 1.067, 0.7627, ) ,
		"mcMuon"             :   ( 1.317e+04, 5533.0, 3123.0, 2794.0, 978.8, 385.1, 165.9, 72.65, 39.67, 21.55, 28.21, ) ,
		"mcZinv"             :   ( 915.4, 492.6, 229.9, 178.3, 58.26, 19.54, 8.315, 3.403, 1.484, 0.6117, 0.4324, ) ,
		"mcMumu"             :   ( 725.6, 312.5, 169.8, 159.5, 63.91, 26.27, 13.39, 6.122, 3.133, 2.163, 2.844, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 44.05, 27.53, 19.44, 17.96, 10.26, 6.279, 4.046, 2.562, 1.96, 1.396, 1.412, ) ,
		"mcMumuErr"          :   ( 8.399, 4.222, 3.186, 2.699, 1.489, 0.832, 0.5754, 0.3904, 0.2414, 0.3037, 0.1734, ) ,
		"mcZinvErr"          :   ( 5.727, 3.494, 2.165, 1.34, 0.6044, 0.3263, 0.2104, 0.1364, 0.09168, 0.05263, 0.04319, ) ,
		"mcHadErr"           :   ( 18.68, 13.04, 8.575, 6.902, 3.162, 1.424, 0.7556, 0.379, 0.3006, 0.1172, 0.1179, ) ,
		"mcTtwErr"           :   ( 17.78, 12.57, 8.297, 6.771, 3.103, 1.386, 0.7257, 0.3536, 0.2863, 0.1047, 0.1097, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.0, 5.647, 3.056, 1.699, 1.158, 0.6843, 0.5178, 0.3359, 0.3385, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 465.0, 147.0, 39.0, 13.0, 3.0, 5.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 3236.0, 1994.0, 876.0, 589.0, 144.0, 44.0, 11.0, 5.0, 2.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 1.104e+04, 4435.0, 2343.0, 2067.0, 670.0, 243.0, 92.0, 45.0, 16.0, 10.0, 15.0, ) ,
		"nMumu"              :   ( 703.0, 314.0, 163.0, 160.0, 60.0, 25.0, 10.0, 5.0, 4.0, 1.0, 1.0, ) ,
	}

        common(self)


class data_2b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.0, 10.89, 7.548, 4.315, 2.335, 1.035, 0.3056, 0.3376, 0.2191, ) ,
		"mcTtw"              :   ( 69.93, 480.8, 192.8, 144.6, 90.84, 34.67, 12.41, 3.928, 3.917, 1.191, 1.087, ) ,
		"mcHad"              :   ( 72.01, 495.1, 199.0, 150.3, 94.54, 36.45, 13.52, 4.414, 4.133, 1.301, 1.141, ) ,
		"mcMuon"             :   ( 495.7, 1852.0, 965.9, 1010.0, 718.5, 382.4, 174.8, 84.7, 46.27, 21.94, 26.75, ) ,
		"mcZinv"             :   ( 2.075, 14.25, 6.19, 5.701, 3.704, 1.779, 1.108, 0.4861, 0.2157, 0.1101, 0.05403, ) ,
		"mcMumu"             :   ( 5.801, 23.37, 10.08, 12.68, 11.25, 5.571, 2.674, 1.212, 0.5862, 0.5818, 0.4887, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 6.72, 12.98, 9.59, 9.768, 8.204, 5.866, 3.925, 2.634, 1.949, 1.294, 1.489, ) ,
		"mcMumuErr"          :   ( 0.6709, 1.401, 1.007, 1.042, 0.9791, 0.6543, 0.4299, 0.2572, 0.1919, 0.1809, 0.1412, ) ,
		"mcZinvErr"          :   ( 0.2267, 0.5874, 0.3642, 0.2767, 0.1469, 0.09514, 0.07273, 0.04761, 0.03681, 0.0223, 0.01148, ) ,
		"mcHadErr"           :   ( 2.301, 6.09, 3.928, 3.358, 2.715, 1.575, 0.9312, 0.4951, 0.7245, 0.2677, 0.2536, ) ,
		"mcTtwErr"           :   ( 2.29, 6.062, 3.911, 3.346, 2.711, 1.572, 0.9284, 0.4928, 0.7235, 0.2668, 0.2534, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.0, 0.8828, 0.6636, 0.4751, 0.3643, 0.2208, 0.06838, 0.1321, 0.08467, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 18.0, 15.0, 10.0, 0.0, 1.0, 2.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 47.0, 369.0, 175.0, 137.0, 77.0, 43.0, 14.0, 1.0, 2.0, 1.0, 2.0, ) ,
		"nMuon"              :   ( 374.0, 1396.0, 701.0, 687.0, 492.0, 234.0, 111.0, 40.0, 23.0, 4.0, 16.0, ) ,
		"nMumu"              :   ( 10.0, 16.0, 11.0, 12.0, 11.0, 4.0, 3.0, 3.0, 1.0, 0.0, 2.0, ) ,
	}

        common(self)


class data_2b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.0, 29.61, 11.31, 3.166, 1.487, 0.3456, 0.2202, 0.2755, 0.04173, ) ,
		"mcTtw"              :   ( 389.5, 325.4, 151.8, 109.2, 23.68, 5.164, 2.177, 0.09036, 0.05383, 0.01284, 0.009423, ) ,
		"mcHad"              :   ( 470.8, 369.3, 172.0, 124.6, 28.35, 6.65, 2.739, 0.3307, 0.161, 0.04333, 0.02767, ) ,
		"mcMuon"             :   ( 4088.0, 1917.0, 1082.0, 964.8, 307.2, 112.7, 41.18, 15.81, 8.6, 4.24, 5.036, ) ,
		"mcZinv"             :   ( 81.27, 43.99, 20.19, 15.46, 4.666, 1.486, 0.5624, 0.2404, 0.1071, 0.03049, 0.01825, ) ,
		"mcMumu"             :   ( 187.7, 78.86, 36.78, 30.45, 10.03, 3.932, 1.942, 0.8323, 0.2057, 0.2039, 0.15, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 20.15, 13.91, 10.5, 10.01, 5.566, 3.337, 1.993, 1.189, 0.8967, 0.5549, 0.6162, ) ,
		"mcMumuErr"          :   ( 4.407, 2.576, 1.831, 1.575, 0.8126, 0.5104, 0.3778, 0.2256, 0.05236, 0.09582, 0.02239, ) ,
		"mcZinvErr"          :   ( 1.827, 1.073, 0.6731, 0.4342, 0.1743, 0.09132, 0.05211, 0.03661, 0.02769, 0.009898, 0.006875, ) ,
		"mcHadErr"           :   ( 5.615, 5.042, 3.517, 3.022, 1.465, 0.6415, 0.3936, 0.04073, 0.04017, 0.01069, 0.007851, ) ,
		"mcTtwErr"           :   ( 5.309, 4.926, 3.452, 2.99, 1.455, 0.635, 0.3901, 0.01786, 0.0291, 0.004032, 0.003792, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.0, 1.461, 0.8565, 0.4049, 0.2724, 0.1042, 0.1258, 0.1506, 0.01084, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 29.0, 10.0, 5.0, 0.0, 0.0, 1.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 374.0, 318.0, 194.0, 109.0, 26.0, 12.0, 1.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 3399.0, 1495.0, 794.0, 658.0, 201.0, 63.0, 15.0, 8.0, 4.0, 0.0, 2.0, ) ,
		"nMumu"              :   ( 193.0, 72.0, 37.0, 34.0, 5.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_3b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.0, 0.6867, 0.3628, 0.2597, 0.1208, 0.0569, 0.009669, 0.04974, 0.008293, ) ,
		"mcTtw"              :   ( 5.739, 46.35, 19.72, 14.13, 9.909, 4.357, 1.531, 0.489, 0.4589, 0.2442, 0.1852, ) ,
		"mcHad"              :   ( 5.804, 47.03, 20.03, 14.39, 10.12, 4.446, 1.606, 0.5244, 0.4763, 0.2522, 0.1877, ) ,
		"mcMuon"             :   ( 48.45, 186.3, 95.55, 102.4, 77.17, 44.1, 20.67, 9.842, 6.804, 2.509, 3.05, ) ,
		"mcZinv"             :   ( 0.06492, 0.6804, 0.3072, 0.2559, 0.2151, 0.08992, 0.07489, 0.0354, 0.01738, 0.008046, 0.002455, ) ,
		"mcMumu"             :   ( 0.5507, 1.483, 0.7009, 0.9888, 0.9797, 0.4356, 0.2196, 0.07527, 0.1039, 0.04797, 0.0477, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 1.013, 1.976, 1.541, 1.593, 1.39, 1.042, 0.7355, 0.4987, 0.4086, 0.2297, 0.2701, ) ,
		"mcMumuErr"          :   ( 0.1657, 0.2072, 0.1455, 0.2039, 0.199, 0.1447, 0.07148, 0.02432, 0.07891, 0.01755, 0.02264, ) ,
		"mcZinvErr"          :   ( 0.01266, 0.07415, 0.04682, 0.02094, 0.01828, 0.01015, 0.01062, 0.008476, 0.008675, 0.002538, 0.0009618, ) ,
		"mcHadErr"           :   ( 0.3163, 0.9244, 0.624, 0.5019, 0.4139, 0.284, 0.1474, 0.09263, 0.1492, 0.08968, 0.05703, ) ,
		"mcTtwErr"           :   ( 0.316, 0.9214, 0.6223, 0.5015, 0.4135, 0.2838, 0.147, 0.09224, 0.149, 0.08964, 0.05703, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.0, 0.1505, 0.07213, 0.06226, 0.02902, 0.01845, 0.002927, 0.0311, 0.004226, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 5.0, 43.0, 18.0, 12.0, 13.0, 2.0, 4.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 40.0, 147.0, 69.0, 82.0, 60.0, 22.0, 16.0, 7.0, 2.0, 0.0, 0.0, ) ,
		"nMumu"              :   ( 0.0, 0.0, 0.0, 1.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_3b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.0, 0.4866, 0.2007, 0.05684, 0.01822, 0.004428, 0.09826, 0.002778, 0.0003035, ) ,
		"mcTtw"              :   ( 11.48, 14.19, 7.465, 5.801, 1.249, 0.3335, 0.2167, 0.0009964, 0.0003482, 7.854e-05, 7.662e-05, ) ,
		"mcHad"              :   ( 12.16, 15.14, 7.827, 6.07, 1.325, 0.377, 0.225, 0.004811, 0.001343, 0.0002674, 0.0001766, ) ,
		"mcMuon"             :   ( 163.3, 88.97, 48.57, 44.11, 13.49, 5.452, 1.725, 0.7671, 0.4178, 0.1089, 0.1632, ) ,
		"mcZinv"             :   ( 0.6804, 0.9519, 0.3623, 0.2689, 0.07655, 0.04353, 0.00825, 0.003815, 0.0009946, 0.0001888, 9.994e-05, ) ,
		"mcMumu"             :   ( 2.645, 1.707, 0.9953, 0.9169, 0.407, 0.0575, 0.04729, 0.0492, 0.00269, 0.002884, 0.005134, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 1.784, 1.372, 1.062, 0.995, 0.5388, 0.3714, 0.181, 0.1357, 0.1007, 0.03222, 0.0392, ) ,
		"mcMumuErr"          :   ( 0.2403, 0.163, 0.1971, 0.1815, 0.1387, 0.008923, 0.01956, 0.0265, 0.001083, 0.001656, 0.003702, ) ,
		"mcZinvErr"          :   ( 0.07805, 0.1044, 0.0452, 0.02489, 0.01076, 0.0113, 0.001171, 0.0008016, 0.0003799, 3.955e-05, 3.475e-05, ) ,
		"mcHadErr"           :   ( 0.4359, 0.4717, 0.3622, 0.3315, 0.1623, 0.06917, 0.0978, 0.0008495, 0.000418, 4.959e-05, 4.81e-05, ) ,
		"mcTtwErr"           :   ( 0.4288, 0.46, 0.3594, 0.3305, 0.162, 0.06824, 0.09779, 0.0002814, 0.0001744, 2.991e-05, 3.326e-05, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.0, 0.0612, 0.03811, 0.01483, 0.005154, 0.002305, 0.09746, 0.002229, 0.0001136, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 7.0, 14.0, 9.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 128.0, 73.0, 43.0, 31.0, 6.0, 4.0, 2.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMumu"              :   ( 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_ge4b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.0, 0.009908, 0.004897, 0.00699, 0.002206, 0.001089, 0.0001109, 0.005551, 0.0001171, ) ,
		"mcTtw"              :   ( 0.1006, 1.08, 0.5355, 0.3122, 0.328, 0.1821, 0.08148, 0.01942, 0.05248, 0.04638, 0.0128, ) ,
		"mcHad"              :   ( 0.101, 1.096, 0.5402, 0.3168, 0.3364, 0.1835, 0.08337, 0.02039, 0.05282, 0.04658, 0.01285, ) ,
		"mcMuon"             :   ( 1.149, 4.416, 2.303, 2.784, 2.943, 1.817, 1.056, 0.5721, 0.5019, 0.1722, 0.1955, ) ,
		"mcZinv"             :   ( 0.0004807, 0.01667, 0.004704, 0.004572, 0.008372, 0.001438, 0.001892, 0.0009677, 0.0003376, 0.000202, 4.933e-05, ) ,
		"mcMumu"             :   ( 0.06539, 0.09968, 0.01215, 0.1541, 0.07129, 0.01508, 0.004823, 0.001513, 0.002083, 0.001408, 0.001185, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 0.1273, 0.1806, 0.1391, 0.164, 0.1943, 0.1208, 0.1118, 0.08732, 0.08173, 0.04248, 0.04441, ) ,
		"mcMumuErr"          :   ( 0.05855, 0.06322, 0.003153, 0.07632, 0.04849, 0.007246, 0.002288, 0.0006944, 0.001733, 0.0008014, 0.0006718, ) ,
		"mcZinvErr"          :   ( 0.0001425, 0.008217, 0.001462, 0.001359, 0.003553, 0.0002128, 0.0004609, 0.000419, 0.0001981, 8.751e-05, 3.04e-05, ) ,
		"mcHadErr"           :   ( 0.01525, 0.07536, 0.07535, 0.02244, 0.03291, 0.02015, 0.01736, 0.004103, 0.04769, 0.02956, 0.005271, ) ,
		"mcTtwErr"           :   ( 0.01525, 0.07491, 0.07534, 0.0224, 0.03271, 0.02015, 0.01736, 0.004081, 0.04769, 0.02956, 0.005271, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.0, 0.002796, 0.001376, 0.002444, 0.0006987, 0.0004358, 3.591e-05, 0.003586, 7.252e-05, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 0.0, 1.0, 0.0, 2.0, 1.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 0.0, 4.0, 2.0, 1.0, 4.0, 2.0, 2.0, 0.0, 0.0, 0.0, 1.0, ) ,
		"nMumu"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)

