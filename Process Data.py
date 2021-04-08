import pandas as pd
# , index_col=['Destination','Year']
dataset_female = pd.read_csv(
    '/Users/eduardo/TeamRobin/UN_MigrantStockByOriginAndDestination_2019_md/Female.csv', sep=';', index_col=['Continent','Region','Destination', 'Year'])
dataset_female.drop('Order',axis='columns', inplace=True)
dataset_female_long = dataset_female.iloc[:, 9:-5].stack(level=-1).reset_index()
dataset_female_long = dataset_female_long.rename(columns = {'level_4': 'Origin', 0: 'Female'}, inplace = False)
dataset_female_long['Gender']='Female' 
dataset_female_long.drop('Gender',axis='columns', inplace=True)

dataset_male = pd.read_csv(
    '/Users/eduardo/TeamRobin/UN_MigrantStockByOriginAndDestination_2019_md/Male.csv', sep=';', index_col=['Continent','Region','Destination', 'Year'])
dataset_male.drop('Order',axis='columns', inplace=True)
dataset_male_long = dataset_male.iloc[:, 9:-5].stack(level=-1).reset_index()
dataset_male_long = dataset_male_long.rename(columns = {'level_4': 'Origin', 0: 'Male'}, inplace = False)
dataset_male_long['Gender']='Male' 
dataset_male_long.drop('Gender',axis='columns', inplace=True)

print(dataset_female_long.head(3))
print(dataset_male_long.head(3))

data_set_merged = pd.merge(dataset_male_long, dataset_female_long, on=['Destination','Origin', 'Year', 'Region', 'Continent'])

data_set_merged = data_set_merged.set_index(['Continent','Region','Destination', 'Year', 'Origin'])

data_set_merged.reset_index().to_csv('/Users/eduardo/TeamRobin/Total_origin_destination.csv')

data_set_merged_year = data_set_merged.groupby(['Year'])[['Female','Male']].sum().reset_index()
data_set_merged_year.to_csv('/Users/eduardo/TeamRobin/Total_year.csv')

data_set_merged_continent = data_set_merged.groupby(['Continent'])[['Female','Male']].sum().reset_index()
data_set_merged_continent.to_csv('/Users/eduardo/TeamRobin/Total_continent.csv')

data_set_merged_continent_year = data_set_merged.groupby(['Continent','Year'])[['Female','Male']].sum().reset_index()
data_set_merged_continent_year.to_csv('/Users/eduardo/TeamRobin/Total_continent_year.csv')

print(dataset_total_long_grouped_region.head())

dataset_total_long_grouped_region_year = data_set_merged.groupby(['Continent','Region', 'Year'])[['Female','Male']].sum().reset_index()
dataset_total_long_grouped_region_year.to_csv('/Users/eduardo/TeamRobin/Total_region_year.csv')

dataset_total_long_grouped_region = data_set_merged.groupby(['Continent','Region'])[['Female','Male']].sum().reset_index()
dataset_total_long_grouped_region.to_csv('/Users/eduardo/TeamRobin/Total_region.csv')



dataset_total_long_grouped_destination_year = data_set_merged.groupby(['Continent','Region','Destination', 'Year'])[['Female','Male']].sum().reset_index()
dataset_total_long_grouped_destination_year.to_csv('/Users/eduardo/TeamRobin/Total_destination_year.csv')


dataset_total_long_grouped_destination_year = data_set_merged.groupby(['Continent','Region','Destination'])[['Female','Male']].sum().reset_index()
dataset_total_long_grouped_destination_year.to_csv('/Users/eduardo/TeamRobin/Total_destination.csv')


dataset_total_long_grouped_origin = data_set_merged.groupby(['Continent','Region', 'Year', 'Origin'])[['Female','Male']].sum().reset_index()
dataset_total_long_grouped_origin.to_csv('/Users/eduardo/TeamRobin/Total_origin_year.csv')

dataset_total_long_grouped_origin = data_set_merged.groupby(['Continent','Region', 'Origin'])[['Female','Male']].sum().reset_index()
dataset_total_long_grouped_origin.to_csv('/Users/eduardo/TeamRobin/Total_origin.csv')

print(dataset_total_long_grouped_origin.head())