import os
import sys
import math

import configuration as conf
import histogramProcessing as hp
import likelihoodSpec
import patches
import pickling
import refXsProcessing as rxs
import utils

import ROOT as r

def setupRoot() :
    #r.gROOT.SetStyle("Plain")
    r.gROOT.SetBatch(True)
    r.gErrorIgnoreLevel = 2000
    r.gStyle.SetPalette(1)
    #r.gStyle.SetPadTickX(True)
    #r.gStyle.SetPadTickY(True)

setupRoot()

def squareCanvas(margin = 0.18, ticks = True, name = "canvas", numbered = False) :
    canvas = (utils.numberedCanvas if numbered else r.TCanvas)(name, name, 2)
    for side in ["Left", "Right", "Top", "Bottom"] :
        getattr(canvas, "Set%sMargin"%side)(margin)
    canvas.SetTickx(ticks)
    canvas.SetTicky(ticks)
    return canvas

def adjustHisto(h, title = "") :
    h.SetStats(False)
    h.SetTitle(title)
    h.GetYaxis().SetTitleOffset(1.6)
    h.GetZaxis().SetTitleOffset(1.5)

def printOnce(model=None, canvas=None, fileName="", alsoC=False):
    text = r.TText()
    text.SetNDC()
    text.SetTextAlign(22)
    #text.DrawText(0.5, 0.85, "CMS")

    if model:
        latex = r.TLatex()
        latex.SetNDC()
        latex.SetTextAlign(22)
        current_stamp = conf.signal.processStamp(model.name)

        latex.SetTextSize(0.6*latex.GetTextSize())
        if current_stamp:
            latex.DrawLatex(current_stamp['xpos'], 0.78, current_stamp['text'])

    canvas.Print(fileName)
    utils.epsToPdf(fileName)
    if alsoC :
        canvas.Print(fileName.replace(".eps",".C"))

def setRange(var, ranges, histo, axisString) :
    if var not in ranges : return
    nums = ranges[var]
    getattr(histo,"Get%saxis"%axisString)().SetRangeUser(*nums[:2])
    if len(nums)==3 : r.gStyle.SetNumberContours(nums[2])
    if axisString=="Z" :
        maxContent = histo.GetBinContent(histo.GetMaximumBin())
        if maxContent>nums[1] :
            print "ERROR: histo truncated in Z (maxContent = %g, maxSpecified = %g) %s"%(maxContent, nums[1], histo.GetName())

def stamp(text = "#alpha_{T}, P.L., 1.1 fb^{-1}", x = 0.25, y = 0.55, factor = 1.3) :
    latex = r.TLatex()
    latex.SetTextSize(factor*latex.GetTextSize())
    latex.SetNDC()
    latex.DrawLatex(x, y, text)
    return latex

def pointsAtYMin(graph) :
    out = []
    x = graph.GetX()
    y = graph.GetY()
    if not graph.GetN() : return out
    yMin = min([y[i] for i in range(graph.GetN())])
    xsAtYMin = []
    for i in range(graph.GetN()) :
        if y[i]==yMin :
            out.append((x[i], y[i]))
    if len(out) :
        xMax = max([coords[0] for coords in out])
        xMin = min([coords[0] for coords in out])
        while (xMax,yMin) in out:
            out.remove((xMax,yMin))
        while (xMin,yMin) in out:
            out.remove((xMin,yMin))
    return out

def pruneGraph(graph, lst = [], debug = False, breakLink = False) :
    if debug: graph.Print()
    nRemoved = 0
    for p in lst:
        x = graph.GetX()
        y = graph.GetY()
        bad = []
        for i in range(graph.GetN()):
            if abs(p[0]-x[i]) < 1.0e-6 and abs(p[1]-y[i]) < 1.0e-6:
                bad.append(i-len(bad))
        nRemoved += len(bad)
        for i in bad:
            if debug :
                print "WARN: Removing point %d = (%g,%g) from %s"%(i, x[i], y[i], graph.GetName())
            graph.RemovePoint(i)
    if breakLink:
        graph.RemovePoint(graph.GetN()-1)
    if debug: graph.Print()
    if nRemoved :
        print "WARN: Removing %d points from graph %s"%(nRemoved, graph.GetName())

