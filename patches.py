import collections

def cmssmCut(iX, x, iY, y, iZ, z) :
    def yMin(x) :
        return 450.0 - (300.0)*(x-500.0)/(1200.0-500.0)

    def yMax(x) :
        return 750.0 - (250.0)*(x-500.0)/(1200.0-500.0)

    if 0.0 <= x <=  500.0 :
        return  500.0 <= y <= 700.0

    if  500.0 <= x <= 1200.0 :
        return yMin(x) <= y <= yMax(x)

    if 1200.0 <= x <= 1500.0:
        return 200.0 <= y <= 450.0

    if 1500.0 <= x:
        return 200.0 <= y <= 400.0

def cutFunc() :
    return {"T1":lambda iX,x,iY,y,iZ,z:(y<(x-150.1) and iZ==1 and x>287.4),
            "T2":lambda iX,x,iY,y,iZ,z:(y<(x-150.1) and iZ==1 and x>287.4 and x<1300.0),
            "T2tt":lambda iX,x,iY,y,iZ,z:(y<(x-150.1) and iZ==1 and x>287.4 and x<900.0 and x<500.0),
            "T2bb":lambda iX,x,iY,y,iZ,z:(y<(x-150.1) and iZ==1 and x>287.4 and x<1300.0),
            "T2bw":lambda iX,x,iY,y,iZ,z:(y<(x-150.1) and iZ==1 and x>287.4),
            "T5zz":lambda iX,x,iY,y,iZ,z:(y<(x-200.1) and iZ==1 and x>399.9),
            "T1bbbb":lambda iX,x,iY,y,iZ,z:(y<(x-150.1) and iZ==1 and x>287.4),
            "T1tttt":lambda iX,x,iY,y,iZ,z:(y<(x-150.1) and iZ==1 and x>287.4),
            "T1tttt_ichep":lambda iX,x,iY,y,iZ,z:(y<(x-150.1) and iZ==1 and x>287.4),
            "tanBeta10":cmssmCut,
            }

