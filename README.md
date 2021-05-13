# Shared Analyst Coverage
This Git repo tries to find out the effect of connected-stock(CS) momentum factor and is based on the paper Shared Analyst Coverage:Unifying Momentum Spillover Effects

## Content
* Introduction to Shared Analyst Coverage 
* CS Momentum Effect
* Data
* Factor Testing
* Discussion
* Reference

## Introduction to Shared Analyst Coverage
### 1. Momentum Spillovers
Momentum Spillover is a effect between companies with fundamental similarities or fundamental linkage, which suggests that past return of one firm can predict the return of firms that it relates to. Firms belonging to same industry, sharing same geographic location  and with same techonology are all proved to have this property. 

### 2. Shared Analyst Coverage
In order to try to unify all these findings together, shared analyst coverage is came up with. That is, there may be one single momentum spillover effect. The reasons that shared analyst coverage is propoesd to represent fundamental similarities or fundamental linkage between companies can be concluded as below:

* **First, analysts are responsible for finding fundalmentals, which means the firms that are studied by same analysts tend to be more likely.**

* **Second, analyst linkages uniquely identify linked firm pairs, in contrast with most previous studies that aggregate stocks into buckets.**

* **Third, the degree of linkage can be measured in a more refined way by using the number of shared analysts as a measure of the strength of the relationship.**

Based on these points, this repo tried to test the effect of shared analyst coverage.

## CS Momentum Effect
The factor used to test this momentum effect is called connected-stock (CS) return, which is calculated as 
![CF Formula](https://github.com/algo21-116010293/Assignment2/blob/main/Others/CS_RET.png)
 
where 𝑅𝑒𝑡𝑗𝑡 is the return of stock j during month t, nij is the number of analysts who cover both stocks i and j, and N is the total number of stocks connected to stock i during the month. Stocks that are co-covered by a greater number of analysts are more likely to be similar to each other so they get a higher weight.

Here, we define two stocks as “connected” if at least one analyst covers both stocks at the end of each month. If one research paper is written by more than 1 analysts, we use the first one because he/she is always the head of the research group. 

## Data
The data used in this repo is divided into two types, the first is the information of companies with the analysts that wrote report towards them and the second is the stock information. The analyst data is yearly and the stock data is monthly. Because of security, the data cannot be uploaded, examples of these two types are shown below

*Plot: The Data Structure of Analysts and Companies*  
![AnalystTable](https://github.com/algo21-116010293/Assignment2/blob/main/Data/Analyst_Info.png) 

*Plot: The Data Structure of Stocks*  
![StockTable](https://github.com/algo21-116010293/Assignment2/blob/main/Data/Stock_Info.png) 

The time interval of the data is from 2011.01 to 2020.07, which is the test interval. 

## Factor Testing
After calculating the monthly CF Return during 2010 to 2020, we got the result data [CF Return](https://github.com/algo21-116010293/Assignment2/blob/main/CF_Ret.xls) 

The indicators used to test the shared analyst coverage factor are Rank IC and Return Rate of longing the highest 10 stock and shorting the lowest 10 stocks ordering by CF Return.

### 1.Rank IC 
Rank IC is the correlation between the order of factor value and the order of next return value, that is 

Rank IC = corr(order(t-1,factor),order(t,return)) 

It tells whether the ranks of our alpha values are correlated with the ranks of the future returns. The higher the Rank IC is, the stronger the interpretability the factor is. 

The result of monthly Rank IC from 2012 to 2020 is calculated in the .xls file [RankIC](https://github.com/algo21-116010293/Assignment2/blob/main/Testing%20Result/IC_result.xls)

To visulize, 

*Plot: The Monthly Rank IC of CF Ret*  
![Rank IC](https://github.com/algo21-116010293/Assignment2/blob/main/Testing%20Result/RankIC.png) 

### 2.Return Rate of Long&Short Portfolio
The portfolio is constructed by longing the 10 stock with the highest CF Return and shorting the 10 stock with the lowest CF Return each month.

The result of monthly Rank IC from 2012 to 2020 is calculated in the .xls file [PortRetun](https://github.com/algo21-116010293/Assignment2/blob/main/Testing%20Result/portRet_result.xls)

To visulize, 

*Plot: The Monthly Rank IC of CF Ret*  
![Port Return](https://github.com/algo21-116010293/Assignment2/blob/main/Testing%20Result/Return.png)

## Discussion
From Rank IC and Portforlio Return above, we can see that the performance of CF Return is not that good. However, the statistics in the report [Shared Analyst Coverage:
Unifying Momentum Spillover Effects](https://github.com/algo21-116010293/Assignment2/blob/main/Shared%20Analyst%20Coverage%20Unifying%20Momentum%20Spillover%20Effects.pdf) is quite good, we think the reasons may come from several respects. 

* **First, the data in this report is from A-Share market while the data in the report is from NYSE, NASDAQ, and NYSE MKT. Different markets will bring different effect.**

* **Second, in the report, a stock is considered to be covered by an analyst if the analyst issues at least one FY1 or FY2 earnings forecast for the stock over the past 12 months. However, this repo has not consider the grade that analysts gave to the stock yet.**

* **Third, the construction of factor can consider more aspects like the number of analysts that cover the same stock.**

Toward these points, further work can be done. Actually, the paper also implied other method try to improve it. 

## Reference
The basic paper that this repo base on is [Shared Analyst Coverage:
Unifying Momentum Spillover Effects](https://github.com/algo21-116010293/Assignment2/blob/main/Shared%20Analyst%20Coverage%20Unifying%20Momentum%20Spillover%20Effects.pdf)

## Code
The codes used to calculate the CF Return are in the `cf.py` [CF code](https://github.com/algo21-116010293/Assignment2/blob/main/Code/cf.py) 
The codes used to calculate the Indicator are `test.py`[test code](https://github.com/algo21-116010293/Assignment2/blob/main/Code/test.py) 
