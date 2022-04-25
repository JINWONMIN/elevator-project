import random
import numpy as np
import pandas as pd

np.random.seed(76923)   # <-함수를 이용하여 임의의 시드 생성 , [시드의 값에 따라 난수와 흡사하지만 항상 같은 값의 결과를 반환]

numlist_0 = [1, 10, 2, 3, 4, 5, 9]            #배열 생성  [임의의 숫자]
numlist_1 = [1, 10, 2, 3, 4, 5]
numlist_2 = [1, 10, 2, 3, 4, 5
]
numlist_3 = [1, 10, 2, 3, 4, 5, 8
]
numlist_4 = [1, 10, 2, 3, 4, 5, 8, 9
]
numlist_5 = [10, 2, 3, 4, 5, 8, 9
]
numlist_6 = [10, 3, 4, 5, 8, 9
]
numlist_7 = [10, 11, 3, 4, 5, 7, 8, 9
]
numlist_8 = [1, 10, 11, 12, 2, 5, 6, 7, 8, 9
]
numlist_9 = [1, 10, 11, 2, 5, 6, 7, 8, 9
]
numlist_10 = [1, 10, 11, 2, 3, 5, 7, 9
]
numlist_11 = [1, 11, 2, 5, 6, 7, 9
]
numlist_12 = [1, 11, 5, 6, 7, 9
]
numlist_13 = [1, 11, 2, 5, 6, 7, 8
]
numlist_14 = [1, 2, 5, 6, 7, 8
]
numlist_15 = [1, 11, 2, 6, 7, 8
]
numlist_16 = [1, 10, 11, 12, 2, 4, 5, 7, 8
]
numlist_17 = [1, 10, 11, 2, 4, 5, 6, 7, 8
]
numlist_18 = [1, 10, 11, 2, 4, 5, 6, 7
]
numlist_19 = [1, 10, 11, 2, 5, 6, 9
]
numlist_20 = [1, 10, 11, 2, 5
]
numlist_21 = [1, 10, 2, 5, 8
]
numlist_22 = [1, 2, 3, 5, 8
]
numlist_23 = [1, 2, 3, 4, 5
]

time_lst =[]

for i in range(0,30):     # i는 0~29까지의 값을 차례로 반환, (아래 숫자로 생성되어 반환) , range(시작시점, 종료시점)
    time_lst.append(np.random.choice(numlist_0, 1, p=[0.316798527,0.073381054,0.147599313,0.144501653,0.139436561,0.145883042,0.032399849       #time_lst 변수에 append 이하의 값 들을 추가한다.
])[0])                                                                                                                                          #np.random.choice(변수(배열), n개의 값을 선택하여 반환, p를 이용하여 데이터가 선택될 확률을 설정
    time_lst.append(np.random.choice(numlist_1, 1, p=[0.217833977,0.143977338,0.211757944,0.14130881,0.14102143,0.144100501                     #p의 값은 '1' 이어야 하며, 배열의 길이는 항상 변수(배열)와 같아야 한다.
])[0])
    time_lst.append(np.random.choice(numlist_2, 1, p=[0.141365527,0.143119341,0.286075536,0.1432417,0.143119341,0.143078555
])[0])
    time_lst.append(np.random.choice(numlist_3, 1, p=[0.144808518,0.142456256,0.215541433,0.140599208,0.190656983,0.144684714,0.021252889
])[0])
    time_lst.append(np.random.choice(numlist_4, 1, p=[0.040917137,0.242950644,0.091384349,0.05083769,0.184662248,0.144362574,0.14263368,0.102251677
])[0])
    time_lst.append(np.random.choice(numlist_5, 1, p=[0.289114384,0.069257105,0.070370829,0.144124077,0.144742812,0.139091697,0.143299097
])[0])
    time_lst.append(np.random.choice(numlist_6, 1, p=[0.284373976,0.141183219,0.14380531,0.143395608,0.14380531,0.143436578
])[0])
    time_lst.append(np.random.choice(numlist_7, 1, p=[0.440017101,0.039461308,0.009918769,0.005002138,0.10722531,0.060111159,0.118683198,0.219581018
])[0])
    time_lst.append(np.random.choice(numlist_8, 1, p=[0.061860492,0.081740046,0.190726773,0.006782436,0.094778694,0.115886102,0.028065252,0.139566158,0.210606326,0.069987721
])[0])
    time_lst.append(np.random.choice(numlist_9, 1, p=[0.140373751,0.015862668,0.094904389,0.405530204,0.085886571,0.00374837,0.026564537,0.044926119,0.18220339
])[0])
    time_lst.append(np.random.choice(numlist_10, 1, p=[0.103497607,0.057125943,0.179764195,0.296877312,0.012628879,0.123871541,0.140989591,0.085244931
])[0])
    time_lst.append(np.random.choice(numlist_11, 1, p=[0.230789637,0.091873729,0.22517464,0.1490848,0.003934919,0.193562649,0.105579627
])[0])
    time_lst.append(np.random.choice(numlist_12, 1, p=[0.462564413,0.146884337,0.236954921,0.012471312,0.023340406,0.11778461
])[0])
    time_lst.append(np.random.choice(numlist_13, 1, p=[0.46017197,0.089127493,0.155863995,0.127275108,0.079219589,0.010344376,0.077997468
])[0])
    time_lst.append(np.random.choice(numlist_14, 1, p=[0.037919448,0.4043723,0.002007244,0.075969804,0.297682943,0.182048261
])[0])
    time_lst.append(np.random.choice(numlist_15, 1, p=[0.265016873,0.135028121,0.384251969,0.019662542,0.114870641,0.081169854
])[0])
    time_lst.append(np.random.choice(numlist_16, 1, p=[0.112517581,0.195405532,0.110876699,0.086966714,0.290107829,0.120721988,0.039568683,0.01734646,0.026488514
])[0])
    time_lst.append(np.random.choice(numlist_17, 1, p=[0.340739644,0.230879376,0.021922678,0.143238039,0.011553844,0.101219572,0.082753172,0.040981583,0.026712092
])[0])
    time_lst.append(np.random.choice(numlist_18, 1, p=[0.271081914,0.093310095,0.184072932,0.19622827,0.098136479,0.144076507,0.010412477,0.002681325
])[0])
    time_lst.append(np.random.choice(numlist_19, 1, p=[0.059267432,0.020962048,0.107634598,0.516593116,0.227537511,0.015357458,0.052647838
])[0])
    time_lst.append(np.random.choice(numlist_20, 1, p=[0.317325885,0.056356429,0.007793495,0.511938012,0.106586179
])[0])
    time_lst.append(np.random.choice(numlist_21, 1, p=[0.204461294,0.134235585,0.58411215,0.059910069,0.017280903
])[0])
    time_lst.append(np.random.choice(numlist_22, 1, p=[0.300875793,0.476595194,0.045860477,0.152853876,0.02381466
])[0])
    time_lst.append(np.random.choice(numlist_23, 1, p=[0.386012218,0.287002317,0.147208763,0.002190857,0.177585844
])[0])

df = pd.DataFrame(time_lst,columns=['value'])    #time_lst 변수에 value 칼럼 넣어 df라는 데이터프레임형성
print(df)
df.plot()
df.to_csv(r'./seq.csv', sep='\t', encoding='utf-8')   #df데이터프레임을 utf-8인코딩 코드로 \t 구분자로 넣어서 csv파일로 내보내는 것