import pandas as pd

afsar ={'Athletes':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],'Shoe Size':[8,10,9,7,19,15,20,26,11,5,12,13,4,3,22]}

afsar = pd.DataFrame(afsar, columns =['Athletes', 'Shoe Size'])

afsar.sort_values(by=['Shoe Size'], inplace = True)

afsar['QuartileRank'] = pd.qcut(afsar['Shoe Size'], q= 4, labels=False)

afsar['QuartileRank'] = pd.qcut(afsar['Shoe Size'], q= 10, labels=False)



print(afsar)