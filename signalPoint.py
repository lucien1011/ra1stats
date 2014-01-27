class scan(object):
    def __init__(self,
                 dataset="",
                 tag="",
                 com=None,
                 xsVariation="default",
                 xsFactors=[1.0],
                 had="",
                 muon="",
                 phot="",
                 mumu="",
                 interBin="LowEdge",
                 aT=[],
                 extraVars=[],
                 weightedHistName="",
                 unweightedHistName="",
                 minSumWeightIn=1,
                 maxSumWeightIn=None,
                 llk=None,
                 whiteList=[],
                 exampleKargs={},
                 sigMcUnc=False,
                 ):

        assert xsVariation in ["default", "up", "down"], xsVariation

        self._boxNames = ["had", "muon", "phot", "mumu"]
        for item in ["dataset", "tag", "interBin", "com",
                     "xsVariation", "xsFactors", "aT", "extraVars",
                     "weightedHistName", "unweightedHistName",
                     "minSumWeightIn", "maxSumWeightIn",
                     "llk", "whiteList", "exampleKargs", "sigMcUnc",
                     ]+self._boxNames:
            setattr(self, "_"+item, eval(item))


    @property
    def name(self):
        out = self._dataset
        if self._tag:
            out += "_"+self._tag
        if self._com != 8:
            out += "_%d" % self._com
        return out

    @property
    def isSms(self):
        return not ("tanBeta" in self._dataset)

    @property
    def com(self):
        return self._com

    @property
    def interBin(self):
        return self._interBin

    @property
    def xsVariation(self):
        return self._xsVariation

    @property
    def xsFactors(self):
        return self._xsFactors

    @property
    def aT(self):
        return self._aT

    @property
    def extraVars(self):
        return self._extraVars

    @property
    def weightedHistName(self):
        return self._weightedHistName

    @property
    def unweightedHistName(self):
        return self._unweightedHistName

    @property
    def llk(self):
        return self._llk

    @property
    def whiteList(self):
        return self._whiteList

    @property
    def exampleKargs(self):
        return self._exampleKargs

    @property
    def sigMcUnc(self):
        return self._sigMcUnc

    def tags(self):
        out = [self.name]
        if not self.isSms:
            out.append(self.xsVariation)
        out += [self.llk] + self.whiteList
        return out

    def sumWeightInRange(self, sumWeightIn):
        out = True
        if self._minSumWeightIn is not None:
            out &= (self._minSumWeightIn <= sumWeightIn)
        if self._maxSumWeightIn is not None:
            out &= (sumWeightIn <= self._maxSumWeightIn)
        return out

    def boxes(self):
        out = []
        for boxName in self._boxNames:
            if getattr(self, "_" + boxName):
                out.append(boxName)
        return out


class signal(object):
    def __init__(self, xs=None, sumWeightIn=None, label="",
                 effUncRel=None, sigMcUnc=False,
                 lineColor=907, lineStyle=2,
                 x=None, y=None,
                 ):

        for item in ["xs", "sumWeightIn", "label", "effUncRel", "sigMcUnc",
                     "lineColor", "lineStyle", "x", "y"]:
            if item not in ["x", "y", "sumWeightIn"]:
                assert eval(item) != None, item
            setattr(self, item, eval(item))
        self.__selEffs = {}

    def effs(self, sel=""):
        return self.__selEffs.get(sel)

    def categories(self):
        return self.__selEffs.keys()

    def insert(self, key, value):
        self.__selEffs[key] = value

    def keyPresent(self, key=""):
        for dct in self.__selEffs():
            if key in dct.keys():
                return True
        return False

    def anyEffHad(self, key="effHadSum"):
        for dct in self.__selEffs.values():
            if dct.get(key):
                return True
        return False

    def __str__(self):
        out = []
        out.append("s = common.signal(xs=%g, sumWeightIn=%g, x=%s, y=%s)" %
                   (self.xs, self.sumWeightIn, self.x, self.y))
        for sel, dct in sorted(self.__selEffs.iteritems()):
            out.append('s.insert("%s", {' % sel)
            nChar = max([len(k) for k in dct.keys()])
            for key, value in sorted(dct.iteritems()):
                o = ('"%s":' % key).ljust(nChar+3)
                if type(value) is list:
                    s = ", ".join(["%8.2e" % x for x in value])
                    out.append('%s [%s],' % (o, s))
                else:
                    out.append('%s %g,' % (o, value))
            out.append("})")
        return "\n".join(out)

    def flattened(self):
        out = {}
        for item in ["xs", "x", "y", "sumWeightIn"]:
            out[item] = (getattr(self, item), '')

        for sel, dct in self.__selEffs.iteritems():
            for key, value in dct.iteritems():
                outKey = "%s_%s" % (sel, key)
                if type(value) in [float, int, bool]:
                    out[outKey] = (value, '')
                elif type(value) in [tuple, list]:
                    for i, x in enumerate(value):
                        out["%s_%d" % (outKey, i)] = (x, '')
                else:
                    assert False, type(value)
        return out
