import requests

# Configuring
API_KEY = "RGAPI-24c831ec-4a4e-44b2-800b-1dbb4257da3e"  # This will be expired by the time grading is done
SUMMONER_NAME = "blaberfish2" # name of the pro-players account
REGION = "na1" # their region
PLATFORM_ROUTING = "americas" 


def get_headers():
    return {
        "X-Riot-Token": API_KEY
    }

# fetching the puuid
def get_puuid(summoner_name):
    url = f"https://{REGION}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        return response.json()["puuid"]
    else:
        print("Error fetching PUUID:", response.json())
        raise Exception("API call failed — check your API key or summoner name.")


# fetching the last x match ids for given puuid
def get_match_ids(puuid, count=10):
    url = f"https://{PLATFORM_ROUTING}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count}"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching match IDs:", response.json())
        raise Exception("Failed to retrieve match IDs.")

# getting match details against match id
def get_match_details(match_id):
    url = f"https://{PLATFORM_ROUTING}.api.riotgames.com/lol/match/v5/matches/{match_id}"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching match details:", response.json())
        raise Exception("Failed to retrieve match details.")

# extracting useful player statistics from the match details
def extract_player_stats(match_data, target_puuid):
    for participant in match_data['info']['participants']:
        if participant['puuid'] == target_puuid:
            return {
                "champion": participant['championName'],
                "kills": participant['kills'],
                "deaths": participant['deaths'],
                "assists": participant['assists'],
                "kda": (participant['kills'] + participant['assists']) / max(1, participant['deaths']),
                "cs": participant['totalMinionsKilled'] + participant['neutralMinionsKilled'],
                "damage": participant['totalDamageDealtToChampions'],
                "gold_per_min": participant['challenges'].get('goldPerMinute', None),
                "queue_id": match_data['info']['queueId'],  # 420 means ranked solo duo, we are removing other match types (Arena, casual, etc)
                "win": participant['win']
            }
    return None

if __name__ == "__main__":
    try:
        puuid = get_puuid(SUMMONER_NAME)
        match_ids = get_match_ids(puuid, count=10)

        print(f"Collected {len(match_ids)} match IDs.")

        for match_id in match_ids:
            match_data = get_match_details(match_id)
            stats = extract_player_stats(match_data, puuid)

            if stats and stats["queue_id"] == 420:  # only ranked solo duo games
                print(stats)

    except Exception as e:
        print("An error occurred:", str(e))