def modifyGraph(graph, dct = {}, debug = True) :
    if debug: graph.Print()
    for old,new in dct.iteritems() :
        x = graph.GetX()
        y = graph.GetY()
        for i in range(graph.GetN()):
            if abs(old[0]-x[i]) < 1.0e-6 and abs(old[1]-y[i]) < 1.0e-6:
                graph.SetPoint(i,new[0],new[1])
                print "WARN: Replacing point %d: (%g,%g) --> (%g,%g) from graph %s" % (i, old[0], old[1], new[0], new[1], graph.GetName())
    if debug: graph.Print()

def insertPoints( graph, lst=[], mode="prepend" ) :
    if not lst : return
    npoints = len(lst)
    ngraph = graph.GetN()

    total_points = npoints + ngraph
    graph.Expand(total_points)

    print "expanding graph", graph.GetName(), "with", graph.GetN(),
    print "points to have", total_points
    if mode=="prepend":
        for p in reversed(range(total_points)):
            if p < npoints:
                graph.SetPoint(p, lst[p][0], lst[p][1])
            else:
                x = r.Double(0.)
                y = r.Double(0.)
                graph.GetPoint(p-npoints,x,y)
                graph.SetPoint(p,x,y)
    elif mode=="append":
        for p in range(total_points):
            if p < ngraph:
                x = r.Double(0.)
                y = r.Double(0.)
                graph.GetPoint(p,x,y)
                graph.SetPoint(p,x,y)
            else:
                graph.SetPoint(p, *lst[p-ngraph])

def spline(points = [], title = "") :
    graph = r.TGraph()
    for i,(x,y) in enumerate(points) :
        graph.SetPoint(i, x, y)
    return r.TSpline3(title, graph)

def exclusionGraphs(model=None, histos={}, interBin="",
                    pruneYMin=False, debug=False):
    cutFunc = patches.cutFunc()[model.name]
    curves = patches.curves()[model.name]

    graphs = {}
    simpleExclHistos = {}
    for histoName, xsVariation in [("ExpectedUpperLimit_m1_Sigma", 0.0),
                                   ("ExpectedUpperLimit_p1_Sigma", 0.0),
                                   ("ExpectedUpperLimit",          0.0),
                                   ("UpperLimit",                  0.0),
                                   ("UpperLimit",                 -1.0),
                                   ("UpperLimit",                  1.0),
                                   ]:

        for xsFactor in model.xsFactors:
            graphName = histoName
            if xsVariation == 1.0:
                graphName += "_p1_Sigma"
            if xsVariation == -1.0:
                graphName += "_m1_Sigma"

            if curves:
                assert False, "FIXME"
                key = (spec["name"], model.xsVariation)
                if key in curves :
                    spec["curve"] = spline(points=curves[key])



            h = histos["%s_%s" % (model.name, histoName)]
            kargs = {"variation": xsVariation,
                     "xsFactor": xsFactor,
                     "model": model,
                     "interBin": interBin}
            graph = rxs.excludedGraph(h, **kargs)
            histo = rxs.excludedHistoSimple(h, **kargs)

            patchesKey = graphName.replace("m1", "-1").replace("p1", "+1")
            graphName += conf.signal.factorString(xsFactor)
            graph.SetName(graphName)
            histo.SetName(graphName+"_simpleExcl")

            pruneGraph(graph, debug=False, breakLink=pruneYMin,
                       lst=patches.graphBlackLists()[patchesKey][model.name]+(pointsAtYMin(graph) if pruneYMin else []))
            modifyGraph(graph, dct=patches.graphReplacePoints()[patchesKey][model.name], debug=False)
            insertPoints(graph, lst=patches.graphAdditionalPoints()[patchesKey][model.name])
            graphs[graphName] = graph
            simpleExclHistos[graphName] = histo
    return graphs, simpleExclHistos


