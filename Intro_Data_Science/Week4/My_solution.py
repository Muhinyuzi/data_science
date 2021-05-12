cities=pd.read_html("assets/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]
cities = cities.rename(columns={'Population (2016 est.)[8]':'Population'})
cities = cities[['Metropolitan area','Population','NHL']]
cities['NHL'] = cities['NHL'].str.replace("\[.*\]","")
cities['NHL'] = cities['NHL'].replace("",np.nan).replace("—",np.nan)
cities = cities.dropna()

nhl_df=pd.read_csv("assets/nhl.csv")
nhl_df = nhl_df[nhl_df['year'] == 2018]
nhl_df = nhl_df[['team','W','L']]
nhl_df = nhl_df.drop([0,9,18,26])
nhl_df['team'] = nhl_df['team'].str.replace(r'\*',"")
nhl_df['team'] = nhl_df['team'].str.replace('[\w.]* ','')    
nhl_df = nhl_df.astype({'team': str,'W': int, 'L': int})
nhl_df['W/L%'] = nhl_df['W']/(nhl_df['W']+nhl_df['L'])




team_df = cities['NHL'].str.extract('([A-Z]{1}[a-z]*\s[A-Z]{0,1}[a-z]*|[A-Z]{0,1}[a-z]*)([A-Z]{1}[a-z]*\ [A-Z]{0,1}[a-z]*|[A-Z]{0,1}[a-z]*)([A-Z]{1}[a-z]*\ [A-Z]{0,1}[a-z]*|[A-Z]{0,1}[a-z]*)')
team_df['Metropolitan area']=cities['Metropolitan area']
team_df = pd.melt(team_df, id_vars=['Metropolitan area']).drop(columns=['variable']).reset_index().rename(columns = {"value":"team"})
team_df=pd.merge(team_df,cities,how='left',on = 'Metropolitan area')
team_df = team_df.astype({'Metropolitan area': str, 'team': str, 'Population': int})
team_df['team']=team_df['team'].str.replace('[\w.]*\ ','')
    

    
final=pd.merge(team_df,nhl_df,'outer', on = 'team')
final=final.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})
    
population_by_region = final['Population']
win_loss_by_region = final['W/L%'] 
print(stats.pearsonr(population_by_region, win_loss_by_region)[0])
print(len(population_by_region))


nba_df=pd.read_csv("assets/nba.csv")
cities=pd.read_html("assets/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]

cities = cities.rename(columns={'Population (2016 est.)[8]':'Population'})
cities = cities[['Metropolitan area','Population','NBA']]
cities['NBA'] = cities['NBA'].str.replace("\[.*\]","")
cities['NBA'] = cities['NBA'].replace("",np.nan).replace("—",np.nan)
cities = cities.dropna()
#print(cities['NBA'])
#team = cities['NBA'].str.extract('([A-Z]{0,1}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)')
team = cities['NBA'].str.extract('([A-Z]{0,1}[a-z0-9]*\ [A-Z]{0,1}[a-z0-9]*|[A-Z]{0,1}[a-z0-9]*)([A-Z]{1}[a-z]*\ [A-Z]{0,1}[a-z]*|[A-Z]{0,1}[a-z]*)')
#print(cities['NBA'])
nba_df = nba_df[nba_df['year'] == 2018]
print(nba_df.head())
nba_df['team'] = nba_df['team'].str.replace(r'\(.*\)',"")
nba_df['team'] = nba_df['team'].str.replace(r'\*',"")
nba_df['team'] = nba_df['team'].str.replace(r'[\xa0]',"")
nba_df = nba_df[['team','W/L%']]
nba_df['team'] = nba_df['team'].str.replace('[\w.]* ','')
nba_df = nba_df.astype({'team': str, 'W/L%': float})
print(nba_df.head(40))
#

team_df = cities['NBA'].str.extract('([A-Z]{0,1}[a-z0-9]*\ [A-Z]{0,1}[a-z0-9]*|[A-Z]{0,1}[a-z0-9]*)([A-Z]{1}[a-z]*\ [A-Z]{0,1}[a-z]*|[A-Z]{0,1}[a-z]*)')
team_df['Metropolitan area']=cities['Metropolitan area']
team_df = pd.melt(team_df, id_vars=['Metropolitan area']).drop(columns=['variable']).reset_index().rename(columns = {"value":"team"})
team_df=pd.merge(team_df,cities,how='left',on = 'Metropolitan area')
team_df = team_df.astype({'Metropolitan area': str, 'team': str, 'Population': int})
team_df['team']=team_df['team'].str.replace('[\w.]*\ ','')
final=pd.merge(team_df,nba_df,'outer', on = 'team')
print(final)
final=final.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})
print(final.head())
population_by_region = final['Population'] # pass in metropolitan area population from cities
win_loss_by_region = final['W/L%']
print(stats.pearsonr(population_by_region, win_loss_by_region))