def curves() :
    return {"tanBeta10":{
            ("ExpectedUpperLimit",          "default"): [( 120, 594), ( 160, 595), ( 240, 595), ( 320, 590), ( 400, 580), ( 480, 567),
                                                         ( 560, 550), ( 640, 530), ( 720, 500), ( 800, 465), ( 880, 423),
                                                         ( 960, 370), (1040, 342), (1120, 325), (1200, 310), (1280, 300),
                                                         (1360, 295), (1440, 293), (1520, 290), (1600, 287), (1680, 285),
                                                         (1760, 283), (1840, 280), (1920, 275), (2000, 269), (2080, 265),
                                                         (2160, 262), (2240, 260), (2320, 260), (2400, 260), (2480, 260),
                                                         (2560, 260), (2640, 265), (2720, 273), (2800, 282), (2880, 290),
                                                         (2960, 300),],
            ("ExpectedUpperLimit_-1_Sigma", "default"): [( 130, 630), ( 160, 630), ( 240, 635), ( 320, 635), ( 400, 630), ( 480, 620),
                                                         ( 560, 608), ( 640, 590), ( 720, 565), ( 800, 535), ( 880, 500),
                                                         ( 960, 440), (1040, 388), (1120, 365), (1200, 359), (1280, 350),
                                                         (1360, 340), (1440, 330), (1520, 328), (1600, 325), (1680, 322),
                                                         (1760, 321), (1840, 319), (1920, 315), (2000, 310), (2080, 305),
                                                         (2160, 300), (2240, 295), (2320, 292), (2400, 290), (2480, 290),
                                                         (2560, 290), (2640, 294), (2720, 300), (2800, 305), (2880, 310),
                                                         (2960, 315),],
            ("ExpectedUpperLimit_+1_Sigma", "default"): [( 130, 570), ( 160, 570), ( 240, 570), ( 320, 565), ( 400, 550), ( 480, 530),
                                                         ( 560, 505), ( 640, 475), ( 720, 430), ( 800, 390), ( 880, 360),
                                                         ( 960, 336), (1040, 318), (1120, 300), (1200, 280), (1280, 265),
                                                         (1360, 260), (1440, 254), (1520, 250), (1600, 250), (1680, 250),
                                                         (1760, 250), (1840, 250), (1920, 250), (2000, 249), (2080, 247),
                                                         (2160, 244), (2240, 240), (2320, 237), (2400, 235), (2480, 235),
                                                         (2560, 237), (2640, 243), (2720, 253), (2800, 265), (2880, 278),
                                                         (2960, 288),],
            ("UpperLimit",                  "default"): [( 120, 629), ( 160, 630), ( 240, 630), ( 320, 625), ( 400, 610), ( 480, 590),
                                                         ( 560, 570), ( 640, 545), ( 720, 520), ( 800, 490), ( 880, 448),
                                                         ( 960, 392), (1040, 355), (1120, 338), (1200, 328), (1280, 319),
                                                         (1360, 309), (1440, 300), (1520, 295), (1600, 292), (1680, 290),
                                                         (1760, 290), (1840, 289), (1920, 287), (2000, 286), (2080, 283),
                                                         (2160, 280), (2240, 280), (2320, 278), (2400, 275), (2480, 275),
                                                         (2560, 276), (2640, 279), (2720, 281), (2800, 285), (2880, 290),
                                                         (2960, 300),],
            ("UpperLimit",                  "up"     ): [( 120, 629), ( 160, 630), ( 240, 630), ( 320, 630), ( 400, 623), ( 480, 610),
                                                         ( 560, 590), ( 640, 570), ( 720, 545), ( 800, 515), ( 880, 480),
                                                         ( 960, 435), (1040, 395), (1120, 355), (1200, 340), (1280, 330),
                                                         (1360, 320), (1440, 315), (1520, 308), (1600, 306), (1680, 303),
                                                         (1760, 300), (1840, 297), (1920, 295), (2000, 295), (2080, 293),
                                                         (2160, 290), (2240, 289), (2320, 288), (2400, 287), (2480, 286),
                                                         (2560, 287), (2640, 290), (2720, 293), (2800, 298), (2880, 303),
                                                         (2960, 310),],
            ("UpperLimit",                  "down"   ): [( 120, 614), ( 160, 615), ( 240, 615), ( 320, 608), ( 400, 590), ( 480, 570),
                                                         ( 560, 550), ( 640, 525), ( 720, 495), ( 800, 455), ( 880, 415),
                                                         ( 960, 355), (1040, 335), (1120, 320), (1200, 311), (1280, 302),
                                                         (1360, 295), (1440, 287), (1520, 283), (1600, 280), (1680, 280),
                                                         (1760, 279), (1840, 278), (1920, 277), (2000, 274), (2080, 270),
                                                         (2160, 268), (2240, 268), (2320, 267), (2400, 266), (2480, 265),
                                                         (2560, 265), (2640, 265), (2720, 270), (2800, 275), (2880, 283),
                                                         (2960, 292),],
            }
            }

def overwriteInput() :
    return collections.defaultdict(list)

