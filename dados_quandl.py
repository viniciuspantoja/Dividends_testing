#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:22:38 2018

@author: ViniciusPantoja
"""
#%%


import good_morning as gm
import pandas as pd
import numpy as np
import os

os.chdir('/Users/ViniciusPantoja/Dropbox/Dividendos/Codigos')

tickers = pd.read_csv('S&P_Ticker.csv')

stock = 'GOOG'
kr = gm.FinancialsDownloader()
kr_frames = kr.download(stock)

#%% DIVIDEND PAYOUT RATIO

###
def get_net_income(financial_statements):
    temp = financial_statements['cash_flow']
    
    temp = temp[temp['title'] == 'Net income']
    temp = np.array(temp)[0][2:]

    return temp

def get_dividend_paid(financial_statements):
    temp = financial_statements['cash_flow']
    
    temp = temp[temp['title'] == 'Dividend paid']
    
    temp = np.array(temp)[0][2:]
    
    return -temp

def div_ratio(financial_statements):
    temp = get_dividend_paid(financial_statements)/get_net_income(financial_statements)
    return temp




dividend_ratio = div_ratio(kr_frames)

#%% EARNINGS PER SHARE

def get_earnings_per_share(financial_statements):
    temp = financial_statements['income_statement']
    index_item = temp.index[temp['title'] == 'Earnings per share'] + 2
    return temp.loc[index_item]

a = get_earnings_per_share(financial_statements)
    
    

#%% DIVIDEND COVERAGE RATIO



















