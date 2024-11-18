import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# Corrected file path with raw string notation
df = pd.read_csv(r"D:\COMPLETE_B.TECH_C.S.E\7th_SEMESTER\MINOR PROJECT\Project\Updated_DATA.csv")

# Verify column name and correct if necessary
df1 = df['Gender'].value_counts(ascending=True)

# Plot settings
plt.xlabel('GENDER', fontweight='bold', color='red', fontsize=10, horizontalalignment='center')
plt.ylabel('No. of users', fontweight='bold', color='red', fontsize=10, horizontalalignment='center')
df1.plot.bar()

# Ensure layout fits well and show the plot
plt.tight_layout()
plt.show()
