import pandas as pd

dataset_female = pd.read_csv(
    '/Users/eduardo/TeamRobin/UN_MigrantStockByOriginAndDestination_2019_md/Female.csv', sep=';', index_col=['Destination','Year'])

dataset_female_long = dataset_female.iloc[:, 9:-5].stack().reset_index()

dataset_male = pd.read_csv(
    '/Users/eduardo/TeamRobin/UN_MigrantStockByOriginAndDestination_2019_md/Male.csv', sep=';', index_col=['Destination','Year'])

dataset_male_long = dataset_male.iloc[:, 9:-5].stack().reset_index()

dataset_male_long.to_csv('/Users/eduardo/TeamRobin/Male_long.csv')

dataset_total = pd.read_csv(
    '/Users/eduardo/TeamRobin/UN_MigrantStockByOriginAndDestination_2019_md/Total.csv', sep=';', index_col=['Destination','Year'])

dataset_total_long = dataset_total.iloc[:, 9:-5].stack().reset_index()

print(dataset_female_long.iloc[60:70])

dataset_total_long.to_csv('/Users/eduardo/TeamRobin/Total_long.csv')
dataset_male_long.to_csv('/Users/eduardo/TeamRobin/Male_long.csv')

dataset_female_long.to_csv('/Users/eduardo/TeamRobin/Female_long.csv')

