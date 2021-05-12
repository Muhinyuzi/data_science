import pandas as pd
import numpy as np

# Filter all warnings. If you would like to see the warnings, please comment the two lines below.
import warnings
warnings.filterwarnings('ignore')

Energy = pd.read_excel("datasets/Energy Indicators.xls",header=17,skipfooter=38) 
Energy = Energy.rename(columns={'Unnamed: 1':'Country','Petajoules':'Energy Supply','Gigajoules':'Energy Supply per Capita','%':'% Renewable'})  
Energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']] = Energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']].replace('...',np.NaN).apply(pd.to_numeric)   
Energy['Energy Supply'] = Energy['Energy Supply']*1000000  
Energy['Country'] = Energy['Country'].replace({'China, Hong Kong Special Administrative Region':'Hong Kong','United Kingdom of Great Britain and Northern Ireland':'United Kingdom','Republic of Korea':'South Korea','United States of America':'United States','Iran (Islamic Republic of)':'Iran'})  
Energy['Country'] = Energy['Country'].str.replace(" \(.*\)","") 
#Creating GDP DataFrame
GDP = pd.read_csv("datasets/world_bank.csv", header=4)
GDP['Country Name'] = GDP['Country Name'].replace('Korea, Rep.','South Korea')
GDP['Country Name'] = GDP['Country Name'].replace('Iran, Islamic Rep.','Iran')
GDP['Country Name'] = GDP['Country Name'].replace('Hong Kong SAR, China','Hong Kong')
columns = ['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
GDP = GDP[columns]
GDP.columns = ['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
ScimEn = pd.read_excel("datasets/scimagojr-3.xlsx")
ScimEn_m = ScimEn[:15] 
merged_1 = pd.merge(ScimEn, Energy, how = 'inner', on = 'Country')
merged_2 = pd.merge(merged_1,GDP, how = 'inner', on = 'Country').set_index('Country')
merged_2 = merged_2[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', 
'2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
print(merged_2)

ScimEn = pd.read_excel("datasets/scimagojr-3.xlsx")
merged_3 = pd.merge(ScimEn, Energy, how = 'outer', on = 'Country')
merged_4 = pd.merge(merged_3,GDP, how = 'outer', on = 'Country').set_index('Country')
merged_4 = merged_4[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', 
'2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
lost = len(merged_4) - len(merged_2)
print(merged_4)
print(len(merged_2))
print(len(merged_4))
print(lost)

GDP_15 = merged_4[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]#.set_index('Country')
GDP_15 = GDP_15[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']] 
GDP_15.fillna(0, inplace=True)
GDP_Top15 = GDP_15
rows = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
GDP_15['Average'] = GDP_15.apply(lambda x: np.average(x[rows]), axis=1)
print(GDP_15.head()) 
print(GDP_15['Average'].head())
GDP_16 = GDP_15['Average']
GDP_16 = GDP_16.sort_values(ascending=False)
GDP_16 = GDP_16.head(15)
print(GDP_16)
print(type(GDP_16))

country = GDP_16.index[5]

change = GDP_Top15.loc[country]['2015'] - GDP_Top15.loc[country]['2006']
print(change)
mean = merged_2['Energy Supply per Capita'].mean()
print(mean)
print(len(merged_2))
max_value = merged_2['% Renewable'].max()
print(max_value)
print(merged_2['% Renewable'])
df=merged_2[merged_2['% Renewable'] == max_value]
country_name = df.index[0]
final = (country_name,max_value)
print(final)

merged_2['citations_ratio'] = merged_2['Self-citations'] / merged_2['Citations']
max_value = merged_2['citations_ratio'].max()
df=merged_2[merged_2['citations_ratio'] == max_value]
country_name = df.index[0]
final = (country_name,max_value)
print(merged_2[['Citations','Self-citations','citations_ratio']])
print(final)

merged_2['population_est'] = merged_2['Energy Supply'] / merged_2['Energy Supply per Capita']
df = merged_2['population_est'].sort_values(ascending=False)
country_name=df.index[2]
print(country_name)

merged_2['population_est'] = merged_2['Energy Supply'] / merged_2['Energy Supply per Capita']
merged_2['Citable docs per Capita'] = merged_2['Citable documents'] / merged_2['population_est']
corr = merged_2.corr().loc['Citable docs per Capita','Energy Supply per Capita']

print(corr)

median = merged_2['% Renewable'].median(axis = 0)
for item in merged_2['% Renewable']:
    if item >= median:
	    merged_2['median_level'] = 1
    else:
	    merged_2['median_level'] = 0
HighRenew = merged_2['median_level'].sort_values(ascending=True)

print(len(merged_2))
print(len(merged_4))
print(lost)







	