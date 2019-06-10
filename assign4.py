import pandas as pd
import numpy as np
salaries=[{'year':1990,'name':'alice','department':'HR','age':25,'salary':50000},{'year':1990,'name':'bob','department':'rd','age':30,
              'salary':48000},{'year':1990,'name':'charlie','department':'admin',
            'age':45,'salary':55000},{'year':1991,'name':'alice','department':'HR','age':26,'salary':52000},{'year':1991,'name':'bob',
              'department':'rd','age':31,'salary':50000},{'year':1991,'name':'charlie','department':'admin','age':46,'salary':60000},
            {'year':1992,'name':'alice','department':'HR','age':27,'salary':60000},{'year':1992,'name':'bob','department':'rd','age':32,
              'salary':52000},{'year':1992,'name':'charlie','department':'admin','age':28,'salary':62000}]
money_spent=pd.DataFrame(salaries,index=[0,1,2,3,4,5,6,7,8])
money_spent
money_spent.describe()
money_spent.corr()
money_spent.groupby(['year'])['salary'].sum()
money_spent.groupby(['name'])['salary'].sum()
money_spent.groupby(['year','department'])['salary'].sum()