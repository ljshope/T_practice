# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:05:11 2020

@author: Joon
"""

import pandas as pd

BM = pd.read_csv (r'C:\Users\reejung\Desktop\New folder\BM.csv')
CM = pd.read_csv (r'C:\Users\reejung\Desktop\New folder\CM.csv')
EM = pd.read_csv (r'C:\Users\reejung\Desktop\New folder\EM.csv')

ebit_ev = pd.read_csv (r'C:\Users\reejung\Desktop\New folder\ebit_ev.csv')
gpa = pd.read_csv (r'C:\Users\reejung\Desktop\New folder\gpa.csv')
market_value = pd.read_csv (r'C:\Users\reejung\Desktop\New folder\market_value.csv')
price = pd.read_csv (r'C:\Users\reejung\Desktop\New folder\price.csv')
roa = pd.read_csv (r'C:\Users\reejung\Desktop\New folder\roa.csv')

#BM.dropna()
#BM.dropna(axis=1, how='all')