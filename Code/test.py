"""
Rank IC
多空收益
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

result_file = pd.read_excel('C:/Users/apple/Desktop/求职/海通资管/test_result.xls',sheet_name = 'RankIC')
time = result_file['Time'].tolist()
'''
'''
Rank IC = corr(order(t-1,factor),order(t,return))
'''
#2011.1-2020.8
RankIC2020 = []
for i in range(1,8):
    sheetname = '%d' %i
    CF_2011m = pd.read_excel('C:/Users/apple/Desktop/求职/海通资管/CF_Ret_new2020.xls',sheet_name = sheetname)
    CFRet_rank = list(CF_2011m['CF_Ret'].rank())
    NMonRet_rank = list(CF_2011m['NmonthRet'].rank())
    df_corr = pd.concat([pd.DataFrame(CFRet_rank,columns = ['CF_rank']),pd.DataFrame(NMonRet_rank,columns = ['NMon_rank'])],axis = 1)
#corr = stats.pearsonr(CFRet_rank,NMonRet_rank)
    corr_mat = df_corr.corr().as_matrix()
    corr = corr_mat[0,1]
    RankIC2020.append(corr)
RankIC = RankIC2011+RankIC2012+RankIC2013+RankIC2014+RankIC2015+RankIC2016+RankIC2017+RankIC2018+RankIC2019+RankIC2020
RankIC_df = pd.DataFrame(RankIC,columns = ['RankIC'])


# Find out the x axis ---- time
time = []
time_year = []
for i in range(1,8):
    if i < 10:
        t = '2020-0%d' %i
    else:
        t = '2020-%d' %i
    time_year.append(t)
time = time + time_year
time = time[0:114]
time_df = pd.DataFrame(time,columns = ['Time'])
df_RankIC = pd.concat([RankIC_df,time_df],axis = 1)


# 解决中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig1,ax = plt.subplots()
ax.bar(time,RankIC,width = 0.2)
xticks=list(range(0,len(time),10))
xlabels=[time[x] for x in xticks]
xticks.append(len(time))
xlabels.append(time[-1])
ax.set_xticks(xticks)
ax.set_xticklabels(xlabels, rotation=40)
plt.ylabel('Rank IC')
plt.title('CF-Ret月度Rank IC序列')
plt.show()
'''

'''
多空收益率 = 前十股票组合的收益率-后十股票组合的收益率
'''
portRet2015 = []
for i in range(1,13):
    sheetname = '%d' %i
    CF = pd.read_excel('C:/Users/apple/Desktop/求职/海通资管/CF_Ret_new2015.xls',sheet_name = sheetname)
    CF = CF.dropna()
    NoStock = round(len(CF)*0.1)
    CF = CF.sort_values(by = ['CF_Ret'])
    data = CF
    first10 = CF.head(NoStock)['NmonthRet'].tolist()
    last10 = CF.tail(NoStock)['NmonthRet'].tolist()
    port_ret = sum(first10)/NoStock - sum(last10)/NoStock
    portRet2015.append(port_ret)

portRet = portRet2011+portRet2012+portRet2013+portRet2014+portRet2015+portRet2016+portRet2017+portRet2018+portRet2019+portRet2020
portRetPer = [i*100 for i in portRet]
portRetPer_df = pd.DataFrame(portRetPer,columns = ['portRetturn %'])
time_df = pd.DataFrame(time,columns = ['Time'])
df_portRet = pd.concat([portRetPer_df,time_df],axis = 1)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig2,ax = plt.subplots()
ax.plot(time,portRetPer)
xticks=list(range(0,len(time),10))
xlabels=[time[x] for x in xticks]
xticks.append(len(time))
xlabels.append(time[-1])
ax.set_xticks(xticks)
ax.set_xticklabels(xlabels, rotation=40)
plt.ylabel('portforlio return')
plt.title('CF-Ret月度多空收益率')
plt.show()

test_df = pd.ExcelWriter('C:/Users/apple/Desktop/求职/海通资管/test_result.xls')
df_RankIC.to_excel(test_df, sheet_name = 'RankIC', index = False)

portRet_df = pd.ExcelWriter('C:/Users/apple/Desktop/求职/海通资管/portRet_result.xls')
df_portRet.to_excel(portRet_df, sheet_name = 'portReturn', index = False)
portRet_df.save()

CF = pd.read_excel('C:/Users/apple/Desktop/求职/海通资管/CF_Ret_new2012.xls',sheet_name = '1')
NoStock = round(len(CF)*0.1)
CF = CF.sort_values(by = ['CF_Ret'])
data = CF
first10 = CF.head(NoStock)['NmonthRet'].tolist()
last10 = CF.tail(NoStock)['NmonthRet'].tolist()
port_ret = (sum(first10)-sum(last10))/NoStock


