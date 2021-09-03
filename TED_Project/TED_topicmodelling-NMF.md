```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from time import time
```


```python
ted_data = pd.read_excel("/Users/Administrator/Downloads/archive/ted_merge.xlsx")
print('load successfully')                         
                           
 
```

    load successfully



```python
ted_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>comments</th>
      <th>description</th>
      <th>duration</th>
      <th>event</th>
      <th>film_date</th>
      <th>film_date_after_conversion</th>
      <th>languages</th>
      <th>main_speaker</th>
      <th>name</th>
      <th>num_speaker</th>
      <th>published_date</th>
      <th>published_date_after_conversion</th>
      <th>ratings</th>
      <th>related_talks</th>
      <th>speaker_occupation</th>
      <th>tags</th>
      <th>title</th>
      <th>url</th>
      <th>views</th>
      <th>transcripts.transcript</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4553</td>
      <td>Sir Ken Robinson makes an entertaining and pro...</td>
      <td>1164</td>
      <td>TED2006</td>
      <td>1140825600</td>
      <td>2006/02/25</td>
      <td>60</td>
      <td>Ken Robinson</td>
      <td>Ken Robinson: Do schools kill creativity?</td>
      <td>1</td>
      <td>1151367060</td>
      <td>2006/06/27</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 19645}, {...</td>
      <td>[{'id': 865, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>Author/educator</td>
      <td>['children', 'creativity', 'culture', 'dance',...</td>
      <td>Do schools kill creativity?</td>
      <td>https://www.ted.com/talks/ken_robinson_says_sc...</td>
      <td>47227110</td>
      <td>Good morning. How are you?(Laughter)It's been ...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>265</td>
      <td>With the same humor and humanity he exuded in ...</td>
      <td>977</td>
      <td>TED2006</td>
      <td>1140825600</td>
      <td>2006/02/25</td>
      <td>43</td>
      <td>Al Gore</td>
      <td>Al Gore: Averting the climate crisis</td>
      <td>1</td>
      <td>1151367060</td>
      <td>2006/06/27</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 544}, {'i...</td>
      <td>[{'id': 243, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>Climate advocate</td>
      <td>['alternative energy', 'cars', 'climate change...</td>
      <td>Averting the climate crisis</td>
      <td>https://www.ted.com/talks/al_gore_on_averting_...</td>
      <td>3200520</td>
      <td>Thank you so much, Chris. And it's truly a gre...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>124</td>
      <td>New York Times columnist David Pogue takes aim...</td>
      <td>1286</td>
      <td>TED2006</td>
      <td>1140739200</td>
      <td>2006/02/24</td>
      <td>26</td>
      <td>David Pogue</td>
      <td>David Pogue: Simplicity sells</td>
      <td>1</td>
      <td>1151367060</td>
      <td>2006/06/27</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 964}, {'i...</td>
      <td>[{'id': 1725, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>Technology columnist</td>
      <td>['computers', 'entertainment', 'interface desi...</td>
      <td>Simplicity sells</td>
      <td>https://www.ted.com/talks/david_pogue_says_sim...</td>
      <td>1636292</td>
      <td>(Music: "The Sound of Silence," Simon &amp; Garfun...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>200</td>
      <td>In an emotionally charged talk, MacArthur-winn...</td>
      <td>1116</td>
      <td>TED2006</td>
      <td>1140912000</td>
      <td>2006/02/26</td>
      <td>35</td>
      <td>Majora Carter</td>
      <td>Majora Carter: Greening the ghetto</td>
      <td>1</td>
      <td>1151367060</td>
      <td>2006/06/27</td>
      <td>[{'id': 3, 'name': 'Courageous', 'count': 760}...</td>
      <td>[{'id': 1041, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>Activist for environmental justice</td>
      <td>['MacArthur grant', 'activism', 'business', 'c...</td>
      <td>Greening the ghetto</td>
      <td>https://www.ted.com/talks/majora_carter_s_tale...</td>
      <td>1697550</td>
      <td>If you're here today ¡ª and I'm very happy tha...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>593</td>
      <td>You've never seen data presented like this. Wi...</td>
      <td>1190</td>
      <td>TED2006</td>
      <td>1140566400</td>
      <td>2006/02/22</td>
      <td>48</td>
      <td>Hans Rosling</td>
      <td>Hans Rosling: The best stats you've ever seen</td>
      <td>1</td>
      <td>1151440680</td>
      <td>2006/06/28</td>
      <td>[{'id': 9, 'name': 'Ingenious', 'count': 3202}...</td>
      <td>[{'id': 2056, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>Global health expert; data visionary</td>
      <td>['Africa', 'Asia', 'Google', 'demo', 'economic...</td>
      <td>The best stats you've ever seen</td>
      <td>https://www.ted.com/talks/hans_rosling_shows_t...</td>
      <td>12005869</td>
      <td>About 10 years ago, I took on the task to teac...</td>
    </tr>
  </tbody>
</table>
</div>




```python
ted_data['transcripts.transcript']
```




    0       Good morning. How are you?(Laughter)It's been ...
    1       Thank you so much, Chris. And it's truly a gre...
    2       (Music: "The Sound of Silence," Simon & Garfun...
    3       If you're here today ¡ª and I'm very happy tha...
    4       About 10 years ago, I took on the task to teac...
                                  ...                        
    2459    Gayle King: Have a seat, Serena Williams, or s...
    2460    Vanessa Garrison: I am Vanessa, daughter of An...
    2461    (Music)Sophie Hawley-Weld: OK, you don't have ...
    2462    Mother Earth: Our end was imminent yet finalit...
    2463    Caitlin Quattromani: The election of 2016 felt...
    Name: transcripts.transcript, Length: 2464, dtype: object




```python
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words="english",
                        use_idf=True,
                        ngram_range=(1,1), # considering only 1-grams
                        min_df = 0.05,     # cut words present in less than 5% of documents
                        max_df = 0.3)      # cut words present in more than 30% of documents 
t0 = time()

tfidf = vectorizer.fit_transform(ted_data['transcripts.transcript'])
print("done in %0.3fs." % (time() - t0))
```

    done in 4.961s.



```python
# Let's make a function to call the top ranked words in a vectorizer
def rank_words(terms, feature_matrix):
    sums = feature_matrix.sum(axis=0)
    data = []
    for col, term in enumerate(terms):
        data.append( (term, sums[0,col]) )
    ranked = pd.DataFrame(data, columns=['term','rank']).sort_values('rank', ascending=False)
    return ranked

ranked = rank_words(terms=vectorizer.get_feature_names(), feature_matrix=tfidf)

fig, ax = plt.subplots(figsize=(6,10), ncols=1, nrows=1)
sns.barplot(x='rank',y='term',data=ranked[:20], palette='Reds_r', ax=ax);
```


    
![png](output_5_0.png)
    



```python
# Let's visualize a word cloud with the frequencies obtained by idf transformation
dic = {ranked.loc[i,'term'].upper(): ranked.loc[i,'rank'] for i in range(0,len(ranked))}

from wordcloud import WordCloud
wordcloud = WordCloud(background_color='white',
                      max_words=100,
                      colormap='Reds').generate_from_frequencies(dic)
fig = plt.figure(1,figsize=(12,15))
plt.imshow(wordcloud,interpolation="bilinear")
plt.axis('off')
plt.show()
```


    
![png](output_6_0.png)
    



```python
from sklearn.decomposition import LatentDirichletAllocation

n_topics = 10
lda = LatentDirichletAllocation(n_components=n_topics,random_state=0)

topics = lda.fit_transform(tfidf)
top_n_words = 5
t_words, word_strengths = {}, {}
for t_id, t in enumerate(lda.components_):
    t_words[t_id] = [vectorizer.get_feature_names()[i] for i in t.argsort()[:-top_n_words - 1:-1]]
    word_strengths[t_id] = t[t.argsort()[:-top_n_words - 1:-1]]
t_words
```




    {0: ['song', 'marriage', 'boys', 'feelings', 'silence'],
     1: ['song', 'marriage', 'boys', 'feelings', 'silence'],
     2: ['song', 'marriage', 'boys', 'feelings', 'silence'],
     3: ['song', 'marriage', 'boys', 'feelings', 'silence'],
     4: ['women', 'music', 'brain', 'kids', 'children'],
     5: ['song', 'marriage', 'boys', 'feelings', 'silence'],
     6: ['song', 'marriage', 'boys', 'feelings', 'silence'],
     7: ['song', 'marriage', 'boys', 'feelings', 'silence'],
     8: ['music', 'ends', 'starts', 'ca', 'welcome'],
     9: ['water', 'energy', 'cells', 'earth', 'planet']}




```python
fig, ax = plt.subplots(figsize=(7,15), ncols=2, nrows=5)
plt.subplots_adjust(
    wspace  =  0.5,
    hspace  =  0.5
)
c=0
for row in range(0,5):
    for col in range(0,2):
        sns.barplot(x=word_strengths[c], y=t_words[c], color="red", ax=ax[row][col])
        c+=1
plt.show()
```


    
![png](output_8_0.png)
    



```python
from sklearn.decomposition import NMF

n_topics = 10
nmf = NMF(n_components=n_topics,random_state=0)

topics = nmf.fit_transform(tfidf)
top_n_words = 5
t_words, word_strengths = {}, {}
for t_id, t in enumerate(nmf.components_):
    t_words[t_id] = [vectorizer.get_feature_names()[i] for i in t.argsort()[:-top_n_words - 1:-1]]
    word_strengths[t_id] = t[t.argsort()[:-top_n_words - 1:-1]]
t_words
```

    /Users/Administrator/opt/anaconda3/lib/python3.8/site-packages/sklearn/decomposition/_nmf.py:312: FutureWarning: The 'init' value, when 'init=None' and n_components is less than n_samples and n_features, will be changed from 'nndsvd' to 'nndsvda' in 1.1 (renaming of 0.26).
      warnings.warn(("The 'init' value, when 'init=None' and "





    {0: ['god', 'book', 'stories', 'oh', 'art'],
     1: ['women', 'men', 'girls', 'woman', 'sex'],
     2: ['music', 'play', 'sound', 'song', 'ends'],
     3: ['brain', 'brains', 'cells', 'body', 'activity'],
     4: ['water', 'earth', 'planet', 'ocean', 'species'],
     5: ['countries', 'africa', 'government', 'global', 'dollars'],
     6: ['cancer', 'cells', 'patients', 'disease', 'cell'],
     7: ['data', 'information', 'computer', 'machine', 'internet'],
     8: ['city', 'design', 'cities', 'building', 'buildings'],
     9: ['kids', 'children', 'education', 'students', 'teachers']}




```python
ted_data['transcripts.transcript'].index
for x in ted_data['transcripts.transcript'].index:
    print(x)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    46
    47
    48
    49
    50
    51
    52
    53
    54
    55
    56
    57
    58
    59
    60
    61
    62
    63
    64
    65
    66
    67
    68
    69
    70
    71
    72
    73
    74
    75
    76
    77
    78
    79
    80
    81
    82
    83
    84
    85
    86
    87
    88
    89
    90
    91
    92
    93
    94
    95
    96
    97
    98
    99
    100
    101
    102
    103
    104
    105
    106
    107
    108
    109
    110
    111
    112
    113
    114
    115
    116
    117
    118
    119
    120
    121
    122
    123
    124
    125
    126
    127
    128
    129
    130
    131
    132
    133
    134
    135
    136
    137
    138
    139
    140
    141
    142
    143
    144
    145
    146
    147
    148
    149
    150
    151
    152
    153
    154
    155
    156
    157
    158
    159
    160
    161
    162
    163
    164
    165
    166
    167
    168
    169
    170
    171
    172
    173
    174
    175
    176
    177
    178
    179
    180
    181
    182
    183
    184
    185
    186
    187
    188
    189
    190
    191
    192
    193
    194
    195
    196
    197
    198
    199
    200
    201
    202
    203
    204
    205
    206
    207
    208
    209
    210
    211
    212
    213
    214
    215
    216
    217
    218
    219
    220
    221
    222
    223
    224
    225
    226
    227
    228
    229
    230
    231
    232
    233
    234
    235
    236
    237
    238
    239
    240
    241
    242
    243
    244
    245
    246
    247
    248
    249
    250
    251
    252
    253
    254
    255
    256
    257
    258
    259
    260
    261
    262
    263
    264
    265
    266
    267
    268
    269
    270
    271
    272
    273
    274
    275
    276
    277
    278
    279
    280
    281
    282
    283
    284
    285
    286
    287
    288
    289
    290
    291
    292
    293
    294
    295
    296
    297
    298
    299
    300
    301
    302
    303
    304
    305
    306
    307
    308
    309
    310
    311
    312
    313
    314
    315
    316
    317
    318
    319
    320
    321
    322
    323
    324
    325
    326
    327
    328
    329
    330
    331
    332
    333
    334
    335
    336
    337
    338
    339
    340
    341
    342
    343
    344
    345
    346
    347
    348
    349
    350
    351
    352
    353
    354
    355
    356
    357
    358
    359
    360
    361
    362
    363
    364
    365
    366
    367
    368
    369
    370
    371
    372
    373
    374
    375
    376
    377
    378
    379
    380
    381
    382
    383
    384
    385
    386
    387
    388
    389
    390
    391
    392
    393
    394
    395
    396
    397
    398
    399
    400
    401
    402
    403
    404
    405
    406
    407
    408
    409
    410
    411
    412
    413
    414
    415
    416
    417
    418
    419
    420
    421
    422
    423
    424
    425
    426
    427
    428
    429
    430
    431
    432
    433
    434
    435
    436
    437
    438
    439
    440
    441
    442
    443
    444
    445
    446
    447
    448
    449
    450
    451
    452
    453
    454
    455
    456
    457
    458
    459
    460
    461
    462
    463
    464
    465
    466
    467
    468
    469
    470
    471
    472
    473
    474
    475
    476
    477
    478
    479
    480
    481
    482
    483
    484
    485
    486
    487
    488
    489
    490
    491
    492
    493
    494
    495
    496
    497
    498
    499
    500
    501
    502
    503
    504
    505
    506
    507
    508
    509
    510
    511
    512
    513
    514
    515
    516
    517
    518
    519
    520
    521
    522
    523
    524
    525
    526
    527
    528
    529
    530
    531
    532
    533
    534
    535
    536
    537
    538
    539
    540
    541
    542
    543
    544
    545
    546
    547
    548
    549
    550
    551
    552
    553
    554
    555
    556
    557
    558
    559
    560
    561
    562
    563
    564
    565
    566
    567
    568
    569
    570
    571
    572
    573
    574
    575
    576
    577
    578
    579
    580
    581
    582
    583
    584
    585
    586
    587
    588
    589
    590
    591
    592
    593
    594
    595
    596
    597
    598
    599
    600
    601
    602
    603
    604
    605
    606
    607
    608
    609
    610
    611
    612
    613
    614
    615
    616
    617
    618
    619
    620
    621
    622
    623
    624
    625
    626
    627
    628
    629
    630
    631
    632
    633
    634
    635
    636
    637
    638
    639
    640
    641
    642
    643
    644
    645
    646
    647
    648
    649
    650
    651
    652
    653
    654
    655
    656
    657
    658
    659
    660
    661
    662
    663
    664
    665
    666
    667
    668
    669
    670
    671
    672
    673
    674
    675
    676
    677
    678
    679
    680
    681
    682
    683
    684
    685
    686
    687
    688
    689
    690
    691
    692
    693
    694
    695
    696
    697
    698
    699
    700
    701
    702
    703
    704
    705
    706
    707
    708
    709
    710
    711
    712
    713
    714
    715
    716
    717
    718
    719
    720
    721
    722
    723
    724
    725
    726
    727
    728
    729
    730
    731
    732
    733
    734
    735
    736
    737
    738
    739
    740
    741
    742
    743
    744
    745
    746
    747
    748
    749
    750
    751
    752
    753
    754
    755
    756
    757
    758
    759
    760
    761
    762
    763
    764
    765
    766
    767
    768
    769
    770
    771
    772
    773
    774
    775
    776
    777
    778
    779
    780
    781
    782
    783
    784
    785
    786
    787
    788
    789
    790
    791
    792
    793
    794
    795
    796
    797
    798
    799
    800
    801
    802
    803
    804
    805
    806
    807
    808
    809
    810
    811
    812
    813
    814
    815
    816
    817
    818
    819
    820
    821
    822
    823
    824
    825
    826
    827
    828
    829
    830
    831
    832
    833
    834
    835
    836
    837
    838
    839
    840
    841
    842
    843
    844
    845
    846
    847
    848
    849
    850
    851
    852
    853
    854
    855
    856
    857
    858
    859
    860
    861
    862
    863
    864
    865
    866
    867
    868
    869
    870
    871
    872
    873
    874
    875
    876
    877
    878
    879
    880
    881
    882
    883
    884
    885
    886
    887
    888
    889
    890
    891
    892
    893
    894
    895
    896
    897
    898
    899
    900
    901
    902
    903
    904
    905
    906
    907
    908
    909
    910
    911
    912
    913
    914
    915
    916
    917
    918
    919
    920
    921
    922
    923
    924
    925
    926
    927
    928
    929
    930
    931
    932
    933
    934
    935
    936
    937
    938
    939
    940
    941
    942
    943
    944
    945
    946
    947
    948
    949
    950
    951
    952
    953
    954
    955
    956
    957
    958
    959
    960
    961
    962
    963
    964
    965
    966
    967
    968
    969
    970
    971
    972
    973
    974
    975
    976
    977
    978
    979
    980
    981
    982
    983
    984
    985
    986
    987
    988
    989
    990
    991
    992
    993
    994
    995
    996
    997
    998
    999
    1000
    1001
    1002
    1003
    1004
    1005
    1006
    1007
    1008
    1009
    1010
    1011
    1012
    1013
    1014
    1015
    1016
    1017
    1018
    1019
    1020
    1021
    1022
    1023
    1024
    1025
    1026
    1027
    1028
    1029
    1030
    1031
    1032
    1033
    1034
    1035
    1036
    1037
    1038
    1039
    1040
    1041
    1042
    1043
    1044
    1045
    1046
    1047
    1048
    1049
    1050
    1051
    1052
    1053
    1054
    1055
    1056
    1057
    1058
    1059
    1060
    1061
    1062
    1063
    1064
    1065
    1066
    1067
    1068
    1069
    1070
    1071
    1072
    1073
    1074
    1075
    1076
    1077
    1078
    1079
    1080
    1081
    1082
    1083
    1084
    1085
    1086
    1087
    1088
    1089
    1090
    1091
    1092
    1093
    1094
    1095
    1096
    1097
    1098
    1099
    1100
    1101
    1102
    1103
    1104
    1105
    1106
    1107
    1108
    1109
    1110
    1111
    1112
    1113
    1114
    1115
    1116
    1117
    1118
    1119
    1120
    1121
    1122
    1123
    1124
    1125
    1126
    1127
    1128
    1129
    1130
    1131
    1132
    1133
    1134
    1135
    1136
    1137
    1138
    1139
    1140
    1141
    1142
    1143
    1144
    1145
    1146
    1147
    1148
    1149
    1150
    1151
    1152
    1153
    1154
    1155
    1156
    1157
    1158
    1159
    1160
    1161
    1162
    1163
    1164
    1165
    1166
    1167
    1168
    1169
    1170
    1171
    1172
    1173
    1174
    1175
    1176
    1177
    1178
    1179
    1180
    1181
    1182
    1183
    1184
    1185
    1186
    1187
    1188
    1189
    1190
    1191
    1192
    1193
    1194
    1195
    1196
    1197
    1198
    1199
    1200
    1201
    1202
    1203
    1204
    1205
    1206
    1207
    1208
    1209
    1210
    1211
    1212
    1213
    1214
    1215
    1216
    1217
    1218
    1219
    1220
    1221
    1222
    1223
    1224
    1225
    1226
    1227
    1228
    1229
    1230
    1231
    1232
    1233
    1234
    1235
    1236
    1237
    1238
    1239
    1240
    1241
    1242
    1243
    1244
    1245
    1246
    1247
    1248
    1249
    1250
    1251
    1252
    1253
    1254
    1255
    1256
    1257
    1258
    1259
    1260
    1261
    1262
    1263
    1264
    1265
    1266
    1267
    1268
    1269
    1270
    1271
    1272
    1273
    1274
    1275
    1276
    1277
    1278
    1279
    1280
    1281
    1282
    1283
    1284
    1285
    1286
    1287
    1288
    1289
    1290
    1291
    1292
    1293
    1294
    1295
    1296
    1297
    1298
    1299
    1300
    1301
    1302
    1303
    1304
    1305
    1306
    1307
    1308
    1309
    1310
    1311
    1312
    1313
    1314
    1315
    1316
    1317
    1318
    1319
    1320
    1321
    1322
    1323
    1324
    1325
    1326
    1327
    1328
    1329
    1330
    1331
    1332
    1333
    1334
    1335
    1336
    1337
    1338
    1339
    1340
    1341
    1342
    1343
    1344
    1345
    1346
    1347
    1348
    1349
    1350
    1351
    1352
    1353
    1354
    1355
    1356
    1357
    1358
    1359
    1360
    1361
    1362
    1363
    1364
    1365
    1366
    1367
    1368
    1369
    1370
    1371
    1372
    1373
    1374
    1375
    1376
    1377
    1378
    1379
    1380
    1381
    1382
    1383
    1384
    1385
    1386
    1387
    1388
    1389
    1390
    1391
    1392
    1393
    1394
    1395
    1396
    1397
    1398
    1399
    1400
    1401
    1402
    1403
    1404
    1405
    1406
    1407
    1408
    1409
    1410
    1411
    1412
    1413
    1414
    1415
    1416
    1417
    1418
    1419
    1420
    1421
    1422
    1423
    1424
    1425
    1426
    1427
    1428
    1429
    1430
    1431
    1432
    1433
    1434
    1435
    1436
    1437
    1438
    1439
    1440
    1441
    1442
    1443
    1444
    1445
    1446
    1447
    1448
    1449
    1450
    1451
    1452
    1453
    1454
    1455
    1456
    1457
    1458
    1459
    1460
    1461
    1462
    1463
    1464
    1465
    1466
    1467
    1468
    1469
    1470
    1471
    1472
    1473
    1474
    1475
    1476
    1477
    1478
    1479
    1480
    1481
    1482
    1483
    1484
    1485
    1486
    1487
    1488
    1489
    1490
    1491
    1492
    1493
    1494
    1495
    1496
    1497
    1498
    1499
    1500
    1501
    1502
    1503
    1504
    1505
    1506
    1507
    1508
    1509
    1510
    1511
    1512
    1513
    1514
    1515
    1516
    1517
    1518
    1519
    1520
    1521
    1522
    1523
    1524
    1525
    1526
    1527
    1528
    1529
    1530
    1531
    1532
    1533
    1534
    1535
    1536
    1537
    1538
    1539
    1540
    1541
    1542
    1543
    1544
    1545
    1546
    1547
    1548
    1549
    1550
    1551
    1552
    1553
    1554
    1555
    1556
    1557
    1558
    1559
    1560
    1561
    1562
    1563
    1564
    1565
    1566
    1567
    1568
    1569
    1570
    1571
    1572
    1573
    1574
    1575
    1576
    1577
    1578
    1579
    1580
    1581
    1582
    1583
    1584
    1585
    1586
    1587
    1588
    1589
    1590
    1591
    1592
    1593
    1594
    1595
    1596
    1597
    1598
    1599
    1600
    1601
    1602
    1603
    1604
    1605
    1606
    1607
    1608
    1609
    1610
    1611
    1612
    1613
    1614
    1615
    1616
    1617
    1618
    1619
    1620
    1621
    1622
    1623
    1624
    1625
    1626
    1627
    1628
    1629
    1630
    1631
    1632
    1633
    1634
    1635
    1636
    1637
    1638
    1639
    1640
    1641
    1642
    1643
    1644
    1645
    1646
    1647
    1648
    1649
    1650
    1651
    1652
    1653
    1654
    1655
    1656
    1657
    1658
    1659
    1660
    1661
    1662
    1663
    1664
    1665
    1666
    1667
    1668
    1669
    1670
    1671
    1672
    1673
    1674
    1675
    1676
    1677
    1678
    1679
    1680
    1681
    1682
    1683
    1684
    1685
    1686
    1687
    1688
    1689
    1690
    1691
    1692
    1693
    1694
    1695
    1696
    1697
    1698
    1699
    1700
    1701
    1702
    1703
    1704
    1705
    1706
    1707
    1708
    1709
    1710
    1711
    1712
    1713
    1714
    1715
    1716
    1717
    1718
    1719
    1720
    1721
    1722
    1723
    1724
    1725
    1726
    1727
    1728
    1729
    1730
    1731
    1732
    1733
    1734
    1735
    1736
    1737
    1738
    1739
    1740
    1741
    1742
    1743
    1744
    1745
    1746
    1747
    1748
    1749
    1750
    1751
    1752
    1753
    1754
    1755
    1756
    1757
    1758
    1759
    1760
    1761
    1762
    1763
    1764
    1765
    1766
    1767
    1768
    1769
    1770
    1771
    1772
    1773
    1774
    1775
    1776
    1777
    1778
    1779
    1780
    1781
    1782
    1783
    1784
    1785
    1786
    1787
    1788
    1789
    1790
    1791
    1792
    1793
    1794
    1795
    1796
    1797
    1798
    1799
    1800
    1801
    1802
    1803
    1804
    1805
    1806
    1807
    1808
    1809
    1810
    1811
    1812
    1813
    1814
    1815
    1816
    1817
    1818
    1819
    1820
    1821
    1822
    1823
    1824
    1825
    1826
    1827
    1828
    1829
    1830
    1831
    1832
    1833
    1834
    1835
    1836
    1837
    1838
    1839
    1840
    1841
    1842
    1843
    1844
    1845
    1846
    1847
    1848
    1849
    1850
    1851
    1852
    1853
    1854
    1855
    1856
    1857
    1858
    1859
    1860
    1861
    1862
    1863
    1864
    1865
    1866
    1867
    1868
    1869
    1870
    1871
    1872
    1873
    1874
    1875
    1876
    1877
    1878
    1879
    1880
    1881
    1882
    1883
    1884
    1885
    1886
    1887
    1888
    1889
    1890
    1891
    1892
    1893
    1894
    1895
    1896
    1897
    1898
    1899
    1900
    1901
    1902
    1903
    1904
    1905
    1906
    1907
    1908
    1909
    1910
    1911
    1912
    1913
    1914
    1915
    1916
    1917
    1918
    1919
    1920
    1921
    1922
    1923
    1924
    1925
    1926
    1927
    1928
    1929
    1930
    1931
    1932
    1933
    1934
    1935
    1936
    1937
    1938
    1939
    1940
    1941
    1942
    1943
    1944
    1945
    1946
    1947
    1948
    1949
    1950
    1951
    1952
    1953
    1954
    1955
    1956
    1957
    1958
    1959
    1960
    1961
    1962
    1963
    1964
    1965
    1966
    1967
    1968
    1969
    1970
    1971
    1972
    1973
    1974
    1975
    1976
    1977
    1978
    1979
    1980
    1981
    1982
    1983
    1984
    1985
    1986
    1987
    1988
    1989
    1990
    1991
    1992
    1993
    1994
    1995
    1996
    1997
    1998
    1999
    2000
    2001
    2002
    2003
    2004
    2005
    2006
    2007
    2008
    2009
    2010
    2011
    2012
    2013
    2014
    2015
    2016
    2017
    2018
    2019
    2020
    2021
    2022
    2023
    2024
    2025
    2026
    2027
    2028
    2029
    2030
    2031
    2032
    2033
    2034
    2035
    2036
    2037
    2038
    2039
    2040
    2041
    2042
    2043
    2044
    2045
    2046
    2047
    2048
    2049
    2050
    2051
    2052
    2053
    2054
    2055
    2056
    2057
    2058
    2059
    2060
    2061
    2062
    2063
    2064
    2065
    2066
    2067
    2068
    2069
    2070
    2071
    2072
    2073
    2074
    2075
    2076
    2077
    2078
    2079
    2080
    2081
    2082
    2083
    2084
    2085
    2086
    2087
    2088
    2089
    2090
    2091
    2092
    2093
    2094
    2095
    2096
    2097
    2098
    2099
    2100
    2101
    2102
    2103
    2104
    2105
    2106
    2107
    2108
    2109
    2110
    2111
    2112
    2113
    2114
    2115
    2116
    2117
    2118
    2119
    2120
    2121
    2122
    2123
    2124
    2125
    2126
    2127
    2128
    2129
    2130
    2131
    2132
    2133
    2134
    2135
    2136
    2137
    2138
    2139
    2140
    2141
    2142
    2143
    2144
    2145
    2146
    2147
    2148
    2149
    2150
    2151
    2152
    2153
    2154
    2155
    2156
    2157
    2158
    2159
    2160
    2161
    2162
    2163
    2164
    2165
    2166
    2167
    2168
    2169
    2170
    2171
    2172
    2173
    2174
    2175
    2176
    2177
    2178
    2179
    2180
    2181
    2182
    2183
    2184
    2185
    2186
    2187
    2188
    2189
    2190
    2191
    2192
    2193
    2194
    2195
    2196
    2197
    2198
    2199
    2200
    2201
    2202
    2203
    2204
    2205
    2206
    2207
    2208
    2209
    2210
    2211
    2212
    2213
    2214
    2215
    2216
    2217
    2218
    2219
    2220
    2221
    2222
    2223
    2224
    2225
    2226
    2227
    2228
    2229
    2230
    2231
    2232
    2233
    2234
    2235
    2236
    2237
    2238
    2239
    2240
    2241
    2242
    2243
    2244
    2245
    2246
    2247
    2248
    2249
    2250
    2251
    2252
    2253
    2254
    2255
    2256
    2257
    2258
    2259
    2260
    2261
    2262
    2263
    2264
    2265
    2266
    2267
    2268
    2269
    2270
    2271
    2272
    2273
    2274
    2275
    2276
    2277
    2278
    2279
    2280
    2281
    2282
    2283
    2284
    2285
    2286
    2287
    2288
    2289
    2290
    2291
    2292
    2293
    2294
    2295
    2296
    2297
    2298
    2299
    2300
    2301
    2302
    2303
    2304
    2305
    2306
    2307
    2308
    2309
    2310
    2311
    2312
    2313
    2314
    2315
    2316
    2317
    2318
    2319
    2320
    2321
    2322
    2323
    2324
    2325
    2326
    2327
    2328
    2329
    2330
    2331
    2332
    2333
    2334
    2335
    2336
    2337
    2338
    2339
    2340
    2341
    2342
    2343
    2344
    2345
    2346
    2347
    2348
    2349
    2350
    2351
    2352
    2353
    2354
    2355
    2356
    2357
    2358
    2359
    2360
    2361
    2362
    2363
    2364
    2365
    2366
    2367
    2368
    2369
    2370
    2371
    2372
    2373
    2374
    2375
    2376
    2377
    2378
    2379
    2380
    2381
    2382
    2383
    2384
    2385
    2386
    2387
    2388
    2389
    2390
    2391
    2392
    2393
    2394
    2395
    2396
    2397
    2398
    2399
    2400
    2401
    2402
    2403
    2404
    2405
    2406
    2407
    2408
    2409
    2410
    2411
    2412
    2413
    2414
    2415
    2416
    2417
    2418
    2419
    2420
    2421
    2422
    2423
    2424
    2425
    2426
    2427
    2428
    2429
    2430
    2431
    2432
    2433
    2434
    2435
    2436
    2437
    2438
    2439
    2440
    2441
    2442
    2443
    2444
    2445
    2446
    2447
    2448
    2449
    2450
    2451
    2452
    2453
    2454
    2455
    2456
    2457
    2458
    2459
    2460
    2461
    2462
    2463



