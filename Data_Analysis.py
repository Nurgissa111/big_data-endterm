import matplotlib.pyplot as plt
import seaborn as sns

# Setting the aesthetic style of the plots
sns.set_style("whitegrid")

# EDA 1: Distribution of Technologies
plt.figure(figsize=(12, 8))
tech_distribution = data_clean['Technology'].value_counts().head(10)
sns.barplot(y=tech_distribution.index, x=tech_distribution.values, palette="viridis")
plt.title('Top 10 Surveillance Technologies')
plt.xlabel('Frequency')
plt.ylabel('Technology Type')
plt.show()

# EDA 2: State-wise Analysis
plt.figure(figsize=(12, 8))
state_distribution = data_clean['State'].value_counts().head(10)
sns.barplot(y=state_distribution.index, x=state_distribution.values, palette="coolwarm")
plt.title('Top 10 States by Surveillance Technology Adoption')
plt.xlabel('Number of Records')
plt.ylabel('State')
plt.show()

# EDA 3: Agency Type Analysis
plt.figure(figsize=(12, 8))
lea_distribution = data_clean['Type of LEA'].value_counts().head(10)
sns.barplot(y=lea_distribution.index, x=lea_distribution.values, palette="muted")
plt.title('Top 10 Types of Law Enforcement Agencies Using Surveillance Technologies')
plt.xlabel('Frequency')
plt.ylabel('Type of LEA')
plt.show()