def overwriteOutput() :
    out = collections.defaultdict(list)
    out.update({"T1": [(35, 25, 1, "ew"),
                       (41, 10, 1, "ew"),
                       (41,  9, 1, "ew"),
                       (41,  8, 1, "ew"),
                       (41,  7, 1, "ew"),
                       (41,  6, 1, "ew"),
                       (41,  5, 1, "ew"),
                       (41,  4, 1, "ew"),
                       (41,  3, 1, "ew"),
                       (41,  2, 1, "ew"),
                       (41,  1, 1, "ew"),
                       (69,  2, 1, "ew"),
                       ],
                "T2": [(38, 22, 1), (44, 29, 1),],
                "T2bb": [(33,  5, 1, "ns"),
                         (34,  5, 1, "ns"),
                         (34,  8, 1, "ns"),
                         (35, 10, 1, "ns"),
                       ],
                "T1bbbb": [(14,  6, 1, "ew"),
                           (40, 22, 1, "ew"),
                           (40, 23, 1, "ew"),
                           (40, 24, 1, "ew"),
                           (40, 25, 1, "ew"),
                           (40, 26, 1, "ew"),
                           (40, 27, 1, "ew"),
                           (40, 28, 1, "ew"),
                           (40, 29, 1, "ew"),
                           (40, 30, 1, "ew"),
                           (40, 31, 1, "ew"),
                           (40, 32, 1, "ew"),

                           (41,  1, 1, "ew"),
                           (41,  2, 1, "ew"),
                           (41,  3, 1, "ew"),
                           (41,  4, 1, "ew"),
                           (41,  5, 1, "ew"),
                           (41,  6, 1, "ew"),
                           (41,  7, 1, "ew"),
                           (41,  8, 1, "ew"),
                           (41,  9, 1, "ew"),
                           (41, 10, 1, "ew"),
                           (41, 11, 1, "ew"),
                           (41, 12, 1, "ew"),
                           (41, 13, 1, "ew"),
                           (41, 14, 1, "ew"),
                           (41, 15, 1, "ew"),
                           (41, 16, 1, "ew"),

                           (69, 39, 1, "ew"),
                           (69, 40, 1, "ew"),
                           (69, 41, 1, "ew"),
                           (69, 42, 1, "ew"),
                           (69, 43, 1, "ew"),
                           (69, 44, 1, "ew"),
                           (69, 45, 1, "ew"),
                           (69, 46, 1, "ew"),
                           (69, 47, 1, "ew"),
                           (69, 48, 1, "ew"),
                           (69, 49, 1, "ew"),
                           (69, 50, 1, "ew"),
                           (69, 51, 1, "ew"),
                           (69, 52, 1, "ew"),
                           (69, 53, 1, "ew"),
                           (69, 54, 1, "ew"),
                           (69, 55, 1, "ew"),
                           (69, 56, 1, "ew"),
                           (69, 57, 1, "ew"),
                           (69, 58, 1, "ew"),
                           ],
                "T1tttt":[(56, 8, 1),(76, 9, 1)],
                "T2tt": [(80,  3, 1, "ew"),
                         (80,  4, 1, "ew"),
                         (80, 13, 1, "ew"),
                         (80, 14, 1, "ew"),
                         (80, 15, 1, "ew"),
                         (80, 16, 1, "ew"),
                         (80, 17, 1, "ew"),
                         (80, 18, 1, "ew"),
                         (80, 19, 1, "ew"),
                         (80, 20, 1, "ew"),
                         ],
                })
    return out

