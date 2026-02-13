import json
import requests
import streamlit as st
from datetime import date 

today = date.today().isoformat()

#Token key
headers ={"X-Auth-token":"fce51d9ca003472a8462356d809538c7"}

st.title("Football Statistics and Winning probability")
#url for the champions league
url_Champions = "https://api.football-data.org/v4/competitions/CL/teams"
response_Champions = requests.get(url_Champions, headers = headers)
data_champions = response_Champions.json()

#url for games playing today
url_today_matches = "https://api.football-data.org/v4/matches"
response_today_matches = requests.get(url_today_matches, headers = headers)

data_today_matches = response_today_matches.json()

#Displaying matches playing today
if response_today_matches.status_code == 200:
    try:
        data_today_matches = response_today_matches.json()
    except ValueError:
        print("Erro: Response was not valid JSON")
        exit

    matches = data_today_matches.get("matches", [])
    if not matches:
        st.write("No matches found today")
    else:
        for match in matches:
            home = match["homeTeam"]["name"]
            away = match["awayTeam"]["name"]
            competition = match["competition"]["name"]
            status = match["status"]
            match_time = match["utcDate"]
            home_score = match["score"]["fullTime"]["home"]
            away_score = match["score"]["fullTime"]["away"]

            if match["status"] is not None and (home_score and away_score) is not None :
                st.write(f"[{competition}] {home} {home_score} - {away_score} {away} -{status} ({match_time})")
            else:
                st.write(f"[{competition}] {home} VS {away} - {status} ({match_time})")

else:
    st.write("Error fetching data:", response_today_matches.text)

"""
if response_Champions.status_code == 200:
    for team in data_champions["teams"]:
        st.write(team["id"], "-", team["name"])
else:
    st.write("error status_code", response_Champions.status_code)
"""