import pandas as pd
# , index_col=['Destination','Year']
dataset_female = pd.read_csv(
    '/Users/eduardo/TeamRobin/UN_MigrantStockByOriginAndDestination_2019_md/Female.csv', sep=';', index_col=['Continent','Region','Destination', 'Year'])

dataset_female.drop('Order',axis='columns', inplace=True)

dataset_female_long = dataset_female.iloc[:, 9:-5].stack(level=-1).reset_index()

dataset_female_long = dataset_female_long.rename(columns = {'level_4': 'Origin', 0: 'Flow'}, inplace = False)

dataset_female_long['Gender']='Female' 

dataset_female_long.to_csv('/Users/eduardo/TeamRobin/Female_origin_destination.csv')

dataset_female_long_grouped_continent = dataset_female_long.groupby(['Continent','Year'])['Flow'].sum().reset_index()
dataset_female_long_grouped_continent.to_csv('/Users/eduardo/TeamRobin/Female_continent.csv')

dataset_female_long_grouped_region = dataset_female_long.groupby(['Region', 'Year'])['Flow'].sum().reset_index()
dataset_female_long_grouped_region.to_csv('/Users/eduardo/TeamRobin/Female_region.csv')

dataset_female_long_grouped_destination = dataset_female_long.groupby(['Destination', 'Year'])['Flow'].sum().reset_index()
dataset_female_long_grouped_destination.to_csv('/Users/eduardo/TeamRobin/Female_destination.csv')

dataset_female_long_grouped_destination = dataset_female_long.groupby(['Origin', 'Year'])['Flow'].sum().reset_index()
dataset_female_long_grouped_destination.to_csv('/Users/eduardo/TeamRobin/Female_origin.csv')

dataset_male = pd.read_csv(
    '/Users/eduardo/TeamRobin/UN_MigrantStockByOriginAndDestination_2019_md/Male.csv', sep=';', index_col=['Continent','Region','Destination', 'Year'])

dataset_male.drop('Order',axis='columns', inplace=True)

print(dataset_male)

dataset_male_long = dataset_male.iloc[:, 9:-5].stack(level=-1).reset_index()

dataset_male_long = dataset_male_long.rename(columns = {'level_4': 'Origin', 0: 'Flow'}, inplace = False)

dataset_male_long['Gender']='Male' 

dataset_male_long.to_csv('/Users/eduardo/TeamRobin/Male_origin_destination.csv')

dataset_male_long_grouped_continent = dataset_male_long.groupby(['Continent','Year'])['Flow'].sum().reset_index()
dataset_male_long_grouped_continent.to_csv('/Users/eduardo/TeamRobin/Male_continent.csv')

dataset_male_long_grouped_region = dataset_male_long.groupby(['Region', 'Year'])['Flow'].sum().reset_index()
dataset_male_long_grouped_region.to_csv('/Users/eduardo/TeamRobin/Male_region.csv')

dataset_male_long_grouped_destination = dataset_male_long.groupby(['Destination', 'Year'])['Flow'].sum().reset_index()
dataset_male_long_grouped_destination.to_csv('/Users/eduardo/TeamRobin/Male_destination.csv')

dataset_male_long_grouped_destination = dataset_male_long.groupby(['Origin', 'Year'])['Flow'].sum().reset_index()
dataset_male_long_grouped_destination.to_csv('/Users/eduardo/TeamRobin/Male_origin.csv')