def graphBlackLists() :
    out = {}
    keys  = [ "UpperLimit", "ExpectedUpperLimit" ]
    keys += [ "ExpectedUpperLimit_%+d_Sigma" % i for i in [-1,1] ]
    keys += [ "UpperLimit_%+d_Sigma" % i for i in [-1,1] ]
    for key in keys :
        out[key] = collections.defaultdict(list)

    out["ExpectedUpperLimit_-1_Sigma"].update({"T1": [(1150,425), (1100,300), (1100,350), (1100,375), (875, 550),
                                                      (825, 600), (850,600), (875,600), (800,550), (750,550), (950,525),
                                                      (1000,525), (1050, 500), (925,550),
                                                      ],
                                               "T2": [(950,175), (925,100), (875,300), (550,375), (575,350),(600,350),
                                                      (525,350), (650,375), (675,400), (825,325), (775,375),
                                                      ],
                                               "T2bb":[(450,250), (500,275), (550,275), (575,275), (600,275), (750,50), (650,250),
                                                       ],
                                               "T1bbbb":[(1225,100), (900,675), (1000,725), (950,725), (875,675), (925,700),
                                                         (1025,750), (1050,750), (1100,700), (1150,650), (1125,725),
                                                         (1200,650),
                                                         ],
                                               "T1tttt":[(475,125), (425,50), (525,125), (650,225), (725,300),
                                                         (750,300), (800,350), (825,350), (875,400), (925,400),
                                                         (950,425), (1100,400), (1000,425), (1050,425),
                                                         ],
                                               })
    out["ExpectedUpperLimit"].update({"T1": [(1000,525),(1075,400), (725,500), (700,525), (950,525),
                                             (875,550), (825,550), (900,525), (800,525), (775,525),
                                             ],
                                      "T2":[(500,300), (600,325), (575,325), (550,325), (725,325), (700,350), (750,325),
                                            (800,300), (850,225), (475,300),
                                            ],
                                      "T2bb": [(700,150), (675,200), (650,150), (600,250), (425,250), (450,225),
                                               (525,225), (550,250), (500,250), (625,250),
                                               ],
                                      "T1bbbb":[(1125,625), (850,650), (925,675), (900,675), (975,700), (825,650),
                                                (1100,700), (1200,575),
                                                ],
                                       "T1tttt":[(1075,250), (525,100), (425,50), (650,225), (750,300), (800,325),
                                                 (950,375), (1000,375), (925,400), (1025,400), (850,375), (1075,325)
                                                 ],
                                      })
    out["ExpectedUpperLimit_+1_Sigma"].update({"T1": [(1000,450), (700,475), (775,500), (725,500), (700,525),
                                                      (950,450), (800,525), (850,525), (875,500), (925,475),
                                                      ],
                                               "T2": [(450,275), (550,275), (625,300), (525,275), (500,275), (575,300),
                                                      (675,325), (700,300), (750,275),
                                                      ],
                                               "T2bb": [(400,200), (525,200), (650, 25), (575,175),
                                                        ],
                                               "T1bbbb": [(1225,500), (1200,150), (825,600), (800,625), (850,650),
                                                          (975,650), (925,650), (900,650), (1050,650), (1150,550),
                                                          ],
                                               "T1tttt":[(1025,300), (525,100),(475,100),(425,50),(550,150),
                                                         (675,225),(750,275),(800,300),(850,350),
                                                         ],
                                               })

    out["UpperLimit"].update({"T1": [(675,500), (650,475), (900,450), (850,475), (950,425), (800,475),
                                     ],
                              "T2": [(575,300),(575,350),(450,275),(525,300), (475,275),
                                     (600,325), (525,325), (700,350), (625,350),
                                     ],
                              "T2bb": [(650,125), (400,200), (575,225),
                                       ],
                              "T1bbbb":[(825,625), (1150,550), (1050,650), (900,650), #(850,650),
                                        (950,700), (875,650), (925,675), (1075,650),
                                        ],
                              "T1tttt":[(500,125), (550,125), (625,225), (650,225), (700,225), (725,275),
                                        (800,300), (850,325), (600,200), (975,350), (425, 50), (400,50), (375,25),
                                        ],
                              })

    out["UpperLimit_-1_Sigma"].update({"T1": [(700,475), (675,475), (625,450), (875,425),
                                              ],
                                       "T2": [(575,300), (525,275), (675,325), (500,275), (600,325), (450,275),
                                              ],
                                       "T2bb": [(425,200), (500,225), (400,200), (525,200),
                                                ],
                                       "T1bbbb":[(800,625), (825,600), (975,625), (1000,650), (875,650), (1050,550),
                                                 ],
                                       "T1tttt":[(875,275), (775,275), (825,325), (850,300), (925,300), (625,175),
                                                 (650,225), (700,225), (750,275), (575,125), (525,100), (475,100),
                                                 (400, 50), (425, 50),
                                                 ],
                                       })
    out["UpperLimit_+1_Sigma"].update({"T1": [(700,475), (675,500), (1050,250), (750,475), (775,475), (925,475), (950,475),
                                              ],
                                       "T2": [(500,300), (550,325), (600,350), (625,350), (650,375), (725,350),
                                              ],
                                       "T2bb":[(450,225), (425,225), (525,225), (600,225),
                                               ],
                                       "T1bbbb":[(1225,450), (1025,725), (850,650), (900,675), (925,700),
                                                 (1075,700), (1100,650),
                                                 ],
                                       "T1tttt":[(1050,50), (525,100), (475,125), (425,50), (400,50),
                                                 (675,225), (700,275), (625,225), (750,275), (825,325), (775,325),
                                                 (1025,375), (850,350), (550,150),
                                                 ],
                                       })

    out["UpperLimit"].update({"T1tttt_ichep" : [ (850,200) ]})
    out["UpperLimit_-1_Sigma"].update({"T1tttt_ichep" : [ (450,50) ]})

    return out

