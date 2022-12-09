#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:48:10 2022

@author: sonyaridesia
"""

import pandas as pd

data = pd.read_csv("Negara.csv")

df = pd.DataFrame(data)
mean = df.groupby(["Benua"]).mean()
std = df.groupby(["Benua"]).std()

print(data)
print(mean)
print(std)