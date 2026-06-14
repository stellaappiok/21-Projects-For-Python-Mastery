import requests


def get_scoreboard():
    url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"

    data = requests.get(url, timeout=10).json()

    events = data.get("events", [])

    print("\nNBA SCOREBOARD\n")

    if not events:
        print("No games today.")
        return

    for game in events:
        comp = game["competitions"][0]
        status = comp["status"]["type"]["description"]

        home = comp["competitors"][0]
        away = comp["competitors"][1]

        home_team = home["team"]["abbreviation"]
        away_team = away["team"]["abbreviation"]

        home_score = home["score"]
        away_score = away["score"]

        print("-" * 40)
        print(f"{away_team} {away_score} - {home_score} {home_team}")
        print(status)


get_scoreboard()
