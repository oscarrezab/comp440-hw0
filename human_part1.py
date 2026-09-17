"""
Part 1: basic rating statistics.

    uv run python human_part1.py

Answer the four questions below with your own code, print each answer under its label, and
explain each in one sentence in WRITEUP.md.
"""

from load_data import load_all


def human_part1(ratings, ratings_df, movies, movies_df, users, users_df):
    print("== (a) ==")
    # (a) How many ratings, users, and movies are there, and how are ratings distributed across 1-5 stars?
    print(f"No. of ratings: {len(ratings)}")
    print(f"No. of users: {len(users)}")
    print(f"No. of movies: {len(movies)}")
    print(f"Ratings distribution:")
    print(ratings_df.groupby("rating").size().to_string())

    print("\n== (b) ==")
    # (b) What is the median number of ratings per user, and how many users have 100 or more ratings?
    ratings_by_user = ratings_df.groupby("user_id").size()
    print(f"Median number of ratings per user: {ratings_by_user.quantile([0.5, 0.75])}")

    more_than_100 = ratings_by_user.ge(100)
    print(
        f"Number of users with 100 or more ratings: {len(ratings_by_user[more_than_100])}"
    )

    print("\n== (c) ==")
    # (c) Join ratings to titles. Which 10 movies have the most ratings?
    joined = ratings_df.join(movies_df, on="movie_id", rsuffix="_movies")
    grouped = (
        joined.groupby(["movie_id", "title"])
        .agg(ratings_count=("rating", "size"), mean_rating=("rating", "mean"))
        .reset_index()
    )
    print("Top 10 movies with the most ratings:")
    print(
        grouped.sort_values(by="ratings_count", ascending=False)["title"]
        .head(10)
        .to_string(index=False)
    )

    print("\n== (d) ==")
    # (d) Among movies with at least 20 ratings, which 10 have the highest mean rating?
    #     Show title, mean, and count.
    more_than_20 = grouped[grouped["ratings_count"] >= 20]
    print("Top 10 movies with highest rating and at least 20 ratings:")
    print(
        more_than_20.sort_values(by="mean_rating", ascending=False)
        .head(10)[["title", "mean_rating", "ratings_count"]]
        .to_string(index=False)
    )


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part1(ratings, ratings_df, movies, movies_df, users, users_df)
