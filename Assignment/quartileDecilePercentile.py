import pandas as pd

afsar = pd.DataFrame({'AthletsName':['A', 'B', 'C', 'D',
               'E', 'F', 'G','H','I','J','K','L','M','N','O'],
       'ShoeSize':[8, 10, 9, 7, 6, 4, 11, 5, 12, 13, 14, 3, 25, 16 , 16]})

afsar.sort_values(by = ['ShoeSize'], inplace = True)
 
afsar['QuantileRank'] = pd.qcut(afsar['ShoeSize'], q = 4, duplicates='drop', labels = False)
 
afsar['DecileRank'] = pd.qcut(afsar['ShoeSize'], q = 10, duplicates='drop', labels = False)

afsar['PercentileRank'] = pd.qcut(afsar['ShoeSize'], q = 100, duplicates='drop', labels = False)

 

print(afsar)