def upperLimitHistos(model=None, inFileName="", shiftX=False, shiftY=False):
    assert len(conf.limit.CL()) == 1
    cl = conf.limit.CL()[0]
    ranges = conf.signal.ranges(model.name)

    #read and adjust histos
    f = r.TFile(inFileName)
    histos = {}
    for name, pretty in [("UpperLimit" if conf.limit.method() == "CLs" else "upperLimit95",
                          "upper limit"),
                         ("ExpectedUpperLimit", "expected upper limit"),
                         ("ExpectedUpperLimit_-1_Sigma", "title"),
                         ("ExpectedUpperLimit_+1_Sigma", "title")]:

        keyName = "%s_%s" % (model.name, name)
        h3 = f.Get(keyName)
        nameReplace = []
        if not h3:
            h3 = f.Get(name)
            if h3:
                print "WARNING: histo %s not found (using %s)" % (keyName, name)
                nameReplace = [(name, keyName)]
            else:
                continue

        h = utils.shifted(utils.threeToTwo(h3), shift = (shiftX, shiftY))
        hp.modifyHisto(h, model)
        title = conf.signal.histoTitle(model=model.name)
        title += ";%g%% CL %s on  #sigma (pb)"%(100.0*cl, pretty)
        adjustHisto(h, title = title)
        setRange("xRange", ranges, h, "X")
        setRange("yRange", ranges, h, "Y")
        if ranges["xDivisions"] : h.GetXaxis().SetNdivisions(*ranges["xDivisions"])
        if ranges["yDivisions"] : h.GetYaxis().SetNdivisions(*ranges["yDivisions"])
        rename(h, nameReplace=nameReplace)
        hp.printHoles(h)
        histos[h.GetName()] = h
    f.Close()
    return histos

def rename(h, nameReplace=[]):
    name = h.GetName()
    for old, new in nameReplace + [("+", "p"),
                                   ("-", "m"),
                                   ("upper", "Upper"),
                                   ("95", ""),
                                   ("_shifted", ""),
                                   ("_2D", "")]:
        name = name.replace(old, new)
    h.SetName(name)

def writeList(fileName = "", objects = []) :
    f = r.TFile(fileName, "RECREATE")
    for obj in objects :
        obj.Write()
    f.Close()

def outFileName(model=None, tag=""):
    base = pickling.mergedFile(model=model).split("/")[-1]
    root = conf.directories.plot()+"/"+base.replace(".root", "_%s.root"%tag)
    return {"root":root,
            "eps" :root.replace(".root",".eps"),
            "pdf" :root.replace(".root",".pdf"),
            }

def makeRootFiles(model=None, limitFileName="", simpleFileName="",
                  shiftX=None, shiftY=None, interBin="",
                  pruneYMin=None):
    for item in ["shiftX", "shiftY", "interBin", "pruneYMin"] :
        assert eval(item)!=None,item
    histos = upperLimitHistos(model=model,
                              inFileName=pickling.mergedFile(model=model),
                              shiftX=shiftX,
                              shiftY=shiftY)
    graphs, simple = exclusionGraphs(model=model,
                                     histos=histos,
                                     interBin=interBin,
                                     pruneYMin=pruneYMin)
    writeList(fileName=limitFileName, objects=histos.values()+graphs.values())
    writeList(fileName=simpleFileName, objects=simple.values())

def makeXsUpperLimitPlots(model=None, logZ=False, curveGopts="", mDeltaFuncs={},
                          diagonalLine=False, pruneYMin=False,
                          expectedOnly=False, debug=False):

    limitFileName = outFileName(model=model,
                                tag="xsLimit")["root"]
    simpleFileName = outFileName(model=model,
                                 tag="xsLimit_simpleExcl")["root"]

    shift = model.interBin == "LowEdge"
    makeRootFiles(model=model, limitFileName=limitFileName,
                  simpleFileName=simpleFileName,
                  shiftX=shift, shiftY=shift, interBin="Center",
                  pruneYMin=pruneYMin)

    specs = [
        {"name":"ExpectedUpperLimit", "label":"Expected Limit",
         "lineStyle":7, "lineWidth":3, "color":r.kViolet},
        ]
    if not expectedOnly:
        specs[0]["label"] += " #pm1 #sigma exp."
        specs = [
            {"name":"ExpectedUpperLimit_m1_Sigma", "label":"",
             "lineStyle":2, "lineWidth":2, "color":r.kViolet},
            {"name":"ExpectedUpperLimit_p1_Sigma", "label":"",
             "lineStyle":2, "lineWidth":2, "color":r.kViolet},
            ] + specs + [
            {"name":"UpperLimit",                  "label":"#sigma^{NLO+NLL} #pm1 #sigma theory",
             "lineStyle":1, "lineWidth":3, "color":r.kBlack},
            {"name":"UpperLimit_m1_Sigma",         "label":"",
             "lineStyle":1, "lineWidth":1, "color":r.kBlack},
            {"name":"UpperLimit_p1_Sigma",         "label":"",
             "lineStyle":1, "lineWidth":1, "color":r.kBlack},
            ]

    makeLimitPdf(model=model,
                 rootFileName=limitFileName,
                 specs=specs,
                 diagonalLine=diagonalLine,
                 logZ=logZ,
                 curveGopts=curveGopts,
                 mDeltaFuncs=mDeltaFuncs,
                 )

    makeSimpleExclPdf(model=model,
                      histoFileName=simpleFileName,
                      graphFileName=limitFileName,
                      specs=specs,
                      curveGopts=curveGopts,
                      )

