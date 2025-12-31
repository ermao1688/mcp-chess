import requests

CHESS_API_BASE = "https://api.chess.com/pub"

headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 Python/3.10 requests/2.31.0"
}


def get_player_profile(username):
    """Fetches the profile of a chess.com player by username."""
    url = f"{CHESS_API_BASE}/player/{username}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


def get_player_stats(username):
    """Fetches the statistics of a chess.com player by username."""
    url = f"{CHESS_API_BASE}/player/{username}/stats"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
