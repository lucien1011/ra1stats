class point(object):
    def __init__(self, xs=None, sumWeightIn=None, label="",
                 sigMcUnc=False,
                 lineColor=907, lineStyle=2,
                 x=None, y=None,
                 ):

        for item in ["xs", "sumWeightIn", "label", "sigMcUnc",
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
        for _,dct in self.__selEffs.iteritems():
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
        out.append("s = signals.point(xs=%g, sumWeightIn=%g, x=%s, y=%s)" %
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