def makeLimitPdf(model=None, rootFileName="", diagonalLine=False, logZ=False,
                 curveGopts="", mDeltaFuncs=False, specs=[]):

    ranges = conf.signal.ranges(model.name)

    epsFile = rootFileName.replace(".root", ".eps")
    f = r.TFile(rootFileName)

    c = squareCanvas()

    expectedOnly = len(specs) == 1
    if conf.limit.method() == "CLs":
        if conf.limit.binaryExclusion():
            # FIXME: handle expected
            hName = "excluded_CLs_95"
        elif expectedOnly:
            hName = "ExpectedUpperLimit"
        else:
            hName = "UpperLimit"
    else:
        hName = "upperLimit95"
    h = f.Get("%s_%s" % (model.name, hName))
    h.Draw("colz")

    if logZ :
        c.SetLogz()
        setRange("xsZRangeLog", ranges, h, "Z")
    else :
        setRange("xsZRangeLin", ranges, h, "Z")
        epsFile = epsFile.replace(".eps", "_linZ.eps")

    graphs = []
    for xsFactor in model.xsFactors:
        for d in specs:
            graph = f.Get(d["name"]+conf.signal.factorString(xsFactor))
            if not graph:
                continue
            graph.SetLineColor(d["color"])
            graph.SetLineWidth(d["lineWidth"])
            graph.SetLineStyle(d["lineStyle"])
            graphs.append({"graph":graph, "label":d["label"]})

        if curveGopts:
            stuff = rxs.drawGraphs(graphs, gopts=curveGopts)
        else:
            epsFile = epsFile.replace(".eps", "_noRef.eps")

    if diagonalLine :
        yx = r.TF1("yx", "x", ranges["xRange"][0], ranges["xMaxDiag"])
        yx.SetLineColor(1)
        yx.SetLineStyle(3)
        yx.SetLineWidth(2)
        yx.Draw("same")

    if mDeltaFuncs :
        epsFile = epsFile.replace(".eps", "_mDelta.eps")
        funcs = rxs.mDeltaFuncs(**mDeltaFuncs)
        for func in funcs :
            func.Draw("same")

    s3 = stamp(text = likelihoodSpec.likelihoodSpec(model.name).legendTitle(),
               x=0.2075, y=0.64, factor=0.65)
    printOnce(model=model, canvas=c, fileName=epsFile, alsoC=True)
    f.Close()

