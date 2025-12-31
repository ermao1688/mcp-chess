from chess.chess_api import get_player_profile, get_player_stats
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Chess.com")


@mcp.tool()
def get_chess_player_profile(username: str) -> dict:
    """Fetches the profile of a chess.com player by username."""
    from chess.chess_api import get_player_profile
    return get_player_profile(username)


@mcp.tool()
def get_chess_player_stats(username: str) -> dict:
    """Fetches the statistics of a chess.com player by username."""
    from chess.chess_api import get_player_stats
    return get_player_stats(username)


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
