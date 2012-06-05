from inputData import syst
from data import data,scaled

def common(x, systMode = 4) :
    x._htBinLowerEdges = (275.0, 325.0, 375.0, 475.0, 575.0, 675.0, 775.0, 875.0)
    x._htMaxForPlot = 975.0
    x._htMeans = ( 2.960e+02, 3.464e+02, 4.128e+02, 5.144e+02, 6.161e+02, 7.171e+02, 8.179e+02, 9.188e+02) #old
    x._mergeBins = None
    x._constantMcRatioAfterHere = (    0,     0,     0,     0,     0,     0,     0,     1)
    x._lumi =  	{
        "mumu"               :   1716.0 ,
        "muon"               :   1716.0 ,
        "mcPhot"             :   1550.0 ,
        "phot"               :   1550.0 ,
        "mcHad"              :   2070.0 ,
        "had"                :   2070.0 ,
        "mcMuon"             :   1716.0 ,
        "mcMumu"             :   1716.0 ,
    }
    x._triggerEfficiencies = {
        "hadBulk":       (     1.000,     1.000,     1.000,     1.000,     1.000,     1.000,     1.000,     1.000),
        "had":           (     0.916,     0.988,     1.000,     1.000,     1.000,     1.000,     1.000,     1.000),
        "muon":          (     0.880,     0.880,     0.880,     0.880,     0.880,     0.880,     0.880,     0.880),
        "phot":          (     1.000,     1.000,     1.000,     1.000,     1.000,     1.000,     1.000,     1.000),
        "mumu":          (     0.950,     0.950,     0.950,     0.950,     0.950,     0.950,     0.950,     0.980),
        }
    x._purities = {
        "phot":          (     1.000,     1.000,     1.000,     1.000,     1.000,     1.000,     1.000,     1.000),
        }
    x._mcExpectationsBeforeTrigger["mcGjets"] =  x._mcExpectationsBeforeTrigger["mcPhot"]
    x._mcExtraBeforeTrigger = {}
    x._observations["nHadBulk"] = (92544000, 43592000, 29373000,  9830500,   3689500,   1458500,    677000,    671000)
    syst.load(x, mode = systMode)


class data_0b(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
            "mcPhot"             :   ( None, None, None,  None, 55.42, 20.65, 8.089, 5.751, ) ,
            "mcHad"              :   ( 453.6, 224.1, 234.6, 75.92, 30.68, 18.42, 3.992, 3.127, ) ,
            "mcTtw"              :   ( 239.0, 107.6, 116.4, 29.07, 17.72, 8.626, 3.631, 2.779, ) ,
            "mcMuon"             :   ( 179.7, 57.31, 74.13, 6.179, 14.75, 6.398, 2.671, 2.616, ) ,
            "mcZinv"             :   ( 214.6, 116.5, 118.2, 46.84, 12.96, 9.792, 0.3614, 0.3478, ) ,
            "mcMumu"             :   ( 13.11, 8.117, 3.764, 9.019, 0.6995, 1.822, 0.0, 0.0, ) ,
        }

        self._mcStatError =  	{
            "mcMuonErr"          :   ( 38.57, 17.16, 26.28, 2.094, 1.155, 0.7281, 0.4932, 0.5535, ) ,
            "mcMumuErr"          :   ( 3.436, 2.681, 1.578, 3.596, 0.6554, 1.815, 0.0, 0.0, ) ,
            "mcHadErr"           :   ( 48.0, 34.13, 42.79, 17.86, 7.164, 5.296, 0.6846, 0.5836, ) ,
            "mcZinvErr"          :   ( 29.16, 20.44, 20.5, 12.82, 7.046, 5.217, 0.2855, 0.3478, ) ,
            "mcTtwErr"           :   ( 38.12, 27.34, 37.56, 12.43, 1.292, 0.9158, 0.6222, 0.4687, ) ,
            "mcPhotErr"          :   ( None, None, None, None, 3.986, 2.512, 1.429, 1.309, ) ,
        }

        self._observations =  	{
            "nPhot"              :   ( None, None, None, None, 64.0, 16.0, 6.0, 3.0, ) ,
            "nHad"               :   ( 468.0, 201.0, 170.0, 78.0, 20.0, 12.0, 5.0, 7.0, ) ,
            "nMuon"              :   ( 133.0, 63.0, 47.0, 25.0, 11.0, 4.0, 0.0, 0.0, ) ,
            "nMumu"              :   ( 18.0, 9.0, 9.0, 1.0, 0.0, 3.0, 0.0, 0.0, ) ,
        }
        
        common(self)

