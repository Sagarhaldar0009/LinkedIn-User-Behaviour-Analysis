import pandas as pd
import numpy as np

# Load the CSV file
file_path = r"D:\COMPLETE_B.TECH_C.S.E\7th_SEMESTER\MINOR PROJECT\Project\DATA.csv"

data = pd.read_csv(file_path)

# Adjust Gender distribution
gender_distribution = ["Male"] * 65 + ["Female"] * 30 + ["Other"] * 5
data['Gender'] = np.random.choice(gender_distribution, size=len(data), replace=True)


fake_account_distribution = ["Yes"] * 30 + ["No"] * 70
data['Fake Profile Indicator'] = np.random.choice(fake_account_distribution, size=len(data), replace=True)


# Adjust Ethnicity distribution
ethnicity_distribution = ["Black"] * 10 + ["White"] * 60 + ["Other"] * 30
data['Ethnicity'] = np.random.choice(ethnicity_distribution, size=len(data), replace=True)

# Set Company distribution (60% Microsoft, 40% across 15 other companies)
companies = ["Microsoft"] * 60 + ["Google", "Amazon", "Facebook", "Apple", "Netflix", "Tesla", "Accenture", 
                                  "IBM", "Oracle", "Intel", "Salesforce", "Cisco", "SAP", "Adobe", "HP", "Dell"] * 3
data['Company Name'] = np.random.choice(companies, size=len(data), replace=True)

# Adjust Age Group for specified percentages
total_users = len(data)
age_groups = (["18-24"] * int(0.13 * total_users) + ["25-34"] * int(0.30 * total_users) + ["35-44"] * int(0.35 * total_users) + 
              ["45-54"] * int(0.20 * total_users) + ["55+"] * int(0.02 * total_users))
data['Age Group'] = np.random.choice(age_groups, size=total_users, replace=True)

# Adjust Followers Count with noticeable differences
data['Followers Count'] = np.random.randint(500, 50000, size=len(data))

# Save the updated data to a new CSV file
updated_file_path = 'D:\\COMPLETE_B.TECH_C.S.E\\7th_SEMESTER\\MINOR PROJECT\\Project\\Updated_DATA.csv'
data.to_csv(updated_file_path, index=False)

print("Updated file saved as:", updated_file_path)
