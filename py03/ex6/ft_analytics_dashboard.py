PLAYERS: list = [
    {"name": "alice",   "score": 2300, "level": 15,
     "status": "active",   "region": "north"},
    {"name": "bob",     "score": 1800, "level": 8,
     "status": "active",   "region": "east"},
    {"name": "charlie", "score": 2150, "level": 12,
     "status": "active",   "region": "central"},
    {"name": "diana",   "score": 2050, "level": 11,
     "status": "inactive", "region": "north"},
    {"name": "eve",     "score": 950,  "level": 4,
     "status": "inactive", "region": "east"},
    {"name": "frank",   "score": 1400, "level": 7,
     "status": "active",   "region": "central"},
]

ACHIEVEMENTS: list = [
    {"player": "alice",   "badge": "first_kill"},
    {"player": "alice",   "badge": "boss_slayer"},
    {"player": "alice",   "badge": "level_10"},
    {"player": "alice",   "badge": "treasure_hunter"},
    {"player": "alice",   "badge": "speed_run"},
    {"player": "bob",     "badge": "first_kill"},
    {"player": "bob",     "badge": "level_10"},
    {"player": "bob",     "badge": "survivor"},
    {"player": "charlie", "badge": "boss_slayer"},
    {"player": "charlie", "badge": "first_kill"},
    {"player": "charlie", "badge": "level_10"},
    {"player": "charlie", "badge": "treasure_hunter"},
    {"player": "charlie", "badge": "speed_run"},
    {"player": "charlie", "badge": "survivor"},
    {"player": "charlie", "badge": "dragon_slayer"},
    {"player": "diana",   "badge": "first_kill"},
    {"player": "diana",   "badge": "level_10"},
    {"player": "diana",   "badge": "survivor"},
    {"player": "eve",     "badge": "first_kill"},
    {"player": "frank",   "badge": "first_kill"},
    {"player": "frank",   "badge": "level_10"},
]


if __name__ == "__main__":
    try:
        print("=== Game Analytics Dashboard ===")

        print("\n=== List Comprehension Examples ===")

        high_scorers: list = [
            p["name"] for p in PLAYERS if p["score"] > 2000
        ]
        print(f"High scorers (>2000): {high_scorers}")

        scores_doubled: list = [
            p["score"] * 2 for p in PLAYERS if p["status"] == "active"
        ]
        print(f"Scores doubled (active): {scores_doubled}")

        active_players: list = [
            p["name"] for p in PLAYERS if p["status"] == "active"
        ]
        print(f"Active players: {active_players}")

        print("\n=== Dict Comprehension Examples ===")

        player_scores: dict = {
            p["name"]: p["score"] for p in PLAYERS
        }
        print(f"Player scores: {player_scores}")

        score_categories: dict = {
            "high":   len([p for p in PLAYERS if p["score"] > 2000]),
            "medium": len([p for p in PLAYERS if 1000 < p["score"] <= 2000]),
            "low":    len([p for p in PLAYERS if p["score"] <= 1000]),
        }
        print(f"Score categories: {score_categories}")

        achievement_counts: dict = {
            p["name"]:
            len([a for a in ACHIEVEMENTS if a["player"] == p["name"]])
            for p in PLAYERS
        }
        print(f"Achievement counts: {achievement_counts}")

        print("\n=== Set Comprehension Examples ===")

        unique_players: set = {
            a["player"] for a in ACHIEVEMENTS
        }
        print(f"Unique players: {unique_players}")

        unique_achievements: set = {
            a["badge"] for a in ACHIEVEMENTS
        }
        print(f"Unique achievements: {unique_achievements}")

        active_regions: set = {
            p["region"] for p in PLAYERS if p["status"] == "active"
        }
        print(f"Active regions: {active_regions}")

        print("\n=== Combined Analysis ===")

        total_players: int = len(unique_players)
        total_achievements: int = len(unique_achievements)

        all_scores: list = [p["score"] for p in PLAYERS]
        average_score: float = sum(all_scores) / len(all_scores)

        top_name: str = max(player_scores, key=lambda n: (
            player_scores[n], achievement_counts[n]
        ))
        top_score: int = player_scores[top_name]
        top_badges: int = achievement_counts[top_name]

        print(f"Total players: {total_players}")
        print(f"Total unique achievements: {total_achievements}")
        print(f"Average score: {average_score}")
        print(
            f"Top performer: {top_name} "
            f"({top_score} points, {top_badges} achievements)"
        )
    except Exception as e:
        print(e)
