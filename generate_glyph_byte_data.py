import typing as t

# newline separated list of homoglyph groupings unicode codepoints
# source: https://raw.githubusercontent.com/codebox/homoglyph/master/raw_data/chars.txt
homog_cp = """20,a0,1680,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,200a,2028,2029,202f,205f
21,1c3,2d51,ff01
24,ff04
25,ff05
26,a778,ff06
27,60,b4,2b9,2bb,2bc,2bd,2be,2c8,2ca,2cb,2f4,374,384,55a,55d,5d9,5f3,7f4,7f5,144a,16cc,1fbd,1fbf,1fef,1ffd,1ffe,2018,2019,201b,2032,2035,a78c,ff07,ff40,16f51,16f52
28,2768,2772,3014,fd3e,ff08,ff3b
29,2769,2773,3015,fd3f,ff09,ff3d
2a,66d,204e,2217,ff0a,1031f
2b,16ed,2795,ff0b,1029b
2c,b8,60d,66b,201a,a4f9,ff0c
2d,2d7,6d4,2010,2011,2012,2013,2043,2212,2796,2cba,fe58
2e,660,6f0,701,702,2024,a4f8,a60e,ff0e,10a50,1d16d
2f,1735,2041,2044,2215,2571,27cb,29f8,2cc6,2f03,3033,30ce,31d3,4e3f,ff0f,1d23a
30,4f,6f,39f,3bf,3c3,41e,43e,555,585,5e1,647,665,6be,6c1,6d5,6f5,7c0,966,9e6,a66,ae6,b20,b66,be6,c02,c66,c82,ce6,d02,d20,d66,d82,e50,ed0,101d,1040,10ff,12d0,1d0f,1d11,2134,2c9e,2c9f,2d54,3007,a4f3,ab3d,fba6,fba7,fba8,fba9,fbaa,fbab,fbac,fbad,fee9,feea,feeb,feec,ff10,ff2f,ff4f,10292,102ab,10404,1042c,104c2,104ea,10516,114d0,118b5,118c8,118d7,118e0,1d40e,1d428,1d442,1d45c,1d476,1d490,1d4aa,1d4de,1d4f8,1d512,1d52c,1d546,1d560,1d57a,1d594,1d5ae,1d5c8,1d5e2,1d5fc,1d616,1d630,1d64a,1d664,1d67e,1d698,1d6b6,1d6d0,1d6d4,1d6f0,1d70a,1d70e,1d72a,1d744,1d748,1d764,1d77e,1d782,1d79e,1d7b8,1d7bc,1d7ce,1d7d8,1d7e2,1d7ec,1d7f6,1ee24,1ee64,1ee84,1fbf0
31,49,69,6c,7c,131,196,1c0,269,26a,2db,37a,399,3b9,406,456,4c0,4cf,5c0,5d5,5df,627,661,6f1,7ca,13a5,16c1,1fbe,2110,2111,2113,2139,2148,2160,2170,217c,2223,2373,23fd,2c92,2d4f,a4f2,a647,ab75,fe8d,fe8e,ff11,ff29,ff49,ff4c,ffe8,1028a,10309,10320,118c3,16f28,1d408,1d422,1d425,1d43c,1d456,1d459,1d470,1d48a,1d48d,1d4be,1d4c1,1d4d8,1d4f2,1d4f5,1d526,1d529,1d540,1d55a,1d55d,1d574,1d58e,1d591,1d5a8,1d5c2,1d5c5,1d5dc,1d5f6,1d5f9,1d610,1d62a,1d62d,1d644,1d65e,1d661,1d678,1d692,1d695,1d6a4,1d6b0,1d6ca,1d6ea,1d704,1d724,1d73e,1d75e,1d778,1d798,1d7b2,1d7cf,1d7d9,1d7e3,1d7ed,1d7f7,1e8c7,1ee00,1ee80,1fbf1
32,1a7,3e8,14bf,a644,a6ef,a75a,ff12,1d7d0,1d7da,1d7e4,1d7ee,1d7f8,1fbf2
33,1b7,21c,417,4e0,2ccc,a76a,a7ab,ff13,118ca,16f3b,1d206,1d7d1,1d7db,1d7e5,1d7ef,1d7f9,1fbf3
34,13ce,ff14,118af,1d7d2,1d7dc,1d7e6,1d7f0,1d7fa,1fbf4
35,1bc,ff15,118bb,1d7d3,1d7dd,1d7e7,1d7f1,1d7fb,1fbf5
36,431,13ee,2cd2,ff16,118d5,1d7d4,1d7de,1d7e8,1d7f2,1d7fc,1fbf6
37,ff17,104d2,118c6,1d212,1d7d5,1d7df,1d7e9,1d7f3,1d7fd,1fbf7
38,222,223,9ea,a6a,b03,ff18,1031a,1d7d6,1d7e0,1d7ea,1d7f4,1d7fe,1e8cb,1fbf8
39,9ed,a67,b68,d6d,2cca,a76e,ff19,118ac,118cc,118d6,1d7d7,1d7e1,1d7eb,1d7f5,1d7ff,1fbf9
3a,2d0,2f8,589,5c3,703,704,903,a83,16ec,1803,1809,205a,2236,a4fd,a789,fe30,ff1a
3b,37e,ff1b
3c,2c2,1438,16b2,2039,276e,ff1c,1d236
3d,1400,2e40,30a0,a4ff,ff1d
3e,2c3,1433,203a,276f,ff1e,16f3f,1d237
3f,241,294,97d,13ae,a6eb,ff1f
40,ff20
41,391,410,13aa,15c5,1d00,a4ee,ab7a,ff21,102a0,16f40,1d400,1d434,1d468,1d49c,1d4d0,1d504,1d538,1d56c,1d5a0,1d5d4,1d608,1d63c,1d670,1d6a8,1d6e2,1d71c,1d756,1d790
42,299,392,412,432,13f4,13fc,15f7,16d2,212c,a4d0,a7b4,ff22,10282,102a1,10301,1d401,1d435,1d469,1d4d1,1d505,1d539,1d56d,1d5a1,1d5d5,1d609,1d63d,1d671,1d6a9,1d6e3,1d71d,1d757,1d791
43,3f9,421,13df,1455,2102,212d,216d,2282,2ca4,2e26,a4da,ff23,102a2,10302,10415,1051c,118e9,118f2,1d402,1d436,1d46a,1d49e,1d4d2,1d56e,1d5a2,1d5d6,1d60a,1d63e,1d672,1f74c
44,13a0,15de,15ea,1d05,2145,216e,a4d3,ab70,ff24,1d403,1d437,1d46b,1d49f,1d4d3,1d507,1d53b,1d56f,1d5a3,1d5d7,1d60b,1d63f,1d673
45,395,415,13ac,1d07,2130,22ff,2d39,a4f0,ab7c,ff25,10286,118a6,118ae,1d404,1d438,1d46c,1d4d4,1d508,1d53c,1d570,1d5a4,1d5d8,1d60c,1d640,1d674,1d6ac,1d6e6,1d720,1d75a,1d794
46,3dc,15b4,2131,a4dd,a798,ff26,10287,102a5,10525,118a2,118c2,1d213,1d405,1d439,1d46d,1d4d5,1d509,1d53d,1d571,1d5a5,1d5d9,1d60d,1d641,1d675,1d7ca
47,262,50c,50d,13c0,13f3,13fb,a4d6,ab90,ff27,1d406,1d43a,1d46e,1d4a2,1d4d6,1d50a,1d53e,1d572,1d5a6,1d5da,1d60e,1d642,1d676
48,29c,397,41d,43d,13bb,157c,210b,210c,210d,2c8e,a4e7,ab8b,ff28,102cf,1d407,1d43b,1d46f,1d4d7,1d573,1d5a7,1d5db,1d60f,1d643,1d677,1d6ae,1d6e8,1d722,1d75c,1d796
4a,37f,408,13ab,148d,1d0a,a4d9,a7b2,ab7b,ff2a,1d409,1d43d,1d471,1d4a5,1d4d9,1d50d,1d541,1d575,1d5a9,1d5dd,1d611,1d645,1d679
4b,39a,41a,13e6,16d5,212a,2c94,a4d7,ff2b,10518,1d40a,1d43e,1d472,1d4a6,1d4da,1d50e,1d542,1d576,1d5aa,1d5de,1d612,1d646,1d67a,1d6b1,1d6eb,1d725,1d75f,1d799
4c,29f,13de,14aa,2112,216c,2cd0,2cd1,a4e1,abae,ff2c,1041b,10443,10526,118a3,118b2,16f16,1d22a,1d40b,1d43f,1d473,1d4db,1d50f,1d543,1d577,1d5ab,1d5df,1d613,1d647,1d67b
4d,39c,3fa,41c,13b7,15f0,16d6,2133,216f,2c98,a4df,ff2d,102b0,10311,1d40c,1d440,1d474,1d4dc,1d510,1d544,1d578,1d5ac,1d5e0,1d614,1d648,1d67c,1d6b3,1d6ed,1d727,1d761,1d79b
4e,274,39d,2115,2c9a,a4e0,ff2e,10513,1d40d,1d441,1d475,1d4a9,1d4dd,1d511,1d579,1d5ad,1d5e1,1d615,1d649,1d67d,1d6b4,1d6ee,1d728,1d762,1d79c
50,3a1,420,13e2,146d,1d18,1d29,2119,2ca2,a4d1,abb2,ff30,10295,1d40f,1d443,1d477,1d4ab,1d4df,1d513,1d57b,1d5af,1d5e3,1d617,1d64b,1d67f,1d6b8,1d6f2,1d72c,1d766,1d7a0
51,211a,2d55,ff31,1d410,1d444,1d478,1d4ac,1d4e0,1d514,1d57c,1d5b0,1d5e4,1d618,1d64c,1d680
52,1a6,280,13a1,13d2,1587,16b1,211b,211c,211d,a4e3,ab71,aba2,ff32,104b4,16f35,1d216,1d411,1d445,1d479,1d4e1,1d57d,1d5b1,1d5e5,1d619,1d64d,1d681
53,405,54f,13d5,13da,a4e2,ff33,10296,10420,16f3a,1d412,1d446,1d47a,1d4ae,1d4e2,1d516,1d54a,1d57e,1d5b2,1d5e6,1d61a,1d64e,1d682
54,3a4,3c4,422,442,13a2,1d1b,22a4,27d9,2ca6,a4d4,ab72,ff34,10297,102b1,10315,118bc,16f0a,1d413,1d447,1d47b,1d4af,1d4e3,1d517,1d54b,1d57f,1d5b3,1d5e7,1d61b,1d64f,1d683,1d6bb,1d6d5,1d6f5,1d70f,1d72f,1d749,1d769,1d783,1d7a3,1d7bd,1f768
55,54d,1200,144c,222a,22c3,a4f4,ff35,104ce,118b8,16f42,1d414,1d448,1d47c,1d4b0,1d4e4,1d518,1d54c,1d580,1d5b4,1d5e8,1d61c,1d650,1d684
56,474,667,6f7,13d9,142f,2164,2d38,a4e6,a6df,ff36,1051d,118a0,16f08,1d20d,1d415,1d449,1d47d,1d4b1,1d4e5,1d519,1d54d,1d581,1d5b5,1d5e9,1d61d,1d651,1d685
57,51c,13b3,13d4,a4ea,ff37,118e6,118ef,1d416,1d44a,1d47e,1d4b2,1d4e6,1d51a,1d54e,1d582,1d5b6,1d5ea,1d61e,1d652,1d686
58,3a7,425,166d,16b7,2169,2573,2cac,2d5d,a4eb,a7b3,ff38,10290,102b4,10317,10322,10527,118ec,1d417,1d44b,1d47f,1d4b3,1d4e7,1d51b,1d54f,1d583,1d5b7,1d5eb,1d61f,1d653,1d687,1d6be,1d6f8,1d732,1d76c,1d7a6
59,3a5,3d2,423,4ae,13a9,13bd,2ca8,a4ec,ff39,102b2,118a4,16f43,1d418,1d44c,1d480,1d4b4,1d4e8,1d51c,1d550,1d584,1d5b8,1d5ec,1d620,1d654,1d688,1d6bc,1d6f6,1d730,1d76a,1d7a4
5a,396,13c3,2124,2128,a4dc,ff3a,102f5,118a9,118e5,1d419,1d44d,1d481,1d4b5,1d4e9,1d585,1d5b9,1d5ed,1d621,1d655,1d689,1d6ad,1d6e7,1d721,1d75b,1d795
5c,2216,27cd,29f5,29f9,2f02,31d4,4e36,fe68,ff3c,1d20f,1d23b
5e,2c4,2c6
5f,7fa,fe4d,fe4e,fe4f,ff3f
61,251,3b1,430,237a,ff41,1d41a,1d44e,1d482,1d4b6,1d4ea,1d51e,1d552,1d586,1d5ba,1d5ee,1d622,1d656,1d68a,1d6c2,1d6fc,1d736,1d770,1d7aa
62,184,42c,13cf,1472,15af,ff42,1d41b,1d44f,1d483,1d4b7,1d4eb,1d51f,1d553,1d587,1d5bb,1d5ef,1d623,1d657,1d68b
63,3f2,441,1d04,217d,2ca5,abaf,ff43,1043d,1d41c,1d450,1d484,1d4b8,1d4ec,1d520,1d554,1d588,1d5bc,1d5f0,1d624,1d658,1d68c
64,501,13e7,146f,2146,217e,a4d2,ff44,1d41d,1d451,1d485,1d4b9,1d4ed,1d521,1d555,1d589,1d5bd,1d5f1,1d625,1d659,1d68d
65,435,4bd,212e,212f,2147,ab32,ff45,1d41e,1d452,1d486,1d4ee,1d522,1d556,1d58a,1d5be,1d5f2,1d626,1d65a,1d68e
66,17f,3dd,584,1e9d,a799,ab35,ff46,1d41f,1d453,1d487,1d4bb,1d4ef,1d523,1d557,1d58b,1d5bf,1d5f3,1d627,1d65b,1d68f,1d7cb
67,18d,261,581,1d83,210a,ff47,1d420,1d454,1d488,1d4f0,1d524,1d558,1d58c,1d5c0,1d5f4,1d628,1d65c,1d690
68,4bb,570,13c2,210e,ff48,1d421,1d489,1d4bd,1d4f1,1d525,1d559,1d58d,1d5c1,1d5f5,1d629,1d65d,1d691
6a,3f3,458,2149,ff4a,1d423,1d457,1d48b,1d4bf,1d4f3,1d527,1d55b,1d58f,1d5c3,1d5f7,1d62b,1d65f,1d693
6b,ff4b,1d424,1d458,1d48c,1d4c0,1d4f4,1d528,1d55c,1d590,1d5c4,1d5f8,1d62c,1d660,1d694
6d,ff4d
6e,578,57c,ff4e,1d427,1d45b,1d48f,1d4c3,1d4f7,1d52b,1d55f,1d593,1d5c7,1d5fb,1d62f,1d663,1d697
70,3c1,3f1,440,2374,2ca3,ff50,1d429,1d45d,1d491,1d4c5,1d4f9,1d52d,1d561,1d595,1d5c9,1d5fd,1d631,1d665,1d699,1d6d2,1d6e0,1d70c,1d71a,1d746,1d754,1d780,1d78e,1d7ba,1d7c8
71,51b,563,566,ff51,1d42a,1d45e,1d492,1d4c6,1d4fa,1d52e,1d562,1d596,1d5ca,1d5fe,1d632,1d666,1d69a
72,433,1d26,2c85,ab47,ab48,ab81,ff52,1d42b,1d45f,1d493,1d4c7,1d4fb,1d52f,1d563,1d597,1d5cb,1d5ff,1d633,1d667,1d69b
73,1bd,455,a731,abaa,ff53,10448,118c1,1d42c,1d460,1d494,1d4c8,1d4fc,1d530,1d564,1d598,1d5cc,1d600,1d634,1d668,1d69c
74,ff54,1d42d,1d461,1d495,1d4c9,1d4fd,1d531,1d565,1d599,1d5cd,1d601,1d635,1d669,1d69d
75,28b,3c5,57d,1d1c,a79f,ab4e,ab52,ff55,104f6,118d8,1d42e,1d462,1d496,1d4ca,1d4fe,1d532,1d566,1d59a,1d5ce,1d602,1d636,1d66a,1d69e,1d6d6,1d710,1d74a,1d784,1d7be
76,3bd,475,5d8,1d20,2174,2228,22c1,aba9,ff56,11706,118c0,1d42f,1d463,1d497,1d4cb,1d4ff,1d533,1d567,1d59b,1d5cf,1d603,1d637,1d66b,1d69f,1d6ce,1d708,1d742,1d77c,1d7b6
77,26f,461,51d,561,1d21,ab83,ff57,1170a,1170e,1170f,1d430,1d464,1d498,1d4cc,1d500,1d534,1d568,1d59c,1d5d0,1d604,1d638,1d66c,1d6a0
78,d7,445,1541,157d,166e,2179,292b,292c,2a2f,ff58,1d431,1d465,1d499,1d4cd,1d501,1d535,1d569,1d59d,1d5d1,1d605,1d639,1d66d,1d6a1
79,263,28f,3b3,443,4af,10e7,1d8c,1eff,213d,ab5a,ff59,118dc,1d432,1d466,1d49a,1d4ce,1d502,1d536,1d56a,1d59e,1d5d2,1d606,1d63a,1d66e,1d6a2,1d6c4,1d6fe,1d738,1d772,1d7ac
7a,1d22,ab93,ff5a,118c4,1d433,1d467,1d49b,1d4cf,1d503,1d537,1d56b,1d59f,1d5d3,1d607,1d63b,1d66f,1d6a3
7b,2774,ff5b,1d114
7d,2775,ff5d
7e,2dc,1fc0,2053,223c
a3,20a4
a9,24b8
ae,24c7
af,2c9,203e,2594,fe49,fe4a,fe4b,fe4c,ffe3
b0,2da,2218,25cb,25e6,2e30
b5,3bc,1d6cd,1d707,1d741,1d77b,1d7b5
b6,2e3f
b7,387,1427,16eb,2022,2027,2219,22c5,2e31,30fb,a78f,ff65,10101
ba,1d52,2070
c4,4d2
c5,226
d6,150,4e6
de,3f7,104c4
df,3b2,3d0,13f0,a7b5,1d6c3,1d6fd,1d737,1d771,1d7ab
e4,4d3
e5,227
f6,4e7,629,6c3,2365,fe93,fe94
f7,2797
fe,1bf,3f8
102,1cd
103,1ce
114,11a
115,11b
11e,1e6
11f,1e7
123,1f5
12c,1cf
12d,1d0
138,3ba,3f0,43a,1d0b,2c95,abb6,1d6cb,1d6de,1d705,1d718,1d73f,1d752,1d779,1d78c,1d7b3,1d7c6
146,272
14e,1d1
14f,1d2
162,21a
163,1ab,21b,13bf
16c,1d3
16d,1d4
185,44c,ab9f
186,3fd,2183,a4db,10423
18e,2203,2d3a,a4f1
18f,4d8
190,510,13cb,2107,10401,16f2d,1d221
1a8,3e9,1d24,a645
1a9,3a3,2140,2211,2d49,1d6ba,1d6f4,1d72e,1d768,1d7a2
1b1,162e,1634,2127
1dd,259,4d9
1f6,50a
21d,292,4e1,10f3,2ccd,a76b
237,575,1d6a5
242,ab7e
245,39b,41b,668,6f8,1431,2d37,a4e5,a6ce,1028d,104b0,16f3d,1d6b2,1d6ec,1d726,1d760,1d79a
24b,1d90
254,37b,1d10,2184,1044b
25b,3b5,3f5,454,511,22f4,2c89,a793,ab9b,10429,118ce,1d6c6,1d6dc,1d700,1d716,1d73a,1d750,1d774,1d78a,1d7ae,1d7c4
25c,437,1d08
25e,10442
270,57a,1223
277,1043f
278,3c6,3d5,444,2cab,1d6d7,1d6df,1d711,1d719,1d74b,1d753,1d785,1d78d,1d7bf,1d7c7
27f,2129
283,222b,ab4d
28c,1d27,104d8
28d,43c,1d0d,ab87
298,2299,2609,2a00,2d59,a668,104c3
29a,a79d,1042a
2a1,a6cd
2b3,18f4
2bf,2d3,559
2c1,2e4
2c7,2d8,a67e
2cf,375
2d9,971,d4e
2e1,18f3
2e2,18db,18f5
2ea,2fb,a716
2eb,a714
2f3,3002
300,340,953
301,341,59c,59d,618,64e,747,954
302,311,65b,7ee,1cd0,a6f0
303,342,653
304,305,659,7eb,1cd2,a6f1
306,30c,36e,658,65a,a67c
307,358,5b9,5ba,5c1,5c2,5c4,6ec,740,741,7ed,8ea,902,a02,a82,bcd
308,7f3,8eb
309,302c
30a,366,5af,652,6df,b82,e4d,ecd,1036,17c6,17d3,2dea,309a,11300
30b,64b,8f0
30d,670
30e,1cda
312,657
313,315,343,619,64f,8f3
314,65d
316,1ced
317,61a,650
320,331,952
321,326,327,339
322,328,345,1ab7
323,5b4,5c5,65c,8ed,93c,9bc,a3c,abc,b3c,1cdd,10a3a,111ca,114c3
324,8ee,1cde
325,f37,302d
329,656,1cdc
32b,1cd5
32d,1cd9
32e,1cd8
333,347
335,336
337,338
350,357,8f8,8ff
352,900
354,8f9
355,8fa
363,2df6
364,2df7
368,2ded
36f,2def
370,13a8,13b0,2c75,a6b1
376,418,a6a1,10425,1d20b
377,438,1d0e,1044d
37d,a73f
393,413,13b1,14a5,213e,2c84,16f07,1d6aa,1d6e4,1d71e,1d758,1d792
394,1403,2206,25b3,2c86,2d60,10285,102a3,16f1a,1d6ab,1d6e5,1d71f,1d759,1d793,1f702
39e,1d6b5,1d6ef,1d729,1d763,1d79d
3a0,41f,213f,220f,2ca0,a6db,1d6b7,1d6f1,1d72b,1d765,1d79f
3a6,424,553,1240,16f0,2caa,102b3,1d6bd,1d6f7,1d731,1d76b,1d7a5
3a8,470,16d8,2cae,102b5,104d1,1d6bf,1d6f9,1d733,1d76d,1d7a7
3a9,162f,1635,2126,102b6,1d6c0,1d6fa,1d734,1d76e,1d7a8
3b4,56e,1577,1e9f,2e39,1d6c5,1d6ff,1d739,1d773,1d7ad
3b6,1d6c7,1d701,1d73b,1d775,1d7af
3bb,2c96,104db,1d6cc,1d706,1d740,1d77a,1d7b4
3be,1d6cf,1d709,1d743,1d77d,1d7b7
3c0,3d6,43f,1d28,213c,1d6d1,1d6e1,1d70b,1d71b,1d745,1d755,1d77f,1d78f,1d7b9,1d7c9
3c2,3db,1d6d3,1d70d,1d747,1d781,1d7bb
3c7,2cad,ab53,ab55,1d6d8,1d712,1d74c,1d786,1d7c0
3c8,471,104f9,1d6d9,1d713,1d74d,1d787,1d7c1
3c9,2375,2cb1,a64d,a7b7,1d6da,1d714,1d74e,1d788,1d7c2
3d7,2ce4
3d8,102ad,10312
3ec,2cdc
3ff,a73e
404,20ac,2c88,a792
40b,104cd
40d,419
428,2cbc
42d,2108
439,45d
43b,1d2b
448,2cbd
44f,1d19
459,ab60
460,13c7,15ef,1d222
4b6,4cb
4b7,4cc
4c3,104bc
4fe,1d202
53b,12ae
544,1206
548,1260,144e,2229,22c2,a4f5,1d245
54a,1323
54c,1261
554,20bd
571,1294
596,5ad
598,5ae
599,5a8
59a,5a4
5d0,2135,fb21
5d1,2136
5d2,2137
5d3,2138,fb22
5d4,fb23
5db,fb24
5dc,fb25
5dd,fb26
5e2,fb20
5e8,fb27
5ea,fb28
60c,66c,2e32
60f,639,fec9,feca,fecb,fecc,1ee0f,1ee2f,1ee4f,1ee6f,1ee8f,1eeaf
61b,2e35
61f,2e2e
621,fe80
622,fe81,fe82
628,fe8f,fe90,fe91,fe92,1ee01,1ee21,1ee61,1ee81,1eea1
62a,fe95,fe96,fe97,fe98,1ee15,1ee35,1ee75,1ee95,1eeb5
62c,fe9d,fe9e,fe9f,fea0,1ee02,1ee22,1ee42,1ee62,1ee82,1eea2
62d,fea1,fea2,fea3,fea4,1ee07,1ee27,1ee47,1ee67,1ee87,1eea7
62e,fea5,fea6,fea7,fea8,1ee17,1ee37,1ee57,1ee77,1ee97,1eeb7
62f,fea9,feaa,102e1,1ee03,1ee83,1eea3
630,feab,feac,1ee18,1ee98,1eeb8
631,fead,feae,1ee13,1ee93,1eeb3
632,feaf,feb0,1ee06,1ee86,1eea6
633,feb1,feb2,feb3,feb4,1ee0e,1ee2e,1ee4e,1ee6e,1ee8e,1eeae
635,feb9,feba,febb,febc,102f2,1ee11,1ee31,1ee51,1ee71,1ee91,1eeb1
636,febd,febe,febf,fec0,1ee19,1ee39,1ee59,1ee79,1ee99,1eeb9
637,fec1,fec2,fec3,fec4,102e8,1ee08,1ee68,1ee88,1eea8
638,fec5,fec6,fec7,fec8,1ee1a,1ee7a,1ee9a,1eeba
63a,fecd,fece,fecf,fed0,1ee1b,1ee3b,1ee5b,1ee7b,1ee9b,1eebb
641,6a7,fed1,fed2,fed3,fed4,1ee10,1ee30,1ee70,1ee90,1eeb0
642,fed5,fed6,fed7,fed8,1ee12,1ee32,1ee52,1ee72,1ee92,1eeb2
643,6a9,6aa,fb8e,fb8f,fb90,fb91,fed9,feda,fedb,fedc,1ee0a,1ee2a,1ee6a
644,fedd,fede,fedf,fee0,1ee0b,1ee2b,1ee4b,1ee8b,1eeab
645,fee1,fee2,fee3,fee4,1ee0c,1ee2c,1ee6c,1ee8c,1eeac
646,fee5,fee6,fee7,fee8,1ee0d,1ee2d,1ee4d,1ee6d,1ee8d,1eead
648,8b1,feed,feee,102e4,1ee05,1ee85,1eea5
649,64a,66e,6ba,6cc,6d2,8bd,fb9e,fb9f,fbae,fbaf,fbe8,fbe9,fbfc,fbfd,fbfe,fbff,feef,fef0,fef1,fef2,fef3,fef4,1ee09,1ee1c,1ee1d,1ee29,1ee49,1ee5d,1ee69,1ee7c,1ee89,1eea9
64c,8e5,8e8,8f1
64d,8f2
655,65f
662,6f2,a9cf
663,6f3,1e8c9
664,6f4
666,6f6
669,6f9,967,118e4
66f,6a1,8bb,8bc,1ee1e,1ee1f,1ee5f,1ee7e
671,fb50,fb51
67a,fb5e,fb5f,fb60,fb61
67b,6d0,fb52,fb53,fb54,fb55,fbe4,fbe5,fbe6,fbe7
67f,fb62,fb63,fb64,fb65
680,fb5a,fb5b,fb5c,fb5d
683,fb76,fb77,fb78,fb79
684,fb72,fb73,fb74,fb75
686,fb7a,fb7b,fb7c,fb7d
687,fb7e,fb7f,fb80,fb81
68c,fb84,fb85
68d,fb82,fb83
6a6,fb6e,fb6f,fb70,fb71
6ac,762
6af,8b0,fb92,fb93,fb94,fb95
6b1,fb9a,fb9b,fb9c,fb9d
6b3,fb96,fb97,fb98,fb99
6c0,6c2,fba4,fba5
6c5,fbe0,fbe1
6d3,fbb0,fbb1
6db,1ab4,20db
73c,742
754,767,8a9
93a,111cb
93d,abd
941,ac1
942,ac2
946,a4b
94d,a4d,acd
964,a830
968,ae8
969,ae9
96a,aea
96e,aee
970,af0,26ac,110bb,111c7
983,a03,c03,c83,d03,d83,1038,114c1
998,11492
99a,11494
99c,11496
99e,11498
99f,11499
9a1,1149b
9a3,114aa
9a4,1149e
9a5,1149f
9a6,114a0
9a7,114a1
9a8,114a2
9aa,114a3
9ac,114a9
9ae,114a7
9af,114a8
9b0,114ab
9b2,1149d
9b7,114ad
9b8,114ae
9bd,114c4
9be,114b0
9bf,114b1
9c7,114b9
9cb,114bc
9cc,114be
9cd,114c2
9d7,114bd
9e7,114d1
9e8,114d2
9ec,114d6
b85,bee
b88,bb0,bbe
b89,be8,d09
b8e,bed
b90,b9c,d1c
b95,be7
b9a,bea
ba3,d23
ba9,bc8
baf,bf0
bb3,bd7
bb4,d34
bb6,d36
bb7,bf8
bbf,d3f,d40
bf3,bf5
c05,c85
c06,c86
c07,c87
c12,c92
c1c,c9c
c1e,c9e
c23,ca3
c2f,caf
c31,cb1
c32,cb2
c67,ce7
c68,ce8
c6f,cef
d1e,d61
d30,d31
d41,d42,d43
da2,dea
daf,deb
e02,e03
e04,e14,e15
e06,e21
e08,e88
e0a,e0b
e0e,e0f
e11,e17
e1a,e9a
e1b,e9b
e1d,e9d
e1e,e9e
e1f,e9f
e20,e26
e22,e8d
e2f,17d4
e32,e45
e34,17b7
e35,17b8
e36,17b9
e37,17ba
e38,eb8
e39,eb9
e48,ec8,17cb
e49,ec9
e4a,eca
e4b,ecb
e4f,17d9
e5a,17d5
e5b,17da
f0b,f0c
f62,f6a
fd5,5350
fd6,534d
1041,1065
10a0,a786
1100,11a8,3131
1102,11ab,3134
1103,11ae,3137
1105,11af,3139
1106,11b7,3141
1107,11b8,3142
1109,11ba,3145
110b,11bc,3147
110c,11bd,3148
110e,11be,314a
110f,11bf,314b
1110,11c0,314c
1111,11c1,314d
1112,11c2,314e
1140,11eb,317f
114c,11f0,3181
1159,11f9,3186
1160,3164
1161,314f
1163,3151
1165,3153
1167,3155
1169,3157
116d,315b
116e,315c
1172,3160
1173,2014,2015,2500,2501,2f00,30fc,3161,31d0,4e00,a7f7,ff0d
1175,239c,239f,23a2,23a5,23aa,23ae,2f01,3163,31d1,4e28
119e,318d
13ef,1ff6
1421,14d1
1429,1540
1435,2369
1450,2283,2e27
1489,1603
1490,1602
14d3,1604
14da,1607
1543,1622
1546,1623
154a,1624
15b5,2132,a4de
15b7,a7fb,1d230
15c4,2200,2c6f,a4ef,1d217
15d2,2aab
15d5,2aaa
15e1,a4f7
1646,1dbb
1660,a4ed
16b9,a6b0
16bc,16e1
16bd,16c2,237f
16cb,1d23f
16cf,2191
16d0,21bf
16da,21be,2a21
16dc,22c4,25c7,25ca,2662,10294,118b7,1f754
16de,22c8,2a1d
16e6,104d0
16e8,2195
16ef,2d63
17a2,17a3
1835,1855
185c,1896
18d4,1dba
18d6,1d3e
199e,19d0
19b1,19d1
1a45,1a80,1a90
1b0d,1b52
1b11,1b53
1b28,1b58
1b50,1b5c
1d34,1d78
1d4b,1d9f
1d4d,1da2
1ddf,2de8
1dee,2dec
1e43,ab51
1e9a,1ea3
1f7d,1ff4
205d,22ee,2d57,fe19
205e,2999,2d42,2e3d
2079,a770
20b8,3012,3036
20e9,a66f
2117,24c5
2141,a4e8
2142,a4f6,10411,16f26,1d215,1d22b
2143,16f00
2144,1d21b
219e,2bec
219f,2bed
21a0,2bee
21a1,2bef
21b2,21b5
21ba,1f10e
2202,1d6db,1d715,1d74f,1d789,1d7c3,1e8cc
2205,2300
2207,118a8,1d6c1,1d6fb,1d735,1d76f,1d7a9
220e,2588,25a0
2210,2a3f
2220,1e8c8
2227,22c0
2234,2e2b
2235,2e2a
2237,2e2c
2248,111de
224f,264e,1f75e
2261,2263
228d,2a03
228e,2a04
228f,1d238
2290,1d239
2293,2a05
2294,2a06
2295,2a01,a69a,102a8,1f728
2297,2a02
229b,235f
22a0,1f771
22a1,1f755
22a5,27c2,a4d5,a7b1,1d21c
22b2,25c1
22b3,25b7
2307,fe34
2312,25e0
2319,2a3d
2324,2325
2329,276c,27e8,3008,304f,31db,21fe8
232a,276d,27e9,3009
233b,29c7
233e,25ce,29be
2341,29c4,303c
2342,29c5
2349,29b0
234b,23c3
234e,23c2
2355,23c1
236d,23c6
2388,2638
23dc,fe35
23dd,fe36
23de,fe37
23df,fe38
23e0,fe39
23e1,fe3a
23e5,25b1
23fb,23fc
23fe,263e,1f318
2460,2780
2461,2781
2462,2782
2463,2783
2464,2784
2465,2785
2466,2786
2467,2787
2468,2788
2469,2789
24be,24db
24ea,1f10d
2502,2503,fe31,ff5c
250c,250f
251c,2523
258c,2590
2596,2597
2598,259d
25a1,2610
25aa,ffed
25b6,25b8,25ba
25bd,102bc,1d214,1f704
2625,1099e,132f9
2627,2ce9
2629,1f70a
2630,2cb6
263d,1f312,1f319
27e6,301a
27e7,301b
299a,29d9
29d6,102c0
29df,1f73a
2a1f,2a3e
2c3f,a992
2c70,1041f
2c76,ab80
2ce8,101a0
2d40,102b8
2e82,31d6,4e5b
2e83,31df,4e5a
2e85,30a4,4ebb
2e89,5202
2e8b,353e
2e8e,5140,fa0c
2e8f,5c23
2e90,2f2a,5c22,2f875
2e92,5df3
2e93,2f33,5e7a
2e94,5f51
2e96,5fc4
2e97,38fa
2e98,624c
2e99,6535
2e9b,65e1
2e9e,6b7a
2e9f,6bcd
2ea0,6c11
2ea1,6c35
2ea2,6c3a
2ea3,706c
2ea4,722b,fa49
2ea6,4e2c
2ea8,72ad
2eab,2eb2,7f52
2ead,793b
2eaf,7cf9
2eb1,7f53
2eb9,8002
2eba,8080
2ebe,2ebf,2ec0,8279,fa5d,fa5e
2ec1,864e
2ec2,8864
2ec3,8980
2ec4,897f
2ec5,89c1
2ec8,8ba0
2ec9,8d1d
2ecb,8f66
2ecc,2ecd,8fb6,fa66
2ecf,2ed6,961d
2ed0,9485
2ed1,2fa7,9577
2ed2,9578
2ed3,957f
2ed4,95e8
2ed8,9752
2ed9,97e6
2eda,9875
2edb,98ce
2edc,98de
2edd,2fb7,98df
2edf,98e0
2ee0,9963
2ee2,9a6c
2ee4,2fc1,9b3c
2ee5,9c7c
2ee8,9ea6
2ee9,9ec4
2eeb,6589
2eec,9f50
2eed,6b6f
2eee,9f7f
2eef,7adc
2ef0,9f99
2ef2,4e80
2ef3,9f9f
2f04,31e0,4e59
2f05,31da,4e85
2f06,30cb,4e8c
2f07,4ea0
2f08,4eba
2f09,513f
2f0a,5165
2f0b,30cf,516b
2f0c,5182
2f0d,5196
2f0e,51ab
2f0f,51e0
2f10,51f5,2f81d
2f11,5200
2f12,30ab,529b,f98a
2f13,52f9
2f14,5315
2f15,531a
2f16,5338
2f17,3038,5341
2f18,30c8,535c
2f19,5369
2f1a,5382
2f1b,53b6
2f1c,53c8
2f1d,2f1e,30ed,53e3,56d7
2f1f,2f20,571f,58eb
2f21,5902
2f22,590a
2f23,30bf,5915
2f24,5927
2f25,5973,f981
2f26,5b50
2f27,5b80
2f28,5bf8
2f29,5c0f
2f2b,5c38
2f2c,5c6e,fa3c,2f878
2f2d,5c71
2f2e,5ddb
2f2f,30a8,5de5
2f30,5df1
2f31,5dfe
2f32,5e72
2f34,5e7f
2f35,5ef4
2f36,5efe,2f890
2f37,5f0b
2f38,5f13
2f39,5f50
2f3a,5f61
2f3b,5f73
2f3c,5fc3
2f3d,6208
2f3e,6236,6238
2f3f,624b
2f40,652f
2f41,6534
2f42,6587
2f43,6597
2f44,65a4
2f45,65b9
2f46,65e0
2f47,65e5
2f48,66f0
2f49,6708
2f4a,6728
2f4b,6b20
2f4c,6b62
2f4d,6b79,fa95
2f4e,6bb3
2f4f,6bcb
2f50,6bd4
2f51,6bdb
2f52,6c0f
2f53,6c14
2f54,6c34
2f55,706b
2f56,722a
2f57,7236
2f58,723b
2f59,723f
2f5a,7247
2f5b,7259
2f5c,725b
2f5d,72ac
2f5e,7384
2f5f,7389
2f60,74dc
2f61,74e6
2f62,7518
2f63,751f
2f64,7528
2f65,7530
2f66,758b
2f67,7592
2f68,7676
2f69,767d
2f6a,76ae
2f6b,76bf
2f6c,76ee
2f6d,77db
2f6e,77e2
2f6f,77f3
2f70,793a
2f71,79b8
2f72,79be
2f73,7a74
2f74,7acb,f9f7
2f75,7af9
2f76,7c73
2f77,7cf8
2f78,7f36
2f79,7f51
2f7a,7f8a
2f7b,7fbd,fa1e
2f7c,8001,f934
2f7d,800c
2f7e,8012
2f7f,8033
2f80,807f
2f81,8089
2f82,81e3
2f83,81ea
2f84,81f3
2f85,81fc
2f86,820c
2f87,821b
2f88,821f
2f89,826e
2f8a,8272
2f8b,8278
2f8c,864d
2f8d,866b
2f8e,8840
2f8f,884c,fa08
2f90,8863,2f9c4
2f91,897e
2f92,898b,fa0a
2f93,89d2
2f94,8a00
2f95,8c37
2f96,8c46
2f97,8c55,2f9d2
2f98,8c78
2f99,8c9d
2f9a,8d64
2f9b,8d70
2f9c,8db3
2f9d,8eab
2f9e,8eca,f902
2f9f,8f9b
2fa0,8fb0,f971
2fa1,8fb5
2fa2,9091
2fa3,9149
2fa4,91c6
2fa5,91cc,f9e9
2fa6,91d1,f90a
2fa8,9580
2fa9,961c
2faa,96b6
2fab,96b9
2fac,96e8
2fad,9751
2fae,975e
2faf,9762
2fb0,9769
2fb1,97cb
2fb2,97ed
2fb3,97f3
2fb4,9801
2fb5,98a8
2fb6,98db
2fb8,9996
2fb9,9999
2fba,99ac
2fbb,9aa8
2fbc,9ad8
2fbd,9adf
2fbe,9b25
2fbf,9b2f
2fc0,9b32
2fc2,9b5a
2fc3,9ce5
2fc4,9e75
2fc5,9e7f,f940
2fc6,9ea5
2fc7,9ebb,2fa15
2fc8,9ec3
2fc9,9ecd
2fca,9ed1,9ed2
2fcb,9ef9,2fa17
2fcc,9efd
2fcd,9f0e
2fce,9f13
2fcf,9f20
2fd0,9f3b,2fa1c
2fd1,9f4a
2fd2,9f52
2fd3,9f8d,f9c4
2fd4,9f9c,f907,f908,face
2fd5,9fa0
301c,ff5e
3039,5344
303a,5345
3078,30d8
309b,ff9e
309c,ff9f
349e,2f80c
34b9,2f813
34bb,2f9ca
34df,2f81f
3515,2f824
3588,439b
363d,39b3
36ee,2f867
36fc,2f868
3781,2f876
382f,2f883
3862,2f888
387c,2f88a
38c7,2f896
38e3,2f89b
391c,2f8a2
393a,2f8a1
3a2e,2f8c2
3a41,6409
3a6c,2f8c7
3ada,66f6
3ae4,2f8d1
3b08,2f8d0
3b19,2f8ce
3b35,80f6
3b3a,5e50
3b3b,4420
3b49,2f8de
3b9d,fad2,2f8e7
3ba3,69e9
3c18,2f8ee
3c4e,2f8f2
3d33,2f90a
3d96,2f916
3eac,2f92a
3eb8,2f92c,2f92d
3f1b,2f933
3ffc,2f93e
4008,2f93f
4018,fad3
4039,9fc3,fad4,2f949
403f,6663
4046,2f94b
4096,2f94c
40e3,2f951
412f,2f958
4202,2f960
4227,2f964
42a0,2f967
4301,2f96d
4334,2f971
4359,2f974
43d5,2f981
43d9,2f8d7
440b,2f984
4443,6726
446b,2f98e
452b,2f9a7
455d,2f9ae
4561,2f9af
456b,2f9b2
45d7,2f9bf
45f9,2f9c2
4635,2f9c8
46b6,8a1e
46be,2f9cd
46c7,2f9ce
4995,2f9ef
49e6,2f9f2
4a6e,2f9f8
4a76,2f9f9
4ab2,2f9fc
4b33,2fa03
4bce,2fa08
4cce,2fa0d
4ced,2fa0e
4cf8,2fa11
4d56,2fa16
4e0d,f967
4e26,fa70
4e32,f905
4e38,2f801
4e39,f95e
4e3d,2f800
4e41,2f802
4e82,f91b
4e86,f9ba
4eae,f977
4ec0,f9fd
4ecc,2f819
4ee4,f9a8
4f60,2f804
4f75,5002,2f807
4f80,fa73
4f86,f92d
4f8b,f9b5
4fae,fa30,2f805
4fbb,2f806
4fbf,f965
5024,503c
502b,f9d4
507a,2f808
5099,2f809
50cf,2f80b
50da,f9bb
50e7,fa31,2f80a
5145,fa74
514d,fa32,2f80e
5154,2f80f
5164,2f810
5167,2f814
5168,fa72
5169,f978
516d,f9d1
5177,2f811
5180,fa75
518d,2f815
5192,2f8d2
5195,2f8d3
5197,2f817
51a4,2f818
51ac,2f81a
51b5,fa71,2f81b
51b7,f92e
51c9,f979
51cc,f955
51dc,f954
51de,fa15
5203,2f81e
5207,fa00,2f850
5217,f99c
5229,f9dd
523a,f9ff
523b,2f820
5246,2f821
5272,2f822
5277,2f823
5289,f9c7
52a3,f99d
52b3,2f992
52c7,fa76,2f825
52c9,fa33,2f826
52d2,f952
52de,f92f
52e4,fa34,2f827
52f5,f97f
52fa,fa77,2f828
5305,2f829
5306,2f82a
5317,f963,2f82b
533f,f9eb
5349,2f82c
5351,fa35,2f82d
535a,2f82e
5373,2f82f
5375,f91c
537d,2f830
537f,2f831,2f832,2f833
53c3,f96b
53ca,2f836
53df,2f837
53e5,f906
53eb,2f839
53f1,2f83a
5406,2f83b
540f,f9de
541d,f9ed
5438,2f83d
5442,f980
5448,2f83e
5468,2f83f
549e,2f83c
54a2,2f840
54bd,f99e
54f6,2f841
5510,2f842
5553,555f,2f843
5555,fa79
5563,2f844
5584,2f845,2f846
5587,f90b
5599,fa7a,2f847
559d,fa36,fa78
55ab,2f848
55b3,2f849
55c0,fa0d
55c2,2f84a
55e2,fa7b
5606,fa37,2f84c
5651,2f84e
5668,fa38
5674,2f84f
56f9,f9a9
5716,2f84b
5717,2f84d
578b,2f855
57ce,2f852
57f4,2f853
580d,2f854
5831,2f857
5832,2f856
5840,fa39
585a,fa10,fa7c
585e,f96c
5861,586b
58a8,fa3a
58ab,58ff
58ac,2f858
58b3,fa7d
58d8,f94a
58df,f942
58ee,2f851
58f2,2f85a
58f7,2f85b
5906,2f85c
591a,2f85d
5922,2f85e
5944,fa7e
5948,f90c
5951,f909
5954,fa7f
5962,2f85f
59d8,2f865
59ec,2f862
5a1b,2f863
5a27,2f864
5a62,fa80
5a66,2f866
5aaf,5b00
5ab5,2f986
5b08,2f869
5b28,fa81
5b3e,2f86a,2f86b
5b85,fa04
5bc3,2f86d
5bd8,2f86e
5be7,f95f,f9aa,2f86f
5bee,f9bc
5bf3,2f870
5bff,2f872
5c06,2f873
5c3f,f9bd
5c60,2f877
5c62,f94b
5c64,fa3b
5c65,f9df
5c8d,2f87a
5cc0,2f879
5d19,f9d5
5d43,2f87c
5d50,f921
5d6b,2f87f
5d6e,2f87e
5d7c,2f880
5db2,2f9f4
5dba,f9ab
5de1,2f881
5de2,2f882
5dfd,2f884
5e21,5e32
5e28,2f885
5e3d,2f886
5e69,2f887
5e74,f98e
5ea6,fa01
5eb0,2f88b
5eb3,2f88c
5eb6,2f88d
5ec9,f9a2
5eca,f928,2f88e
5ed2,fa82
5ed3,fa0b
5ed9,fa83
5eec,f982
5f04,f943
5f22,2f894,2f895
5f53,2f874
5f62,2f899
5f69,fa84
5f6b,2f89a
5f8b,f9d8
5f9a,2f89c
5fa9,f966
5fad,fa85
5fcd,2f89d
5fd7,2f89e
5ff5,f9a3
5ff9,2f89f
6012,f960
601c,f9ac
6075,fa6b
6081,2f8a0
6094,fa3d,2f8a3
60c7,2f8a5
60d8,fa86
60e1,f9b9
6108,fa88
6144,f9d9
6148,2f8a6
614c,2f8a7,2f8a9
614e,fa87,2f8a8
6160,fa8a
6168,fa3e
617a,2f8aa
618e,fa3f,fa89,2f8ab
6190,f98f
61a4,2f8ad
61af,2f8ae
61b2,2f8ac
61de,2f8af
61f2,fa40,fa8b,2f8b0
61f6,f90d,2f8b1
6200,f990
6210,2f8b2
621b,2f8b3
622e,f9d2
6234,fa8c
625d,2f8b4
62b1,2f8b5
62c9,f925
62cf,f95b
62d3,fa02
62d4,2f8b6
62fc,2f8ba
62fe,f973
633d,2f8b9
6350,2f8b7
6368,2f8bb
637b,f9a4
6383,2f8bc
63a0,f975
63a9,2f8c1
63c4,fa8d
63c5,2f8c0
63e4,2f8bd
641c,fa8e
6422,2f8bf
6452,fa8f
6469,2f8c3
6477,2f8c6
647e,2f8c4
649a,f991
649d,2f8c5
64c4,f930
654f,fa41,2f8c8
6556,fa90
656c,2f8c9
6578,f969
6599,f9be
65c5,f983
65e2,fa42
65e3,2f8cb
6613,f9e0
6649,2f8cd
665a,6669
6674,fa12,fa91
6688,f9c5
6691,fa43,2f8cf
669c,2f8d5
66b4,fa06
66c6,f98b
66f4,f901
66f8,2f8cc
6700,2f8d4
670c,80a6
670f,80d0
6710,80ca
6713,8101
6717,f929,fa92,2f8d8
6718,8127
671b,fa93,2f8d9
6721,2f8da
6723,81a7
674e,f9e1
6753,2f8dc
6756,fa94
675e,2f8db
676e,67ff
677b,f9c8
6785,2f8e0
6797,f9f4
67f3,f9c9
67fa,2f8df
6817,f9da
681f,2f8e5
6852,2f8e1
6881,f97a
6885,fa44,2f8e2
688e,2f8e4
68a8,f9e2
6914,2f8e6
6942,2f8e8
699d,6a27
69a3,2f8e9
69ea,2f8ea
6a02,f914,f95c,f9bf
6a13,f94c
6aa8,2f8eb
6ad3,f931
6adb,2f8ed
6b04,f91d
6b21,2f8ef
6b54,2f8f1
6b72,2f8f3
6b77,f98c
6b9f,2f8f4
6bae,f9a5
6bba,f970,fa96,2f8f5
6bbb,2f8f6
6c4e,2f8fa
6c67,2f8fe
6c88,f972
6cbf,2f8fc
6ccc,f968
6ccd,2f8fd
6ce5,f9e3
6d16,2f8ff
6d1b,f915
6d1e,fa05
6d34,2f907
6d3e,2f900
6d41,f9ca,fa97,2f902
6d69,2f903
6d6a,f92a
6d77,fa45,2f901
6d78,2f904
6d85,2f905
6dcb,f9f5
6dda,f94d
6dea,f9d6
6df9,2f90e
6e1a,fa46
6e2f,2f908
6e6e,2f909
6e88,6f59
6e9c,f9cb
6eba,f9ec
6ec7,2f90c
6ecb,fa99,2f90b
6ed1,f904
6edb,fa98
6f0f,f94e
6f22,fa47,fa9a
6f23,f992
6f6e,2f90f
6fc6,2f912
6feb,f922
6ffe,f984
701b,2f915
701e,fa9b,2f914
7039,2f913
704a,2f917
7070,2f835
7077,2f919
707d,2f918
7099,f9fb
70ad,2f91a
70c8,f99f
70d9,f916
7145,2f91c
7149,f993
716e,fa48,fa9c
719c,2f91e
71ce,f9c0
71d0,f9ee
7210,f932
721b,f91e
7228,2f920
7235,fa9e,2f921
7250,2f922
7262,f946
7280,2f924
7295,2f925
72af,fa9f
72c0,f9fa
72fc,f92b
732a,fa16,faa0
7375,f9a7
737a,2f928
7387,f961,f9db
738b,2f929
73a5,2f92b
73b2,f9ad
73de,f917
7406,f9e4
7409,f9cc
7422,fa4a
7447,2f92e
745c,2f92f
7469,f9ae
7471,faa1,2f930
7485,2f931
7489,f994
7498,f9ef
74ca,2f932
7506,faa2
7524,2f934
753b,faa3
753e,2f936
7559,f9cd
7565,f976
7570,f962,2f938
75e2,f9e5
7610,2f93a
761d,faa4
761f,faa5
7642,f9c1
7669,f90e
76ca,fa17,faa6
76db,faa7
76e7,f933
76f4,faa8,2f940
7701,f96d
771e,2f945
771f,2f946,2f947
7740,faaa
774a,faa9,2f948
778b,2f94a
77a7,fa9d
7814,784f
784e,2f94e
786b,f9ce
788c,f93b,2f94f
7891,fa4b
78ca,f947
78cc,faab,2f950
78fb,f964
792a,f985
793c,fa18
793e,fa4c
7948,fa4e
7949,fa4d
7950,fa4f
7956,fa50,2f953
795d,fa51
795e,fa19
7965,fa1a
797f,f93c
798d,fa52
798e,fa53
798f,fa1b,2f956
79ae,f9b6
79ca,f995
79eb,2f957
7a1c,f956
7a40,fa54,2f959
7a4a,2f95a
7a4f,2f95b
7a81,fa55
7ab1,faac
7aee,2f95f
7b20,f9f8
7bc0,fa56,faad
7bc6,2f962
7bc9,2f963
7c3e,f9a6
7c60,f944
7c7b,faae
7c92,f9f9
7cbe,fa1d
7cd2,2f966
7cd6,fa03
7ce3,2f969
7ce7,f97b
7ce8,2f968
7d00,2f96a
7d10,f9cf
7d22,f96a
7d2f,f94f
7d55,7d76
7d5b,faaf
7d63,2f96c
7da0,f93d
7dbe,f957
7dc7,2f96e
7df4,f996,fa57,fab0
7e02,2f96f
7e09,fa58
7e37,f950
7e41,fa59
7e45,2f970
7f3e,fab1
7f72,fa5a
7f79,f9e6
7f7a,2f976
7f85,f90f
7f95,2f978
7f9a,f9af
7ffa,2f979
8005,fa5b,fab2,2f97a
8046,f9b0
8060,2f97d
806f,f997
8070,2f97f
807e,f945
808b,f953
80ad,2f8d6
80b2,2f982
80fc,8141
8103,2f983
813e,2f985
81d8,f926
81e8,f9f6
81ed,fa5c
8201,2f893,2f98b
8204,2f98c
8218,fa6d
826f,f97c
828b,2f990
8291,2f98f
829d,2f991
82b1,2f993
82b3,2f994
82bd,2f995
82e5,f974,2f998
82e6,2f996
831d,2f999
8323,2f99c
8336,f9fe
8352,fab3
8353,2f9a0
8363,2f99a
83ad,2f99b
83bd,2f99d
83c9,f93e
83ca,2f9a1
83cc,2f9a2
83dc,2f9a3
83e7,2f99e
83ef,fab4
83f1,f958
843d,f918
8449,f96e
8457,fa5f,2f99f
848d,853f
84ee,f999
84f1,2f9a8
84f3,2f9a9
84fc,f9c2
8516,2f9aa
8564,2f9ac
85cd,f923
85fa,f9f0
8606,f935
8612,fa20
862d,f91f
8637,8641
863f,f910
8650,2f9b3
865c,f936,2f9b4
8667,2f9b5
8669,2f9b6
8688,2f9b8
86a9,2f9b7
86e2,2f9ba
870e,2f9b9
8728,2f9bc
876b,2f9bd
8779,fab5,2f9bb
8786,2f9be
87ba,f911
87e1,2f9c0
8801,2f9c1
881f,f927
8860,2f9c3
88c2,f9a0
88cf,f9e7
88d7,2f9c6
88de,2f9c7
88e1,f9e8
88f8,f912
88fa,2f9c9
8910,fa60
8941,fab6
8964,f924
8986,fab7
8996,fa61,fab8
8a2e,8a7d
8aa0,2f9cf
8aaa,f96f,f9a1
8abf,fab9
8acb,fabb
8ad2,f97d
8ad6,f941
8aed,fabe,2f9d0
8af8,fa22,faba
8afe,f95d,fabd
8b01,fa62,fabc
8b39,fa63,fabf
8b58,f9fc
8b80,f95a
8b86,8b8f
8b8a,fac0,2f9d1
8c48,f900
8c5c,8c63
8cab,2f9d4
8cc1,2f9d5
8cc2,f948
8cc8,f903
8cd3,fa64
8d08,fa65,fac1
8d1b,2f9d6
8d77,2f9d7
8d7f,8d86
8dbc,2f9db
8dcb,2f9da
8de5,8dfa
8def,f937
8df0,2f9dc
8e97,8e9b
8ed4,2f9de
8eff,8f27
8f26,f998
8f2a,f9d7
8f38,fac2,2f9df
8f3b,fa07
8f62,f98d
8f9e,2f98d
9023,f99a
9038,fa25,fa67
9072,fac3
907c,f9c3
908f,f913
9094,2f9e2
90ce,90de,f92c,fa2e
90f1,2f9e3
90fd,fa26
9111,2f9e4
911b,2f9e6
916a,f919
9199,fac4
91b4,f9b7
91cf,f97e
9234,f9b1
9238,2f9e7
9276,fac5
927c,2f9ea
92d7,2f9e8
92d8,2f9e9
9304,f93f
934a,f99b
93ad,93ae
93f9,2f9eb
9415,2f9ec
958b,2f9ee
95ad,f986
95b7,2f9f0
962e,f9c6
964b,f951
964d,fa09
9675,f959
9678,f9d3
967c,fac6
9686,f9dc
96a3,f9f1
96b7,96b8,f9b8,fa2f
96c3,2f9f3
96e2,f9ea
96e3,fa68,fac7
96f6,f9b2
96f7,f949
9723,2f9f5
9732,f938
9748,f9b3
9756,fa1c,fac8
97db,fac9
97e0,2f9fa
97ff,fa69,faca
980b,facb,2f9fe,2f9ff
9818,f9b4
9829,2fa00
983b,fa6a,facc
985e,f9d0
98e2,2fa02
98ef,fa2a
98fc,fa2b
9928,fa2c
9929,2fa04
99a7,2fa05
99c2,2fa06
99f1,f91a
99fe,2fa07
9a6a,f987
9b12,facd,2fa0a
9b6f,f939
9c40,2fa0b
9c57,f9f2
9cfd,2fa0c
9d67,2fa0f
9db4,fa2d
9dfa,f93a
9e1e,f920
9e42,9e43
9e97,f988
9e9f,f9f3
9ece,f989
9efe,2fa18
9f05,2fa19
9f0f,2fa1a
9f16,2fa1b
9f43,fad8
9f8e,fad9
a04a,a49e
a050,a4ac
a0c0,a49c
a132,a4a8
a259,a4bf
a2b1,a4be
a2cd,a494
a3ab,a4c0
a3b5,a4c2
a3bf,a4ba
a3c2,a4b0
a458,a4a7
a4e4,a79e
a64c,a7b6
a658,16f1c,1f701
a669,104eb
a727,a795
a779,a77a
a79a,10412
a79b,1043a
a8fb,111dc
a8fc,111db
a99d,a9a3
a9c6,a9d0
aa01,aa53
aa23,aa56
fa6c,242ee
facf,2284a
fad0,22844
fad1,233d5
fad5,25249
fad6,25cd0
fad7,27ed3
fb1d,fb39
fb2a,fb2b,fb49
fb2c,fb2d
fb2e,fb2f,fb30
fe3f,ff3e
10382,103d1
10393,103d3
1039a,12038
10486,104a0
10c82,10cfc
10ca5,10cfa
11582,115d8,115d9
11583,115da
11584,115db
115b2,115dc
115b3,115dd
11caa,11cb2
20122,2f803
2051c,2f812
20525,2f91b
2054b,2f816
2063a,2f80d
20804,2f9d9
208de,2f9dd
20a2c,2f834
20b63,2f838
214e4,2f859
216a8,2f860
216ea,2f861
219c8,2f86c
21b18,2f871
21d0b,2f8f8
21de4,2f87b
21de6,2f87d
22183,2f889
2219f,2f939
22331,2f891,2f892
226d4,2f8a4
22b0c,2f8b8
22bf1,2f8be
2300a,2f8ca
232b8,2f897
2335f,2f980
23393,2f989
2339c,2f98a
233c3,2f8dd
2346d,2f8e3
236a3,2f8ec
238a7,2f8f0
23a8d,2f8f7
23afa,2f8f9
23cbc,2f8fb
23d1e,2f906
23ed1,2f90d
23f5e,2f910
23f8e,2f911
24263,2f91d
243ab,2f91f
24608,2f923
24735,2f926
24814,2f927
24c36,2f935
24c92,2f937
24fa1,2f93b
24fb8,2f93c
25044,2f93d
250f2,2f942
250f3,2f941
25119,2f943
25133,2f944
2541d,2f94d
25626,2f952
2569a,2f954
256c5,2f955
2597c,2f95c
25aa7,2f95d,2f95e
25bab,2f961
25c80,2f965
25f86,2f96b
261da,2f898
26228,2f972
26247,2f973
262d9,2f975
2633e,2f977
264da,2f97b
26523,2f97c
265a8,2f97e
267a7,2f987
267b5,2f988
26b3c,2f997
26c36,2f9a4
26cd5,2f9a6
26d6b,2f9a5
26f2c,2f9ad
26fb1,2f9b0
270d2,2f9b1
273ca,2f9ab
27667,2f9c5
278ae,2f9cb
27966,2f9cc
27ca8,2f9d3
27f2f,2f9d8
285d2,2f9e0
285ed,2f9e1
2872e,2f9e5
28bfa,2f9ed
28d77,2f9f1
29145,2f9f6
291df,2f81c
2921a,2f9f7
2940a,2f9fb
29496,2f9fd
295b6,2fa01
29b30,2fa09
2a0ce,2fa10
2a105,2fa12
2a20e,2fa13
2a291,2fa14
2a392,2f88f
2a600,2fa1d"""
# convert to list of lists
homog_cp: t.List[t.List[int]] = [[int(cp, 16) for cp in x.split(',')] for x in homog_cp.split('\n')]

