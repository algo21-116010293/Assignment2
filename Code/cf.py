'''
info_df: ['stock_code','stock_name','author_name','create_date','create_year',
                               'create_month']，指定时间段内的分析师数据表格
stk_mod: 可以用来计算的股票
stkAnalyst_dict: key是股票，value是其分析师
returns: 股票对应的月收益率
'''
import pandas as pd
import numpy as np
import numpy.matlib

stk_2010 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/分析师预测数据（2010-2020）_20200915_203919/rpt_forecast_stk_2010.csv')
stk_2011 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/分析师预测数据（2010-2020）_20200915_203919/rpt_forecast_stk_2011.csv')
stk_2012 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/分析师预测数据（2010-2020）_20200915_203919/rpt_forecast_stk_2012.csv')
stk_2013 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/分析师预测数据（2010-2020）_20200915_203919/rpt_forecast_stk_2013.csv')
stk_2014 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/分析师预测数据（2010-2020）_20200915_203919/rpt_forecast_stk_2014.csv')
stk_2015 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/分析师预测数据（2010-2020）_20200915_203919/rpt_forecast_stk_2015.csv')
stk_2016 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/分析师预测数据（2010-2020）_20200915_203919/rpt_forecast_stk_2016.csv')
stk_2017 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/分析师预测数据（2010-2020）_20200915_203919/rpt_forecast_stk_2017.csv')
stk_2019 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/分析师预测数据（2010-2020）_20200915_203919/rpt_forecast_stk_2019.csv')
stk_2020 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/分析师预测数据（2010-2020）_20200915_203919/rpt_forecast_stk_2020.csv')

stk_total = pd.concat([stk_2010,stk_2011,stk_2012,stk_2013,stk_2014,stk_2015,stk_2016,stk_2017,
                       stk_2019,stk_2020], axis = 0)
stk_total['create_date'] = pd.to_datetime(stk_total['create_date'], format = '%Y-%m-%d')
stk_total['create_year'] = stk_total['create_date'].map(lambda x: x.year)
stk_total['create_month'] = stk_total['create_date'].map(lambda x: x.month)
stk_need = stk_total[['stock_code','stock_name','author_name','create_date','create_year',
                               'create_month']]
# Find the dateframe that cover from now to 1 year ago
def FindPeriod(year,month):
    if month == 12:
        stk_select = stk_need.loc[stk_need['create_year'] == year]
    else:
        sel0 = stk_need.loc[stk_need['create_year'] == year-1]
        sel1 = sel0.loc[(sel0['create_month'] >= month+1) &(sel0['create_month'] <= 12)]
        sel2 = stk_need.loc[stk_need['create_year'] == year]
        sel3 = sel2.loc[(sel2['create_month'] >= 1) &(sel2['create_month'] <= month)]
        stk_select = pd.concat([sel1,sel3], axis = 0)
    return stk_select
#peirod_test   = FindPeriod(2011,1)      

# Find stocks
def Stock(year,month):
    info_df = FindPeriod(year,month)
    stocks = list(set(info_df['stock_name']))
    return stocks
test_stk = Stock(2011,5)

# Find analysts for certain stk
def FindAnalyst(stk,y,m):
    info_df = FindPeriod(y,m)
    stock = info_df.loc[info_df['stock_name'] == stk]
    analysts = list(set(stock['author_name']))
    if '无' in analysts:
        analysts.remove('无')
    analysts_mod = []
    for i in analysts:
        if ',' not in i:
            analysts_mod.append(i)
        else:
            items = i.split(',')
            analysts_mod.append(items[0])
    analysts_mod = list(set(analysts_mod))
    return analysts_mod
   
#2010.1
def FindStk_avail(df,y,m):
    stocks = Stock(y,m)
    stk_available = list(df['Name'])  #有return的股票
    StkAvail = list(set(stocks).intersection(set(stk_available)))  #可以用来计算的股票
    return StkAvail
#test_stkA = FindStk_avail(stkData1,2011,5) 

def MakeAnalystDict(df,y,m):
    stk_avail = FindStk_avail(df,y,m)
    StkAnalystDict = {}
    for i in range(len(stk_avail)):
        analystList = FindAnalyst(stk_avail[i],y,m)
        StkAnalystDict[stk_avail[i]] = analystList
    return StkAnalystDict
#test_SADict = MakeAnalystDict(stkData1,2011,5)  #== 原来stkAnalyst_dic

def FindRet(df,y,m):
    stk_avail = FindStk_avail(df,y,m)
    Returns = []
    for i in stk_avail:
        ret = df.loc[df['Name'] == i].iloc[0,-1]
        Returns.append(ret)
    return Returns
#test_ret = FindRet(stkData1,2011,5)  #== 原来returns

# returns里面可能存在nan的值，把值去掉
def FindNan(df,y,m):
    returns = FindRet(df,y,m)
    nans = np.argwhere(np.isnan(returns))
    NansList = []
    for item in nans:
        NansList.append(item[0])
    return NansList
#test_nan = FindNan(stkData1,2011,5) #== nans_list

