import requests
import pandas as pd
from bs4 import BeautifulSoup
import sqlite3

base_url = 'https://www.trackitdown.net/genre/tech_house_minimal/featured_tracks.html?offset={}'
offset = 0

track_data = []
while True:
    r = requests.get(base_url.format(offset))
    soup = BeautifulSoup(r.text, 'lxml')
    tracks = soup.findAll('div', {'class':'featuredTracks track'})
    conn = sqlite3.connect('Beatscrape.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Tracks(Artist TEXT, Song TEXT, Label TEXT, Price DECIMAL, ChartPosition TEXT, Genre TEXT, Websource TEXT)')
    if len(tracks) == 0:
        break
    for track in tracks:
        genrex = track['data-genre']
        songx = track.find('strong', {'class':'trackTitle'}).text
        artistx = track.find('a', {'class':'artistName'}).text
        labelx = track.find('a', {'class':'labelName'}).text
        pricex = '1.99'
        web_source = 'TrackItDown'
        positionx = '11'
#        track_data.append(track_dict)

        conn = sqlite3.connect('Beatscrape.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Tracks VALUES (?, ?, ?, ?, ?, ?, ?)", (artistx, songx, labelx, pricex, positionx, genrex, web_source))
        conn.commit()
        cursor.close()
        conn.close()


    offset += 20

df = pd.DataFrame(track_data)
