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

data_set_merged = pd.merge(dataset_male_long, dataset_female_long, on=['Destination','Origin', 'Year', 'Region', 'Continent'])

data_set_merged = data_set_merged.set_index(['Continent','Region', 'Year', 'Origin','Destination'])

print(data_set_merged_year)


data_set_merged_year = data_set_merged.pivot_table(index=['Destination','Origin', 'Region', 'Continent'], columns='Year', values=['Male', 'Female'], fill_value=0).reset_index()

data_set_merged_year.reset_index().to_csv('/Users/eduardo/TeamRobin/Total_origin_destination_pivot_.csv')

dataset = pd.read_csv('/Users/eduardo/TeamRobin/Total_origin_destination_pivot.csv', sep=';', index_col=['Continent','Region','Destination', 'Origin'])

dataset = dataset.drop(columns=['Unnamed: 0', 'index']).reset_index()


dataset.to_csv('/Users/eduardo/TeamRobin/Final/Total_origin_destination.csv')

##data_set_merged_year = data_set_merged.groupby(['Year'])[['Female','Male']].sum().reset_index()
##data_set_merged_year.to_csv('/Users/eduardo/TeamRobin/Total_year.csv')

colums =['Female_1990' ,'Female_1995' ,'Female_2000' ,'Female_2005' , 'Female_2010' , 'Female_2015' , 'Female_2019','Male_1990','Male_1995','Male_2000','Male_2005' , 'Male_2010' , 'Male_2015' , 'Male_2019']

data_set_merged_continent = dataset.groupby(['Continent'])[colums].sum().reset_index()
print(dataset_total_long_grouped_region_year)
data_set_merged_continent.to_csv('/Users/eduardo/TeamRobin/Final/Total_continent.csv')

dataset_total_long_grouped_region_year = dataset.groupby(['Continent','Region'])[colums].sum().reset_index()
dataset_total_long_grouped_region_year.to_csv('/Users/eduardo/TeamRobin/Final/Total_region_year.csv')

dataset_total_long_grouped_destination_year = dataset.groupby(['Continent','Region','Destination'])[colums].sum().reset_index()
dataset_total_long_grouped_destination_year.to_csv('/Users/eduardo/TeamRobin/Final/Total_destination_year.csv')

data_set_merged_bis = dataset.set_index(['Continent','Region', 'Origin'])

dataset_total_long_grouped_origin = dataset.groupby(['Continent','Region', 'Origin'])[colums].sum().reset_index()
dataset_total_long_grouped_origin.to_csv('/Users/eduardo/TeamRobin/Final/Total_origin_year.csv')
print(dataset_total_long_grouped_origin)
"""
data_set_merged_bis = data_set_merged[['Continent','Region','Origin', 'Female', 'Male']]

dataset_total_long_grouped_origin = data_set_merged_bis.groupby(['Origin'])[['Female','Male']].sum().reset_index()

data_set_merged_new = pd.merge(dataset_total_long_grouped_origin,  dataset_female_long, on=['Origin'], how='left')

dataset_total_long_grouped_origin.to_csv('/Users/eduardo/TeamRobin/Total_origin.csv')

print(data_set_merged_new)