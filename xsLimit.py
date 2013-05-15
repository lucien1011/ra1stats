#!/usr/bin/env python

import configuration as conf
import plottingGrid as pg

for model in conf.signal.models():
    pg.makeXsUpperLimitPlots(model=model,
                             logZ=True,
                             debug=False,
                             pruneYMin=True,
                             curveGopts="c",
                             #mDeltaFuncs={"mDeltaMin": 0.0,
                             #             "mDeltaMax": 400.0,
                             #             "nSteps": 4,
                             #             "mGMax": 1250.,
                             #             },
                             #diagonalLine=True,
                             expectedOnly=False,
                             )
    #pg.makeEfficiencyPlotBinned(model=model, key=["effHad", "effMuon"][0])
