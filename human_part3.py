"""
Part 3: the most ___ movie.

    uv run python human_part3.py

Pick an adjective. Write it on the `**My adjective:**` line of WRITEUP.md and a one-sentence
definition a classmate could code on the `**My definition:**` line. Print the top 5 movies
under it.
"""

from load_data import load_all


def top5_my_definition(ratings, ratings_df, movies, movies_df):
    print("== My definition ==")

    joined = ratings_df.join(movies_df, on="movie_id", rsuffix="_movies")
    grouped = (
        joined.groupby(["movie_id", "title", "Romance"])
        .agg(ratings_count=("rating", "size"), mean_rating=("rating", "mean"))
        .reset_index()
    )

    filtered = grouped.query(
        "ratings_count >= 65 and ratings_count <= 148 and Romance == True"
    )
    print(
        filtered.sort_values(by="mean_rating", ascending=False)
        .head()[["title", "mean_rating"]]
        .to_string(index=False)
    )


def human_part3(ratings, ratings_df, movies, movies_df):
    top5_my_definition(ratings, ratings_df, movies, movies_df)


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part3(ratings, ratings_df, movies, movies_df)