# 根据nans调整returns, stk_mod, stkAnalyst_dict:去掉含有nan的stock
def ModItems(df,y,m):
    nans_list = FindNan(df,y,m)
    returns = FindRet(df,y,m)
    stkAnalyst_dict = MakeAnalystDict(df,y,m)
    stk_avail = FindStk_avail(df,y,m)
    returns = [returns[i] for i in range(len(returns)) if i not in nans_list]
    for i in nans_list:
        del stkAnalyst_dict[stk_avail[i]]
    stk_mod = [stk_avail[i] for i in range(len(stk_avail)) if i not in nans_list]
    return returns, stkAnalyst_dict, stk_mod
# test_ret, test_stkD, test_stk = ModItems(stkData1,2011,5) #== returns, stkAnalyst_dict, stk_mod

# Calculate CF_Ret
def CalCfRet(df,y,m):
    returns, stkAnalyst_dict, stk_mod = ModItems(df,y,m)
    n = len(stk_mod)
    # Find the number of related stock analyst of a certain stk
    analyst_mat = np.matlib.zeros((n,n))
    for i in range(len(stk_mod)-1):
        for j in range(i+1,len(stk_mod)):
            common_Ana = set(stkAnalyst_dict[stk_mod[i]]).intersection(set(stkAnalyst_dict[stk_mod[j]]))
            analyst_mat[i,j] = len(common_Ana)
    analyst_mat += analyst_mat.T - np.diag(analyst_mat.diagonal()) # (nij)1496*1496
    totAna_mat = analyst_mat.sum(axis = 1) # the sum of nij for stock i
    returns_mat = np.matrix(returns).T
    CF_Ret = np.dot(analyst_mat,returns_mat)
    CF_Ret1 = CF_Ret/totAna_mat
    CF_Ret1[np.isnan(CF_Ret1)] = 0  #分母为0返回nan
    return CF_Ret1
# test_CFR = CalCfRet(stkData1)

def FindStkCode(df,y,m):
    stk_mod = ModItems(df,y,m)[2]
    stk_code = []
    for i in stk_mod:
        code = df.loc[df['Name'] == i].iloc[0,0]
        stk_code.append(code)
    return stk_code
# test_code = FindStkCode(stkData1)

def CreateDF(df,y,m):
    stk_code = pd.DataFrame(FindStkCode(df,y,m),columns = ['StockNum'])
    stk_mod = pd.DataFrame(ModItems(df,y,m)[2], columns = ['StockName'])
    CFRet = pd.DataFrame(CalCfRet(df,y,m),columns = ['CF Ret'])
    final_df = pd.concat([stk_code,stk_mod,CFRet], axis = 1)
    final_df = final_df.sort_values(by = ['StockNum'])
    return final_df
# test_df = CreateDF(stkData1)

stkData1 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/StockBasicData_20200917/data/MonthStockList_20110131.csv')
stkData2 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/StockBasicData_20200917/data/MonthStockList_20110228.csv')
stkData3 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/StockBasicData_20200917/data/MonthStockList_20110331.csv')
stkData4 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/StockBasicData_20200917/data/MonthStockList_20110429.csv')
stkData5 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/StockBasicData_20200917/data/MonthStockList_20110531.csv')
stkData6 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/StockBasicData_20200917/data/MonthStockList_20110630.csv')
stkData7 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/StockBasicData_20200917/data/MonthStockList_20110729.csv')
stkData8 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/StockBasicData_20200917/data/MonthStockList_20110831.csv')
stkData9 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管//StockBasicData_20200917/data/MonthStockList_20110930.csv')
stkData10 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/StockBasicData_20200917/data/MonthStockList_20111031.csv')
stkData11 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/StockBasicData_20200917/data/MonthStockList_20111130.csv')
stkData12 = pd.read_csv(
        '/Users/minjue/Desktop/求职/海通资管/StockBasicData_20200917/data/MonthStockList_20111230.csv')
'''
result2011_1 = CreateDF(stkData1,2011,1)
result2010_2 = CreateDF(stkData2)
result2010_3 = CreateDF(stkData3)
result2010_4 = CreateDF(stkData4)
result2010_5 = CreateDF(stkData5)
result2010_6 = CreateDF(stkData6)
result2010_7 = CreateDF(stkData7)
result2010_8 = CreateDF(stkData8)
result2010_9 = CreateDF(stkData9)
result2010_10 = CreateDF(stkData10)
result2010_11 = CreateDF(stkData11)
result2010_12 = CreateDF(stkData12)

result_df = pd.ExcelWriter('/Users/minjue/Desktop/求职/海通资管/CF_Ret_2011.xls')
result2011_1.to_excel(result_df, sheet_name = '2017.01', index = False)
result2010_2.to_excel(result_df, sheet_name = '2017.02', index = False)
result2010_3.to_excel(result_df, sheet_name = '2017.03', index = False)
result2010_4.to_excel(result_df, sheet_name = '2017.04', index = False)
result2010_5.to_excel(result_df, sheet_name = '2017.05', index = False)
result2010_6.to_excel(result_df, sheet_name = '2017.06', index = False)
result2010_7.to_excel(result_df, sheet_name = '2017.07', index = False)
result2010_8.to_excel(result_df, sheet_name = '2017.08', index = False)
result2010_9.to_excel(result_df, sheet_name = '2017.09', index = False)
result2010_10.to_excel(result_df, sheet_name = '2017.10', index = False)
result2010_11.to_excel(result_df, sheet_name = '2017.11', index = False)
result2010_12.to_excel(result_df, sheet_name = '2017.12', index = False)
result_df.save()
'''
