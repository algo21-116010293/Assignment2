# Shared Analyst Coverage
This Git repo tries to find out the effect of connected-stock(CS) momentum factor and is based on the paper Shared Analyst Coverage:Unifying Momentum Spillover Effects

## Content
* Introduction to Shared Analyst Coverage 
* CS Momentum Effect
* Data
* Factor Testing
* Result
* Further Analysis
* Reference
* Contact

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
![R1](https://github.com/algo21-116010293/Assignment1/blob/main/Asset%20Allocation/R1.png)
 where 𝑅𝑒𝑡𝑗𝑡 is the return of stock j during month t, nij is the number of analysts who cover both stocks i and j, and N is the total number of stocks connected to stock i during the month. Stocks that are co-covered by a greater number of analysts are more likely to be similar to each other so they get a higher weight.

## Data
The data used in this repo is divided into two types, the first is the information of companies with the analysts that wrote report towards them and the second is the stock information. The analyst data is yearly and the stock data is monthly. Because of security, the data cannot be uploaded, examples of these two types are shown below

*Plot: The Data Structure of Analysts and Companies*  
![AnalystTable](https://github.com/algo21-116010293/Assignment1/blob/main/Asset%20Allocation/R1.png) 

*Plot: The Data Structure of Analysts and Companies*  
![StockTable](https://github.com/algo21-116010293/Assignment1/blob/main/Asset%20Allocation/R1.png) 

The time interval of the data is from 2010.01 to 2020.07, which is the test interval. 

## Factor Testing
After calculating the monthly CF Return during 2010 to 2020, we got the result data in folder [CF Return](https://github.com/algo21-116010293/Assignment1/blob/main/asset.xlsx) 

The indicators used to test the shared analyst coverage factor are Rank IC and Return Rate of longing the highest 10 stock and shorting the lowest 10 stocks ordering by CF Return.

### 1. Rank IC

### 2. Return Rate of Long&Short Portfolio
