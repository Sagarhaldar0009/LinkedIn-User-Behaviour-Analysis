import pandas as pd
import matplotlib.pyplot as plt

# Read in the Dataframe
df = pd.read_csv(r"D:\COMPLETE_B.TECH_C.S.E\7th_SEMESTER\MINOR PROJECT\Project\Updated_DATA.csv")

# Creating a Histogram
plt.hist(df['Followers Count'], edgecolor='black', range=[150, 5000])

plt.xlabel('No. of users FOLLOWERS', fontweight='bold', color = 'red', fontsize='10', horizontalalignment='center')
plt.ylabel('No. of users', fontweight='bold', color = 'red', fontsize='10', horizontalalignment='center')

plt.show()