class data_1b(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
            "mcPhot"             :   ( None, None, None, None, 5.769, 1.977, 0.5422, 1.332, ) ,
            "mcHad"              :   ( 123.1, 52.19, 45.41, 18.51, 10.4, 4.864, 2.488, 1.393, ) ,
            "mcTtw"              :   ( 90.79, 36.39, 31.31, 11.9, 7.709, 3.056, 1.453, 1.292, ) ,
            "mcMuon"             :   ( 413.4, 237.7, 240.8, 122.3, 60.02, 30.4, 18.15, 22.58, ) ,
            "mcZinv"             :   ( 32.33, 15.8, 14.1, 6.612, 2.696, 1.808, 1.035, 0.1011, ) ,
            "mcMumu"             :   ( 11.13, 7.946, 7.157, 5.022, 2.249, 0.8029, 0.5994, 0.5792, ) ,
        }

        self._mcStatError =  	{
            "mcMuonErr"          :   ( 35.16, 10.7, 21.85, 8.728, 4.838, 2.889, 3.12, 4.05, ) ,
            "mcMumuErr"          :   ( 2.8, 1.527, 2.802, 1.41, 0.7144, 0.4574, 0.3151, 0.0611, ) ,
            "mcHadErr"           :   ( 13.52, 3.345, 2.972, 1.846, 2.6, 0.9298, 1.393, 0.8583, ) ,
            "mcZinvErr"          :   ( 3.76, 1.545, 0.01622, 0.1418, 1.491, 0.0, 1.007, 0.0, ) ,
            "mcTtwErr"           :   ( 12.98, 2.966, 2.972, 1.841, 2.13, 0.9298, 0.9633, 0.8583, ) ,
            "mcPhotErr"          :   ( None, None, None, None, 1.313, 0.5975, 0.2707, 0.7021, ) ,
        }

        self._observations =  	{
            "nPhot"              :   ( None, None, None, None, 6.0, 5.0, 1.0, 0.0, ) ,
            "nHad"               :   ( 94.0, 36.0, 29.0, 13.0, 6.0, 1.0, 1.0, 0.0, ) ,
            "nMuon"              :   ( 399.0, 201.0, 226.0, 107.0, 61.0, 39.0, 21.0, 9.0, ) ,
            "nMumu"              :   ( 19.0, 7.0, 10.0, 10.0, 4.0, 0.0, 1.0, 0.0, ) ,
        }
        
        common(self)