```python
# Formulating a pipeline to insert a document and extract the topics pertinency
from sklearn.pipeline import Pipeline
pipe = Pipeline([
    ('tfidf', vectorizer),
    ('nmf', nmf)
])


document_id = 4
t = pipe.transform([ted_data['transcripts.transcript'].iloc[document_id]]) 
print('Topic distribution for document #{}: \n'.format(document_id),t)
print('Relevant topics for document #{}: \n'.format(document_id),np.where(t>0.01)[1])
print('\nTranscript:\n',ted_data['transcripts.transcript'].iloc[document_id][:500],'...')
#talk = ted_main_df[ted_main_df['url']==transcripts_df['url'].iloc[document_id]]
#print('\nTrue tags from ted_main.csv: \n',talk['tags'])
```

    Topic distribution for document #4: 
     [[0.         0.         0.         0.         0.         0.12614375
      0.         0.06512969 0.         0.04380911]]
    Relevant topics for document #4: 
     [5 7 9]
    
    Transcript:
     About 10 years ago, I took on the task to teach global development to Swedish undergraduate students. That was after having spent about 20 years together with African institutions studying hunger in Africa, so I was sort of expected to know a little about the world. And I started in our medical university, Karolinska Institute, an undergraduate course called Global Health. But when you get that opportunity, you get a little nervous. I thought, these students coming to us actually have the highes ...