def makeSimpleExclPdf(model=None, histoFileName="", graphFileName="",
                      specs=[], curveGopts=""):
    ranges = conf.signal.ranges(model.name)

    c = squareCanvas()
    pdf = histoFileName.replace(".root", ".pdf")

    hFile = r.TFile(histoFileName)
    gFile = r.TFile(graphFileName)

    c.Print(pdf+"[")
    for xsFactor in model.xsFactors:
        for d in specs:
            name = d["name"]+conf.signal.factorString(xsFactor)
            foo = {'color': 880, 'lineWidth': 2, 'lineStyle': 2, 'name': 'ExpectedUpperLimit_m1_Sigma', 'label': ''}
            h = hFile.Get(name+"_simpleExcl")
            if not h : continue
            h.Draw("colz")
            h.SetMinimum(-1.0)
            h.SetMaximum(1.0)
            h.SetTitle(name)
            r.gPad.SetGridx()
            r.gPad.SetGridy()

            g = gFile.Get(name)
            if g and curveGopts:
                g.SetMarkerColor(r.kBlack)
                g.SetMarkerStyle(20)
                g.SetMarkerSize(0.3*g.GetMarkerSize())
                g.SetLineColor(r.kYellow)
                g.SetLineStyle(1)
                g.Draw("%spsame"%curveGopts)
            if d.get("curve") and d["curve"].GetNp():
                d["curve"].SetMarkerStyle(20)
                d["curve"].SetMarkerSize(0.3*d["curve"].GetMarkerSize())
                d["curve"].Draw("lpsame")
            c.Print(pdf)

    c.Print(pdf+"]")
    print "INFO: %s has been written."%pdf
    hFile.Close()
    gFile.Close()

def efficiencyHistos(model=None, key=""):
    out = {}
    for cat, dct in pickling.effHistos(model).iteritems():
        total = None
        for histo in dct[key]:
            if not total:
                total = histo.Clone("%s_%s" % (cat, key))
            else:
                total.Add(histo)
        out[cat] = total
    return out

def makeEfficiencyPlotBinned(model=None, key="effHad"):
    def prep(p) :
        p.SetTopMargin(0.15)
        p.SetBottomMargin(0.15)
        p.SetLeftMargin(0.15)
        p.SetRightMargin(0.15)

    can = r.TCanvas("canvas", "canvas", 400, 1000)
    can.Divide(2, 5)

    dct = efficiencyHistos(model=model, key=key)
    maximum = max([h.GetMaximum() for h in dct.values()])
    keep = []
    pad = {0:2, 1:1, 2:4, 3:3, 4:6, 5:5, 6:8, 7:7, 8:10}

    label = "%s_%s"%(model.name, key)
    total = None
    for i,(cat,h) in enumerate(sorted(dct.iteritems())) :
        can.cd(pad[i])
        prep(r.gPad)

        h2 = utils.threeToTwo(h)
        keep.append(h2)
        h2.SetTitle(cat)
        h2.SetStats(False)
        h2.SetMinimum(0.0)
        h2.SetMaximum(maximum)
        h2.Draw("colz")

        if not total :
            total = h2.Clone(label)
        else :
            total.Add(h2)
        #h2.GetListOfFunctions().FindObject("palette").GetAxis().SetTitle("")

    can.cd(9)
    prep(r.gPad)

    total.Draw("colz")
    total.SetTitle("%s#semicolon max = %4.2f"%(label, total.GetMaximum()))

    can.cd(0)
    can.Print("%s.pdf"%label)

def makeEfficiencyPlot(model=None):
    if not model.isSms:
        return

    inFile = pickling.mergedFile(model=model)
    f = r.TFile(inFile)
    fileName = inFile.replace(".root","_efficiency.eps")

    c = squareCanvas()

    h3 = None
    for item in f.GetListOfKeys() :
        h = f.Get(item.GetName())
        if "effHadSum" not in h.GetName() : continue

        if not h3 :
            h3 = h.Clone("eff")
            h3.SetDirectory(0)
        else :
            h3.Add(h)
    f.Close()

    h2 = utils.threeToTwo(h3)
    assert h2

    hp.modifyHisto(h2, model)

    title = conf.signal.histoTitle(model=model.name)
    title += ";A #times #epsilon"
    adjustHisto(h2, title = title)

    #output a root file
    g = r.TFile(fileName.replace(".eps",".root"), "RECREATE")
    h2.Write()
    g.Close()

    ranges = conf.signal.ranges(model.name)
    setRange("xRange", ranges, h2, "X")
    setRange("yRange", ranges, h2, "Y")

    h2.Draw("colz")

    printName = fileName
    setRange("effZRange", ranges, h2, "Z")

    s2 = stamp(text = "#alpha_{T}", x = 0.22, y = 0.55, factor = 1.3)

    printOnce(model=model, canvas=c, fileName=printName)
    hp.printHoles(h2)

