import urllib
from urllib import urlopen as uReq
import re
import json
import sqlite3

# htmltext = urllib.urlopen("http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/celtics_roster.json")



urls = ['http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/hawks_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/celtics_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/nets_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/hornets_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/bulls_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/cavaliers_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/mavericks_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/nuggets_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/pistons_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/warriors_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/rockets_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/pacers_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/clippers_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/lakers_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/grizzlies_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/heat_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/bucks_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/timberwolves_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/pelicans_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/knicks_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/thunder_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/magic_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/76ers_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/suns_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/kings_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/spurs_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/raptors_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/jazz_roster.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/wizards_roster.json',]

for url in urls:

	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()

	data = json.loads(page_html)

	teamID = data['t']['tid']
	team = data['t']['tn']

	for x in data['t']['pl']:
		PID = x['pid']
		first_name = x['fn']
		last_name = x['ln']
		College_Country = x['hcc']
		height = x['ht']
		weight = x['wt']
		position = x['pos']
		dob = x['dob']
		conn = sqlite3.connect('NBA.db')
		cursor = conn.cursor()
		cursor.execute("INSERT INTO Players VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (PID, first_name, last_name, College_Country, height, weight, position, dob, team, teamID))

		conn.commit()
		cursor.close()
		conn.close() 



