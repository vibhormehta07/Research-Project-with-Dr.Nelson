#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:19:18 2019

@author: adi
"""

import pandas as pd
import numpy as np
import sys



file = pd.read_csv(sys.argv[1])
df = pd.DataFrame(file)
Size_min = df['Size(bp)'].min()
Size_max = df['Size(bp)'].max()
Size_mean = df['Size(bp)'].mean()
exons_min = df['Number_of_exons'].min()
exons_max = df['Number_of_exons'].max()
exons_mean = df['Number_of_exons'].mean()

print('Size-min:',Size_min,'Size-max:',Size_max,'Size-mean:',Size_mean,'Number_of_exons-min:',exons_min,'Number_of_exons-max:',exons_max,'Number_of_exons-mean:',exons_mean)



