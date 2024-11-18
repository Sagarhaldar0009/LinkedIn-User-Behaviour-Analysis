import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# df = pd.read_csv ("C://Users//Downloads//data.csv") 
df = pd.read_csv(r"D:\COMPLETE_B.TECH_C.S.E\7th_SEMESTER\MINOR PROJECT\Project\Updated_DATA.csv")
df1 = df['Ethnicity'].value_counts(ascending=True) 

plt.xlabel('ETHNICITY', fontweight='bold', color = 'red', fontsize='10', horizontalalignment='center')
plt.ylabel('No. of users', fontweight='bold', color = 'red', fontsize='10', horizontalalignment='center')

df1.plot.bar() 

plt.show()