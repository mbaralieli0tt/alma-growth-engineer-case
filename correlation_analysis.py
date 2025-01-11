import pandas as pd

df = pd.read_csv('HubSpot_Salesforce_Sync_Issues.csv')

# On se focalise sur les 3 colonnes qui ont des NaN
cols_to_check = ['LeadSource', 'MarketSegment', 'IntentSignals']

# 1. Créer un DataFrame de booléens indiquant True si la valeur est NaN
df_isnull = df[cols_to_check].isna()

# 2. Afficher le nombre de NaN par colonne
print('\nNombre de NaN par colonne :')
print(df_isnull.sum())

# 3. Calculer la corrélation entre ces colonnes booléennes
#    (corrélation de Pearson sur des 0/1 => indique la tendance à être "vides" ensemble)
corr_matrix = df_isnull.corr()
print('\nCorrélation entre colonnes (valeurs manquantes) :')
print(corr_matrix)

# 4. Optionnel : compter combien de lignes sont vides en même temps dans LeadSource et MarketSegment, etc.
both_leadsource_marketsegment = (df_isnull['LeadSource'] & df_isnull['MarketSegment']).sum()
both_leadsource_intentsignals  = (df_isnull['LeadSource'] & df_isnull['IntentSignals']).sum()
both_marketsegment_intentsignals = (df_isnull['MarketSegment'] & df_isnull['IntentSignals']).sum()
all_three = (df_isnull['LeadSource'] & df_isnull['MarketSegment'] & df_isnull['IntentSignals']).sum()

print('\nOverlap de NaN :')
print(f"- LeadSource & MarketSegment : {both_leadsource_marketsegment}")
print(f"- LeadSource & IntentSignals : {both_leadsource_intentsignals}")
print(f"- MarketSegment & IntentSignals : {both_marketsegment_intentsignals}")
print(f"- Tous les trois : {all_three}")
