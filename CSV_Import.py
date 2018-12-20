import pandas as pd
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

def nickimportdata():
    playerstatsfile = "nba_2016_2017_100.csv"
    playerstats_df = pd.read_csv(playerstatsfile, encoding="ISO-8859-1")
    playerstats_trimmed_df = playerstats_df[["PLAYER_ID","PLAYER_NAME", "TEAM_ABBREVIATION","TWITTER_HANDLE","ACTIVE_TWITTER_LAST_YEAR"]]
    playerstats_trimmed_df = playerstats_trimmed_df.set_index('PLAYER_ID')
    playerstats_trimmed_df.to_csv("playerstats_trimmed_df.csv", index=False, header=True)
    playerstats_trimmed_df = playerstats_trimmed_df.loc[playerstats_trimmed_df['TWITTER_HANDLE']!='0',:]

    playerstats_trimmed_df.count()

    engine = create_engine('mysql://root:ELD4play@localhost:3306/nba_analysis')
    conn=engine.connect()

    playerstats_trimmed_df.to_sql('playerstats', conn, if_exists='append')
  