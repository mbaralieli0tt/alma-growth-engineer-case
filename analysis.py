import pandas as pd

df = pd.read_csv('HubSpot_Salesforce_Sync_Issues.csv')

# 1. Which size is the data sample?
print('\nSize of the data sample :')
print(df.shape)

# 2. What is the data type of each column?
print('\nData type of each column :')
print(df.dtypes)

# 3. What is the distribution of the data in the column LeadSource counting empty as well?
print('\nLeadSource :\n')
print(df['LeadSource'].value_counts(dropna=False))

# 4. What is the distribution of the data in the column MarketSegment counting empty as well?
print('\nMarketSegment :\n')
print(df['MarketSegment'].value_counts(dropna=False))

# 5. What is the distribution of the data in the column LifecycleStage counting empty as well?
print('\nLifecycleStage :\n')
print(df['LifecycleStage'].value_counts(dropna=False))

# 6. What is the distribution of the data in the column IntentSignals counting empty as well?
print('\nIntentSignals :\n')
print(df['IntentSignals'].value_counts(dropna=False))