class data_2b(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
            "mcPhot"             :   ( None, None, None, None, 1.763, 0.02514, 0.002818, 0.3037, ) ,
            "mcHad"              :   ( 29.92, 10.75, 8.075, 4.514, 4.188, 1.242, 1.576, 0.4021, ) ,
            "mcTtw"              :   ( 26.66, 9.815, 7.524, 4.214, 3.168, 1.104, 0.5622, 0.3911, ) ,
            "mcMuon"             :   ( 174.8, 86.07, 86.09, 50.67, 22.11, 11.38, 7.008, 7.326, ) ,
            "mcZinv"             :   ( 3.255, 0.9373, 0.5512, 0.2995, 1.02, 0.1376, 1.014, 0.01101, ) ,
            "mcMumu"             :   ( 3.254, 2.658, 1.259, 2.745, 0.5144, 0.1916, 0.1738, 0.07006, ) ,
        }

        self._mcStatError =  	{
            "mcMuonErr"          :   ( 11.41, 6.098, 6.881, 3.166, 1.678, 1.335, 0.9095, 1.005, ) ,
            "mcMumuErr"          :   ( 0.7817, 1.236, 0.3777, 1.999, 0.2764, 0.1788, 0.2455, 0.09432, ) ,
            "mcHadErr"           :   ( 3.389, 1.449, 2.097, 0.9846, 1.595, 0.4671, 1.594, 0.1295, ) ,
            "mcZinvErr"          :   ( 1.64, 1.014, 0.7747, 0.6797, 1.44, 0.2328, 1.553, 0.0, ) ,
            "mcTtwErr"           :   ( 2.965, 1.035, 1.949, 0.7123, 0.6849, 0.405, 0.3563, 0.1295, ) ,
            "mcPhotErr"          :   ( None, None, None, None, 0.7756, 0.02514, 0.002818, 0.3037, ) ,
        }

        self._observations =  	{
            "nPhot"              :   ( None, None, None, None, 2.0, 0.0, 0.0, 0.0, ) ,
            "nHad"               :   ( 14.0, 16.0, 8.0, 7.0, 3.0, 2.0, 0.0, 0.0, ) ,
            "nMuon"              :   ( 193.0, 87.0, 70.0, 30.0, 26.0, 12.0, 2.0, 2.0, ) ,
            "nMumu"              :   ( 4.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, ) ,
        }
        
        common(self)

class data_ge3b(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
            "mcPhot"             :   ( None, None, None, None, 0.0, 0.0, 0.0, 0.0, ) ,
            "mcHad"              :   ( 2.194, 0.7369, 0.5399, 0.4576, 0.6681, 0.1897, 0.2248, 0.09548, ) ,
            "mcTtw"              :   ( 2.067, 0.7132, 0.5383, 0.4576, 0.4649, 0.1897, 0.1138, 0.09548, ) ,
            "mcMuon"             :   ( 8.997, 5.168, 3.971, 5.162, 1.812, 1.176, 0.8893, 0.8902, ) ,
            "mcZinv"             :   ( 0.127, 0.02368, 0.001622, 0.0, 0.2032, 0.0, 0.111, 0.0, ) ,
            "mcMumu"             :   ( 0.06148, 0.03538, 0.02562, 0.09683, 0.02222, 0.01116, 0.006346, 0.002647, ) ,
        }

        self._mcStatError =  	{
            "mcMuonErr"          :   ( 0.4053, 0.2559, 0.2104, 0.1903, 0.09283, 0.08645, 0.06925, 0.06952, ) ,
            "mcMumuErr"          :   ( 0.01408, 0.008417, 0.006974, 0.05091, 0.009347, 0.007596, 0.006183, 0.001901, ) ,
            "mcHadErr"           :   ( 0.1636, 0.05923, 0.05374, 0.05282, 0.1799, 0.04248, 0.1145, 0.01581, ) ,
            "mcZinvErr"          :   ( 0.06827, 0.01858, 0.001584, 0.0, 0.1705, 0.0, 0.1074, 0.0, ) ,
            "mcTtwErr"           :   ( 0.1487, 0.05624, 0.05372, 0.05282, 0.05723, 0.04248, 0.03978, 0.01581, ) ,
            "mcPhotErr"          :   ( None, None, None, None, 0.0, 0.0, 0.0, 0.0, ) ,
        }

        self._observations =  	{
            "nPhot"              :   ( None, None, None, None, 0.0, 0.0, 0.0, 0.0, ) ,
            "nHad"               :   ( 3.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, ) ,
            "nMuon"              :   ( 12.0, 6.0, 4.0, 3.0, 2.0, 2.0, 0.0, 2.0, ) ,
            "nMumu"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
        }

        common(self)
