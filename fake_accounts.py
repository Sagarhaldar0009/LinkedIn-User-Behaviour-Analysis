import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset with the correct file path
df = pd.read_csv(r"D:\COMPLETE_B.TECH_C.S.E\7th_SEMESTER\MINOR PROJECT\Project\Updated_DATA.csv")

# Count the number of fake and real profiles based on the 'Fake Profile Indicator' column
fake_profile_counts = df['Fake Profile Indicator'].value_counts()

# Plot settings
plt.figure(figsize=(6, 4))
plt.bar(fake_profile_counts.index, fake_profile_counts.values, color=['red', 'green'])
plt.xlabel('Fake Profile Indicator', fontweight='bold', color='blue', fontsize=10, horizontalalignment='center')
plt.ylabel('Number of Accounts', fontweight='bold', color='blue', fontsize=10, horizontalalignment='center')
plt.title('LinkedIn Fake vs Real Accounts', fontweight='bold', color='purple', fontsize=12)

# Show exact counts on top of the bars
for index, value in enumerate(fake_profile_counts.values):
    plt.text(index, value + 50, str(value), ha='center', fontweight='bold', color='black')

# Ensure layout fits well and show the plot
plt.tight_layout()
plt.show()