mlb_df=pd.read_csv("assets/mlb.csv")
#print(mlb_df)
cities=pd.read_html("assets/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]
cities = cities.rename(columns={'Population (2016 est.)[8]':'Population'})
cities = cities[['Metropolitan area','Population','MLB']]
cities['MLB'] = cities['MLB'].str.replace("\[.*\]","")
cities['MLB'] = cities['MLB'].replace("",np.nan).replace("—",np.nan)
cities = cities.replace("",np.nan).replace("—",np.nan)
cities = cities.dropna()
#print(cities)

mlb_df=pd.read_csv("assets/mlb.csv")
mlb_df = mlb_df[mlb_df['year'] == 2018]
mlb_df['team'] = mlb_df['team'].str.replace(r'[\*]',"")
mlb_df['team'] = mlb_df['team'].str.replace(r'\(\d*\)',"")
mlb_df['team'] = mlb_df['team'].str.replace(r'[\xa0]',"")
mlb_df = mlb_df[['team','W-L%']]
mlb_df = mlb_df.rename(columns={'W-L%':'W/L%'})
mlb_df['team'] = mlb_df['team'].str.replace('[\w.]* ','')
mlb_df = mlb_df.astype({'team': str, 'W/L%': float})
print(mlb_df['team'])




team_df = cities['MLB'].str.extract('([A-Z]{0,1}[a-z0-9]*\ [A-Z]{0,1}[a-z0-9]*|[A-Z]{0,1}[a-z0-9]*)([A-Z]{1}[a-z]*\ [A-Z]{0,1}[a-z]*|[A-Z]{0,1}[a-z]*)')
team_df['Metropolitan area']=cities['Metropolitan area']
team_df = pd.melt(team_df, id_vars=['Metropolitan area']).drop(columns=['variable']).reset_index().rename(columns = {"value":"team"})
team_df=pd.merge(team_df,cities,how='left',on = 'Metropolitan area')
team_df = team_df.astype({'Metropolitan area': str, 'team': str, 'Population': int})
print(team_df)
team_df['team']=team_df['team'].str.replace('[\w.]*\ ','')


    
final=pd.merge(team_df,mlb_df,'outer', on = 'team')
final=final.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})
print(final)

#raise NotImplementedError()
    
population_by_region = final['Population'] # pass in metropolitan area population from cities
win_loss_by_region = final['W/L%']
print(stats.pearsonr(population_by_region, win_loss_by_region))
print(len(population_by_region))


nfl_df=pd.read_csv("assets/nfl.csv")
cities=pd.read_html("assets/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]
cities = cities.rename(columns={'Population (2016 est.)[8]':'Population'})
cities = cities[['Metropolitan area','Population','NFL']]
cities['NFL'] = cities['NFL'].str.replace("\[.*\]","")
cities['NFL'] = cities['NFL'].str.replace("\—","")
cities['NFL'] = cities['NFL'].replace("",np.nan).replace("—",np.nan)
cities = cities.replace(" ",np.nan).replace("—",np.nan)
cities = cities.dropna()
print(cities['NFL'])


nfl_df=pd.read_csv("assets/nfl.csv")
nfl_df = nfl_df[nfl_df['year'] == 2018]
nfl_df['team'] = nfl_df['team'].str.replace(r'[\*]',"")
nfl_df['team'] = nfl_df['team'].str.replace(r'[\+]',"")
nfl_df['team'] = nfl_df['team'].str.replace(r'\(\d*\)',"")
nfl_df['team'] = nfl_df['team'].str.replace(r'[\xa0]',"")
nfl_df = nfl_df.rename(columns={'W-L%':'W/L%'})
nfl_df = nfl_df[['team','W/L%']]
print(nfl_df)
i = 0
list_to_drop = []
while i < 36:
    #droplist = []
    list_to_drop.append(i)
    i+=5
nfl_df = nfl_df.drop(list_to_drop)
nfl_df = nfl_df.astype({'team': str, 'W/L%': float})
nfl_df['team'] = nfl_df['team'].str.replace('[\w.]*\ ','')
#print(nfl_df)

#print(nfl_df)


team_df = cities['NFL'].str.extract('([A-Z]{0,1}[a-z0-9]*\ [A-Z]{0,1}[a-z0-9]*|[A-Z]{0,1}[a-z0-9]*)([A-Z]{1}[a-z]*\ [A-Z]{0,1}[a-z]*|[A-Z]{0,1}[a-z]*)')
team_df['Metropolitan area']=cities['Metropolitan area']
team_df = pd.melt(team_df, id_vars=['Metropolitan area']).drop(columns=['variable']).reset_index().rename(columns = {"value":"team"})
team_df=pd.merge(team_df,cities,how='left',on = 'Metropolitan area')
team_df = team_df.astype({'Metropolitan area': str, 'team': str, 'Population': int})
team_df['team']=team_df['team'].str.replace('[\w.]*\ ','')



final=pd.merge(team_df,nfl_df,'outer', on = 'team')
final=final.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})

#raise NotImplementedError()
    
population_by_region = final['Population'] # pass in metropolitan area population from cities
win_loss_by_region = final['W/L%']
print(stats.pearsonr(population_by_region, win_loss_by_region))



def test_columns(alpha=0.1):
    # I want to keep track of how many differ
    num_diff=0
    # And now we can just iterate over the columns
    for col in df1.columns:
    # we can run out ttest_ind between the two dataframes
    teststat,pval=ttest_ind(df1[col],df2[col])
    # and we check the pvalue versus the alpha
    if pval<=alpha:
        # And now we'll just print out if they are different and increment␣
        the num_diff
        print("Col {} is statistically significantly different at alpha={},pval={}".format(col,alpha,pval))
        num_diff=num_diff+1
    # and let's print out some summary stats
    print("Total number different was {}, which is {}%".format(num_diff,float(num_diff)/len(df1.columns)*100))
    # And now lets actually run this
test_columns()