# print([cp for block in homog_cp for cp in block])

# split each codepoint into 4 bytes
homog_cp_by = []
def addintby(_by: t.List[int], _int: int, _cnt: int = 4):
  for off in range(0, _cnt * 8, 8):
    _by.append((_int >> off) & 0xff)
index = 0
for cp in [cp for block in homog_cp for cp in block]:
    addintby(homog_cp_by, cp)
    index += 1
# print(homog_cp_by)

# create a array of hash positions for each codepoint use a array size of 8419 because we have 6184 codepoints
homog_cp_hash_len = 8419
homog_cp_hash = [0] * homog_cp_hash_len
homog_cp_hash_blocki = [0] * homog_cp_hash_len
homog_cp_hash_blockl = [0] * homog_cp_hash_len
hash_collisions = [0]
def insert_hash(_cp: int, _i: int, _len: int):
#   h = (_cp * 0x1F31D) >> 27
  h = _cp
  predication = h % homog_cp_hash_len
  i = 0
  while homog_cp_hash[predication] != 0:
    i += 1
    predication = (predication + i * i) % homog_cp_hash_len
  hash_collisions[0] += i
  homog_cp_hash[predication] = _cp
  homog_cp_hash_blocki[predication] = _i
  homog_cp_hash_blockl[predication] = _len

index = 0
for block in homog_cp:
  l = len(block)
  for cp in block:
    insert_hash(cp, index, l)
  index += l
# print(hash_collisions[0])
# print(homog_cp_hash.count(0)+6184-homog_cp_hash_len)

# print(homog_cp_hash)
# print(homog_cp_hash_blocki)
# print(homog_cp_hash_blockl)


# split each homog_cp_hash_blocki value into 2 bytes
homog_cp_hash_blocki_by = []
for blocki in homog_cp_hash_blocki:
  addintby(homog_cp_hash_blocki_by, blocki, 2)
# print(homog_cp_hash_blocki_by)

# split the hash ordered homoglpyh block lengths into 4 bytes
homog_by_value = []
for cp in homog_cp_hash:
  addintby(homog_by_value, cp)
print(homog_by_value)