```python
for x in ted_data['transcripts.transcript'].index:
    t = pipe.transform([ted_data['transcripts.transcript'].iloc[x]]) 
    #print('Topic distribution for document #{}: \n'.format(document_id),t)
    print('Relevant topics for document #{}: \n'.format(x),np.where(t>0.01)[1])
#print('\nTranscript:\n',ted_data['transcripts.transcript'].iloc[document_id][:500],'...')
```

    Relevant topics for document #0: 
     [0 1 2 3 4 9]
    Relevant topics for document #1: 
     [0 4 5 8]
    Relevant topics for document #2: 
     [0 2 5 7]
    Relevant topics for document #3: 
     [1 4 5 8 9]
    Relevant topics for document #4: 
     [5 7 9]
    Relevant topics for document #5: 
     [0 3 5 6 7 9]
    Relevant topics for document #6: 
     [0 1 9]
    Relevant topics for document #7: 
     [0 7 8]
    Relevant topics for document #8: 
     [0 2 3 4 7 8 9]
    Relevant topics for document #9: 
     [0 5 9]
    Relevant topics for document #10: 
     [1 5 6 7 8 9]
    Relevant topics for document #11: 
     [0 1 2 5 9]
    Relevant topics for document #12: 
     [0 1 5 6 9]
    Relevant topics for document #13: 
     [7]
    Relevant topics for document #14: 
     [0 5 7 9]
    Relevant topics for document #15: 
     [0 2 7 8 9]
    Relevant topics for document #16: 
     [0 2 7 8]
    Relevant topics for document #17: 
     [1 4 5 6 7 8 9]
    Relevant topics for document #18: 
     [0 4 7 8]
    Relevant topics for document #19: 
     [0 5 7 8 9]
    Relevant topics for document #20: 
     [0 2 5 7 8 9]
    Relevant topics for document #21: 
     [0 2 5 7]
    Relevant topics for document #22: 
     [0 2 7 9]
    Relevant topics for document #23: 
     [1 3 5]
    Relevant topics for document #24: 
     [0 1 4 8]
    Relevant topics for document #25: 
     [3 4 7]
    Relevant topics for document #26: 
     [0 3 4 7]
    Relevant topics for document #27: 
     [0 1 5 6 7 8]
    Relevant topics for document #28: 
     [0 4 5 6 7 9]
    Relevant topics for document #29: 
     [0 3 6 7 9]
    Relevant topics for document #30: 
     [0 5 6 7 9]
    Relevant topics for document #31: 
     [3 6]
    Relevant topics for document #32: 
     [0 3 4 5 6 7]
    Relevant topics for document #33: 
     [5 7 8]
    Relevant topics for document #34: 
     [1 4 5 9]
    Relevant topics for document #35: 
     [0 5 7]
    Relevant topics for document #36: 
     [1 5 7 8]
    Relevant topics for document #37: 
     [0 4 5 7 8 9]
    Relevant topics for document #38: 
     [0 2 4]
    Relevant topics for document #39: 
     [0 5 7]
    Relevant topics for document #40: 
     [0 4 5 7 8 9]
    Relevant topics for document #41: 
     [0 3 6 7]
    Relevant topics for document #42: 
     [0 3 4 5 6 7 9]
    Relevant topics for document #43: 
     [0 2 3 4 7]
    Relevant topics for document #44: 
     [3 4 5 6 7 8]
    Relevant topics for document #45: 
     [0 3 4 6 7]
    Relevant topics for document #46: 
     [0 1 2 4 5 7 9]
    Relevant topics for document #47: 
     [0 7 9]
    Relevant topics for document #48: 
     [0 2 7 9]
    Relevant topics for document #49: 
     [5 6 9]
    Relevant topics for document #50: 
     [1 4 5 8 9]
    Relevant topics for document #51: 
     [4 5 6 7 9]
    Relevant topics for document #52: 
     [0 3 4 5 9]
    Relevant topics for document #53: 
     [0 4 5 9]
    Relevant topics for document #54: 
     [4 5 7]
    Relevant topics for document #55: 
     [0 3 5 7]
    Relevant topics for document #56: 
     [0 4 6 8]
    Relevant topics for document #57: 
     [2 5 7 8 9]
    Relevant topics for document #58: 
     [0 1 9]
    Relevant topics for document #59: 
     [4 7 8]
    Relevant topics for document #60: 
     [4 5 7 8 9]
    Relevant topics for document #61: 
     [0 4 5 8 9]
    Relevant topics for document #62: 
     [4 5 6 8 9]
    Relevant topics for document #63: 
     [4 5 6]
    Relevant topics for document #64: 
     [0 1 5 9]
    Relevant topics for document #65: 
     [0 1 3 4 5 7 9]
    Relevant topics for document #66: 
     [0 2 5 7 8]
    Relevant topics for document #67: 
     [0 6 7 9]
    Relevant topics for document #68: 
     [0 1 3 4 7 8]
    Relevant topics for document #69: 
     [0 4 5 8]
    Relevant topics for document #70: 
     [2 4 5 6 7]
    Relevant topics for document #71: 
     [0 7 8]
    Relevant topics for document #72: 
     [2 4 5 7 8 9]
    Relevant topics for document #73: 
     [3 4 8]
    Relevant topics for document #74: 
     [0 1 7 8]
    Relevant topics for document #75: 
     [0 6]
    Relevant topics for document #76: 
     [0 6 7 8 9]
    Relevant topics for document #77: 
     [0 4 7 8]
    Relevant topics for document #78: 
     [0 2 3 4 5 6 7]
    Relevant topics for document #79: 
     [0 4 6 7 8 9]
    Relevant topics for document #80: 
     [3 4 6 7 8]
    Relevant topics for document #81: 
     [0 2 7]
    Relevant topics for document #82: 
     [0 2 3 4 7 9]
    Relevant topics for document #83: 
     [4]
    Relevant topics for document #84: 
     [0 2 3 4 6 7]
    Relevant topics for document #85: 
     [0 4]
    Relevant topics for document #86: 
     [0 2 4]
    Relevant topics for document #87: 
     [0 3 7]
    Relevant topics for document #88: 
     [0 2 3 4]
    Relevant topics for document #89: 
     [4 5 6 8 9]
    Relevant topics for document #90: 
     [0 4 5 7 8]
    Relevant topics for document #91: 
     [0 1 4 8 9]
    Relevant topics for document #92: 
     [0]
    Relevant topics for document #93: 
     [0 2 4 5 7]
    Relevant topics for document #94: 
     [0 2 3 4 7 8 9]
    Relevant topics for document #95: 
     [0 2 5 7]
    Relevant topics for document #96: 
     [1]
    Relevant topics for document #97: 
     [0 5 8 9]
    Relevant topics for document #98: 
     [0 4 7 8 9]
    Relevant topics for document #99: 
     [5 8]
    Relevant topics for document #100: 
     [3 4 7]
    Relevant topics for document #101: 
     [0 4 7]
    Relevant topics for document #102: 
     [4 7]
    Relevant topics for document #103: 
     [4 5]
    Relevant topics for document #104: 
     [1 5]
    Relevant topics for document #105: 
     [0 7]
    Relevant topics for document #106: 
     [0 3 4 8]
    Relevant topics for document #107: 
     [0 8]
    Relevant topics for document #108: 
     [0 5 7]
    Relevant topics for document #109: 
     [4 7 8]
    Relevant topics for document #110: 
     [1 5 6 9]
    Relevant topics for document #111: 
     [0 4 5 7 8]
    Relevant topics for document #112: 
     [0 3 5 7]
    Relevant topics for document #113: 
     [0 3 5 6 8]
    Relevant topics for document #114: 
     [0 1 4 7]
    Relevant topics for document #115: 
     [1 5 6 7 9]
    Relevant topics for document #116: 
     [0 2 4 7 8 9]
    Relevant topics for document #117: 
     [0 2 6]
    Relevant topics for document #118: 
     [0 2 3 6 7 9]
    Relevant topics for document #119: 
     [0 6 9]
    Relevant topics for document #120: 
     [5]
    Relevant topics for document #121: 
     [1 5 9]
    Relevant topics for document #122: 
     [0 5 7]
    Relevant topics for document #123: 
     [4 5]
    Relevant topics for document #124: 
     [0 1 5 9]
    Relevant topics for document #125: 
     [0 1 5 9]
    Relevant topics for document #126: 
     [1 5 6 9]
    Relevant topics for document #127: 
     [0 2]
    Relevant topics for document #128: 
     [0 1 5 7]
    Relevant topics for document #129: 
     [0 4 9]
    Relevant topics for document #130: 
     [0 7]
    Relevant topics for document #131: 
     [5]
    Relevant topics for document #132: 
     [2 3 4]
    Relevant topics for document #133: 
     [0 3 7 8 9]
    Relevant topics for document #134: 
     [0 1 3 4 5]
    Relevant topics for document #135: 
     [0 5 7]
    Relevant topics for document #136: 
     [0 1 3 4 5 6 7 9]
    Relevant topics for document #137: 
     [0 4 7 9]
    Relevant topics for document #138: 
     [0 4 5 6 7]
    Relevant topics for document #139: 
     [0 2 4 7]
    Relevant topics for document #140: 
     [0 4]
    Relevant topics for document #141: 
     [2]
    Relevant topics for document #142: 
     [0 4 5 7]
    Relevant topics for document #143: 
     [0 3 4 7 8]
    Relevant topics for document #144: 
     [0 2 8 9]
    Relevant topics for document #145: 
     [0 5 7 8]
    Relevant topics for document #146: 
     [0 3 6]
    Relevant topics for document #147: 
     [5]
    Relevant topics for document #148: 
     [0 3 5 6 9]
    Relevant topics for document #149: 
     [0 3 4 9]
    Relevant topics for document #150: 
     [0 2 5 7 9]
    Relevant topics for document #151: 
     [4 6 7]
    Relevant topics for document #152: 
     [0 4 5 7]
    Relevant topics for document #153: 
     [4 5 6 7 8]
    Relevant topics for document #154: 
     [4 5 6]
    Relevant topics for document #155: 
     [0 3 4 7 8]
    Relevant topics for document #156: 
     [0 3 4 5 7 8 9]
    Relevant topics for document #157: 
     [0 3 4 7 8]
    Relevant topics for document #158: 
     [0 3 4 7]
    Relevant topics for document #159: 
     [4 5 8]
    Relevant topics for document #160: 
     [0 7]
    Relevant topics for document #161: 
     [0 1 3 5 7 8 9]
    Relevant topics for document #162: 
     [0 6 9]
    Relevant topics for document #163: 
     [0 2 3 7 9]
    Relevant topics for document #164: 
     [0 1 2 3 4 5 6 9]
    Relevant topics for document #165: 
     [0 1 4 5 6 7]
    Relevant topics for document #166: 
     [0 3 4 5 6 7 9]
    Relevant topics for document #167: 
     [0 7]
    Relevant topics for document #168: 
     [0 4]
    Relevant topics for document #169: 
     [0 7 8]
    Relevant topics for document #170: 
     [0 8]
    Relevant topics for document #171: 
     [0 2]
    Relevant topics for document #172: 
     [0 2 5 8 9]
    Relevant topics for document #173: 
     [0 1 2 4 5 9]
    Relevant topics for document #174: 
     [0 2 5 7]
    Relevant topics for document #175: 
     [0 5 7 8]
    Relevant topics for document #176: 
     [0 3 4 5 7]
    Relevant topics for document #177: 
     [5 7 8]
    Relevant topics for document #178: 
     [2 8 9]
    Relevant topics for document #179: 
     [0 4 7 8]
    Relevant topics for document #180: 
     [0 3 4 6]
    Relevant topics for document #181: 
     [3 5 7 8]
    Relevant topics for document #182: 
     [0 2 3 9]
    Relevant topics for document #183: 
     [0 4 7 8 9]
    Relevant topics for document #184: 
     [0 4 8 9]
    Relevant topics for document #185: 
     [0 2]
    Relevant topics for document #186: 
     [0 1 4 5 8 9]
    Relevant topics for document #187: 
     [0 2 4 7 9]
    Relevant topics for document #188: 
     [0 3 4 7 8 9]
    Relevant topics for document #189: 
     [4 6 7 8]
    Relevant topics for document #190: 
     [0 7 9]
    Relevant topics for document #191: 
     [0 3 4]
    Relevant topics for document #192: 
     [0 4 7 8]
    Relevant topics for document #193: 
     [0 7 8 9]
    Relevant topics for document #194: 
     [0 1 5]
    Relevant topics for document #195: 
     [4 5 7 9]
    Relevant topics for document #196: 
     [4 5 7 8]
    Relevant topics for document #197: 
     [3]
    Relevant topics for document #198: 
     [0 2 4 7 9]
    Relevant topics for document #199: 
     [0 4]
    Relevant topics for document #200: 
     [0 4 5 7 8]
    Relevant topics for document #201: 
     [0 2 8]
    Relevant topics for document #202: 
     [4 5 7]
    Relevant topics for document #203: 
     [0 4 5]
    Relevant topics for document #204: 
     [4 7 9]
    Relevant topics for document #205: 
     [5 7 8]
    Relevant topics for document #206: 
     [5 6 9]
    Relevant topics for document #207: 
     [0 3 4 5]
    Relevant topics for document #208: 
     [3 4 7 8]
    Relevant topics for document #209: 
     [0 4 7]
    Relevant topics for document #210: 
     [0 2]
    Relevant topics for document #211: 
     [1 2 5 7 9]
    Relevant topics for document #212: 
     [0 4 5 6 7]
    Relevant topics for document #213: 
     [3 4 5 6 7 8]
    Relevant topics for document #214: 
     [0 2 4 7 8]
    Relevant topics for document #215: 
     [0 3 4 7 8 9]
    Relevant topics for document #216: 
     [0 5 7]
    Relevant topics for document #217: 
     [4 5 6 9]
    Relevant topics for document #218: 
     [0 4 9]
    Relevant topics for document #219: 
     [0 2 4 7 8 9]
    Relevant topics for document #220: 
     [0 3 4 7 8]
    Relevant topics for document #221: 
     [0 4 5 6 7 9]
    Relevant topics for document #222: 
     [4 5]
    Relevant topics for document #223: 
     [0 3 4 7]
    Relevant topics for document #224: 
     [0 1 4 6 7 8]
    Relevant topics for document #225: 
     [0 1 4]
    Relevant topics for document #226: 
     [0 5]
    Relevant topics for document #227: 
     [4 7]
    Relevant topics for document #228: 
     [0 1 3 4 5 7 9]
    Relevant topics for document #229: 
     [3 6]
    Relevant topics for document #230: 
     [0 3 4 7 8]
    Relevant topics for document #231: 
     [4 5 6 7 9]
    Relevant topics for document #232: 
     [0 6 7 8 9]
    Relevant topics for document #233: 
     [0 2 9]
    Relevant topics for document #234: 
     [0 5 7 8 9]
    Relevant topics for document #235: 
     [0 6]
    Relevant topics for document #236: 
     [0 4 6 8 9]
    Relevant topics for document #237: 
     [0 9]
    Relevant topics for document #238: 
     [0 4]
    Relevant topics for document #239: 
     [0 4 5 6 8 9]
    Relevant topics for document #240: 
     [0 2 3 4 6 7]
    Relevant topics for document #241: 
     [0 1 9]
    Relevant topics for document #242: 
     [0 5 7 8 9]
    Relevant topics for document #243: 
     [0 1 4 8 9]
    Relevant topics for document #244: 
     [4]
    Relevant topics for document #245: 
     [0 1 3 4]
    Relevant topics for document #246: 
     [0 5 6]
    Relevant topics for document #247: 
     [0 1 3 5 7]
    Relevant topics for document #248: 
     [0 3]
    Relevant topics for document #249: 
     [0 3 5 6 7 8 9]
    Relevant topics for document #250: 
     [4 5 7 8]
    Relevant topics for document #251: 
     [0 1 9]
    Relevant topics for document #252: 
     [0 1 3 4 5]
    Relevant topics for document #253: 
     [0 1 4 7 8]
    Relevant topics for document #254: 
     [0 2 7 8]
    Relevant topics for document #255: 
     [3 7]
    Relevant topics for document #256: 
     [3 7]
    Relevant topics for document #257: 
     [0 3 4 7 8]
    Relevant topics for document #258: 
     [0 4 7 8]
    Relevant topics for document #259: 
     [0 4 5 6 7]
    Relevant topics for document #260: 
     [0 4 5 8]
    Relevant topics for document #261: 
     [0 3]
    Relevant topics for document #262: 
     [0 9]
    Relevant topics for document #263: 
     [0]
    Relevant topics for document #264: 
     [0 2 7]
    Relevant topics for document #265: 
     [7 8 9]
    Relevant topics for document #266: 
     [0 5 6 9]
    Relevant topics for document #267: 
     [0 2 4]
    Relevant topics for document #268: 
     [4 6 7 8]
    Relevant topics for document #269: 
     [0 4 5 7 8]
    Relevant topics for document #270: 
     [0 1 2 5 7]
    Relevant topics for document #271: 
     [0 4 7 9]
    Relevant topics for document #272: 
     [0 1 3 4 5 8 9]
    Relevant topics for document #273: 
     [0 4 5 8]
    Relevant topics for document #274: 
     [0 2 5 7 9]
    Relevant topics for document #275: 
     [0 2 4]
    Relevant topics for document #276: 
     [0 1 8 9]
    Relevant topics for document #277: 
     [0 2 4 8]
    Relevant topics for document #278: 
     [4 5 9]
    Relevant topics for document #279: 
     [0 1 3 4 5 7]
    Relevant topics for document #280: 
     [0 1 4 5]
    Relevant topics for document #281: 
     [0 3 5 7]
    Relevant topics for document #282: 
     [3 4 5 6 7 8 9]
    Relevant topics for document #283: 
     [0 1 3 5 6 7 9]
    Relevant topics for document #284: 
     [0 7 9]
    Relevant topics for document #285: 
     [0 4 7 8 9]
    Relevant topics for document #286: 
     [0 1 2 3 4 5 7 8 9]
    Relevant topics for document #287: 
     [0 3 4 7 8]
    Relevant topics for document #288: 
     [0 7 8]
    Relevant topics for document #289: 
     [0 5]
    Relevant topics for document #290: 
     [0 2 3 4 7 8]
    Relevant topics for document #291: 
     [0 5 6]
    Relevant topics for document #292: 
     [0 2 3 7 9]
    Relevant topics for document #293: 
     [0 1 5 9]
    Relevant topics for document #294: 
     [0 3 7 8]
    Relevant topics for document #295: 
     [0 2]
    Relevant topics for document #296: 
     [0 3 4 7 8]
    Relevant topics for document #297: 
     [1 6 7 8]
    Relevant topics for document #298: 
     [0 1 4 7 8]
    Relevant topics for document #299: 
     [0 1 3 4 5 6 9]
    Relevant topics for document #300: 
     [0 1 3 4 8]
    Relevant topics for document #301: 
     [0 2 4 7 9]
    Relevant topics for document #302: 
     [0 2 3 5 7]
    Relevant topics for document #303: 
     [0 1 5 9]
    Relevant topics for document #304: 
     [4 5]
    Relevant topics for document #305: 
     [0 2 4]
    Relevant topics for document #306: 
     [0 1 5 9]
    Relevant topics for document #307: 
     [0]
    Relevant topics for document #308: 
     [0 3 5 9]
    Relevant topics for document #309: 
     [0 8 9]
    Relevant topics for document #310: 
     [0]
    Relevant topics for document #311: 
     [0 3 4 9]
    Relevant topics for document #312: 
     [0 3 5]
    Relevant topics for document #313: 
     [0 4]
    Relevant topics for document #314: 
     [0 4 5 7]
    Relevant topics for document #315: 
     [0 4 9]
    Relevant topics for document #316: 
     [0 2 7 8 9]
    Relevant topics for document #317: 
     [0 4 7 8]
    Relevant topics for document #318: 
     [1 3 4 5 7]
    Relevant topics for document #319: 
     [0 1 5 8]
    Relevant topics for document #320: 
     [0 2 4 7 8]
    Relevant topics for document #321: 
     [0 8]
    Relevant topics for document #322: 
     [0 4 8]
    Relevant topics for document #323: 
     [0 1 7 9]
    Relevant topics for document #324: 
     [0 5 7]
    Relevant topics for document #325: 
     [4 7 8]
    Relevant topics for document #326: 
     [0 4 5 6 7 8]
    Relevant topics for document #327: 
     [0 4 5 9]
    Relevant topics for document #328: 
     [0]
    Relevant topics for document #329: 
     [3 5 6]
    Relevant topics for document #330: 
     [0 4 9]
    Relevant topics for document #331: 
     [0 1 5 7 8]
    Relevant topics for document #332: 
     [2 4 5 6 7 8]
    Relevant topics for document #333: 
     [0 4 7 8]
    Relevant topics for document #334: 
     [0 2 9]
    Relevant topics for document #335: 
     [0 5 8]
    Relevant topics for document #336: 
     [0 4 5 6 8 9]
    Relevant topics for document #337: 
     [0 3 4 7 8]
    Relevant topics for document #338: 
     [0 3 4 5 7]
    Relevant topics for document #339: 
     [0 3 4 5 7 8]
    Relevant topics for document #340: 
     [4 7]
    Relevant topics for document #341: 
     [0 2 3 4 6 7 8]
    Relevant topics for document #342: 
     [5 9]
    Relevant topics for document #343: 
     [0 5 8]
    Relevant topics for document #344: 
     [0 4 5 7]
    Relevant topics for document #345: 
     [0 2 7 8]
    Relevant topics for document #346: 
     [0 3 4 5 6 7 8 9]
    Relevant topics for document #347: 
     [0 3 4 5 7 8]
    Relevant topics for document #348: 
     [3 4 7 8]
    Relevant topics for document #349: 
     [0 7 8]
    Relevant topics for document #350: 
     [0 2 4 7 8]
    Relevant topics for document #351: 
     [0 4 6 9]
    Relevant topics for document #352: 
     [0 2 5 8]
    Relevant topics for document #353: 
     [0 2 7 8 9]
    Relevant topics for document #354: 
     [0 2 7 8 9]
    Relevant topics for document #355: 
     [4 5 7]
    Relevant topics for document #356: 
     [0 4 6 7]
    Relevant topics for document #357: 
     [0 5 6]
    Relevant topics for document #358: 
     [0 2 3 4 7 8 9]
    Relevant topics for document #359: 
     [0 4]
    Relevant topics for document #360: 
     [0 1 4]
    Relevant topics for document #361: 
     [4 6 7]
    Relevant topics for document #362: 
     [0 1 2 9]
    Relevant topics for document #363: 
     [4 5 6 7 8]
    Relevant topics for document #364: 
     [5 6 7 9]
    Relevant topics for document #365: 
     [0 2 4]
    Relevant topics for document #366: 
     [0 7 8]
    Relevant topics for document #367: 
     [2 7 9]
    Relevant topics for document #368: 
     [0 5 9]
    Relevant topics for document #369: 
     [0 3 4 5 6 7 9]
    Relevant topics for document #370: 
     [1 2 5 9]
    Relevant topics for document #371: 
     [0 2 5]
    Relevant topics for document #372: 
     [4]
    Relevant topics for document #373: 
     [3 4 7]
    Relevant topics for document #374: 
     [0 6 7]
    Relevant topics for document #375: 
     [4 5 9]
    Relevant topics for document #376: 
     [0 4 6]
    Relevant topics for document #377: 
     [0 8]
    Relevant topics for document #378: 
     [0 5 7]
    Relevant topics for document #379: 
     [0 1 2 7 9]
    Relevant topics for document #380: 
     [4 5 8 9]
    Relevant topics for document #381: 
     [0 1 2 4 7 8 9]
    Relevant topics for document #382: 
     [0 3 4 5 7]
    Relevant topics for document #383: 
     [0 3 4 7 8]
    Relevant topics for document #384: 
     [0 1 8 9]
    Relevant topics for document #385: 
     [0 2 3 7 9]
    Relevant topics for document #386: 
     [7]
    Relevant topics for document #387: 
     [0 3 4 7 8]
    Relevant topics for document #388: 
     [0 5 6 7 9]
    Relevant topics for document #389: 
     [0 4 7 8]
    Relevant topics for document #390: 
     [0 7 8]
    Relevant topics for document #391: 
     [4 6 8]
    Relevant topics for document #392: 
     [0 4 5 7 9]
    Relevant topics for document #393: 
     [0 1 5 6 8 9]
    Relevant topics for document #394: 
     [0 2 7]
    Relevant topics for document #395: 
     [0 7 9]
    Relevant topics for document #396: 
     [0 3 4 5 6 7 9]
    Relevant topics for document #397: 
     [0 1 2 3 9]
    Relevant topics for document #398: 
     [0 2 5 7 8]
    Relevant topics for document #399: 
     [0 4]
    Relevant topics for document #400: 
     [0 7 8]
    Relevant topics for document #401: 
     [0 5 7]
    Relevant topics for document #402: 
     [0 2 8]
    Relevant topics for document #403: 
     [0 4 5 7 9]
    Relevant topics for document #404: 
     [0 3 4 6 7]
    Relevant topics for document #405: 
     [0 1 3 7 8]
    Relevant topics for document #406: 
     [0 5 7]
    Relevant topics for document #407: 
     [0 4 5 7 8]
    Relevant topics for document #408: 
     [0 3 4 5 6 7 9]
    Relevant topics for document #409: 
     [2 3 4 7]
    Relevant topics for document #410: 
     [0 1 4 9]
    Relevant topics for document #411: 
     [0 1 4]
    Relevant topics for document #412: 
     [0 4 7 8 9]
    Relevant topics for document #413: 
     [0 4 7 8]
    Relevant topics for document #414: 
     [5 7]
    Relevant topics for document #415: 
     [0 1 5 8 9]
    Relevant topics for document #416: 
     [0 2 3 4 8 9]
    Relevant topics for document #417: 
     [4 5 6 7]
    Relevant topics for document #418: 
     [3 9]
    Relevant topics for document #419: 
     [0 1 2 5 9]
    Relevant topics for document #420: 
     [0 4 5 6 8 9]
    Relevant topics for document #421: 
     [0 4 7]
    Relevant topics for document #422: 
     [1 5 7]
    Relevant topics for document #423: 
     [0 1 2 3 4 5 6 7 8 9]
    Relevant topics for document #424: 
     [0 2 4 7 8]
    Relevant topics for document #425: 
     [4 5]
    Relevant topics for document #426: 
     [4 5 8 9]
    Relevant topics for document #427: 
     [0 5 7 8]
    Relevant topics for document #428: 
     [1 3 5 6]
    Relevant topics for document #429: 
     [5 8 9]
    Relevant topics for document #430: 
     [0 4]
    Relevant topics for document #431: 
     [4 5 8 9]
    Relevant topics for document #432: 
     [0 3 5 6 7]
    Relevant topics for document #433: 
     [0 1 3 4 6 7]
    Relevant topics for document #434: 
     [4]
    Relevant topics for document #435: 
     [0 4 8]
    Relevant topics for document #436: 
     [0 9]
    Relevant topics for document #437: 
     [0 2 9]
    Relevant topics for document #438: 
     [0 1 5 8 9]
    Relevant topics for document #439: 
     [4 5]
    Relevant topics for document #440: 
     [0 2 4]
    Relevant topics for document #441: 
     [0 1 5 7 8 9]
    Relevant topics for document #442: 
     [3 5 7]
    Relevant topics for document #443: 
     [0 1 4 5]
    Relevant topics for document #444: 
     [0 1 9]
    Relevant topics for document #445: 
     [4 5 8]
    Relevant topics for document #446: 
     [4 5 7]
    Relevant topics for document #447: 
     [0 4 5 7 8 9]
    Relevant topics for document #448: 
     [0 1 3 5 6]
    Relevant topics for document #449: 
     [0 3 4 6 7 8]
    Relevant topics for document #450: 
     [0 9]
    Relevant topics for document #451: 
     [0 4 6 8 9]
    Relevant topics for document #452: 
     [0 5 7 8]
    Relevant topics for document #453: 
     [0 3]
    Relevant topics for document #454: 
     [0 3 5 6 7]
    Relevant topics for document #455: 
     [0 5 9]
    Relevant topics for document #456: 
     [1 5]
    Relevant topics for document #457: 
     [0 1 4 5 7 8]
    Relevant topics for document #458: 
     [0 4 5 9]
    Relevant topics for document #459: 
     [7 9]
    Relevant topics for document #460: 
     [7 8 9]
    Relevant topics for document #461: 
     [3 8]
    Relevant topics for document #462: 
     [0 2 4 7 8 9]
    Relevant topics for document #463: 
     [0 3 7 8]
    Relevant topics for document #464: 
     [0 1 5 9]
    Relevant topics for document #465: 
     [0 4 6]
    Relevant topics for document #466: 
     [4 5 8 9]
    Relevant topics for document #467: 
     [0 3 4 8]
    Relevant topics for document #468: 
     [3 6]
    Relevant topics for document #469: 
     [0 1 3 9]
    Relevant topics for document #470: 
     [3 4 5 6]
    Relevant topics for document #471: 
     [0 5 9]
    Relevant topics for document #472: 
     [0 5]
    Relevant topics for document #473: 
     [0 2 3 7 8]
    Relevant topics for document #474: 
     [0 3 4 6]
    Relevant topics for document #475: 
     [0 4 7 8]
    Relevant topics for document #476: 
     [0 4 8 9]
    Relevant topics for document #477: 
     [5 8 9]
    Relevant topics for document #478: 
     [4 6 7 8]
    Relevant topics for document #479: 
     [0 1 2 5 9]
    Relevant topics for document #480: 
     [0 3 4 5 7 8 9]
    Relevant topics for document #481: 
     [0 4 7 8]
    Relevant topics for document #482: 
     [5 9]
    Relevant topics for document #483: 
     [0 2 7 8 9]
    Relevant topics for document #484: 
     [0 4 5 8]
    Relevant topics for document #485: 
     [5 6 7]
    Relevant topics for document #486: 
     [5 8 9]
    Relevant topics for document #487: 
     [0 2 3 4 7 9]
    Relevant topics for document #488: 
     [0 1 4 7 8]
    Relevant topics for document #489: 
     [0 4 5 7 8]
    Relevant topics for document #490: 
     [0 4 9]
    Relevant topics for document #491: 
     [3 9]
    Relevant topics for document #492: 
     [0 1 5 7]
    Relevant topics for document #493: 
     [0 4 5 8]
    Relevant topics for document #494: 
     [0 1 3 4 6 7]
    Relevant topics for document #495: 
     [0 3 6 8]
    Relevant topics for document #496: 
     [0 4]
    Relevant topics for document #497: 
     [0 5 7]
    Relevant topics for document #498: 
     [0 5 7]
    Relevant topics for document #499: 
     [0 4 7 9]
    Relevant topics for document #500: 
     [0 1 4 5 7 8]
    Relevant topics for document #501: 
     [1 4 5 8 9]
    Relevant topics for document #502: 
     [4 5]
    Relevant topics for document #503: 
     [5 6 7 8 9]
    Relevant topics for document #504: 
     [0 5]
    Relevant topics for document #505: 
     [4]
    Relevant topics for document #506: 
     [0 2 7 8]
    Relevant topics for document #507: 
     [4 5 8 9]
    Relevant topics for document #508: 
     [0 5 6 7]
    Relevant topics for document #509: 
     [0 1 5 9]
    Relevant topics for document #510: 
     [0 2 3 4 7]
    Relevant topics for document #511: 
     [0 4 8]
    Relevant topics for document #512: 
     [4 8]
    Relevant topics for document #513: 
     [0 4 7 8]
    Relevant topics for document #514: 
     [0 4 5 7 9]
    Relevant topics for document #515: 
     [3 4 7 8]
    Relevant topics for document #516: 
     [0 2 3 4]
    Relevant topics for document #517: 
     [0 5 7 8 9]
    Relevant topics for document #518: 
     [0 3 4 7]
    Relevant topics for document #519: 
     [0 2]
    Relevant topics for document #520: 
     [0 4 5 6 7 9]
    Relevant topics for document #521: 
     [3 4 5 6 7]
    Relevant topics for document #522: 
     [0 3 4 5 7]
    Relevant topics for document #523: 
     [4 6 8]
    Relevant topics for document #524: 
     [0 1 4 5]
    Relevant topics for document #525: 
     [0 3 4 7 8]
    Relevant topics for document #526: 
     [0 1 5 7 8 9]
    Relevant topics for document #527: 
     [1 4 5 8 9]
    Relevant topics for document #528: 
     [4 5 6 7 9]
    Relevant topics for document #529: 
     [4 5 8]
    Relevant topics for document #530: 
     [1 2 5 7]
    Relevant topics for document #531: 
     [0 7]
    Relevant topics for document #532: 
     [0 3 4 6 7 8 9]
    Relevant topics for document #533: 
     [0 1 2 4 5 8 9]
    Relevant topics for document #534: 
     [0 2 4 5]
    Relevant topics for document #535: 
     [0 4 7 8]
    Relevant topics for document #536: 
     [5 9]
    Relevant topics for document #537: 
     [0 4 5 8 9]
    Relevant topics for document #538: 
     [4 5 8 9]
    Relevant topics for document #539: 
     [0 1 2 4 5 9]
    Relevant topics for document #540: 
     [0 5 9]
    Relevant topics for document #541: 
     [4 5]
    Relevant topics for document #542: 
     [0 1 4 7]
    Relevant topics for document #543: 
     [4 8 9]
    Relevant topics for document #544: 
     [0 3 7 8]
    Relevant topics for document #545: 
     [0 1 9]
    Relevant topics for document #546: 
     [0 4 5]
    Relevant topics for document #547: 
     [0 1 3]
    Relevant topics for document #548: 
     [0 2 5 6 7 8 9]
    Relevant topics for document #549: 
     [0 1 2]
    Relevant topics for document #550: 
     [0 5]
    Relevant topics for document #551: 
     [0 1 5 9]
    Relevant topics for document #552: 
     [0 5 7]
    Relevant topics for document #553: 
     [4 5]
    Relevant topics for document #554: 
     [0 3 5 7]
    Relevant topics for document #555: 
     [0 5 7 8 9]
    Relevant topics for document #556: 
     [4 5 8]
    Relevant topics for document #557: 
     [0 2 5 6 8 9]
    Relevant topics for document #558: 
     [0 4 5 8]
    Relevant topics for document #559: 
     [0 3]
    Relevant topics for document #560: 
     [0 2 4 6 7 8]
    Relevant topics for document #561: 
     [0 1 3 4 5 6 9]
    Relevant topics for document #562: 
     [0 4 5 8 9]
    Relevant topics for document #563: 
     [2]
    Relevant topics for document #564: 
     [1 4 5 9]
    Relevant topics for document #565: 
     [1 2 8 9]
    Relevant topics for document #566: 
     [5 7 8]
    Relevant topics for document #567: 
     [0 4 7]
    Relevant topics for document #568: 
     [0 3 4 6 8]
    Relevant topics for document #569: 
     [0 1 4 5 7 8]
    Relevant topics for document #570: 
     [3 6]
    Relevant topics for document #571: 
     [0 4 5 6 7 8 9]
    Relevant topics for document #572: 
     [0 3 5 7 8]
    Relevant topics for document #573: 
     [0 1 4 6 9]
    Relevant topics for document #574: 
     [1 4 5 6 8 9]
    Relevant topics for document #575: 
     [0 2 8]
    Relevant topics for document #576: 
     [0 1 3 4 5 6 7 8 9]
    Relevant topics for document #577: 
     [6 7]
    Relevant topics for document #578: 
     [0 4 5 6 7 9]
    Relevant topics for document #579: 
     [6]
    Relevant topics for document #580: 
     [5 8]
    Relevant topics for document #581: 
     [0 4 5 6 9]
    Relevant topics for document #582: 
     [0 4 7 8]
    Relevant topics for document #583: 
     [5 7 9]
    Relevant topics for document #584: 
     [0 5 6 9]
    Relevant topics for document #585: 
     [4 5 7 8]
    Relevant topics for document #586: 
     [3 4 5 6 7 9]
    Relevant topics for document #587: 
     [0 5 7 9]
    Relevant topics for document #588: 
     [0 3 5 6 7]
    Relevant topics for document #589: 
     [0 3 7 8 9]
    Relevant topics for document #590: 
     [3 6 7 9]
    Relevant topics for document #591: 
     [0 8 9]
    Relevant topics for document #592: 
     [0 3 5 6]
    Relevant topics for document #593: 
     [0 2 5 8 9]
    Relevant topics for document #594: 
     [7]
    Relevant topics for document #595: 
     [0 4 7 9]
    Relevant topics for document #596: 
     [0 2 7 9]
    Relevant topics for document #597: 
     [0 3 4 5 7 9]
    Relevant topics for document #598: 
     [7 8]
    Relevant topics for document #599: 
     [0 5 8]
    Relevant topics for document #600: 
     [4]
    Relevant topics for document #601: 
     [0 3 4 6 7]
    Relevant topics for document #602: 
     [0 4 5 6]
    Relevant topics for document #603: 
     [0 5 6 7 9]
    Relevant topics for document #604: 
     [0 2 4 5 7 9]
    Relevant topics for document #605: 
     [0 3 4]
    Relevant topics for document #606: 
     [0 1 2 4 8]
    Relevant topics for document #607: 
     [0 1 3 4 5 7 9]
    Relevant topics for document #608: 
     [3 4 5 6]
    Relevant topics for document #609: 
     [0 5 7]
    Relevant topics for document #610: 
     [4]
    Relevant topics for document #611: 
     [0 2]
    Relevant topics for document #612: 
     [0 2 4 5 9]
    Relevant topics for document #613: 
     [0 9]
    Relevant topics for document #614: 
     [0 3 4 5]
    Relevant topics for document #615: 
     [0 5]
    Relevant topics for document #616: 
     [9]
    Relevant topics for document #617: 
     [1 3 5 6 7]
    Relevant topics for document #618: 
     [0 3 7 9]
    Relevant topics for document #619: 
     [0 3 4 5 6 7 8 9]
    Relevant topics for document #620: 
     [0 1 4 6 8]
    Relevant topics for document #621: 
     [0 2 9]
    Relevant topics for document #622: 
     [0 4 5 6 7 9]
    Relevant topics for document #623: 
     [0 3 4 5 7]
    Relevant topics for document #624: 
     [4 8]
    Relevant topics for document #625: 
     [0 8]
    Relevant topics for document #626: 
     [3 4 6 7]
    Relevant topics for document #627: 
     [0 4 5 7 9]
    Relevant topics for document #628: 
     [5 6]
    Relevant topics for document #629: 
     [7 8 9]
    Relevant topics for document #630: 
     [0 4 5 7]
    Relevant topics for document #631: 
     [0 1 2 5]
    Relevant topics for document #632: 
     [3 4 7 8 9]
    Relevant topics for document #633: 
     [0 4]
    Relevant topics for document #634: 
     [0 4 5 6 7 8]
    Relevant topics for document #635: 
     [0 7 8]
    Relevant topics for document #636: 
     [5 6 9]
    Relevant topics for document #637: 
     [0 3 5 7]
    Relevant topics for document #638: 
     [0 4 5]
    Relevant topics for document #639: 
     [0 1 2 4 5 7 8 9]
    Relevant topics for document #640: 
     [0 3 5 6 7 8]
    Relevant topics for document #641: 
     [0 4 5 6 7 9]
    Relevant topics for document #642: 
     [4 5]
    Relevant topics for document #643: 
     [0 7 9]
    Relevant topics for document #644: 
     [0 1 7 9]
    Relevant topics for document #645: 
     [6]
    Relevant topics for document #646: 
     [0 4 5 6 9]
    Relevant topics for document #647: 
     [0 4 5 7 9]
    Relevant topics for document #648: 
     [4 5 8]
    Relevant topics for document #649: 
     [4 6 7]
    Relevant topics for document #650: 
     [0 4 5 7 9]
    Relevant topics for document #651: 
     [0 2 5 7 8]
    Relevant topics for document #652: 
     [0 1 9]
    Relevant topics for document #653: 
     [0 2 3 4 5 6 7]
    Relevant topics for document #654: 
     [0 2 5 7 8]
    Relevant topics for document #655: 
     [0 4 7 8]
    Relevant topics for document #656: 
     [0 4]
    Relevant topics for document #657: 
     [0 5 7 8 9]
    Relevant topics for document #658: 
     [4]
    Relevant topics for document #659: 
     [0 2 7]
    Relevant topics for document #660: 
     [0 1 2 3 5 7 9]
    Relevant topics for document #661: 
     [0 1 4 5 8 9]
    Relevant topics for document #662: 
     [0 2 3 5 7 9]
    Relevant topics for document #663: 
     [0 2 5]
    Relevant topics for document #664: 
     [0 1 3 4 6 7]
    Relevant topics for document #665: 
     [0 2 5 7]
    Relevant topics for document #666: 
     [0 2 3 4 5 7]
    Relevant topics for document #667: 
     [0 5 7 8 9]
    Relevant topics for document #668: 
     [0 2 6]
    Relevant topics for document #669: 
     [0 5 7]
    Relevant topics for document #670: 
     [0 3 7 8]
    Relevant topics for document #671: 
     [2 5 7 8 9]
    Relevant topics for document #672: 
     [3 9]
    Relevant topics for document #673: 
     [0 7 8 9]
    Relevant topics for document #674: 
     [0 5 7 8 9]
    Relevant topics for document #675: 
     [4 5 8 9]
    Relevant topics for document #676: 
     [1 4 5 6 9]
    Relevant topics for document #677: 
     [2 4 7]
    Relevant topics for document #678: 
     [4 6 8 9]
    Relevant topics for document #679: 
     [0 3 4 5 7]
    Relevant topics for document #680: 
     [4 5 9]
    Relevant topics for document #681: 
     [0 1 4 8]
    Relevant topics for document #682: 
     [4 5 9]
    Relevant topics for document #683: 
     [4 5]
    Relevant topics for document #684: 
     [0 1 3 4 5 6 7]
    Relevant topics for document #685: 
     [0 5 7]
    Relevant topics for document #686: 
     [0 1 5 8 9]
    Relevant topics for document #687: 
     [0 5 7]
    Relevant topics for document #688: 
     [0 1 5 8 9]
    Relevant topics for document #689: 
     [4 7]
    Relevant topics for document #690: 
     [3 5 7]
    Relevant topics for document #691: 
     [4 6 7 8]
    Relevant topics for document #692: 
     [0 1 3 5 9]
    Relevant topics for document #693: 
     [4 5 6 7]
    Relevant topics for document #694: 
     [4 7]
    Relevant topics for document #695: 
     [0 3 4 5 7 9]
    Relevant topics for document #696: 
     [0 4]
    Relevant topics for document #697: 
     [4 5 7]
    Relevant topics for document #698: 
     [0 1 4 5 9]
    Relevant topics for document #699: 
     [0 1 3 7 9]
    Relevant topics for document #700: 
     [0 1 3 5 7]
    Relevant topics for document #701: 
     [0 5]
    Relevant topics for document #702: 
     [0 5 7]
    Relevant topics for document #703: 
     [5 7]
    Relevant topics for document #704: 
     [4 5]
    Relevant topics for document #705: 
     [0 4 9]
    Relevant topics for document #706: 
     [4 5]
    Relevant topics for document #707: 
     [4 7 9]
    Relevant topics for document #708: 
     [0 4 5 7 9]
    Relevant topics for document #709: 
     [4 5]
    Relevant topics for document #710: 
     [0 1 3 5 6 7 8 9]
    Relevant topics for document #711: 
     [0 7]
    Relevant topics for document #712: 
     [0 3 4 8]
    Relevant topics for document #713: 
     [2 7 9]
    Relevant topics for document #714: 
     [0 2 4 8]
    Relevant topics for document #715: 
     [0 5]
    Relevant topics for document #716: 
     [0 1 2 5 7]
    Relevant topics for document #717: 
     [4]
    Relevant topics for document #718: 
     [0 2 4 5 7 9]
    Relevant topics for document #719: 
     [0 3 4 6]
    Relevant topics for document #720: 
     [5 7]
    Relevant topics for document #721: 
     [0 2]
    Relevant topics for document #722: 
     [0 4 5 6 7 8]
    Relevant topics for document #723: 
     [0 3 4 5 7 8]
    Relevant topics for document #724: 
     [1 5 6 9]
    Relevant topics for document #725: 
     [0 1 5 6 9]
    Relevant topics for document #726: 
     [7 8]
    Relevant topics for document #727: 
     [0 1 2 3 6]
    Relevant topics for document #728: 
     [0 3 6 7 9]
    Relevant topics for document #729: 
     [0 3 4 7]
    Relevant topics for document #730: 
     [0 1 5 6 9]
    Relevant topics for document #731: 
     [1 5 8 9]
    Relevant topics for document #732: 
     [4 6 7 8]
    Relevant topics for document #733: 
     [0 4 5 7]
    Relevant topics for document #734: 
     [4 7]
    Relevant topics for document #735: 
     [1 5 6 9]
    Relevant topics for document #736: 
     [0 3 6]
    Relevant topics for document #737: 
     [3 4]
    Relevant topics for document #738: 
     [0 1 5 6 7 9]
    Relevant topics for document #739: 
     [5 8 9]
    Relevant topics for document #740: 
     [4 5 6 8 9]
    Relevant topics for document #741: 
     [0 2 7 8]
    Relevant topics for document #742: 
     [0 5 9]
    Relevant topics for document #743: 
     [3 4 9]
    Relevant topics for document #744: 
     [4 9]
    Relevant topics for document #745: 
     [0 2 5 7]
    Relevant topics for document #746: 
     [0 4 5 6 7 8 9]
    Relevant topics for document #747: 
     [5]
    Relevant topics for document #748: 
     [4 5 6 9]
    Relevant topics for document #749: 
     [0 3 4 5 6 8]
    Relevant topics for document #750: 
     [2 4]
    Relevant topics for document #751: 
     [0 2 3 4 5 7 9]
    Relevant topics for document #752: 
     [0 5 7]
    Relevant topics for document #753: 
     [0 4 5]
    Relevant topics for document #754: 
     [3 4 6 7]
    Relevant topics for document #755: 
     [0 2 3 6]
    Relevant topics for document #756: 
     [7 8 9]
    Relevant topics for document #757: 
     [1 5 8]
    Relevant topics for document #758: 
     [0 1 4 5]
    Relevant topics for document #759: 
     [5 9]
    Relevant topics for document #760: 
     [4 5 7]
    Relevant topics for document #761: 
     [7 9]
    Relevant topics for document #762: 
     [0 1 2 3 4 8]
    Relevant topics for document #763: 
     [0 4 9]
    Relevant topics for document #764: 
     [2 4 8 9]
    Relevant topics for document #765: 
     [4 5]
    Relevant topics for document #766: 
     [0 2 3 9]
    Relevant topics for document #767: 
     [0 1 2 5 9]
    Relevant topics for document #768: 
     [0 5 7 8]
    Relevant topics for document #769: 
     [0 4 5 6 7 8 9]
    Relevant topics for document #770: 
     [4 6 9]
    Relevant topics for document #771: 
     [0 1 5]
    Relevant topics for document #772: 
     [4 5 6 9]
    Relevant topics for document #773: 
     [3 4 5 6 9]
    Relevant topics for document #774: 
     [4 8 9]
    Relevant topics for document #775: 
     [1 5]
    Relevant topics for document #776: 
     [0 1 8]
    Relevant topics for document #777: 
     [0 1 5 9]
    Relevant topics for document #778: 
     [1 5 7 8 9]
    Relevant topics for document #779: 
     [7 9]
    Relevant topics for document #780: 
     [0 1 3 9]
    Relevant topics for document #781: 
     [0 2 5 7 8]
    Relevant topics for document #782: 
     [0 1 4 5]
    Relevant topics for document #783: 
     [1 7 9]
    Relevant topics for document #784: 
     [1 4 5 6 8 9]
    Relevant topics for document #785: 
     [0 7 9]
    Relevant topics for document #786: 
     [0 5 6 9]
    Relevant topics for document #787: 
     [0 1]
    Relevant topics for document #788: 
     [0 1 2]
    Relevant topics for document #789: 
     [2 3 7]
    Relevant topics for document #790: 
     [1 5 6 7]
    Relevant topics for document #791: 
     [0 4 9]
    Relevant topics for document #792: 
     [0 1 5]
    Relevant topics for document #793: 
     [0 3 4 7 8]
    Relevant topics for document #794: 
     [0 2 4 7 8 9]
    Relevant topics for document #795: 
     [0 1 5]
    Relevant topics for document #796: 
     [0 1 7 9]
    Relevant topics for document #797: 
     [0 1 4 5]
    Relevant topics for document #798: 
     [0 6]
    Relevant topics for document #799: 
     [4 5 6 9]
    Relevant topics for document #800: 
     [3 6 7]
    Relevant topics for document #801: 
     [0 6 7]
    Relevant topics for document #802: 
     [5]
    Relevant topics for document #803: 
     [5 6 7]
    Relevant topics for document #804: 
     [0 1 5]
    Relevant topics for document #805: 
     [0 2 3 7 8 9]
    Relevant topics for document #806: 
     [0 1 6 8 9]
    Relevant topics for document #807: 
     [4 8]
    Relevant topics for document #808: 
     [0 2 4 7 8 9]
    Relevant topics for document #809: 
     [1 5 7]
    Relevant topics for document #810: 
     [0 1 3 4 6]
    Relevant topics for document #811: 
     [0 1]
    Relevant topics for document #812: 
     [0 5 8 9]
    Relevant topics for document #813: 
     [0 2 3 7 9]
    Relevant topics for document #814: 
     [0 1 6 9]
    Relevant topics for document #815: 
     [4 5 8]
    Relevant topics for document #816: 
     [0 2]
    Relevant topics for document #817: 
     [0 1 4 5 6]
    Relevant topics for document #818: 
     [3 9]
    Relevant topics for document #819: 
     [0 1 4 5 9]
    Relevant topics for document #820: 
     [5 7 8]
    Relevant topics for document #821: 
     [1 5]
    Relevant topics for document #822: 
     [0 1 3 5 6 7]
    Relevant topics for document #823: 
     [0 3 6 9]
    Relevant topics for document #824: 
     [0 1 4 7]
    Relevant topics for document #825: 
     [6 7]
    Relevant topics for document #826: 
     [2]
    Relevant topics for document #827: 
     [0 1 5]
    Relevant topics for document #828: 
     [0 1 8]
    Relevant topics for document #829: 
     [0 5 7]
    Relevant topics for document #830: 
     [3 5 6 7 9]
    Relevant topics for document #831: 
     [3 6 8]
    Relevant topics for document #832: 
     [0 1 4 5 9]
    Relevant topics for document #833: 
     [7 9]
    Relevant topics for document #834: 
     [0 4 7 9]
    Relevant topics for document #835: 
     [4 5]
    Relevant topics for document #836: 
     [0 1 3 4 5 7 9]
    Relevant topics for document #837: 
     [0 2 4]
    Relevant topics for document #838: 
     [0 5 8 9]
    Relevant topics for document #839: 
     [0 4 8]
    Relevant topics for document #840: 
     [0 4 8 9]
    Relevant topics for document #841: 
     [1 4 5 7 9]
    Relevant topics for document #842: 
     [0 1 2 3 4 7 9]
    Relevant topics for document #843: 
     [3 4 6 7 8]
    Relevant topics for document #844: 
     [0 4 7 8]
    Relevant topics for document #845: 
     [0 2 4]
    Relevant topics for document #846: 
     [0 9]
    Relevant topics for document #847: 
     [3 4 5 6 7]
    Relevant topics for document #848: 
     [0 2 3 4 5 8]
    Relevant topics for document #849: 
     [0 7 8]
    Relevant topics for document #850: 
     [0 2 7]
    Relevant topics for document #851: 
     [2 4 7 9]
    Relevant topics for document #852: 
     [0 1 5 7 9]
    Relevant topics for document #853: 
     [0 3 5 7 9]
    Relevant topics for document #854: 
     [0 5 7]
    Relevant topics for document #855: 
     [0 7 8]
    Relevant topics for document #856: 
     [0 9]
    Relevant topics for document #857: 
     [0 2 4]
    Relevant topics for document #858: 
     [3 4 6 7]
    Relevant topics for document #859: 
     [0 5 7 8]
    Relevant topics for document #860: 
     [0 2 6 7]
    Relevant topics for document #861: 
     [4 5 7 8]
    Relevant topics for document #862: 
     [3 6]
    Relevant topics for document #863: 
     [0 5 9]
    Relevant topics for document #864: 
     [0 4 7]
    Relevant topics for document #865: 
     [0 4 5 7 8 9]
    Relevant topics for document #866: 
     [0 1 4 8]
    Relevant topics for document #867: 
     [0 4 9]
    Relevant topics for document #868: 
     [3 4 5 6]
    Relevant topics for document #869: 
     [0 3 5 6 7]
    Relevant topics for document #870: 
     [4 6 7 8]
    Relevant topics for document #871: 
     [0 4 7]
    Relevant topics for document #872: 
     [0 4 7 8 9]
    Relevant topics for document #873: 
     [0 5 7]
    Relevant topics for document #874: 
     [0 1 9]
    Relevant topics for document #875: 
     [2 4 7 8]
    Relevant topics for document #876: 
     [0 4 6 8]
    Relevant topics for document #877: 
     [4 7]
    Relevant topics for document #878: 
     [0 2 4]
    Relevant topics for document #879: 
     [0 2 4]
    Relevant topics for document #880: 
     [0 4 6 7 8]
    Relevant topics for document #881: 
     [0 3 4 9]
    Relevant topics for document #882: 
     [0 7 8 9]
    Relevant topics for document #883: 
     [0 7 9]
    Relevant topics for document #884: 
     [3 4 6]
    Relevant topics for document #885: 
     [0 4 8 9]
    Relevant topics for document #886: 
     [0 3 6]
    Relevant topics for document #887: 
     [0 4 7]
    Relevant topics for document #888: 
     [0 9]
    Relevant topics for document #889: 
     [0 2 7 8]
    Relevant topics for document #890: 
     [5 6 9]
    Relevant topics for document #891: 
     [0 1 2 5]
    Relevant topics for document #892: 
     [0 1 5]
    Relevant topics for document #893: 
     [3 7 8]
    Relevant topics for document #894: 
     [0 1 2 5 7 8]
    Relevant topics for document #895: 
     [0 2 3 4 7 8]
    Relevant topics for document #896: 
     [0 9]
    Relevant topics for document #897: 
     [0 2 5 7]
    Relevant topics for document #898: 
     [0 4 6 7 8 9]
    Relevant topics for document #899: 
     [0 4 7 8 9]
    Relevant topics for document #900: 
     [5 8]
    Relevant topics for document #901: 
     [0 1 3 4 5 6]
    Relevant topics for document #902: 
     [0 5 9]
    Relevant topics for document #903: 
     [3 5 6 7]
    Relevant topics for document #904: 
     [0 8]
    Relevant topics for document #905: 
     [0 2 3 5 7 9]
    Relevant topics for document #906: 
     [0 2 4]
    Relevant topics for document #907: 
     [2 4 8]
    Relevant topics for document #908: 
     [2 9]
    Relevant topics for document #909: 
     [0 4 5 7 8]
    Relevant topics for document #910: 
     [0 3 4 7]
    Relevant topics for document #911: 
     [0 6 9]
    Relevant topics for document #912: 
     [0 2 4 7]
    Relevant topics for document #913: 
     [0 3]
    Relevant topics for document #914: 
     [0 1 5 6 8]
    Relevant topics for document #915: 
     [0 3 4 7]
    Relevant topics for document #916: 
     [0 6 7]
    Relevant topics for document #917: 
     [0 5 8]
    Relevant topics for document #918: 
     [0 7]
    Relevant topics for document #919: 
     [0 4 7 9]
    Relevant topics for document #920: 
     [0 4 6]
    Relevant topics for document #921: 
     [0 3 4 5 6 9]
    Relevant topics for document #922: 
     [3 6]
    Relevant topics for document #923: 
     [5 7]
    Relevant topics for document #924: 
     [0 1 5]
    Relevant topics for document #925: 
     [0 5 6 7]
    Relevant topics for document #926: 
     [0 1 5 7]
    Relevant topics for document #927: 
     [3 5 7]
    Relevant topics for document #928: 
     [0 1 3]
    Relevant topics for document #929: 
     [0 4 5 7 8]
    Relevant topics for document #930: 
     [3 4 7]
    Relevant topics for document #931: 
     [0 4 5]
    Relevant topics for document #932: 
     [4 5 6 7 8]
    Relevant topics for document #933: 
     [0 2 3 5 7 9]
    Relevant topics for document #934: 
     [1 3 4 5 9]
    Relevant topics for document #935: 
     [0 2 3]
    Relevant topics for document #936: 
     [0 5 6 7]
    Relevant topics for document #937: 
     [4 7]
    Relevant topics for document #938: 
     [0 3 4 5 7 9]
    Relevant topics for document #939: 
     [4 6 7 8]
    Relevant topics for document #940: 
     [1 7 9]
    Relevant topics for document #941: 
     [0 1 4 6]
    Relevant topics for document #942: 
     [4 5 8]
    Relevant topics for document #943: 
     [0 4 5]
    Relevant topics for document #944: 
     [0 1 5 9]
    Relevant topics for document #945: 
     [4]
    Relevant topics for document #946: 
     [0 1 2 3]
    Relevant topics for document #947: 
     [0 1 6 7]
    Relevant topics for document #948: 
     [3 4 5 6 7]
    Relevant topics for document #949: 
     [0 1 2 3 5 9]
    Relevant topics for document #950: 
     [4 6 7 8]
    Relevant topics for document #951: 
     [0 1 3 6]
    Relevant topics for document #952: 
     [0 2 3 4 5 6 7]
    Relevant topics for document #953: 
     [0 1 9]
    Relevant topics for document #954: 
     [3 4 6 7 8]
    Relevant topics for document #955: 
     [0 2 8 9]
    Relevant topics for document #956: 
     [1 5]
    Relevant topics for document #957: 
     [0 3 5 7]
    Relevant topics for document #958: 
     [0 4 7 8]
    Relevant topics for document #959: 
     [0 1 4 5 6 7 9]
    Relevant topics for document #960: 
     [0 1 5 7]
    Relevant topics for document #961: 
     [0 4 5]
    Relevant topics for document #962: 
     [0 1 5]
    Relevant topics for document #963: 
     [6]
    Relevant topics for document #964: 
     [0 3 7 9]
    Relevant topics for document #965: 
     [0 6 9]
    Relevant topics for document #966: 
     [5 7 8 9]
    Relevant topics for document #967: 
     [0 5]
    Relevant topics for document #968: 
     [5 6 7]
    Relevant topics for document #969: 
     [0 2 4]
    Relevant topics for document #970: 
     [0 1 5 7 8 9]
    Relevant topics for document #971: 
     [0 4 6 7]
    Relevant topics for document #972: 
     [0 4 7 8]
    Relevant topics for document #973: 
     [4 5 7 8]
    Relevant topics for document #974: 
     [0 2 5]
    Relevant topics for document #975: 
     [3 4 7 9]
    Relevant topics for document #976: 
     [0 3 4 7 8]
    Relevant topics for document #977: 
     [0 7]
    Relevant topics for document #978: 
     [0 1 3 7 9]
    Relevant topics for document #979: 
     [0 3 4 5 6 8]
    Relevant topics for document #980: 
     [1 4 8 9]
    Relevant topics for document #981: 
     [0 4 5 6 8]
    Relevant topics for document #982: 
     [0 5 7]
    Relevant topics for document #983: 
     [0 3 6 7]
    Relevant topics for document #984: 
     [2 4 7]
    Relevant topics for document #985: 
     [1 5 7 9]
    Relevant topics for document #986: 
     [0 4 5 7]
    Relevant topics for document #987: 
     [6 7]
    Relevant topics for document #988: 
     [0 8]
    Relevant topics for document #989: 
     [0 5 7 8]
    Relevant topics for document #990: 
     [0 1 3 5 6 7]
    Relevant topics for document #991: 
     [0 4 5 7 8]
    Relevant topics for document #992: 
     [3 4 7 9]
    Relevant topics for document #993: 
     [2 7]
    Relevant topics for document #994: 
     [0 5 7]
    Relevant topics for document #995: 
     [3 4 6 7 8]
    Relevant topics for document #996: 
     [0 2 4 7 8]
    Relevant topics for document #997: 
     [0 4 5 7 8 9]
    Relevant topics for document #998: 
     [3 6 7]
    Relevant topics for document #999: 
     [0 7 8 9]
    Relevant topics for document #1000: 
     [0 2 3 6 7 8]
    Relevant topics for document #1001: 
     [0 2 4 7]
    Relevant topics for document #1002: 
     [4 7 8 9]
    Relevant topics for document #1003: 
     [3 4 6]
    Relevant topics for document #1004: 
     [0 3 4 9]
    Relevant topics for document #1005: 
     [0 4 8]
    Relevant topics for document #1006: 
     [0 2 7]
    Relevant topics for document #1007: 
     [0 2 7]
    Relevant topics for document #1008: 
     [4 5 7 8 9]
    Relevant topics for document #1009: 
     [0 4 9]
    Relevant topics for document #1010: 
     [0 9]
    Relevant topics for document #1011: 
     [0 1 3 4 6 7 9]
    Relevant topics for document #1012: 
     [0 2 3 9]
    Relevant topics for document #1013: 
     [0 3 5 7 9]
    Relevant topics for document #1014: 
     [0 1 4 8 9]
    Relevant topics for document #1015: 
     [0 5 7 8]
    Relevant topics for document #1016: 
     [0 3 7 9]
    Relevant topics for document #1017: 
     [4 6 7]
    Relevant topics for document #1018: 
     [0 1 3 6]
    Relevant topics for document #1019: 
     [0 2]
    Relevant topics for document #1020: 
     [0 1 4 5]
    Relevant topics for document #1021: 
     [0 6 8]
    Relevant topics for document #1022: 
     [4 5 8]
    Relevant topics for document #1023: 
     [0 6 8 9]
    Relevant topics for document #1024: 
     [1 4 5 6 8 9]
    Relevant topics for document #1025: 
     [0 3]
    Relevant topics for document #1026: 
     [3 6 7]
    Relevant topics for document #1027: 
     [0 1 3 5 7]
    Relevant topics for document #1028: 
     [0 1 5 9]
    Relevant topics for document #1029: 
     [0 6 8 9]
    Relevant topics for document #1030: 
     [0 3 6 9]
    Relevant topics for document #1031: 
     [0 1 3 5 6]
    Relevant topics for document #1032: 
     [0 4 5 8]
    Relevant topics for document #1033: 
     [0 7]
    Relevant topics for document #1034: 
     [0]
    Relevant topics for document #1035: 
     [0 5]
    Relevant topics for document #1036: 
     [4 6 7]
    Relevant topics for document #1037: 
     [0 1 2]
    Relevant topics for document #1038: 
     [4 7]
    Relevant topics for document #1039: 
     [0 5 8 9]
    Relevant topics for document #1040: 
     [5 7]
    Relevant topics for document #1041: 
     [0 5 7 9]
    Relevant topics for document #1042: 
     [0 5 7]
    Relevant topics for document #1043: 
     [4 5 6 8 9]
    Relevant topics for document #1044: 
     [0 3 4 7]
    Relevant topics for document #1045: 
     [7 8]
    Relevant topics for document #1046: 
     [0 4 6 9]
    Relevant topics for document #1047: 
     [0 6]
    Relevant topics for document #1048: 
     [1 5]
    Relevant topics for document #1049: 
     [0 5 7 8]
    Relevant topics for document #1050: 
     [0 1 2 5]
    Relevant topics for document #1051: 
     [6]
    Relevant topics for document #1052: 
     [0 3 5 9]
    Relevant topics for document #1053: 
     [4 6 7 8]
    Relevant topics for document #1054: 
     [3 4 6 7 8]
    Relevant topics for document #1055: 
     [0 4]
    Relevant topics for document #1056: 
     [3 6 8]
    Relevant topics for document #1057: 
     [0 5]
    Relevant topics for document #1058: 
     [0 1 5 8]
    Relevant topics for document #1059: 
     [0 4 6 8 9]
    Relevant topics for document #1060: 
     [0 3 4 7 8]
    Relevant topics for document #1061: 
     [0 1 5 9]
    Relevant topics for document #1062: 
     [0 1 7 9]
    Relevant topics for document #1063: 
     [2 5 6 7 8 9]
    Relevant topics for document #1064: 
     [0 1 4 5 6 7]
    Relevant topics for document #1065: 
     [5 7 8]
    Relevant topics for document #1066: 
     [4 5]
    Relevant topics for document #1067: 
     [0 5]
    Relevant topics for document #1068: 
     [0 3 4 5 7]
    Relevant topics for document #1069: 
     [0 2 4 7 9]
    Relevant topics for document #1070: 
     [0 5 7 9]
    Relevant topics for document #1071: 
     [0 1 9]
    Relevant topics for document #1072: 
     [6 7 8]
    Relevant topics for document #1073: 
     [0 2 7 8]
    Relevant topics for document #1074: 
     [4 7]
    Relevant topics for document #1075: 
     [4 5]
    Relevant topics for document #1076: 
     [4 5 6 7]
    Relevant topics for document #1077: 
     [0 4 5]
    Relevant topics for document #1078: 
     [2 3 4 7 8]
    Relevant topics for document #1079: 
     [0 5 7 9]
    Relevant topics for document #1080: 
     [0 1 5 9]
    Relevant topics for document #1081: 
     [0 7 9]
    Relevant topics for document #1082: 
     [4 5]
    Relevant topics for document #1083: 
     [5 7 8]
    Relevant topics for document #1084: 
     [2 4 7]
    Relevant topics for document #1085: 
     [0 9]
    Relevant topics for document #1086: 
     [0 2 3 4 5 7 8]
    Relevant topics for document #1087: 
     [2 5 7]
    Relevant topics for document #1088: 
     [0 1 7]
    Relevant topics for document #1089: 
     [4 5]
    Relevant topics for document #1090: 
     [1 6]
    Relevant topics for document #1091: 
     [4 5 7 9]
    Relevant topics for document #1092: 
     [0 2 3 4 8 9]
    Relevant topics for document #1093: 
     [0 5 6]
    Relevant topics for document #1094: 
     [4 5 6 7 8 9]
    Relevant topics for document #1095: 
     [0 3 4 7]
    Relevant topics for document #1096: 
     [0 1 9]
    Relevant topics for document #1097: 
     [2 4 7 8 9]
    Relevant topics for document #1098: 
     [0 7]
    Relevant topics for document #1099: 
     [0 4 5 7 8]
    Relevant topics for document #1100: 
     [0 1 7 9]
    Relevant topics for document #1101: 
     [0 7 8]
    Relevant topics for document #1102: 
     [0 3 6 7 9]
    Relevant topics for document #1103: 
     [0 2 3 4 6 7 8]
    Relevant topics for document #1104: 
     [4 5 8]
    Relevant topics for document #1105: 
     [0 7 9]
    Relevant topics for document #1106: 
     [0 3 4 7 9]
    Relevant topics for document #1107: 
     [1 5 9]
    Relevant topics for document #1108: 
     [0 4 5 6 7 8 9]
    Relevant topics for document #1109: 
     [0 2 5 9]
    Relevant topics for document #1110: 
     [0 5 6 7 8 9]
    Relevant topics for document #1111: 
     [0 5 7]
    Relevant topics for document #1112: 
     [0 1 4 5 6 7 9]
    Relevant topics for document #1113: 
     [0 3 5 6 7 9]
    Relevant topics for document #1114: 
     [4 5 6 7]
    Relevant topics for document #1115: 
     [4 7]
    Relevant topics for document #1116: 
     [0 5 7 9]
    Relevant topics for document #1117: 
     [2 8]
    Relevant topics for document #1118: 
     [0 7 9]
    Relevant topics for document #1119: 
     [0 7]
    Relevant topics for document #1120: 
     [0 4 7 9]
    Relevant topics for document #1121: 
     [0 4 5 8]
    Relevant topics for document #1122: 
     [4 5 8]
    Relevant topics for document #1123: 
     [0 4 7 8]
    Relevant topics for document #1124: 
     [2 5 7 9]
    Relevant topics for document #1125: 
     [0 3 4 5 7 8 9]
    Relevant topics for document #1126: 
     [1 3 7]
    Relevant topics for document #1127: 
     [0 2 8 9]
    Relevant topics for document #1128: 
     [3 4 7 9]
    Relevant topics for document #1129: 
     [0 2 4]
    Relevant topics for document #1130: 
     [0 3 7 8]
    Relevant topics for document #1131: 
     [0 7]
    Relevant topics for document #1132: 
     [0 3 4 6]
    Relevant topics for document #1133: 
     [0 3 5 6 7 9]
    Relevant topics for document #1134: 
     [0 3 4 5 7]
    Relevant topics for document #1135: 
     [0 6 7 9]
    Relevant topics for document #1136: 
     [3 6 7 8]
    Relevant topics for document #1137: 
     [0 5 8 9]
    Relevant topics for document #1138: 
     [0 4 5 7 8]
    Relevant topics for document #1139: 
     [4 6 7]
    Relevant topics for document #1140: 
     [1 5 9]
    Relevant topics for document #1141: 
     [0 2 4 8]
    Relevant topics for document #1142: 
     [1 5 6]
    Relevant topics for document #1143: 
     [0 2 4 7]
    Relevant topics for document #1144: 
     [4 5 8]
    Relevant topics for document #1145: 
     [0 6 7 8 9]
    Relevant topics for document #1146: 
     [0 4 7]
    Relevant topics for document #1147: 
     [1 5]
    Relevant topics for document #1148: 
     [0 3 5 6 7 8 9]
    Relevant topics for document #1149: 
     [2]
    Relevant topics for document #1150: 
     [0 4 7 9]
    Relevant topics for document #1151: 
     [0 5 7 9]
    Relevant topics for document #1152: 
     [3 4 6 7]
    Relevant topics for document #1153: 
     [0 3 4 6 7 8]
    Relevant topics for document #1154: 
     [0 2 7]
    Relevant topics for document #1155: 
     [4 5]
    Relevant topics for document #1156: 
     [2 3 7 8]
    Relevant topics for document #1157: 
     [0 3 5 6 7 9]
    Relevant topics for document #1158: 
     [0 7 8 9]
    Relevant topics for document #1159: 
     [0 5 6 9]
    Relevant topics for document #1160: 
     [0 1 2 5 9]
    Relevant topics for document #1161: 
     [4 7 8]
    Relevant topics for document #1162: 
     [0 1 2 5]
    Relevant topics for document #1163: 
     [0 2 7 8]
    Relevant topics for document #1164: 
     [1 5 7]
    Relevant topics for document #1165: 
     [0 5 6 9]
    Relevant topics for document #1166: 
     [0 1 6]
    Relevant topics for document #1167: 
     [0 3 4 7 8 9]
    Relevant topics for document #1168: 
     [0 7 9]
    Relevant topics for document #1169: 
     [4 8]
    Relevant topics for document #1170: 
     [0 4 7 9]
    Relevant topics for document #1171: 
     [5 7]
    Relevant topics for document #1172: 
     [0 3 4 5 6 7 9]
    Relevant topics for document #1173: 
     [0 4 6]
    Relevant topics for document #1174: 
     [2 7 8 9]
    Relevant topics for document #1175: 
     [5 7 9]
    Relevant topics for document #1176: 
     [0 3 5 6]
    Relevant topics for document #1177: 
     [0 3 4 7]
    Relevant topics for document #1178: 
     [0 3 6 9]
    Relevant topics for document #1179: 
     [0 7 9]
    Relevant topics for document #1180: 
     [4 5 7 8]
    Relevant topics for document #1181: 
     [0 3 7 9]
    Relevant topics for document #1182: 
     [0 3 4 5 6 8 9]
    Relevant topics for document #1183: 
     [0 3 7 8]
    Relevant topics for document #1184: 
     [1 5 6 7 8]
    Relevant topics for document #1185: 
     [0 2 3 4 7]
    Relevant topics for document #1186: 
     [0 3 5 7 8]
    Relevant topics for document #1187: 
     [0 2 7]
    Relevant topics for document #1188: 
     [6]
    Relevant topics for document #1189: 
     [5 7 9]
    Relevant topics for document #1190: 
     [0 5 6 7]
    Relevant topics for document #1191: 
     [0 2 3]
    Relevant topics for document #1192: 
     [2 7]
    Relevant topics for document #1193: 
     [5 6 7 8 9]
    Relevant topics for document #1194: 
     [0 1 4 5 7]
    Relevant topics for document #1195: 
     [5 7]
    Relevant topics for document #1196: 
     [0 1 8 9]
    Relevant topics for document #1197: 
     [0 2 4 7]
    Relevant topics for document #1198: 
     [3 4 6 7 8]
    Relevant topics for document #1199: 
     [4 5 6 8 9]
    Relevant topics for document #1200: 
     [5 7]
    Relevant topics for document #1201: 
     [8 9]
    Relevant topics for document #1202: 
     [5 7 9]
    Relevant topics for document #1203: 
     [0 1 4 8 9]
    Relevant topics for document #1204: 
     [0 2]
    Relevant topics for document #1205: 
     [0 1 5 9]
    Relevant topics for document #1206: 
     [0 1 5 6 7 9]
    Relevant topics for document #1207: 
     [5 6 7 9]
    Relevant topics for document #1208: 
     [4 5 8 9]
    Relevant topics for document #1209: 
     [0 2 3 5 7]
    Relevant topics for document #1210: 
     [0 1 4 5 9]
    Relevant topics for document #1211: 
     [0 5]
    Relevant topics for document #1212: 
     [0 3 5 7]
    Relevant topics for document #1213: 
     [0 3 9]
    Relevant topics for document #1214: 
     [0 6 7 8 9]
    Relevant topics for document #1215: 
     [0 2 3 4 7]
    Relevant topics for document #1216: 
     [5 8]
    Relevant topics for document #1217: 
     [7]
    Relevant topics for document #1218: 
     [0 3 4 6 8]
    Relevant topics for document #1219: 
     [4 8]
    Relevant topics for document #1220: 
     [1 5 6 7 8]
    Relevant topics for document #1221: 
     [0 3 4 7 8]
    Relevant topics for document #1222: 
     [3 5 6 9]
    Relevant topics for document #1223: 
     [0 1 5 8 9]
    Relevant topics for document #1224: 
     [3 6]
    Relevant topics for document #1225: 
     [0 2 3 7]
    Relevant topics for document #1226: 
     [5 7 8]
    Relevant topics for document #1227: 
     [4 5 9]
    Relevant topics for document #1228: 
     [3 5 9]
    Relevant topics for document #1229: 
     [0 2 3 5 6 8 9]
    Relevant topics for document #1230: 
     [0 4 5 7 8]
    Relevant topics for document #1231: 
     [0 1 5 7 9]
    Relevant topics for document #1232: 
     [0 6 8 9]
    Relevant topics for document #1233: 
     [0 5 7 8]
    Relevant topics for document #1234: 
     [0 5 7]
    Relevant topics for document #1235: 
     [0 3 5 6 7]
    Relevant topics for document #1236: 
     [0 5 7 8]
    Relevant topics for document #1237: 
     [0 5 6 7]
    Relevant topics for document #1238: 
     [0 1 8]
    Relevant topics for document #1239: 
     [3 7 8]
    Relevant topics for document #1240: 
     [4 5 8]
    Relevant topics for document #1241: 
     [0 1 3 5 6 7 9]
    Relevant topics for document #1242: 
     [0 2 3 6 9]
    Relevant topics for document #1243: 
     [0 2 5]
    Relevant topics for document #1244: 
     [0 7 8 9]
    Relevant topics for document #1245: 
     [0 7 8]
    Relevant topics for document #1246: 
     [0 3 5 7]
    Relevant topics for document #1247: 
     [0 7 8 9]
    Relevant topics for document #1248: 
     [0 3]
    Relevant topics for document #1249: 
     [0 3 4 7 9]
    Relevant topics for document #1250: 
     [0 7 8]
    Relevant topics for document #1251: 
     [0 4 5 7 8 9]
    Relevant topics for document #1252: 
     [1 5 6 7]
    Relevant topics for document #1253: 
     [0 1 5 7 9]
    Relevant topics for document #1254: 
     [7]
    Relevant topics for document #1255: 
     [0 5 7]
    Relevant topics for document #1256: 
     [0 1 3 5 6 7]
    Relevant topics for document #1257: 
     [0 1 9]
    Relevant topics for document #1258: 
     [4 7 8]
    Relevant topics for document #1259: 
     [0 1 2 7]
    Relevant topics for document #1260: 
     [0 1 5]
    Relevant topics for document #1261: 
     [5 8 9]
    Relevant topics for document #1262: 
     [0 3 4 5 6 7]
    Relevant topics for document #1263: 
     [0 1 5 6 8 9]
    Relevant topics for document #1264: 
     [0 3 9]
    Relevant topics for document #1265: 
     [0 3 7 9]
    Relevant topics for document #1266: 
     [0 5 8]
    Relevant topics for document #1267: 
     [3 4 6]
    Relevant topics for document #1268: 
     [1 3 5 9]
    Relevant topics for document #1269: 
     [0 7]
    Relevant topics for document #1270: 
     [0 2 4 8]
    Relevant topics for document #1271: 
     [0 1 5 6 7 9]
    Relevant topics for document #1272: 
     [0 7 8 9]
    Relevant topics for document #1273: 
     [2 7 8]
    Relevant topics for document #1274: 
     [0 1 2 5 8]
    Relevant topics for document #1275: 
     [2 3 7 9]
    Relevant topics for document #1276: 
     [5 6 7 8 9]
    Relevant topics for document #1277: 
     [1 2 9]
    Relevant topics for document #1278: 
     [0 2 4]
    Relevant topics for document #1279: 
     [0 2 5 8]
    Relevant topics for document #1280: 
     [0 5 8 9]
    Relevant topics for document #1281: 
     [0 5 7 8]
    Relevant topics for document #1282: 
     [0 3 4 6]
    Relevant topics for document #1283: 
     [4 5 6]
    Relevant topics for document #1284: 
     [0 7 8]
    Relevant topics for document #1285: 
     [0 1 5]
    Relevant topics for document #1286: 
     [0 4 5 6 7 9]
    Relevant topics for document #1287: 
     [0 1 5 6 7 9]
    Relevant topics for document #1288: 
     [3 6 7]
    Relevant topics for document #1289: 
     [0 2 3 4 8 9]
    Relevant topics for document #1290: 
     [5 6]
    Relevant topics for document #1291: 
     [0 4 7]
    Relevant topics for document #1292: 
     [0 5]
    Relevant topics for document #1293: 
     [0 3 4]
    Relevant topics for document #1294: 
     [0 4]
    Relevant topics for document #1295: 
     [0 5 7 8]
    Relevant topics for document #1296: 
     [3 5]
    Relevant topics for document #1297: 
     [0 8]
    Relevant topics for document #1298: 
     [0 5 7]
    Relevant topics for document #1299: 
     [0 7]
    Relevant topics for document #1300: 
     [0 1 4 9]
    Relevant topics for document #1301: 
     [1 4 5 6 8]
    Relevant topics for document #1302: 
     [0 2 3 6 7]
    Relevant topics for document #1303: 
     [0 1 4 5 7 9]
    Relevant topics for document #1304: 
     [0 1 2 4]
    Relevant topics for document #1305: 
     [0 8 9]
    Relevant topics for document #1306: 
     [5 6 7 9]
    Relevant topics for document #1307: 
     [0 3 7 9]
    Relevant topics for document #1308: 
     [0 1 9]
    Relevant topics for document #1309: 
     [0 4 5 6 7 8]
    Relevant topics for document #1310: 
     [0 1 4 5 7]
    Relevant topics for document #1311: 
     [4 6 7]
    Relevant topics for document #1312: 
     [0 1 2 7 9]
    Relevant topics for document #1313: 
     [0 1 5 9]
    Relevant topics for document #1314: 
     [0 8 9]
    Relevant topics for document #1315: 
     [0 5 6 7 9]
    Relevant topics for document #1316: 
     [0 1 8 9]
    Relevant topics for document #1317: 
     [5 7 8]
    Relevant topics for document #1318: 
     [0 2 7 8 9]
    Relevant topics for document #1319: 
     [0 1 2 5 8 9]
    Relevant topics for document #1320: 
     [4 5 8]
    Relevant topics for document #1321: 
     [1 5]
    Relevant topics for document #1322: 
     [0 4 6 7 9]
    Relevant topics for document #1323: 
     [0 7 8]
    Relevant topics for document #1324: 
     [6 7]
    Relevant topics for document #1325: 
     [0 1 5 8]
    Relevant topics for document #1326: 
     [0 1 9]
    Relevant topics for document #1327: 
     [4 7 8]
    Relevant topics for document #1328: 
     [3 4 5 7]
    Relevant topics for document #1329: 
     [0 1 3 4 5 8]
    Relevant topics for document #1330: 
     [0 2 9]
    Relevant topics for document #1331: 
     [3 6]
    Relevant topics for document #1332: 
     [0 3 5 7 9]
    Relevant topics for document #1333: 
     [0 5 7]
    Relevant topics for document #1334: 
     [5 7 9]
    Relevant topics for document #1335: 
     [3 4 7]
    Relevant topics for document #1336: 
     [0 5 7 9]
    Relevant topics for document #1337: 
     [2]
    Relevant topics for document #1338: 
     [0 3 4 7 9]
    Relevant topics for document #1339: 
     [2 4 5]
    Relevant topics for document #1340: 
     [0 2 5 7 8]
    Relevant topics for document #1341: 
     [1 4 5]
    Relevant topics for document #1342: 
     [0 2 4]
    Relevant topics for document #1343: 
     [4 5 8 9]
    Relevant topics for document #1344: 
     [0 1 9]
    Relevant topics for document #1345: 
     [0 9]
    Relevant topics for document #1346: 
     [5 6 7 9]
    Relevant topics for document #1347: 
     [3 6 7 9]
    Relevant topics for document #1348: 
     [0 4 6 7]
    Relevant topics for document #1349: 
     [0 3 5 7 9]
    Relevant topics for document #1350: 
     [2 4 6 7 8 9]
    Relevant topics for document #1351: 
     [5 7 8]
    Relevant topics for document #1352: 
     [4 5 7 8]
    Relevant topics for document #1353: 
     [0 4 5]
    Relevant topics for document #1354: 
     [3 5 6 7 9]
    Relevant topics for document #1355: 
     [0 2 4]
    Relevant topics for document #1356: 
     [6 7 8]
    Relevant topics for document #1357: 
     [4 8]
    Relevant topics for document #1358: 
     [0 4 8 9]
    Relevant topics for document #1359: 
     [3 5 7 9]
    Relevant topics for document #1360: 
     [0 2 3 4 8]
    Relevant topics for document #1361: 
     [2 4 7 8]
    Relevant topics for document #1362: 
     [0 5]
    Relevant topics for document #1363: 
     [4 6 7 8]
    Relevant topics for document #1364: 
     [0 3 7 9]
    Relevant topics for document #1365: 
     [1 7 9]
    Relevant topics for document #1366: 
     [0 2 3 7 9]
    Relevant topics for document #1367: 
     [0 5 7 8 9]
    Relevant topics for document #1368: 
     [0 5 6 7 9]
    Relevant topics for document #1369: 
     [0 1 4 5 7 9]
    Relevant topics for document #1370: 
     [0 1 4 5 6 9]
    Relevant topics for document #1371: 
     [3 5 6]
    Relevant topics for document #1372: 
     [0 8]
    Relevant topics for document #1373: 
     [3 6]
    Relevant topics for document #1374: 
     [0 2]
    Relevant topics for document #1375: 
     [0 7]
    Relevant topics for document #1376: 
     [1 4 5 7 8 9]
    Relevant topics for document #1377: 
     [2 5 7 9]
    Relevant topics for document #1378: 
     [0 7 8]
    Relevant topics for document #1379: 
     [0 7]
    Relevant topics for document #1380: 
     [0 5 6 7 8]
    Relevant topics for document #1381: 
     [4 5 6 8]
    Relevant topics for document #1382: 
     [0 4 5 8]
    Relevant topics for document #1383: 
     [0 7]
    Relevant topics for document #1384: 
     [0 9]
    Relevant topics for document #1385: 
     [5 9]
    Relevant topics for document #1386: 
     [0 1 4 8]
    Relevant topics for document #1387: 
     [2 7 9]
    Relevant topics for document #1388: 
     [0 7 9]
    Relevant topics for document #1389: 
     [0 9]
    Relevant topics for document #1390: 
     [0 1 8 9]
    Relevant topics for document #1391: 
     [5 7 9]
    Relevant topics for document #1392: 
     [3 7 8 9]
    Relevant topics for document #1393: 
     [5 9]
    Relevant topics for document #1394: 
     [0 2 3 5 9]
    Relevant topics for document #1395: 
     [2 5 7]
    Relevant topics for document #1396: 
     [0 2 5 6 8]
    Relevant topics for document #1397: 
     [0 2 4 7 8 9]
    Relevant topics for document #1398: 
     [0 2 7]
    Relevant topics for document #1399: 
     [0 5 6 9]
    Relevant topics for document #1400: 
     [0 8]
    Relevant topics for document #1401: 
     [0 5 6 9]
    Relevant topics for document #1402: 
     [5 7 8]
    Relevant topics for document #1403: 
     [0 2 6]
    Relevant topics for document #1404: 
     [0 2 7 8]
    Relevant topics for document #1405: 
     [1]
    Relevant topics for document #1406: 
     [0 4 5 6]
    Relevant topics for document #1407: 
     [0 5 9]
    Relevant topics for document #1408: 
     [0 1 3 9]
    Relevant topics for document #1409: 
     [4 5 8 9]
    Relevant topics for document #1410: 
     [0 1 2 5 9]
    Relevant topics for document #1411: 
     [0 2 3 4 7 9]
    Relevant topics for document #1412: 
     [0 2 4 7 8]
    Relevant topics for document #1413: 
     [0 5 7 9]
    Relevant topics for document #1414: 
     [3 4 7 8]
    Relevant topics for document #1415: 
     [0 5]
    Relevant topics for document #1416: 
     [5 7]
    Relevant topics for document #1417: 
     [0 1 5 7 8]
    Relevant topics for document #1418: 
     [3 4 5 7]
    Relevant topics for document #1419: 
     [5 7 8]
    Relevant topics for document #1420: 
     [0 5 9]
    Relevant topics for document #1421: 
     [0 4 5 6 8 9]
    Relevant topics for document #1422: 
     [0 4]
    Relevant topics for document #1423: 
     [0 2 5]
    Relevant topics for document #1424: 
     [0 1 4 5 6]
    Relevant topics for document #1425: 
     [0 2 6 7 8]
    Relevant topics for document #1426: 
     [0 3 4 6 7]
    Relevant topics for document #1427: 
     [0 3 5 7 9]
    Relevant topics for document #1428: 
     [5]
    Relevant topics for document #1429: 
     [5 6 7 9]
    Relevant topics for document #1430: 
     [7 8]
    Relevant topics for document #1431: 
     [2]
    Relevant topics for document #1432: 
     [4 5]
    Relevant topics for document #1433: 
     [4 5 8]
    Relevant topics for document #1434: 
     [6 7]
    Relevant topics for document #1435: 
     [0 2 3 7 9]
    Relevant topics for document #1436: 
     [0 2 3 4 7]
    Relevant topics for document #1437: 
     [0 4 7]
    Relevant topics for document #1438: 
     [0 4 5 8 9]
    Relevant topics for document #1439: 
     [4 5 6 7 8 9]
    Relevant topics for document #1440: 
     [0 2 8]
    Relevant topics for document #1441: 
     [0 2 3 4 7]
    Relevant topics for document #1442: 
     [0 2 4 7 8]
    Relevant topics for document #1443: 
     [0 2 3 9]
    Relevant topics for document #1444: 
     [0 2 5 7 8]
    Relevant topics for document #1445: 
     [0 4 8 9]
    Relevant topics for document #1446: 
     [1 4 6 7 8]
    Relevant topics for document #1447: 
     [0 5 6 8 9]
    Relevant topics for document #1448: 
     [0 1 2 4 8]
    Relevant topics for document #1449: 
     [6 7 9]
    Relevant topics for document #1450: 
     [0 2 7]
    Relevant topics for document #1451: 
     [0 5 7]
    Relevant topics for document #1452: 
     [0 1 4 7]
    Relevant topics for document #1453: 
     [0 1 5 8 9]
    Relevant topics for document #1454: 
     [0 5 6]
    Relevant topics for document #1455: 
     [0 1 5 6 9]
    Relevant topics for document #1456: 
     [2 5 8 9]
    Relevant topics for document #1457: 
     [0 3]
    Relevant topics for document #1458: 
     [0 1 5 6 8]
    Relevant topics for document #1459: 
     [0 1 4 7 9]
    Relevant topics for document #1460: 
     [0 3 5 6 9]
    Relevant topics for document #1461: 
     [5]
    Relevant topics for document #1462: 
     [0 4 8]
    Relevant topics for document #1463: 
     [4 5 8]
    Relevant topics for document #1464: 
     [0 7 8]
    Relevant topics for document #1465: 
     [0 5 7 9]
    Relevant topics for document #1466: 
     [0 4 5 6 9]
    Relevant topics for document #1467: 
     [0 2 3 7]
    Relevant topics for document #1468: 
     [5 7]
    Relevant topics for document #1469: 
     [0 4 5 6 8 9]
    Relevant topics for document #1470: 
     [3 4 6 8]
    Relevant topics for document #1471: 
     [5 8]
    Relevant topics for document #1472: 
     [0 3 6 7 9]
    Relevant topics for document #1473: 
     [0 3 4 7 9]
    Relevant topics for document #1474: 
     [0 5 7]
    Relevant topics for document #1475: 
     [0 3 4 5 8 9]
    Relevant topics for document #1476: 
     [0 3]
    Relevant topics for document #1477: 
     [0 4]
    Relevant topics for document #1478: 
     [0 5 6 9]
    Relevant topics for document #1479: 
     [0 1 7]
    Relevant topics for document #1480: 
     [0 2 3 4 7 8]
    Relevant topics for document #1481: 
     [4 5 6]
    Relevant topics for document #1482: 
     [5 7]
    Relevant topics for document #1483: 
     [0 5 7 9]
    Relevant topics for document #1484: 
     [5 8]
    Relevant topics for document #1485: 
     [0 5]
    Relevant topics for document #1486: 
     [0 1 5 6 8 9]
    Relevant topics for document #1487: 
     [0 1 7 8]
    Relevant topics for document #1488: 
     [5 8 9]
    Relevant topics for document #1489: 
     [0 6 8 9]
    Relevant topics for document #1490: 
     [4 5 8 9]
    Relevant topics for document #1491: 
     [5 7]
    Relevant topics for document #1492: 
     [1 4 5 8 9]
    Relevant topics for document #1493: 
     [5 9]
    Relevant topics for document #1494: 
     [0 1 7 9]
    Relevant topics for document #1495: 
     [4 7]
    Relevant topics for document #1496: 
     [4 8]
    Relevant topics for document #1497: 
     [5 7]
    Relevant topics for document #1498: 
     [4 5 6 7]
    Relevant topics for document #1499: 
     [0 2 3 4 7]
    Relevant topics for document #1500: 
     [0 1 4 5 6]
    Relevant topics for document #1501: 
     [0 4 7 8 9]
    Relevant topics for document #1502: 
     [1 5 6 7 8]
    Relevant topics for document #1503: 
     [0 4 5 8]
    Relevant topics for document #1504: 
     [0 3 5 8]
    Relevant topics for document #1505: 
     [5 7]
    Relevant topics for document #1506: 
     [4 7 9]
    Relevant topics for document #1507: 
     [5]
    Relevant topics for document #1508: 
     [0 3 8]
    Relevant topics for document #1509: 
     [1 5 8 9]
    Relevant topics for document #1510: 
     [5 6 7 9]
    Relevant topics for document #1511: 
     [0 2 3 7 9]
    Relevant topics for document #1512: 
     [0 4 7 8]
    Relevant topics for document #1513: 
     [4 5 7 8]
    Relevant topics for document #1514: 
     [0 3 4 5 7 9]
    Relevant topics for document #1515: 
     [4 5 7 8]
    Relevant topics for document #1516: 
     [0 3 7]
    Relevant topics for document #1517: 
     [1 5 6 9]
    Relevant topics for document #1518: 
     [3]
    Relevant topics for document #1519: 
     [0 5 9]
    Relevant topics for document #1520: 
     [5 7 9]
    Relevant topics for document #1521: 
     [3 6 7]
    Relevant topics for document #1522: 
     [0 5]
    Relevant topics for document #1523: 
     [0 4 7 8]
    Relevant topics for document #1524: 
     [5 8 9]
    Relevant topics for document #1525: 
     [0 1 4 5]
    Relevant topics for document #1526: 
     [0 1 4 8 9]
    Relevant topics for document #1527: 
     [4 8]
    Relevant topics for document #1528: 
     [0 3 4 6 9]
    Relevant topics for document #1529: 
     [0 4 5]
    Relevant topics for document #1530: 
     [5 8]
    Relevant topics for document #1531: 
     [5 6 7]
    Relevant topics for document #1532: 
     [0 3 6 9]
    Relevant topics for document #1533: 
     [0 5 7 8]
    Relevant topics for document #1534: 
     [0 3 5 7 9]
    Relevant topics for document #1535: 
     [0 4]
    Relevant topics for document #1536: 
     [5 8]
    Relevant topics for document #1537: 
     [0 1 8 9]
    Relevant topics for document #1538: 
     [0 9]
    Relevant topics for document #1539: 
     [5 6 7]
    Relevant topics for document #1540: 
     [3 4 6 9]
    Relevant topics for document #1541: 
     [4 7 8]
    Relevant topics for document #1542: 
     [2 8]
    Relevant topics for document #1543: 
     [1 4 5 7 8 9]
    Relevant topics for document #1544: 
     [0 3 4 5 6 7]
    Relevant topics for document #1545: 
     [0 1 7]
    Relevant topics for document #1546: 
     [0 3 4 7 8]
    Relevant topics for document #1547: 
     [0 2 3 7 8]
    Relevant topics for document #1548: 
     [0 1 2 3 5]
    Relevant topics for document #1549: 
     [1 6]
    Relevant topics for document #1550: 
     [0 5 7 8]
    Relevant topics for document #1551: 
     [0 2 6]
    Relevant topics for document #1552: 
     [7 9]
    Relevant topics for document #1553: 
     [5 6 7 8]
    Relevant topics for document #1554: 
     [0 1 7 9]
    Relevant topics for document #1555: 
     [3 4 5 7 8]
    Relevant topics for document #1556: 
     [0 2 4 5 7 8 9]
    Relevant topics for document #1557: 
     [1 7 9]
    Relevant topics for document #1558: 
     [4 5 7 8]
    Relevant topics for document #1559: 
     [5 8]
    Relevant topics for document #1560: 
     [3 4 5 7]
    Relevant topics for document #1561: 
     [0 2 3 4 7 8]
    Relevant topics for document #1562: 
     [0 1 5 9]
    Relevant topics for document #1563: 
     [4 5 7 8]
    Relevant topics for document #1564: 
     [4 5 7]
    Relevant topics for document #1565: 
     [0 2 7]
    Relevant topics for document #1566: 
     [0 5 7]
    Relevant topics for document #1567: 
     [3 4 6 7 8]
    Relevant topics for document #1568: 
     [1 5 7]
    Relevant topics for document #1569: 
     [0 1 3 4 5 6]
    Relevant topics for document #1570: 
     [0 1 9]
    Relevant topics for document #1571: 
     [3 6]
    Relevant topics for document #1572: 
     [5 7 8]
    Relevant topics for document #1573: 
     [5]
    Relevant topics for document #1574: 
     [4 7]
    Relevant topics for document #1575: 
     [5 7 8]
    Relevant topics for document #1576: 
     [1 3 7]
    Relevant topics for document #1577: 
     [5 7]
    Relevant topics for document #1578: 
     [2 5 7]
    Relevant topics for document #1579: 
     [2 6 7]
    Relevant topics for document #1580: 
     [0 4 6 7 8 9]
    Relevant topics for document #1581: 
     [0 3 7 9]
    Relevant topics for document #1582: 
     [1 5 9]
    Relevant topics for document #1583: 
     [5 7 8]
    Relevant topics for document #1584: 
     [1 3 4 6]
    Relevant topics for document #1585: 
     [0 3 5 6 9]
    Relevant topics for document #1586: 
     [0 5 7]
    Relevant topics for document #1587: 
     [0 2 4 7 8]
    Relevant topics for document #1588: 
     [5 7]
    Relevant topics for document #1589: 
     [0 5 7]
    Relevant topics for document #1590: 
     [0 2 5 7]
    Relevant topics for document #1591: 
     [0 1 9]
    Relevant topics for document #1592: 
     [0 4 7 8 9]
    Relevant topics for document #1593: 
     [0 3 4 6]
    Relevant topics for document #1594: 
     [0 3 5 7]
    Relevant topics for document #1595: 
     [0 2 3 4 6 7 8]
    Relevant topics for document #1596: 
     [0 1 8 9]
    Relevant topics for document #1597: 
     [0 2]
    Relevant topics for document #1598: 
     [0 4 7]
    Relevant topics for document #1599: 
     [1 5 7]
    Relevant topics for document #1600: 
     [0 5]
    Relevant topics for document #1601: 
     [8]
    Relevant topics for document #1602: 
     [0 7 9]
    Relevant topics for document #1603: 
     [0 2 4 6 7]
    Relevant topics for document #1604: 
     [0 1 5 6 7 9]
    Relevant topics for document #1605: 
     [0 3 5]
    Relevant topics for document #1606: 
     [0 5 8]
    Relevant topics for document #1607: 
     [0 1 9]
    Relevant topics for document #1608: 
     [0 1 6 9]
    Relevant topics for document #1609: 
     [4 7]
    Relevant topics for document #1610: 
     [0 7 8]
    Relevant topics for document #1611: 
     [0 1 4 5]
    Relevant topics for document #1612: 
     [4 5 7]
    Relevant topics for document #1613: 
     [3 4 6 7 9]
    Relevant topics for document #1614: 
     [2 3 7 8]
    Relevant topics for document #1615: 
     [0]
    Relevant topics for document #1616: 
     [3 5 6 7 9]
    Relevant topics for document #1617: 
     [0 1 3 4 6 7]
    Relevant topics for document #1618: 
     [3 5 6 7 9]
    Relevant topics for document #1619: 
     [4 5 7]
    Relevant topics for document #1620: 
     [0 1 2 3]
    Relevant topics for document #1621: 
     [0 1 5 9]
    Relevant topics for document #1622: 
     [0 2 7]
    Relevant topics for document #1623: 
     [5 7]
    Relevant topics for document #1624: 
     [7]
    Relevant topics for document #1625: 
     [0 2]
    Relevant topics for document #1626: 
     [0 5]
    Relevant topics for document #1627: 
     [3 4 6 7]
    Relevant topics for document #1628: 
     [0]
    Relevant topics for document #1629: 
     [0 1 3 4 6 7 9]
    Relevant topics for document #1630: 
     [0 2 7]
    Relevant topics for document #1631: 
     [0 1 5 9]
    Relevant topics for document #1632: 
     [4 5]
    Relevant topics for document #1633: 
     [0 1 5 9]
    Relevant topics for document #1634: 
     [0 4 7]
    Relevant topics for document #1635: 
     [0 1 5]
    Relevant topics for document #1636: 
     [0 1 3 5]
    Relevant topics for document #1637: 
     [0 1 4 9]
    Relevant topics for document #1638: 
     [0 2 5 8 9]
    Relevant topics for document #1639: 
     [5 6 7 8 9]
    Relevant topics for document #1640: 
     [0 1 2 4 8 9]
    Relevant topics for document #1641: 
     [0 3 4 7]
    Relevant topics for document #1642: 
     [0 2 5 7 9]
    Relevant topics for document #1643: 
     [0 1 2 4]
    Relevant topics for document #1644: 
     [0 3 4 6 7 8]
    Relevant topics for document #1645: 
     [0 1 5]
    Relevant topics for document #1646: 
     [0 7 9]
    Relevant topics for document #1647: 
     [0 5 7]
    Relevant topics for document #1648: 
     [0 4 5]
    Relevant topics for document #1649: 
     [0 2 3 4 6 7 9]
    Relevant topics for document #1650: 
     [0 2 4 6 7 9]
    Relevant topics for document #1651: 
     [0 5]
    Relevant topics for document #1652: 
     [0 7]
    Relevant topics for document #1653: 
     [0 5 8]
    Relevant topics for document #1654: 
     [0 9]
    Relevant topics for document #1655: 
     [0 4 9]
    Relevant topics for document #1656: 
     [0 1 6 9]
    Relevant topics for document #1657: 
     [0 7 9]
    Relevant topics for document #1658: 
     [1 3 4 7]
    Relevant topics for document #1659: 
     [2 7]
    Relevant topics for document #1660: 
     [0 2]
    Relevant topics for document #1661: 
     [2 3 7]
    Relevant topics for document #1662: 
     [0 1 3 4]
    Relevant topics for document #1663: 
     [0 4 5]
    Relevant topics for document #1664: 
     [0 1 3 5]
    Relevant topics for document #1665: 
     [0 1 5 9]
    Relevant topics for document #1666: 
     [5 6 7 9]
    Relevant topics for document #1667: 
     [0 2 3 5 7 9]
    Relevant topics for document #1668: 
     [0 3 5 7 9]
    Relevant topics for document #1669: 
     [0 1 5 9]
    Relevant topics for document #1670: 
     [0 3 7]
    Relevant topics for document #1671: 
     [0 3 4 7]
    Relevant topics for document #1672: 
     [0 2 3 6 7]
    Relevant topics for document #1673: 
     [0 4 7 8]
    Relevant topics for document #1674: 
     [3 4 6 7 8 9]
    Relevant topics for document #1675: 
     [0 2 7]
    Relevant topics for document #1676: 
     [5 7 9]
    Relevant topics for document #1677: 
     [7 8]
    Relevant topics for document #1678: 
     [0 5 7]
    Relevant topics for document #1679: 
     [6 7]
    Relevant topics for document #1680: 
     [0 2 3 8]
    Relevant topics for document #1681: 
     [0 1 6 7]
    Relevant topics for document #1682: 
     [5 8 9]
    Relevant topics for document #1683: 
     [0 1 3 4 5 6 7 8 9]
    Relevant topics for document #1684: 
     [0 5 7 8]
    Relevant topics for document #1685: 
     [0 9]
    Relevant topics for document #1686: 
     [5 7]
    Relevant topics for document #1687: 
     [4 8]
    Relevant topics for document #1688: 
     [0 1 9]
    Relevant topics for document #1689: 
     [0 3 4 6]
    Relevant topics for document #1690: 
     [0 3 4 5]
    Relevant topics for document #1691: 
     [4 5 6 7 9]
    Relevant topics for document #1692: 
     [0 5 7]
    Relevant topics for document #1693: 
     [0 1 5]
    Relevant topics for document #1694: 
     [0 1 5 7]
    Relevant topics for document #1695: 
     [0]
    Relevant topics for document #1696: 
     [0 4 7]
    Relevant topics for document #1697: 
     [0 1 3 4 9]
    Relevant topics for document #1698: 
     [4 5 7 8]
    Relevant topics for document #1699: 
     [0 1 9]
    Relevant topics for document #1700: 
     [0 1 9]
    Relevant topics for document #1701: 
     [4 8]
    Relevant topics for document #1702: 
     [0 1 9]
    Relevant topics for document #1703: 
     [4 5 6 8 9]
    Relevant topics for document #1704: 
     [4 7]
    Relevant topics for document #1705: 
     [0 8 9]
    Relevant topics for document #1706: 
     [0 4 5 7 8]
    Relevant topics for document #1707: 
     [2 4]
    Relevant topics for document #1708: 
     [4 5 8]
    Relevant topics for document #1709: 
     [7]
    Relevant topics for document #1710: 
     [0 1 4 8]
    Relevant topics for document #1711: 
     [0 6 9]
    Relevant topics for document #1712: 
     [5 8]
    Relevant topics for document #1713: 
     [4 5 6 8 9]
    Relevant topics for document #1714: 
     [1 5 7]
    Relevant topics for document #1715: 
     [5 6 8 9]
    Relevant topics for document #1716: 
     [3]
    Relevant topics for document #1717: 
     [0 2 9]
    Relevant topics for document #1718: 
     [5 7]
    Relevant topics for document #1719: 
     [0 1 2 3 5 6 7 9]
    Relevant topics for document #1720: 
     [0 5 7 8]
    Relevant topics for document #1721: 
     [5 9]
    Relevant topics for document #1722: 
     [0 3 5 7]
    Relevant topics for document #1723: 
     [3 6]
    Relevant topics for document #1724: 
     [1 5 6 9]
    Relevant topics for document #1725: 
     [6 7]
    Relevant topics for document #1726: 
     [0 1 5 8 9]
    Relevant topics for document #1727: 
     [0 3 6]
    Relevant topics for document #1728: 
     [0 1 7]
    Relevant topics for document #1729: 
     [1 5]
    Relevant topics for document #1730: 
     [1 5 7 9]
    Relevant topics for document #1731: 
     [0 3 4 7 9]
    Relevant topics for document #1732: 
     [0 3 4 6 8 9]
    Relevant topics for document #1733: 
     [0 1 5]
    Relevant topics for document #1734: 
     [0 4 7]
    Relevant topics for document #1735: 
     [0 3 4 6]
    Relevant topics for document #1736: 
     [0 6]
    Relevant topics for document #1737: 
     [0 5 7]
    Relevant topics for document #1738: 
     [5 8]
    Relevant topics for document #1739: 
     [4 5 6]
    Relevant topics for document #1740: 
     [0 5 8 9]
    Relevant topics for document #1741: 
     [4 5 8 9]
    Relevant topics for document #1742: 
     [0 1 8 9]
    Relevant topics for document #1743: 
     [4 5 6 9]
    Relevant topics for document #1744: 
     [5 7]
    Relevant topics for document #1745: 
     [1 5 6 9]
    Relevant topics for document #1746: 
     [0 1 5 6 9]
    Relevant topics for document #1747: 
     [0 5 7]
    Relevant topics for document #1748: 
     [4 5 7]
    Relevant topics for document #1749: 
     [0 4 6 7 9]
    Relevant topics for document #1750: 
     [0 3 4 6 7 8]
    Relevant topics for document #1751: 
     [0 1 3 4 6 9]
    Relevant topics for document #1752: 
     [0 4 5 6]
    Relevant topics for document #1753: 
     [0 3 4 6 7]
    Relevant topics for document #1754: 
     [0 2 4 7 8 9]
    Relevant topics for document #1755: 
     [0 1 5 7 8]
    Relevant topics for document #1756: 
     [0 4]
    Relevant topics for document #1757: 
     [1 5 7]
    Relevant topics for document #1758: 
     [1 3 4 6 9]
    Relevant topics for document #1759: 
     [2]
    Relevant topics for document #1760: 
     [0 1 4 5]
    Relevant topics for document #1761: 
     [0 1 4 8]
    Relevant topics for document #1762: 
     [0 2 4 7 9]
    Relevant topics for document #1763: 
     [5 7 8]
    Relevant topics for document #1764: 
     [2 5 7 8]
    Relevant topics for document #1765: 
     [0 1]
    Relevant topics for document #1766: 
     [3 6 7 9]
    Relevant topics for document #1767: 
     [3 7 9]
    Relevant topics for document #1768: 
     [0 1 5 7 8]
    Relevant topics for document #1769: 
     [0 5 8]
    Relevant topics for document #1770: 
     [0 3]
    Relevant topics for document #1771: 
     [0 2 3 4 7]
    Relevant topics for document #1772: 
     [4 5]
    Relevant topics for document #1773: 
     [0 7 8]
    Relevant topics for document #1774: 
     [0 2 5 8 9]
    Relevant topics for document #1775: 
     [0 1 4 6 7 9]
    Relevant topics for document #1776: 
     [4 5]
    Relevant topics for document #1777: 
     [4 5 6 7 8]
    Relevant topics for document #1778: 
     [0 1 4 5]
    Relevant topics for document #1779: 
     [1 5 8]
    Relevant topics for document #1780: 
     [0 9]
    Relevant topics for document #1781: 
     [0 3 4 5 6 9]
    Relevant topics for document #1782: 
     [0 4 6 7 8 9]
    Relevant topics for document #1783: 
     [1 4 5 8 9]
    Relevant topics for document #1784: 
     [0 5 8]
    Relevant topics for document #1785: 
     [0 3 7]
    Relevant topics for document #1786: 
     [1 5 8]
    Relevant topics for document #1787: 
     [0 1 9]
    Relevant topics for document #1788: 
     [0 1 5 8 9]
    Relevant topics for document #1789: 
     [0 5 7]
    Relevant topics for document #1790: 
     [5 6 9]
    Relevant topics for document #1791: 
     [1 2 3 7]
    Relevant topics for document #1792: 
     [3 5 7 8]
    Relevant topics for document #1793: 
     [0 7]
    Relevant topics for document #1794: 
     [3 4 6]
    Relevant topics for document #1795: 
     [0 5 7 8 9]
    Relevant topics for document #1796: 
     [0 6 7 8]
    Relevant topics for document #1797: 
     [0 1 3 4 5 7]
    Relevant topics for document #1798: 
     [0 6 9]
    Relevant topics for document #1799: 
     [3 5 6 9]
    Relevant topics for document #1800: 
     [1 5 7 9]
    Relevant topics for document #1801: 
     [0 4 7 8 9]
    Relevant topics for document #1802: 
     [0 4 5 8 9]
    Relevant topics for document #1803: 
     [1 3 4 6 7 8 9]
    Relevant topics for document #1804: 
     [0 1 2 5 7 8 9]
    Relevant topics for document #1805: 
     [1 5 6 8 9]
    Relevant topics for document #1806: 
     [7 8]
    Relevant topics for document #1807: 
     [0 7]
    Relevant topics for document #1808: 
     [5 6 7 8 9]
    Relevant topics for document #1809: 
     [0 4 5 6 7]
    Relevant topics for document #1810: 
     [0 4 7 9]
    Relevant topics for document #1811: 
     [5 7]
    Relevant topics for document #1812: 
     [0 1 5 6]
    Relevant topics for document #1813: 
     [5]
    Relevant topics for document #1814: 
     [7 8]
    Relevant topics for document #1815: 
     [0 1 2 5 6 8 9]
    Relevant topics for document #1816: 
     [2 7]
    Relevant topics for document #1817: 
     [0 1 5 7 8]
    Relevant topics for document #1818: 
     [0 1 2 3 5 9]
    Relevant topics for document #1819: 
     [1 3 6 7]
    Relevant topics for document #1820: 
     [0 3 4 7]
    Relevant topics for document #1821: 
     [4 6 7 8]
    Relevant topics for document #1822: 
     [0 1 5 7]
    Relevant topics for document #1823: 
     [3 7 9]
    Relevant topics for document #1824: 
     [0 1 5 9]
    Relevant topics for document #1825: 
     [0 1 6 9]
    Relevant topics for document #1826: 
     [0 2 8]
    Relevant topics for document #1827: 
     [0 1 5 7 9]
    Relevant topics for document #1828: 
     [0 6 8]
    Relevant topics for document #1829: 
     [0 2 3 7]
    Relevant topics for document #1830: 
     [0 5]
    Relevant topics for document #1831: 
     [0 1 2 5]
    Relevant topics for document #1832: 
     [4 5 6 7 9]
    Relevant topics for document #1833: 
     [0 5 7]
    Relevant topics for document #1834: 
     [0 4 7 9]
    Relevant topics for document #1835: 
     [1 5 7 9]
    Relevant topics for document #1836: 
     [4 7]
    Relevant topics for document #1837: 
     [0 1 4 5 9]
    Relevant topics for document #1838: 
     [0 1 4 5 9]
    Relevant topics for document #1839: 
     [4 8 9]
    Relevant topics for document #1840: 
     [0 5]
    Relevant topics for document #1841: 
     [4]
    Relevant topics for document #1842: 
     [0 1 5 9]
    Relevant topics for document #1843: 
     [1 4 7]
    Relevant topics for document #1844: 
     [0 2 7 8]
    Relevant topics for document #1845: 
     [0 1 4 9]
    Relevant topics for document #1846: 
     [0 4 7 8]
    Relevant topics for document #1847: 
     [3 4 5 7]
    Relevant topics for document #1848: 
     [3]
    Relevant topics for document #1849: 
     [0 1 2 3 4 7]
    Relevant topics for document #1850: 
     [0 1 5 8 9]
    Relevant topics for document #1851: 
     [3 4 5 6 7 9]
    Relevant topics for document #1852: 
     [0 2 3 4 7]
    Relevant topics for document #1853: 
     [4 6 7]
    Relevant topics for document #1854: 
     [0 1 2 4 8]
    Relevant topics for document #1855: 
     [0 2 3 4 6 7]
    Relevant topics for document #1856: 
     [0 1 4 8 9]
    Relevant topics for document #1857: 
     [0 2 8]
    Relevant topics for document #1858: 
     [0 1 2]
    Relevant topics for document #1859: 
     [0 1 5 6 7]
    Relevant topics for document #1860: 
     [0 6 7 9]
    Relevant topics for document #1861: 
     [0 5]
    Relevant topics for document #1862: 
     [0 1 5 6]
    Relevant topics for document #1863: 
     [0 2 4]
    Relevant topics for document #1864: 
     [0 1 2 5 8 9]
    Relevant topics for document #1865: 
     [0 1 5 7 8 9]
    Relevant topics for document #1866: 
     [4 7]
    Relevant topics for document #1867: 
     [0 4 9]
    Relevant topics for document #1868: 
     [5 7]
    Relevant topics for document #1869: 
     [1 2 3 6 7 9]
    Relevant topics for document #1870: 
     [0 2 3 4 7 8 9]
    Relevant topics for document #1871: 
     [0 1 5 7]
    Relevant topics for document #1872: 
     [0 5 7 9]
    Relevant topics for document #1873: 
     [0 7 9]
    Relevant topics for document #1874: 
     [0 1 7 9]
    Relevant topics for document #1875: 
     [0 3 4 7]
    Relevant topics for document #1876: 
     [0 1 6 9]
    Relevant topics for document #1877: 
     [0 1 3 7]
    Relevant topics for document #1878: 
     [0 1 2 5 7 9]
    Relevant topics for document #1879: 
     [0 2 3 5 6 7 9]
    Relevant topics for document #1880: 
     [0 1 4 5 6 8]
    Relevant topics for document #1881: 
     [2]
    Relevant topics for document #1882: 
     [0 1 2]
    Relevant topics for document #1883: 
     [0 7 8]
    Relevant topics for document #1884: 
     [0 4 5 6]
    Relevant topics for document #1885: 
     [0 7 8]
    Relevant topics for document #1886: 
     [0 4 5 8]
    Relevant topics for document #1887: 
     [1 5]
    Relevant topics for document #1888: 
     [0 6]
    Relevant topics for document #1889: 
     [1]
    Relevant topics for document #1890: 
     [0 7]
    Relevant topics for document #1891: 
     [0 1 2 5 9]
    Relevant topics for document #1892: 
     [0 1 4 5 6 8]
    Relevant topics for document #1893: 
     [0 1 9]
    Relevant topics for document #1894: 
     [0 1 5 9]
    Relevant topics for document #1895: 
     [0 1]
    Relevant topics for document #1896: 
     [3 6 7]
    Relevant topics for document #1897: 
     [0 1 3 4 6]
    Relevant topics for document #1898: 
     [0 1 5 7]
    Relevant topics for document #1899: 
     [0 1 5 9]
    Relevant topics for document #1900: 
     [0 4 5 7 8 9]
    Relevant topics for document #1901: 
     [0 2 8]
    Relevant topics for document #1902: 
     [0 3 4 5 7]
    Relevant topics for document #1903: 
     [5 7]
    Relevant topics for document #1904: 
     [0 1 4 5 8 9]
    Relevant topics for document #1905: 
     [0 5 7]
    Relevant topics for document #1906: 
     [3 6]
    Relevant topics for document #1907: 
     [0 2 3 5 7 8 9]
    Relevant topics for document #1908: 
     [3 4 7 8]
    Relevant topics for document #1909: 
     [3 6]
    Relevant topics for document #1910: 
     [5 7]
    Relevant topics for document #1911: 
     [0 4 6 8]
    Relevant topics for document #1912: 
     [0 3 4 6 7 8]
    Relevant topics for document #1913: 
     [5 6 7]
    Relevant topics for document #1914: 
     [4 5 7 8]
    Relevant topics for document #1915: 
     [1 3 4 5 7]
    Relevant topics for document #1916: 
     [1 4 7 8]
    Relevant topics for document #1917: 
     [1 5 8 9]
    Relevant topics for document #1918: 
     [0 5 6 7]
    Relevant topics for document #1919: 
     [0 4 5 7 9]
    Relevant topics for document #1920: 
     [0 4 7]
    Relevant topics for document #1921: 
     [0 4 5 7 8]
    Relevant topics for document #1922: 
     [0 2 4 6 8]
    Relevant topics for document #1923: 
     [0 1 5 7]
    Relevant topics for document #1924: 
     [0 5 7]
    Relevant topics for document #1925: 
     [0 1 5 8 9]
    Relevant topics for document #1926: 
     [0 1 7 9]
    Relevant topics for document #1927: 
     [0 7 9]
    Relevant topics for document #1928: 
     [0 4 5 7 8 9]
    Relevant topics for document #1929: 
     [0 1 9]
    Relevant topics for document #1930: 
     [0 5 7 8]
    Relevant topics for document #1931: 
     [1 4 5]
    Relevant topics for document #1932: 
     [0 1 2 3 4 6 8]
    Relevant topics for document #1933: 
     [3 5 6]
    Relevant topics for document #1934: 
     [0 5 8 9]
    Relevant topics for document #1935: 
     [0 4 5 8 9]
    Relevant topics for document #1936: 
     [0 3 9]
    Relevant topics for document #1937: 
     [0 5 7 8 9]
    Relevant topics for document #1938: 
     [4 5]
    Relevant topics for document #1939: 
     [3 6 7 8]
    Relevant topics for document #1940: 
     [3 4 6 7 8]
    Relevant topics for document #1941: 
     [3 6 9]
    Relevant topics for document #1942: 
     [0 1 2]
    Relevant topics for document #1943: 
     [5]
    Relevant topics for document #1944: 
     [3 4 6 7 8]
    Relevant topics for document #1945: 
     [1 6]
    Relevant topics for document #1946: 
     [0 4 5 6 9]
    Relevant topics for document #1947: 
     [0 2 3 4 9]
    Relevant topics for document #1948: 
     [0 1 5]
    Relevant topics for document #1949: 
     [4 6 7]
    Relevant topics for document #1950: 
     [7 8 9]
    Relevant topics for document #1951: 
     [0 4 7 8]
    Relevant topics for document #1952: 
     [0 5 6 7 8 9]
    Relevant topics for document #1953: 
     [4 7 8 9]
    Relevant topics for document #1954: 
     [0 2 3]
    Relevant topics for document #1955: 
     [0 1 5 7 8]
    Relevant topics for document #1956: 
     [0 3 5 6]
    Relevant topics for document #1957: 
     [0 7 9]
    Relevant topics for document #1958: 
     [0 1 4 5 9]
    Relevant topics for document #1959: 
     [3 4 5 6 7 9]
    Relevant topics for document #1960: 
     [4 6 7]
    Relevant topics for document #1961: 
     [2]
    Relevant topics for document #1962: 
     [0 1 5 9]
    Relevant topics for document #1963: 
     [0 7 9]
    Relevant topics for document #1964: 
     [0 1 5 9]
    Relevant topics for document #1965: 
     [0 1 3 6]
    Relevant topics for document #1966: 
     [5 7]
    Relevant topics for document #1967: 
     [0 7 8 9]
    Relevant topics for document #1968: 
     [0 4 5]
    Relevant topics for document #1969: 
     [0 3 4 6 9]
    Relevant topics for document #1970: 
     [0 3 4 5 7 8]
    Relevant topics for document #1971: 
     [0 5 7 9]
    Relevant topics for document #1972: 
     [0 5 7 9]
    Relevant topics for document #1973: 
     [0 1 2 4 6 8]
    Relevant topics for document #1974: 
     [0 4 5 6 9]
    Relevant topics for document #1975: 
     [0 1 5 9]
    Relevant topics for document #1976: 
     [0 7]
    Relevant topics for document #1977: 
     [0 3 4 6]
    Relevant topics for document #1978: 
     [0 1 4 5 7 8]
    Relevant topics for document #1979: 
     [0 2 7 8]
    Relevant topics for document #1980: 
     [0 4 5 6 7 8]
    Relevant topics for document #1981: 
     [0 2]
    Relevant topics for document #1982: 
     [4 5]
    Relevant topics for document #1983: 
     [4]
    Relevant topics for document #1984: 
     [5 6 8]
    Relevant topics for document #1985: 
     [5]
    Relevant topics for document #1986: 
     [5 7]
    Relevant topics for document #1987: 
     [0 2 4 8]
    Relevant topics for document #1988: 
     [0 1 3 5 6 9]
    Relevant topics for document #1989: 
     [4 7]
    Relevant topics for document #1990: 
     [7]
    Relevant topics for document #1991: 
     [4]
    Relevant topics for document #1992: 
     [4 8]
    Relevant topics for document #1993: 
     [0 5 7]
    Relevant topics for document #1994: 
     [0 2 7 9]
    Relevant topics for document #1995: 
     [0 1 5 8 9]
    Relevant topics for document #1996: 
     [0 1 5 7]
    Relevant topics for document #1997: 
     [7 8]
    Relevant topics for document #1998: 
     [4]
    Relevant topics for document #1999: 
     [4 5 6]
    Relevant topics for document #2000: 
     [0 7]
    Relevant topics for document #2001: 
     [0 4 8 9]
    Relevant topics for document #2002: 
     [0 1 4 8]
    Relevant topics for document #2003: 
     [5]
    Relevant topics for document #2004: 
     [2 3 4]
    Relevant topics for document #2005: 
     [0 1 4 5 6 7]
    Relevant topics for document #2006: 
     [0 3 4 6 7 8]
    Relevant topics for document #2007: 
     [0 4 5 8 9]
    Relevant topics for document #2008: 
     [0 2 7 9]
    Relevant topics for document #2009: 
     [0 4 8]
    Relevant topics for document #2010: 
     [0 3 4 7 9]
    Relevant topics for document #2011: 
     [0 5 6 7 8 9]
    Relevant topics for document #2012: 
     [0 1 5 6 7 9]
    Relevant topics for document #2013: 
     [5]
    Relevant topics for document #2014: 
     [7 8]
    Relevant topics for document #2015: 
     [0 2 4 5 7 8 9]
    Relevant topics for document #2016: 
     [4 5]
    Relevant topics for document #2017: 
     [0 1 5 6]
    Relevant topics for document #2018: 
     [3 6]
    Relevant topics for document #2019: 
     [0 5 9]
    Relevant topics for document #2020: 
     [0 2 3 9]
    Relevant topics for document #2021: 
     [0 2 4 7]
    Relevant topics for document #2022: 
     [3 4 7 8]
    Relevant topics for document #2023: 
     [1 4 5 8]
    Relevant topics for document #2024: 
     [0 5 9]
    Relevant topics for document #2025: 
     [0 4 5]
    Relevant topics for document #2026: 
     [0 1 5 6 8 9]
    Relevant topics for document #2027: 
     [0 1 5 6 8 9]
    Relevant topics for document #2028: 
     [0 2 4 5]
    Relevant topics for document #2029: 
     [0 6 8]
    Relevant topics for document #2030: 
     [6 7]
    Relevant topics for document #2031: 
     [2 3 5 8 9]
    Relevant topics for document #2032: 
     [0 5 7 8]
    Relevant topics for document #2033: 
     [1 6 7 9]
    Relevant topics for document #2034: 
     [4 5 7 8 9]
    Relevant topics for document #2035: 
     [4]
    Relevant topics for document #2036: 
     [0 5 6 7 8 9]
    Relevant topics for document #2037: 
     [1 4 5]
    Relevant topics for document #2038: 
     [0 1 5 8 9]
    Relevant topics for document #2039: 
     [0 5 7 8 9]
    Relevant topics for document #2040: 
     [0 3 7]
    Relevant topics for document #2041: 
     [0 1 5 7 9]
    Relevant topics for document #2042: 
     [0 2 5 9]
    Relevant topics for document #2043: 
     [0 3 7 8 9]
    Relevant topics for document #2044: 
     [0 1 5 6 8 9]
    Relevant topics for document #2045: 
     [0 1 5 7 9]
    Relevant topics for document #2046: 
     [0 2 3 4]
    Relevant topics for document #2047: 
     [0 5]
    Relevant topics for document #2048: 
     [0 4 7]
    Relevant topics for document #2049: 
     [0 1 3 7 8 9]
    Relevant topics for document #2050: 
     [0 1 3 5 9]
    Relevant topics for document #2051: 
     [4 6]
    Relevant topics for document #2052: 
     [0 5 6 7 9]
    Relevant topics for document #2053: 
     [0 2 5 7 9]
    Relevant topics for document #2054: 
     [5 7]
    Relevant topics for document #2055: 
     [4 5 8]
    Relevant topics for document #2056: 
     [0 3 4 7]
    Relevant topics for document #2057: 
     [4 7]
    Relevant topics for document #2058: 
     [0 5 7]
    Relevant topics for document #2059: 
     [0 5 7 8]
    Relevant topics for document #2060: 
     [5 9]
    Relevant topics for document #2061: 
     [4]
    Relevant topics for document #2062: 
     [6]
    Relevant topics for document #2063: 
     [0 4 5 7 8]
    Relevant topics for document #2064: 
     [0 2]
    Relevant topics for document #2065: 
     [4 5 8]
    Relevant topics for document #2066: 
     [0 3 7 8]
    Relevant topics for document #2067: 
     [0]
    Relevant topics for document #2068: 
     [0 1 4 6 7 9]
    Relevant topics for document #2069: 
     [0 1 6 9]
    Relevant topics for document #2070: 
     [0 2 4]
    Relevant topics for document #2071: 
     [5 7]
    Relevant topics for document #2072: 
     [0 1 2 7 8]
    Relevant topics for document #2073: 
     [0 1 2 4 8 9]
    Relevant topics for document #2074: 
     [4 5]
    Relevant topics for document #2075: 
     [0 3 4 6 7]
    Relevant topics for document #2076: 
     [0 3 6 9]
    Relevant topics for document #2077: 
     [5 6 7 8]
    Relevant topics for document #2078: 
     [0 4 5 9]
    Relevant topics for document #2079: 
     [0 4 6 8]
    Relevant topics for document #2080: 
     [6 7 9]
    Relevant topics for document #2081: 
     [0 3 4 6 7]
    Relevant topics for document #2082: 
     [0 3]
    Relevant topics for document #2083: 
     [0 1 5 8]
    Relevant topics for document #2084: 
     [4 6 7 8]
    Relevant topics for document #2085: 
     [0 3 9]
    Relevant topics for document #2086: 
     [6]
    Relevant topics for document #2087: 
     [0 1 5]
    Relevant topics for document #2088: 
     [1 5]
    Relevant topics for document #2089: 
     [1 5 7]
    Relevant topics for document #2090: 
     [0 1 4 8 9]
    Relevant topics for document #2091: 
     [0 3 4 7 8]
    Relevant topics for document #2092: 
     [0 3 4 5 6]
    Relevant topics for document #2093: 
     [0 1 6 8]
    Relevant topics for document #2094: 
     [1 5 6 9]
    Relevant topics for document #2095: 
     [0 1 5]
    Relevant topics for document #2096: 
     [0 4 8]
    Relevant topics for document #2097: 
     [0 3 4 7 9]
    Relevant topics for document #2098: 
     [0 3 7 8 9]
    Relevant topics for document #2099: 
     [1 4 5 9]
    Relevant topics for document #2100: 
     [5 7 9]
    Relevant topics for document #2101: 
     [0 1 5 7 8]
    Relevant topics for document #2102: 
     [4 5 9]
    Relevant topics for document #2103: 
     [0 1 5 8]
    Relevant topics for document #2104: 
     [2 3 4 6 7]
    Relevant topics for document #2105: 
     [0 2 4 7 9]
    Relevant topics for document #2106: 
     [0 5 7 8 9]
    Relevant topics for document #2107: 
     [0 1 4 8]
    Relevant topics for document #2108: 
     [1 4 5 6 7 8 9]
    Relevant topics for document #2109: 
     [5 7 9]
    Relevant topics for document #2110: 
     [0 1 3 4 7 9]
    Relevant topics for document #2111: 
     [0 6 8]
    Relevant topics for document #2112: 
     [2 3 4 7 9]
    Relevant topics for document #2113: 
     [3 4 7 8]
    Relevant topics for document #2114: 
     [0 3 5 7 9]
    Relevant topics for document #2115: 
     [4 6]
    Relevant topics for document #2116: 
     [0 1 5 9]
    Relevant topics for document #2117: 
     [5 8]
    Relevant topics for document #2118: 
     [0 5 9]
    Relevant topics for document #2119: 
     [0 2 7 9]
    Relevant topics for document #2120: 
     [0 2 5 7 8]
    Relevant topics for document #2121: 
     [0 1 5 9]
    Relevant topics for document #2122: 
     [0 1 4 6 7]
    Relevant topics for document #2123: 
     [0 4 8 9]
    Relevant topics for document #2124: 
     [4 8]
    Relevant topics for document #2125: 
     [0 4 8 9]
    Relevant topics for document #2126: 
     [4 5]
    Relevant topics for document #2127: 
     [0 8 9]
    Relevant topics for document #2128: 
     [0 5 7]
    Relevant topics for document #2129: 
     [3 4 6 8]
    Relevant topics for document #2130: 
     [0 4 6 7 9]
    Relevant topics for document #2131: 
     [5 7 9]
    Relevant topics for document #2132: 
     [5 6 7 8]
    Relevant topics for document #2133: 
     [4 5 6 8 9]
    Relevant topics for document #2134: 
     [1 5 9]
    Relevant topics for document #2135: 
     [4]
    Relevant topics for document #2136: 
     [4 5 8]
    Relevant topics for document #2137: 
     [4]
    Relevant topics for document #2138: 
     [1 4 7 8 9]
    Relevant topics for document #2139: 
     [0 5 9]
    Relevant topics for document #2140: 
     [0 2 7 8 9]
    Relevant topics for document #2141: 
     [4 5 7 8]
    Relevant topics for document #2142: 
     [0 5 6 9]
    Relevant topics for document #2143: 
     [0 4 5 9]
    Relevant topics for document #2144: 
     [2 5 7]
    Relevant topics for document #2145: 
     [0 1 3 6 8]
    Relevant topics for document #2146: 
     [1 5 8]
    Relevant topics for document #2147: 
     [0 1 5 7 9]
    Relevant topics for document #2148: 
     [0 3 8 9]
    Relevant topics for document #2149: 
     [0 1 5]
    Relevant topics for document #2150: 
     [0 7]
    Relevant topics for document #2151: 
     [6 7 8 9]
    Relevant topics for document #2152: 
     [0 1 5 6 8 9]
    Relevant topics for document #2153: 
     [3 7 9]
    Relevant topics for document #2154: 
     [0 1 6 7 8 9]
    Relevant topics for document #2155: 
     [5 7]
    Relevant topics for document #2156: 
     [0 9]
    Relevant topics for document #2157: 
     [4 5]
    Relevant topics for document #2158: 
     [0 1 5 6 8]
    Relevant topics for document #2159: 
     [0 3 5 6]
    Relevant topics for document #2160: 
     [0 5 8]
    Relevant topics for document #2161: 
     [0 1 5 7]
    Relevant topics for document #2162: 
     [5 8 9]
    Relevant topics for document #2163: 
     [4 6 7]
    Relevant topics for document #2164: 
     [1 5 7]
    Relevant topics for document #2165: 
     [0 5 9]
    Relevant topics for document #2166: 
     [0 1 2 5]
    Relevant topics for document #2167: 
     [0 4 6 7 8]
    Relevant topics for document #2168: 
     [3 5 7 8]
    Relevant topics for document #2169: 
     [0 1 3 5]
    Relevant topics for document #2170: 
     [0 4 6 7]
    Relevant topics for document #2171: 
     [0 1 5 8 9]
    Relevant topics for document #2172: 
     [3 6]
    Relevant topics for document #2173: 
     [0 3 4]
    Relevant topics for document #2174: 
     [0 2 3 4 5 9]
    Relevant topics for document #2175: 
     [0 7 9]
    Relevant topics for document #2176: 
     [0 1 5 7]
    Relevant topics for document #2177: 
     [0 4 5 8 9]
    Relevant topics for document #2178: 
     [0 1 3 5]
    Relevant topics for document #2179: 
     [0 5 7 8 9]
    Relevant topics for document #2180: 
     [0 5 7]
    Relevant topics for document #2181: 
     [0 5 6 7 9]
    Relevant topics for document #2182: 
     [1 5 7]
    Relevant topics for document #2183: 
     [0 1 5 9]
    Relevant topics for document #2184: 
     [0 3 5 7]
    Relevant topics for document #2185: 
     [3 4 6 8]
    Relevant topics for document #2186: 
     [0 5]
    Relevant topics for document #2187: 
     [0 4 6 8 9]
    Relevant topics for document #2188: 
     [0 2 3 4 7]
    Relevant topics for document #2189: 
     [0 1 3 5 6 8]
    Relevant topics for document #2190: 
     [1 5 7]
    Relevant topics for document #2191: 
     [0 8 9]
    Relevant topics for document #2192: 
     [5 7]
    Relevant topics for document #2193: 
     [0 1 2 3 5 7 8]
    Relevant topics for document #2194: 
     [0 1 5 7]
    Relevant topics for document #2195: 
     [0 1 5 9]
    Relevant topics for document #2196: 
     [1 2 7 8 9]
    Relevant topics for document #2197: 
     [0 3 5 6 9]
    Relevant topics for document #2198: 
     [5 7]
    Relevant topics for document #2199: 
     [2 7 9]
    Relevant topics for document #2200: 
     [0 1 5 8 9]
    Relevant topics for document #2201: 
     [0 2 3 4 7]
    Relevant topics for document #2202: 
     [0 1 5]
    Relevant topics for document #2203: 
     [0 3 4 6]
    Relevant topics for document #2204: 
     [0 1 7]
    Relevant topics for document #2205: 
     [4 5]
    Relevant topics for document #2206: 
     [4 5 8]
    Relevant topics for document #2207: 
     [0 2 5 8 9]
    Relevant topics for document #2208: 
     [0 3 5 9]
    Relevant topics for document #2209: 
     [2 4 5 7 8]
    Relevant topics for document #2210: 
     [0 7 9]
    Relevant topics for document #2211: 
     [0 1 6]
    Relevant topics for document #2212: 
     [0 9]
    Relevant topics for document #2213: 
     [0 4 6 9]
    Relevant topics for document #2214: 
     [3 4 5 7]
    Relevant topics for document #2215: 
     [0 3 5 6 7]
    Relevant topics for document #2216: 
     [0 9]
    Relevant topics for document #2217: 
     [0 4 7 9]
    Relevant topics for document #2218: 
     [5 7 9]
    Relevant topics for document #2219: 
     [0 1 9]
    Relevant topics for document #2220: 
     [4]
    Relevant topics for document #2221: 
     [0 1 5]
    Relevant topics for document #2222: 
     [4 7 9]
    Relevant topics for document #2223: 
     [0 5 6 7 9]
    Relevant topics for document #2224: 
     [4 5 8]
    Relevant topics for document #2225: 
     [1 9]
    Relevant topics for document #2226: 
     [1]
    Relevant topics for document #2227: 
     [0 3 8]
    Relevant topics for document #2228: 
     [3 4 6 7 8 9]
    Relevant topics for document #2229: 
     [0 6 7 8 9]
    Relevant topics for document #2230: 
     [0 3 4 6]
    Relevant topics for document #2231: 
     [0 1 5]
    Relevant topics for document #2232: 
     [0 1 3 6]
    Relevant topics for document #2233: 
     [0 1 3 5 7]
    Relevant topics for document #2234: 
     [4 8]
    Relevant topics for document #2235: 
     [0 5]
    Relevant topics for document #2236: 
     [0 3 4 5 6 7 9]
    Relevant topics for document #2237: 
     [5 8 9]
    Relevant topics for document #2238: 
     [5 7]
    Relevant topics for document #2239: 
     [0 1 2 5 9]
    Relevant topics for document #2240: 
     [4 9]
    Relevant topics for document #2241: 
     [0 4 5 7 8]
    Relevant topics for document #2242: 
     [1 5 7 9]
    Relevant topics for document #2243: 
     [5 7 9]
    Relevant topics for document #2244: 
     [0 3 5 6 9]
    Relevant topics for document #2245: 
     [0 4 9]
    Relevant topics for document #2246: 
     [7 8]
    Relevant topics for document #2247: 
     [6]
    Relevant topics for document #2248: 
     [0 8]
    Relevant topics for document #2249: 
     [1 5 9]
    Relevant topics for document #2250: 
     [1 5 6 9]
    Relevant topics for document #2251: 
     [2]
    Relevant topics for document #2252: 
     [0 1 5 7]
    Relevant topics for document #2253: 
     [0 5 7]
    Relevant topics for document #2254: 
     [0 1 3 5 6 8 9]
    Relevant topics for document #2255: 
     [0 3 4 7 8 9]
    Relevant topics for document #2256: 
     [0 1 4 5 9]
    Relevant topics for document #2257: 
     [4 6 8 9]
    Relevant topics for document #2258: 
     [5 6 7]
    Relevant topics for document #2259: 
     [0 1 5 7]
    Relevant topics for document #2260: 
     [1 2 4 6 7 8]
    Relevant topics for document #2261: 
     [7 8 9]
    Relevant topics for document #2262: 
     [0 2 7 9]
    Relevant topics for document #2263: 
     [0 3 6 9]
    Relevant topics for document #2264: 
     [0 6]
    Relevant topics for document #2265: 
     [0 5 7 9]
    Relevant topics for document #2266: 
     [0 1 4 9]
    Relevant topics for document #2267: 
     [0 1 2]
    Relevant topics for document #2268: 
     [0 5 7 9]
    Relevant topics for document #2269: 
     [0 3]
    Relevant topics for document #2270: 
     [0 4 5 6]
    Relevant topics for document #2271: 
     [4 8]
    Relevant topics for document #2272: 
     [1 9]
    Relevant topics for document #2273: 
     [0 3 7 9]
    Relevant topics for document #2274: 
     [0 2 7]
    Relevant topics for document #2275: 
     [0 3 6 7 9]
    Relevant topics for document #2276: 
     [0 8 9]
    Relevant topics for document #2277: 
     [1 5 6 9]
    Relevant topics for document #2278: 
     [0 4 5]
    Relevant topics for document #2279: 
     [1 5 7]
    Relevant topics for document #2280: 
     [0 4 5 7 8 9]
    Relevant topics for document #2281: 
     [1 3 4 5 6 9]
    Relevant topics for document #2282: 
     [0 5 6 9]
    Relevant topics for document #2283: 
     [3 4 5 6 9]
    Relevant topics for document #2284: 
     [0 1 4 9]
    Relevant topics for document #2285: 
     [0 1 5 7]
    Relevant topics for document #2286: 
     [0 4 7]
    Relevant topics for document #2287: 
     [0 1 7 9]
    Relevant topics for document #2288: 
     [0 1 5 6 9]
    Relevant topics for document #2289: 
     [7]
    Relevant topics for document #2290: 
     [0 5 7 9]
    Relevant topics for document #2291: 
     [5 8]
    Relevant topics for document #2292: 
     [0 4 6]
    Relevant topics for document #2293: 
     [1 5 6 8 9]
    Relevant topics for document #2294: 
     [0 1 9]
    Relevant topics for document #2295: 
     [0 4 7 8]
    Relevant topics for document #2296: 
     [0 4 7]
    Relevant topics for document #2297: 
     [0 2 6 7 9]
    Relevant topics for document #2298: 
     [0 6 9]
    Relevant topics for document #2299: 
     [0 5 6 9]
    Relevant topics for document #2300: 
     [0 1 7 9]
    Relevant topics for document #2301: 
     [1 4 5 6 7 8 9]
    Relevant topics for document #2302: 
     [0 1 3 4 5 6 9]
    Relevant topics for document #2303: 
     [0 3 6]
    Relevant topics for document #2304: 
     [0 4 5 7 8]
    Relevant topics for document #2305: 
     [0 1 4 5]
    Relevant topics for document #2306: 
     [5 7]
    Relevant topics for document #2307: 
     [0 3 5 6 9]
    Relevant topics for document #2308: 
     [8 9]
    Relevant topics for document #2309: 
     [0 1 6 8 9]
    Relevant topics for document #2310: 
     [0 1 3 4 5 6]
    Relevant topics for document #2311: 
     [0 2 5]
    Relevant topics for document #2312: 
     [2 4]
    Relevant topics for document #2313: 
     [0 4 5 9]
    Relevant topics for document #2314: 
     [0 7 9]
    Relevant topics for document #2315: 
     [0 6 9]
    Relevant topics for document #2316: 
     [4 5]
    Relevant topics for document #2317: 
     [0 3 5 6 9]
    Relevant topics for document #2318: 
     [3 5 7 9]
    Relevant topics for document #2319: 
     [0 9]
    Relevant topics for document #2320: 
     [0 1 5 8]
    Relevant topics for document #2321: 
     [0 3 4 5 6 7 8]
    Relevant topics for document #2322: 
     [0 2 3 7 8 9]
    Relevant topics for document #2323: 
     [4]
    Relevant topics for document #2324: 
     [0 3 7]
    Relevant topics for document #2325: 
     [0 2 5 8 9]
    Relevant topics for document #2326: 
     [0 1 5 6 8 9]
    Relevant topics for document #2327: 
     [0 2 4]
    Relevant topics for document #2328: 
     [0 8 9]
    Relevant topics for document #2329: 
     [0 3 5 7]
    Relevant topics for document #2330: 
     [8]
    Relevant topics for document #2331: 
     [0 4]
    Relevant topics for document #2332: 
     [3 7]
    Relevant topics for document #2333: 
     [0 4 9]
    Relevant topics for document #2334: 
     [0 5 6 7 9]
    Relevant topics for document #2335: 
     [0 2 3 4 7 9]
    Relevant topics for document #2336: 
     [0 4 5 6 8]
    Relevant topics for document #2337: 
     [0 5 6 7 9]
    Relevant topics for document #2338: 
     [0 5 6 8 9]
    Relevant topics for document #2339: 
     [4 5 6 7 8 9]
    Relevant topics for document #2340: 
     [0 1 5 8 9]
    Relevant topics for document #2341: 
     [0 7 8 9]
    Relevant topics for document #2342: 
     [0 1 4 5]
    Relevant topics for document #2343: 
     [0 1 5 9]
    Relevant topics for document #2344: 
     [0 4 6 7 9]
    Relevant topics for document #2345: 
     [0 1 5]
    Relevant topics for document #2346: 
     [0 2 5 6 7]
    Relevant topics for document #2347: 
     [4 8]
    Relevant topics for document #2348: 
     [0 4 5 7 8 9]
    Relevant topics for document #2349: 
     [4 5 7]
    Relevant topics for document #2350: 
     [0 3 4]
    Relevant topics for document #2351: 
     [5 7]
    Relevant topics for document #2352: 
     [0 5 8]
    Relevant topics for document #2353: 
     [0 1 8 9]
    Relevant topics for document #2354: 
     [0 3 5 8 9]
    Relevant topics for document #2355: 
     [6]
    Relevant topics for document #2356: 
     [0 3 5 7 8 9]
    Relevant topics for document #2357: 
     [0 3 4 6 7]
    Relevant topics for document #2358: 
     [0 4 5 6 9]
    Relevant topics for document #2359: 
     [0 3 4 7 8]
    Relevant topics for document #2360: 
     [0 8 9]
    Relevant topics for document #2361: 
     [0 1 4 5]
    Relevant topics for document #2362: 
     [0 1 7 8]
    Relevant topics for document #2363: 
     [3 4 6 7]
    Relevant topics for document #2364: 
     [6 7 8]
    Relevant topics for document #2365: 
     [0 1 3 4 5]
    Relevant topics for document #2366: 
     [0 1 3 4 5 6 9]
    Relevant topics for document #2367: 
     [0 4]
    Relevant topics for document #2368: 
     [4 6]
    Relevant topics for document #2369: 
     [0 5 8]
    Relevant topics for document #2370: 
     [0 3 7]
    Relevant topics for document #2371: 
     [0 1 9]
    Relevant topics for document #2372: 
     [0 2 5 7 8]
    Relevant topics for document #2373: 
     [4 5 8]
    Relevant topics for document #2374: 
     [5 8 9]
    Relevant topics for document #2375: 
     [0 1 3 5 6 7 8]
    Relevant topics for document #2376: 
     [2 4]
    Relevant topics for document #2377: 
     [1 7 9]
    Relevant topics for document #2378: 
     [0 5 7 8]
    Relevant topics for document #2379: 
     [0 4]
    Relevant topics for document #2380: 
     [0 3 4 5 7]
    Relevant topics for document #2381: 
     [6]
    Relevant topics for document #2382: 
     [0 2 8 9]
    Relevant topics for document #2383: 
     [0 1 5 8 9]
    Relevant topics for document #2384: 
     [0 5 8]
    Relevant topics for document #2385: 
     [5 9]
    Relevant topics for document #2386: 
     [0 3 4 7 9]
    Relevant topics for document #2387: 
     [0 1 5 7]
    Relevant topics for document #2388: 
     [0 4 7 8]
    Relevant topics for document #2389: 
     [0 1 5]
    Relevant topics for document #2390: 
     [0 3 4 5 8]
    Relevant topics for document #2391: 
     [0 1 2 5 7]
    Relevant topics for document #2392: 
     [0 3 5 7]
    Relevant topics for document #2393: 
     [0 4 8]
    Relevant topics for document #2394: 
     [4 5 8]
    Relevant topics for document #2395: 
     [1 2 5 8 9]
    Relevant topics for document #2396: 
     [0 9]
    Relevant topics for document #2397: 
     [0 1 5 7]
    Relevant topics for document #2398: 
     [4 5 8 9]
    Relevant topics for document #2399: 
     [5 7 8]
    Relevant topics for document #2400: 
     [0 3 4 7 9]
    Relevant topics for document #2401: 
     [0 1 5 8]
    Relevant topics for document #2402: 
     [4 5 6 7 9]
    Relevant topics for document #2403: 
     [4 5]
    Relevant topics for document #2404: 
     [0 5 7 8 9]
    Relevant topics for document #2405: 
     [4]
    Relevant topics for document #2406: 
     [3 4 7 8]
    Relevant topics for document #2407: 
     [0 1 4 5 7]
    Relevant topics for document #2408: 
     [8]
    Relevant topics for document #2409: 
     [0 8]
    Relevant topics for document #2410: 
     [0 4]
    Relevant topics for document #2411: 
     [5]
    Relevant topics for document #2412: 
     [4 8]
    Relevant topics for document #2413: 
     [0 5 7 8]
    Relevant topics for document #2414: 
     [0]
    Relevant topics for document #2415: 
     [4 7 9]
    Relevant topics for document #2416: 
     [0 2 3 6 7 8 9]
    Relevant topics for document #2417: 
     [0 2 7]
    Relevant topics for document #2418: 
     [0 2 4 6 7 8]
    Relevant topics for document #2419: 
     [0 3 6 7]
    Relevant topics for document #2420: 
     [0 3 4 7]
    Relevant topics for document #2421: 
     [0 2 4 8]
    Relevant topics for document #2422: 
     [4 5 8]
    Relevant topics for document #2423: 
     [0 2 4]
    Relevant topics for document #2424: 
     [2]
    Relevant topics for document #2425: 
     [0 4 7]
    Relevant topics for document #2426: 
     [0 2 3 4 5 6 7 8]
    Relevant topics for document #2427: 
     [0 4 6 7 9]
    Relevant topics for document #2428: 
     [1 4 5 6 7 8 9]
    Relevant topics for document #2429: 
     [1 2 4 5 6 9]
    Relevant topics for document #2430: 
     [0 2 7]
    Relevant topics for document #2431: 
     [0 2 3 7 9]
    Relevant topics for document #2432: 
     [0 4 5 7 8 9]
    Relevant topics for document #2433: 
     [0 2 3 4 7 9]
    Relevant topics for document #2434: 
     [0 2 3 4 7]
    Relevant topics for document #2435: 
     [0 2 3 9]
    Relevant topics for document #2436: 
     [3 6]
    Relevant topics for document #2437: 
     [3 4 5 7 8]
    Relevant topics for document #2438: 
     [0 1 2 4 5]
    Relevant topics for document #2439: 
     [0 1 3 4 5]
    Relevant topics for document #2440: 
     [0 1 5 7 9]
    Relevant topics for document #2441: 
     [0 1 5 7 9]
    Relevant topics for document #2442: 
     [0 2 3 4 7 8]
    Relevant topics for document #2443: 
     [2 4]
    Relevant topics for document #2444: 
     [0 1 2 8]
    Relevant topics for document #2445: 
     [1]
    Relevant topics for document #2446: 
     [0 5 8]
    Relevant topics for document #2447: 
     [0 1 9]
    Relevant topics for document #2448: 
     [0 1 2 7]
    Relevant topics for document #2449: 
     [0 2]
    Relevant topics for document #2450: 
     [2 4]
    Relevant topics for document #2451: 
     [0 5 7]
    Relevant topics for document #2452: 
     [0 1 5]
    Relevant topics for document #2453: 
     [0 1 5]
    Relevant topics for document #2454: 
     [0 1 5 6 8]
    Relevant topics for document #2455: 
     [0 1 5]
    Relevant topics for document #2456: 
     [0 4 5 7]
    Relevant topics for document #2457: 
     [0]
    Relevant topics for document #2458: 
     [0 1 5 7]
    Relevant topics for document #2459: 
     [0 1 2]
    Relevant topics for document #2460: 
     [0 1 6 8 9]
    Relevant topics for document #2461: 
     [2]
    Relevant topics for document #2462: 
     [2 4]
    Relevant topics for document #2463: 
     [0 1 5]