def printTimeStamp() :
    text = r.TText()
    text.SetNDC()
    text.DrawText(0.1, 0.1, "file created at %s"%r.TDatime().AsString())
    text.DrawText(0.1, 0.35, "[restore useful info here]")
    #text.DrawText(0.1, 0.35, "REwk = %s"%(l["REwk"] if l["REwk"] else "[no form assumed]"))
    #text.DrawText(0.1, 0.30, "RQcd = %s"%(l["RQcd"] if l["RQcd"] else "[no form assumed]"))
    #text.DrawText(0.1, 0.25, "nFZinv = %s"%(l["nFZinv"].replace("fZinv","")))
    return text

def printSuppressed(l) :
    text = r.TText()
    text.SetTextSize(0.3*text.GetTextSize())
    text.SetNDC()
    text.DrawText(0.1, 0.9, "empty histograms: %s"%str(l))
    return text

def printLumis() :
    text = r.TText()
    text.SetNDC()
    text.SetTextFont(102)
    text.SetTextSize(0.5*text.GetTextSize())

    x = 0.1
    y = 0.9
    s = 0.035
    text.DrawText(x, y  , "restore useful info here")
    return text

    text.DrawText(x, y  , "sample     lumi (/pb)")
    text.DrawText(x, y-s, "---------------------")
    inputData = conf.data()
    i = 1
    d = inputData.lumi()
    for key in sorted(d.keys()) :
        i += 1
        text.DrawText(x, y-i*s, "%8s       %6.0f"%(key, d[key]))
    text.DrawText(x, y-(i+1)*s, "HT bins: %s"%str(inputData.htBinLowerEdges()))
    return text

def drawBenchmarks(model=None):
    parameters = conf.signal.scanParameters()
    if not (model in parameters):
        return

    params = parameters[model.name]

    text = r.TText()
    out = []
    for label, coords in conf.signal.benchmarkPoints().iteritems():
        drawIt = True
        for key, value in coords.iteritems():
            if key in params and value != params[key]:
                drawIt = False
        if not drawIt:
            continue
        marker = r.TMarker(coords["m0"], coords["m12"], 20)
        marker.Draw()
        out.append(marker)
        out.append(text.DrawText(10+coords["m0"], 10+coords["m12"], label))
    return out

def printOneHisto(h2=None, name="", canvas=None, fileName="",
                  effRatioPlots=False, drawBenchmarkPoints=False,
                  logZ=[], model=None, suppressed=[]):
    if "upper" in name :
        hp.printHoles(h2)
    h2.SetStats(False)
    h2.SetTitle("%s%s"%(name, conf.signal.histoTitle(model=model.name)))
    h2.Draw("colz")
    if not h2.Integral() :
        suppressed.append(name)
        return

    canvas.SetLogz(name in logZ)
    if name=="xs" and name in logZ : h2.SetMinimum(1.0e-2)
    if name=="nEventsHad" and name in logZ : h2.SetMinimum(0.9)
    if "NLO_over_LO" in name :
        h2.SetMinimum(0.5)
        h2.SetMaximum(3.0)

    if drawBenchmarkPoints:
        stuff = drawBenchmarks(model)

    if "excluded" in name and model.isSms:
        return

    printSinglePage  = (not model.isSms) and "excluded" in name
    printSinglePage |= model.isSms and "upperLimit" in name

    if printSinglePage :
        title = h2.GetTitle()
        h2.SetTitle("")
#        eps = fileName.replace(".ps","_%s.eps"%name)
#        super(utils.numberedCanvas, canvas).Print(eps)
#        utils.epsToPdf(eps)
        pdf_fileName = fileName.replace(".pdf","_%s.pdf"%name)
        super(utils.numberedCanvas, canvas).Print(pdf_fileName)
        h2.SetTitle(title)

    canvas.Print(fileName)
    minEventsIn, maxEventsIn = conf.signal.nEventsIn(model.name)
    if "nEventsIn" in name and (minEventsIn or maxEventsIn):
        if minEventsIn : h2.SetMinimum(minEventsIn)
        if maxEventsIn : h2.SetMaximum(maxEventsIn)
        canvas.Print(fileName)

    #effMu/effHad
    if effRatioPlots:
        for name in names :
            num = utils.threeToTwo(f.Get(name))
            if name[:7]!="effmuon" : continue
            denName = name.replace("muon", "had")
            den = utils.threeToTwo(f.Get(denName))
            num.Divide(den)
            num.SetStats(False)
            num.SetTitle("%s/%s%s;"%(name, denName, conf.signal.histoTitle(model=model.name)))
            num.Draw("colz")
            if not num.Integral() : continue
            num.SetMinimum(0.0)
            num.SetMaximum(0.5)
            if drawBenchmarkPoints:
                stuff = drawBenchmarks(model)
            canvas.Print(fileName)

