import sys

if __name__ == "__main__":

    try:
        print("=== Player Score Analytics ===")
        count = len(sys.argv)
        if count == 1:
            raise ValueError("No scores provided. Usage: python3 "
                             "ft_score_analytics.py <score1> <score2> ...")
        else:
            i = 1
            scores = []
            while i < count:
                try:
                    scores += [int(sys.argv[i])]
                except ValueError:
                    raise ValueError(f"{sys.argv[i]} is not an integer")
                i += 1

        print(f"Scores processed: {scores}")
        print(f"Total players: {count - 1}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / (count - 1)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")

    except Exception as e:
        print(e)
