# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:55:55 2023

@author: user
"""

import requests 
import pandas as pd
from bs4 import BeautifulSoup


data_EPL = {
    'date': [],
    'comp': [],
    'round': [],
    'dayofweek': [],
    'venue': [],
    'result': [],
    'goals_for': [],
    'goals_against': [],
    'opponent': [],
    'xg_for': [],
    'xg_against': [],
    'possession': [],
    'captain': [],
    'formation': [],
    'referee': [],
    'Team': [],
}
url="https://fbref.com/en/comps/9/2022-2023/2022-2023-Premier-League-Stats"
page=requests.get(url)
src=page.content
soup=BeautifulSoup(src,"lxml")
table = soup.find('table', {'id': 'results2022-202391_overall'})
resultat=table.contents[7]

for tr_tag in resultat.find_all('tr') :
    team=tr_tag.find("td",{'data-stat':'team'}).find('a').text
    team_url ='https://fbref.com'+ tr_tag.find("td",{'data-stat':'team'}).find('a')['href']
    page_team=requests.get(team_url)
    soup_team=BeautifulSoup(page_team.content,"lxml")
    table_team=soup_team.find('table',{'id':'matchlogs_for'})
    res_team=table_team.contents[7]
    for tr__tag in res_team.find_all('tr') :
        comp=tr__tag.find("td",{'data-stat':'comp'})
        if comp.text=='Premier League' :
            date=tr__tag.find("td",{'data-stat':'start_time'}).text
            data_EPL['date'].append(date)
            comp=tr__tag.find("td",{'data-stat':'comp'}).text
            data_EPL['comp'].append(comp)
            rouund=tr__tag.find("td",{'data-stat':'round'}).text
            data_EPL['round'].append(rouund)
            dayofweek=tr__tag.find("td",{'data-stat':'dayofweek'}).text
            data_EPL['dayofweek'].append(dayofweek)
            venue=tr__tag.find("td",{'data-stat':'venue'}).text
            data_EPL['venue'].append(venue)
            result=tr__tag.find("td",{'data-stat':'result'}).text
            data_EPL['result'].append(result)
            goals_for=tr__tag.find("td",{'data-stat':'goals_for'}).text
            data_EPL['goals_for'].append(goals_for)
            goal_against=tr__tag.find("td",{'data-stat':'goals_against'}).text
            data_EPL['goals_against'].append(goal_against)
            oppenent=tr__tag.find("td",{'data-stat':'opponent'}).text
            data_EPL['opponent'].append(oppenent)
            xg_for=tr__tag.find("td",{'data-stat':'xg_for'}).text
            data_EPL['xg_for'].append(xg_for)
            xg_against=tr__tag.find("td",{'data-stat':'xg_against'}).text
            data_EPL['xg_against'].append(xg_against)
            possession=tr__tag.find("td",{'data-stat':'possession'}).text
            data_EPL['possession'].append(possession)
            captain=tr__tag.find("td",{'data-stat':'captain'}).text
            data_EPL['captain'].append(captain)
            formation=tr__tag.find("td",{'data-stat':'formation'}).text
            data_EPL['formation'].append(formation)
            referee=tr__tag.find("td",{'data-stat':'referee'}).text
            data_EPL['referee'].append(referee)
            data_EPL['Team'].append(team)


            
            

            
    
    

