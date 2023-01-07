import sqlite3
import pandas as pd

conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()

artists = pd.read_csv('lastfm_artist_list.csv')
users = pd.read_csv('lastfm_user_scrobbles.csv')
users.to_sql('prediction_user', conn, if_exists='replace', index_label='id')
artists.to_sql('prediction_artist', conn, if_exists='replace', index_label='id')