def sortedNames(histos = [], first = [], last = []) :
    start = []
    end = []
    names = sorted([histo.GetName() for histo in histos])
    for name in names :
        for item in first :
	        if item==name[:len(item)] :
	            start.append(name)
        for item in last :
	        if item==name[:len(item)] :
	            end.append(name)

    for item in list(set(start+end)) :
        names.remove(item)
    return start+names+end

def multiPlots(model=None, tag="", first=[], last=[], whiteListMatch=[], blackListMatch=[],
               outputRootFile=False, modify=False, square=False):
    assert tag

    inFile = pickling.mergedFile(model=model)
    f = r.TFile(inFile)
    r.gROOT.cd()

    fileNames = outFileName(model=model, tag=tag)
    fileName = fileNames["pdf"]

    if square :
        canvas = squareCanvas(numbered = True)
    else :
        canvas = utils.numberedCanvas()
        canvas.SetRightMargin(0.15)

    canvas.Print(fileName+"[")
    canvas.SetTickx()
    canvas.SetTicky()

    text1 = printTimeStamp()
    text2 = printLumis()
    canvas.Print(fileName)
    canvas.Clear()

    names = sortedNames(histos = f.GetListOfKeys(), first = first, last = last)

    if outputRootFile :
        outFile = r.TFile(fileNames["root"], "RECREATE")
        r.gROOT.cd()

    suppressed = []
    for name in names :
        if whiteListMatch and not any([item in name for item in whiteListMatch]) : continue
        if any([item in name for item in blackListMatch]) : continue

        h2 = utils.threeToTwo(f.Get(name))
        if modify:
            hp.modifyHisto(h2, model)
        printOneHisto(h2=h2, name=name, canvas=canvas, fileName=fileName,
                      logZ=["xs", "nEventsHad"], model=model,
                      suppressed=suppressed)
        if outputRootFile :
            outFile.cd()
            h2.Write()
            r.gROOT.cd()

    if outputRootFile :
        print "%s has been written."%fileNames["root"]
        outFile.Close()

    canvas.Clear()
    text3 = printSuppressed(suppressed)
    canvas.Print(fileName)

    canvas.Print(fileName+"]")

    print "%s has been written."%fileName