```python
fig, ax = plt.subplots(figsize=(7,15), ncols=2, nrows=5)
plt.subplots_adjust(
    wspace  =  0.5,
    hspace  =  0.5
)
c=0
for row in range(0,5):
    for col in range(0,2):
        sns.barplot(x=word_strengths[c], y=t_words[c], color="red", ax=ax[row][col])
        c+=1
plt.show()
```


    
![png](output_13_0.png)
    



```python
t = pipe.transform(ted_data['transcripts.transcript']) 
t = pd.DataFrame(t, columns=[str(t_words[i]) for i in range(0,10)])
t.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>['god', 'book', 'stories', 'oh', 'art']</th>
      <th>['women', 'men', 'girls', 'woman', 'sex']</th>
      <th>['music', 'play', 'sound', 'song', 'ends']</th>
      <th>['brain', 'brains', 'cells', 'body', 'activity']</th>
      <th>['water', 'earth', 'planet', 'ocean', 'species']</th>
      <th>['countries', 'africa', 'government', 'global', 'dollars']</th>
      <th>['cancer', 'cells', 'patients', 'disease', 'cell']</th>
      <th>['data', 'information', 'computer', 'machine', 'internet']</th>
      <th>['city', 'design', 'cities', 'building', 'buildings']</th>
      <th>['kids', 'children', 'education', 'students', 'teachers']</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.052221</td>
      <td>0.027318</td>
      <td>0.032362</td>
      <td>0.023086</td>
      <td>0.014491</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.161931</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.032351</td>
      <td>0.000000</td>
      <td>0.000150</td>
      <td>0.000000</td>
      <td>0.035539</td>
      <td>0.073795</td>
      <td>0.000000</td>
      <td>0.003728</td>
      <td>0.039604</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.069865</td>
      <td>0.000000</td>
      <td>0.037985</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.012010</td>
      <td>0.000000</td>
      <td>0.084761</td>
      <td>0.008095</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.008961</td>
      <td>0.011324</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.021494</td>
      <td>0.063281</td>
      <td>0.001415</td>
      <td>0.000000</td>
      <td>0.153677</td>
      <td>0.032108</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.126145</td>
      <td>0.000000</td>
      <td>0.065130</td>
      <td>0.000000</td>
      <td>0.043809</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_t = t.melt()

# fig = plt.figure(1,figsize=(12,6))
fig, ax = plt.subplots(figsize=(12,6), ncols=1, nrows=1)
sns.violinplot(x="variable", y="value", data=new_t, palette='Reds', ax=ax)
# plt.xticks(rotation=75)
plt.setp( ax.xaxis.get_majorticklabels(), rotation=-45, ha="left", rotation_mode="anchor") 

plt.show()
```


    
![png](output_15_0.png)
    


# 0: god, 1:sex 2: music: 3:brain 4: earth 5: government 6: cancer 7: computer 8:city 9 education 

