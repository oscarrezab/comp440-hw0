"""
Part 2: the best movie.

    uv run python human_part2.py

Write your rule on the `**My rule:**` line of WRITEUP.md. Print the top 10 movies (id, title,
ratings count, mean rating) under it.
"""

from load_data import load_all


def top10_my_rule(ratings, ratings_df, movies, movies_df):
    print("== My rule ==")

    joined = ratings_df.join(movies_df, on="movie_id", rsuffix="_movies")
    grouped = (
        joined.groupby(["movie_id", "title"])
        .agg(ratings_count=("rating", "size"), mean_rating=("rating", "mean"))
        .reset_index()
    )

    filtered = grouped.query("ratings_count >= 65 and ratings_count <= 148")
    print(
        filtered.sort_values(by="mean_rating", ascending=False)
        .head(10)[["title", "mean_rating"]]
        .to_string(index=False)
    )


def human_part2(ratings, ratings_df, movies, movies_df):
    top10_my_rule(ratings, ratings_df, movies, movies_df)


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part2(ratings, ratings_df, movies, movies_df)