def clsValidation(model=None, cl=None, tag="", masterKey="",
                  yMin=0.0, yMax=1.0, lineHeight=0.5,
                  divide=(4,3), whiteList=[], stampTitle=True):
    def allHistos(fileName = "") :
        f = r.TFile(fileName)
        r.gROOT.cd()
        out = {}
        for key in f.GetListOfKeys() :
            name = key.GetName()
            out[name] = utils.threeToTwo(f.Get(name))
            out[name].SetDirectory(0)
        f.Close()
        return out

    assert tag
    assert masterKey
    assert cl
    if whiteList :
        assert len(whiteList)==divide[0]*divide[1], "%d != %d"%(len(whiteList), divide[0]*divide[1])

    # FIXME: remove hard-coded 2
    specialKey = "%s_CLb_2" % model.name
    histos = allHistos(fileName=pickling.mergedFile(model=model))
    master = histos[model.name+"_"+masterKey]
    graphs = {}
    for iBinX in range(1, 1 + master.GetNbinsX()) :
        for iBinY in range(1, 1 + master.GetNbinsY()) :
            if whiteList and (iBinX, iBinY) not in whiteList : continue
            if not master.GetBinContent(iBinX, iBinY) : continue
            if specialKey not in histos or not histos[specialKey] : continue
            if not histos[specialKey].GetBinContent(iBinX, iBinY) : continue

            name = "%s_CLs_%d_%d"%(model.name, iBinX, iBinY)
            graph = r.TGraphErrors()
            graph.SetName(name)
            graph.SetTitle("%s;#sigma (pb);CL_{s}"%(name.replace("CLs_","") if stampTitle else ""))
            graph.SetMarkerStyle(20)
            graph.SetMinimum(yMin)
            graph.SetMaximum(yMax)
            iPoint = 0
            while True:
                s = "" if not iPoint else "_%d"%iPoint
                if "%s_CLs%s" % (model.name, s) not in histos:
                    break
                x = histos["%s_PoiValue%s" % (model.name, s)].GetBinContent(iBinX, iBinY)
                if not iPoint:
                    xMin = x
                xMax = x
                graph.SetPoint(iPoint, x, histos["%s_CLs%s" % (model.name, s)].GetBinContent(iBinX, iBinY))
                graph.SetPointError(iPoint, 0.0, histos["%s_CLsError%s" %(model.name, s)].GetBinContent(iBinX, iBinY))
                iPoint += 1

            e = 0.1*(xMax-xMin)
            y = 1.0 - cl
            clLine = r.TLine(xMin-e, y, xMax+e, y)
            clLine.SetLineColor(r.kRed)

            xLim = histos["%s_UpperLimit" % model.name].GetBinContent(iBinX, iBinY)
            limLine = r.TLine(xLim, yMin, xLim, yMax*lineHeight)
            limLine.SetLineColor(r.kBlue)
            graphs[name] = [graph, clLine, limLine]

            if not whiteList :
                xLimPl = histos["%s_PlUpperLimit" % model.name].GetBinContent(iBinX, iBinY)
                plLimLine = r.TLine(xLimPl, yMin, xLimPl, yMax*lineHeight)
                plLimLine.SetLineColor(r.kGreen)
                graphs[name].append(plLimLine)

    fileName = outFileName(model=model,
                           tag=tag+"_"+str(cl).replace("0.",""))["pdf"]
    if whiteList :
        fileName = fileName.replace(".pdf", ".eps")
        canvas = r.TCanvas("canvas", "", 500*divide[0], 500*divide[1])
    else :
        canvas = utils.numberedCanvas()
        canvas.Print(fileName+"[")
        text1 = printTimeStamp()
        text2 = printLumis()
        canvas.Print(fileName)
        canvas.Clear()

    canvas.SetRightMargin(0.15)
    utils.cyclePlot(d = graphs, f = None, args = {}, optStat = 1110, canvas = canvas, fileName = fileName, divide = divide, goptions = "alp")

    if whiteList :
        utils.epsToPdf(fileName, sameDir = True)
        print "%s has been written."%fileName.replace(".eps", ".pdf")
    else :
        canvas.Print(fileName+"]")
        print "%s has been written."%fileName

def makePlots(square=False):
    for model in conf.signal.models():
        multiPlots(model=model,
                   tag="validation",
                   first=["excluded", "upperLimit", "CLs", "CLb", "xs"],
                   last=["lowerLimit"],
                   blackListMatch=["eff", "_nEvents"],
                   square=square)

    	#multiPlots(model=model,
    	#           tag="nEvents",
    	#           whiteListMatch=["nEvents"],
    	#           square=square)
    	#
    	#multiPlots(model=model,
    	#           tag="effHad",
    	#           whiteListMatch=["effHad"],
    	#           blackListMatch=["UncRel"],
    	#           outputRootFile=True,
    	#           modify=True,
    	#           square=square)
    	#
    	#multiPlots(model=model,
    	#           tag="effMu",
    	#           whiteListMatch=["effMu"],
    	#           blackListMatch=["UncRel"],
    	#           outputRootFile=True,
    	#           modify=True,
    	#           square=square)
    	#
    	#multiPlots(model=model,
    	#           tag="xs",
    	#           whiteListMatch=["xs"],
    	#           outputRootFile=True,
    	#           modify=True,
    	#           square=square)

    	if model.isSms and conf.limit.method() == "CLs":
    	    for cl in conf.limit.CL():
    	        clsValidation(model=model,
    	                      tag="clsValidation",
    	                      cl=cl,
    	                      masterKey="xs")
