import pandas as pd
import requests
import numpy as np
import re
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib.colors as col
import scipy.stats as stats
import seaborn as sns

# List of seasons I wish to scrap
seasons = ['20192020', '20182019', '20172018', '20162017', '20152016']

# Setup our DataFrame
matchs = pd.DataFrame(columns=['Rang', 'Unnamed: 1', 'Team', 'Matches',
                                'V', 'N', 'D', 'Buts', '+/-', 'Points', 'saison'])
buteurs = pd.DataFrame(columns=['index', 'Nom', 'Unnamed: 1', 'Team', 'Pos.', 'Matches',
                                'Buts', 'Penalties', 'Taux', 'saison'])
passeurs = pd.DataFrame(columns=['index', 'Nom', 'Unnamed: 1', 'Team', 'Pos.', 'Matches',
                                'Assists', 'Taux', 'saison'])

# Scrap the sfl website for data
for x in seasons:
    url = 'https://www.sfl.ch/fr/statistiques-archives/archives/super-league/archives-des-saisons/{}/'.format(x)
    html = requests.get(url).content
    df1 = pd.read_html(html)[0]
    df1['saison'] = x
    matchs = matchs.append(df1, ignore_index = True)

    url = 'https://www.sfl.ch/fr/statistiques-archives/superleague/joueurs/classement-des-buteurs/league/super-league-{}/'.format(x)
    html = requests.get(url).content
    df2 = pd.read_html(html)[0]
    df2 = df2.reset_index()
    df2['saison'] = x
    buteurs = buteurs.append(df2, ignore_index = True)

    url = 'https://www.sfl.ch/fr/statistiques-archives/superleague/joueurs/classement-des-passeurs/league/super-league-{}/'.format(x)
    html = requests.get(url).content
    df3 = pd.read_html(html)[0]
    df3 = df3.reset_index()
    df3['saison'] = x
    passeurs = passeurs.append(df3, ignore_index = True)


# Clean the scrapped data
matchs['Team'] = matchs['Team'].str.findall('[A-Z]{2,3}$').str[0]
buteurs['Team'] = buteurs['Team'].str.findall('[A-Z]{2,3}$').str[0]
passeurs['Team'] = passeurs['Team'].str.findall('[A-Z]{2,3}$').str[0]


# Compute W/L ratio
matchs['W/L'] = matchs['V'].astype(int) / matchs['Matches'].astype(int)
matchs = matchs[['Team', 'Rang', 'saison', 'W/L']]


# Get average ranking by team for best scorers
buteurs = buteurs.rename(columns = {'Buts': 'scorers',
                                    'index': 'Rank_scorers'})
buteurs['Rank_scorers'] = buteurs['Rank_scorers'].astype(int)+1
buteurs['scorers'] = buteurs['scorers'].astype(int)
buteurs = buteurs[['Team', 'saison', 'scorers', 'Rank_scorers']].groupby(['saison', 'Team']).mean()
#

# Get average ranking by team for best setters
passeurs = passeurs.rename(columns = {'Assists': 'setters',
                                      'index': 'Rank_setters'})
passeurs['Rank_setters'] = passeurs['Rank_setters'].astype(int)+1
passeurs['setters'] = passeurs['setters'].astype(int)
passeurs = passeurs[['Team', 'saison', 'setters', 'Rank_setters']].groupby(['saison', 'Team']).mean()

# Merge all the datasets
final = matchs.merge(buteurs, 'left', on=['Team', 'saison']).merge(passeurs, 'left', on=['Team', 'saison'])
# NaN mean no players made it into the ranking, assign zero
final['scorers'] = final['scorers'].fillna(0)
final['setters'] = final['setters'].fillna(0)
final['Rank_scorers'] = final['Rank_scorers'].fillna((final['Rank_scorers'].max()+1))
final['Rank_setters'] = final['Rank_setters'].fillna((final['Rank_setters'].max()+1))



# Compute a simple correlation
scorers = stats.pearsonr(final['W/L'], final['scorers'])
setters = stats.pearsonr(final['W/L'], final['setters'])

fig, (ax1, ax2) = plt.subplots(2)

sns.regplot(final['W/L'], final['scorers'], color = "#beaed4", ax = ax1)
sns.regplot(final['W/L'], final['setters'], color = '#7fc97f', ax = ax2)

ax1.set_xticks([])
ax1.set_xlabel('')
ax1.set_ylabel('Average scorers\nperformance (n goals)')
ax2.set_ylabel('Average setters\nperformance (n assists)')

fig.suptitle("W/L ratio of super league teams against players performance\n(2015-2020)")




#1b9e77
#7570b3