def graphReplacePoints():
    out = {}
    keys  = [ "UpperLimit", "ExpectedUpperLimit" ]
    keys += [ "ExpectedUpperLimit_%+d_Sigma" % i for i in [-1,1] ]
    keys += [ "UpperLimit_%+d_Sigma" % i for i in [-1,1] ]
    for key in keys :
        out[key] = collections.defaultdict(dict)

    out["ExpectedUpperLimit_-1_Sigma"].update({"T1": {(1075,500):(1075,487.5),
                                                      (1125,350):(1125,300),
                                                      (1100,  0):(1120,0),
                                                      },
                                               "T2": {(900,175):(895,175),
                                                      (850,300):(860,300),
                                                      (875,250):(880,250),
                                                      (800,350):(800,360),
                                                      (750,375):(750,372),
                                                      },
                                               "T2bb":{(525,300):(525,287.5),
                                                       (725,125):(725, 50),
                                                       (725,  0):(730,  0  ),
                                                       (700,175):(705, 175),
                                                       (675,225):(675, 235),
                                                       },
                                               "T1bbbb":{(1250,450):(1237.5,450),
                                                         (1250,325):(1237.5,325),
                                                         (1250,275):(1237.5,275),
                                                         (1200,  0):(1220,    0),
                                                         (1075,725):(1075,  730),
                                                         (1225,625):(1225, 550),
                                                         },
                                               "T1tttt":{(1125,200):(1126,200),
                                                         (1100,325):(1110,325),
                                                         (1075,425):(1075,400),
                                                         (675,250):(675,255),
                                                         (850,375):(850,380),
                                                         (400,50):(400,45),
                                                         },
                                               })
    out["ExpectedUpperLimit"].update({"T1": {(850,525):(850,550),
                                             (1050,0):(1072.5,0),
                                             (750,525):(750,537.5),
                                             },
                                      "T2": {(825,325):(825,265),

                                             (875,  0):(865,  0),
                                             (875, 50):(865, 50),
                                             (875,100):(860,100),
                                             (875,150):(855,150),
                                             },
                                      "T2bb": {(575,275):(575,255),
                                               (700,75):(685,75),
                                               (700,25):(687,25),
                                               (675, 0):(687.5, 0),
                                               },
                                      "T1bbbb":{(950,700):(950,692.5),
                                                (1225,500):(1213,450),
                                                (1225,200):(1211,300),
                                                (1225,150):(1208,200),
                                                (1225,100):(1205,100),
                                                },
                                      "T1tttt":{(1100,100):(1080,100),
                                                (1100,250):(1090,200),
                                                (1075,  0):(1070,  0),
                                                (975,400):(975,387.5),
                                                (725,300):(725,285),
                                                (625,225):(625,215),
                                                (500,125):(500,115),
                                                (600,200):(600,190),
                                                (575,175):(575,165),
                                                (700,275):(700,265),
                                                (775,325):(775,315),
                                                (400,50):(400,45),
                                                },
                                      })
    out["ExpectedUpperLimit_+1_Sigma"].update({"T1": {(750,525):(750,512.5),
                                                      (675,500):(687.5,500),
                                                      (1050,275):(1037.5,275),
                                                      (1050,200):(1037.5,200),
                                                      (1050,100):(1037.5,100),
                                                      (1025,  0):(1032,    0),
                                                      (1025,375):(1030,350),
                                                      (1000,400):(1012.5,400),
                                                      },
                                               "T2":{(600,325):(600,320),
                                                     (650,325):(650,320),
                                                     (825, 75):(820, 75),
                                                     (775,250):(780,250),
                                                     },
                                               "T2bb": {(550,200):(555,205),
                                                        (500,225):(500,220),
                                                        (600,200):(600,175),
                                                        (625,75):(637.5,75),
                                                        },
                                               "T1bbbb": {(950,675):(950,667.5),
                                                          (1175,400):(1175,300),
                                                          (1125,550):(1135,550),
                                                          (1175,225):(1170,225),
                                                          (1150,  0):(1162.5,0),
                                                          (1075,650):(1080,640),
                                                          },
                                               "T1tttt":{(1025,0):(1020,0),
                                                         (1025,250):(1025,175),
                                                         (400,50):(400,45),
                                                         },
                                               })
    out["UpperLimit"].update({"T1": {#(950,425):(950,437.5),
                                     (975,425):(980,375),
                                     #(875,475):(874,467.5),
                                     (1000,350):(1000,225),
                                     (925,450):(935,455),
                                     },
                              "T2": {(800,200):(795,150),
                                     },
                              "T2bb":{(625,125):(632,125),
                                      (650,50): (647,50),
                                      (425,225):(425,224),
                                      (550,225):(550,224),
                                      },
                              "T1bbbb":{(1175,225):(1167.5,225),
                                        (1175,275):(1167.5,275),
                                        (1175,325):(1167.5,325),
                                        (1175,350):(1167.5,350),
                                        (1175,400):(1167.5,400),
                                        (1150,500):(1160, 475),
                                        (1125,550):(1135,550),
                                        },
                              "T1tttt":{(1025,250):(1025,175),
                                        (1025,75):(1020,75),
                                        (1000, 0):(1010, 0),

                                        (525,100):(525,125),
                                        (475,100):(487.5,100),
                                        (675,225):(650,218),
                                        (750,275):(730,275),
                                        (575,175):(575,165),
                                        },
                              })
    
    out["UpperLimit_-1_Sigma"].update({"T1":{(950,325):(950,275),
                                             (850,450):(850,448),
                                             },
                                       "T2":{(775,100):(770,100),
                                             (625,325):(610,325),
                                             (550,300):(550,310)
                                             },
                                       "T2bb":{(600,125):(590,125),
                                               (575,175):(575,185),
                                               (450,225):(450,212.5),
                                               (475,225):(475,212.5),
                                               (550,200):(560,200),
                                               },
                                       "T1bbbb":{(1125,175): (1120,175),
                                                 (1125,100): (1115,100),
                                                 (1100,  0): (1112.5,0),
                                                 (1125,400): (1125,300),
                                                 (1025,625): (1025,600),
                                                 (850, 625): (850,637.5),
                                                 },
                                       "T1tttt":{(975,200):(973,200),
                                                 (975,100):(968,100),
                                                 (950,  0):(960,  0),
                                                 (600,175):(610,175),
                                                 (675,225):(675,220),
                                                 (550,125):(550,128)
                                                 },
                                       })

    out["UpperLimit_+1_Sigma"].update({"T1":{(1025,400):(1025,325),
                                             },
                                       "T2":{(825,200):(817.5,175),
                                             (475,300):(485,300),
                                             },
                                       "T2bb":{(475,250):(475,245),
                                               (500,250):(500,245),
                                               (550,250):(550,245),
                                               (575,250):(575,242),
                                               (675,75):(670,70),
                                               },
                                       "T1bbbb":{(950,700):(935,700),
                                                 (1200,525):(1200,400),
                                                 (1200,100):(1195,100),
                                                 (1200, 50):(1192.5, 50),
                                                 (1200, 25):(1190, 25),
                                                 (1175,  0):(1187.5,  0),
                                                 },
                                       "T1tttt":{(1050,  0):(1055,  0),
                                                 (1075,175):(1060,75),
                                                 (1075,225):(1070,175),
                                                 (1075,250):(1070,220),
                                                 (1050,300):(1050,310),
                                                 (800,325):(790,325),
                                                 (725,275):(715,275),
                                                 (650,225):(640,225),
                                                 (500,125):(500,120),
                                                 (575,175):(575,178),
                                                 },
                                       })

    return out

def graphAdditionalPoints():
    out = {}
    keys  = [ "UpperLimit", "ExpectedUpperLimit" ]
    keys += [ "ExpectedUpperLimit_%+d_Sigma" % i for i in [-1,1] ]
    keys += [ "UpperLimit_%+d_Sigma" % i for i in [-1,1] ]
    for key in keys :
        out[key] = collections.defaultdict(list)

    return out
