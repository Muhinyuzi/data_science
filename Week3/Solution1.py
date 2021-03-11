import pandas as pd
import numpy as np
 

energy = pd.read_excel('datasets/Energy Indicators.xls', skiprows=17,skipfooter= 38)  
energy = energy[['Unnamed: 1','Petajoules','Gigajoules','%']]
energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']  
energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']] =  energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']].replace('...',np.NaN).apply(pd.to_numeric)  
energy['Energy Supply'] = energy['Energy Supply']*1000000  
energy['Country'] = energy['Country'].replace({'China, Hong Kong Special Administrative Region':'Hong Kong','United Kingdom of Great Britain and Northern Ireland':'United Kingdom','Republic of Korea':'South Korea','United States of America':'United States','Iran (Islamic Republic of)':'Iran'})  
energy['Country'] = energy['Country'].str.replace(" \(.*\)","")  
    
GDP = pd.read_csv('datasets/world_bank.csv', skiprows=4)
GDP['Country Name'] = GDP['Country Name'].replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"})  
GDP = GDP[['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]  
    
ScimEn = pd.read_excel('datasets/scimagojr-3.xlsx')
ScimEn = ScimEn[0:15]  
    
df = pd.merge(ScimEn, energy, how = 'inner', left_on = 'Country', right_on='Country')
dff = pd.merge(df,GDP, how = 'inner', left_on = 'Country', right_on='Country Name').set_index('Country')  
dff = dff[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
#print(dff)
#print(dff.columns)
#print(GDP)
#print(ScimEn)
print(energy.columns)



def answer_two():
    import pandas as pd
    import numpy as np
 
    energy = pd.read_excel('datasets/Energy Indicators.xls', skiprows=17,skipfooter= 38)
    energy = energy[['Unnamed: 1','Petajoules','Gigajoules','%']]
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']] =  energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']].replace('...',np.NaN).apply(pd.to_numeric)
    energy['Energy Supply'] = energy['Energy Supply']*1000000
    energy['Country'] = energy['Country'].replace({'China, Hong Kong Special Administrative Region':'Hong Kong','United Kingdom of Great Britain and Northern Ireland':'United Kingdom','Republic of Korea':'South Korea','United States of America':'United States','Iran (Islamic Republic of)':'Iran'})
    energy['Country'] = energy['Country'].str.replace(" \(.*\)","")
    
    GDP = pd.read_csv('datasets/world_bank.csv',skiprows=4)
    GDP['Country Name'] = GDP['Country Name'].replace('Korea, Rep.','South Korea')
    GDP['Country Name'] = GDP['Country Name'].replace('Iran, Islamic Rep.','Iran')
    GDP['Country Name'] = GDP['Country Name'].replace('Hong Kong SAR, China','Hong Kong')
 
    columns = ['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
    
    GDP = GDP[columns]
    GDP.columns = ['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
    
    ScimEn = pd.read_excel('datasets/scimagojr-3.xlsx')
    ScimEn_m = ScimEn[:15]
    
    df = pd.merge(ScimEn, energy, how = 'inner', left_on = 'Country', right_on='Country')
    final_df = pd.merge(df,GDP, how = 'inner', left_on = 'Country', right_on='Country')
    final_df = final_df.set_index('Country')
    columns = ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    ans = final_df[columns]

    df2 = pd.merge(ScimEn, energy, how = 'outer', left_on = 'Country', right_on='Country')
    final_df2 = pd.merge(df2,GDP, how = 'outer', left_on = 'Country', right_on='Country')   

    return len(final_df2) - len(final_df)
 
print(answer_two())





def answer_three():
    # YOUR CODE HERE
    GDP_15 = dff
    GDP_15 = GDP_15[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]#.set_index('Country')
    GDP_15['mean'] = GDP_15.mean(axis=1)
    GDP_15 = GDP_15['mean']
    avgGDP = GDP_15
    return avgGDP

print(answer_three())
print(type(answer_three()))
print(type(answer_three() == pd.Series))   