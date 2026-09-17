"""
Claude's answers to the three questions in questions.md.

    uv run python claude_answers_1_2_3.py

Filled in by a Claude that has never seen the student's work. Kept as it was written.
"""

from load_data import GENRES, load_all

MIN_RATINGS = 20  # threshold used throughout for "enough ratings to trust the mean"


def question_1(ratings_df, movies_df):
    print("=" * 70)
    print("1(a). Basic counts and rating distribution")
    print("=" * 70)
    n_ratings = len(ratings_df)
    n_users = ratings_df["user_id"].nunique()
    n_movies = ratings_df["movie_id"].nunique()
    print(f"{n_ratings:,} ratings, {n_users:,} users, {n_movies:,} movies")

    dist = ratings_df["rating"].value_counts().sort_index()
    print("\nRating distribution:")
    for stars, count in dist.items():
        pct = 100 * count / n_ratings
        print(f"  {stars} star: {count:>6,}  ({pct:5.1f}%)  {'#' * int(pct)}")

    print("\n" + "=" * 70)
    print("1(b). Ratings per user")
    print("=" * 70)
    per_user = ratings_df.groupby("user_id").size()
    median_per_user = per_user.median()
    n_heavy_users = (per_user >= 100).sum()
    print(f"Median ratings per user: {median_per_user}")
    print(f"Users with >= 100 ratings: {n_heavy_users:,} (out of {n_users:,})")

    print("\n" + "=" * 70)
    print("1(c). Ten most-rated movies")
    print("=" * 70)
    merged = ratings_df.merge(movies_df[["movie_id", "title"]], on="movie_id")
    most_rated = merged.groupby("title").size().sort_values(ascending=False).head(10)
    for title, count in most_rated.items():
        print(f"  {count:>4,}  {title}")

    print("\n" + "=" * 70)
    print(f"1(d). Highest mean rating (movies with >= {MIN_RATINGS} ratings)")
    print("=" * 70)
    stats = merged.groupby("title")["rating"].agg(mean="mean", count="count")
    top_rated = stats[stats["count"] >= MIN_RATINGS].sort_values("mean", ascending=False).head(10)
    for title, row in top_rated.iterrows():
        print(f"  {row['mean']:.3f}  ({row['count']:>3.0f} ratings)  {title}")

    return stats  # reused by question 2


def question_2(stats):
    print("\n" + "=" * 70)
    print("2. What is the best movie in this dataset?")
    print("=" * 70)
    qualifying = stats[stats["count"] >= MIN_RATINGS].sort_values(
        ["mean", "count"], ascending=False
    )
    best_title = qualifying.index[0]
    best_mean = qualifying.iloc[0]["mean"]
    best_count = qualifying.iloc[0]["count"]
    print(
        f"'Best' has to mean something more than 'highest raw average': a movie with one\n"
        f"5-star rating would otherwise beat everything. Restricting to movies with at\n"
        f"least {MIN_RATINGS} ratings (same cutoff as 1(d)) and ranking by mean rating gives:\n"
    )
    print(f"  {best_title} -- mean {best_mean:.3f} over {best_count:.0f} ratings")
    print(
        f"\nThat's the answer: {best_title} is the best movie here by consensus "
        "(high average, not just a lucky handful of votes)."
    )


def question_3(ratings_df, movies_df):
    print("\n" + "=" * 70)
    print("3. Which movie is the most Romantic?")
    print("=" * 70)
    print(
        "Interpreting 'most Romantic' as 'most purely a romance' rather than 'best-rated\n"
        "romance movie': many movies tagged Romance are also Comedy, Drama, War, etc., so\n"
        "the genre is diluted. The purest signal is a movie whose *only* genre is Romance.\n"
        f"Among those, break ties with mean rating (requiring >= {MIN_RATINGS} ratings so the\n"
        "average is meaningful)."
    )

    genre_count = movies_df[GENRES].sum(axis=1)
    pure_romance = movies_df[(movies_df["Romance"]) & (genre_count == 1)]
    print(f"\n{len(pure_romance)} movies are tagged Romance and nothing else:")

    merged = ratings_df.merge(pure_romance[["movie_id", "title"]], on="movie_id")
    stats = merged.groupby("title")["rating"].agg(mean="mean", count="count")
    stats = stats.sort_values(["mean", "count"], ascending=False)
    for title, row in stats.iterrows():
        print(f"  {row['mean']:.3f}  ({row['count']:>3.0f} ratings)  {title}")

    qualifying = stats[stats["count"] >= MIN_RATINGS]
    winner = qualifying.index[0] if len(qualifying) else stats.index[0]
    winner_row = stats.loc[winner]
    print(
        f"\nMost Romantic: {winner} -- a pure Romance film, "
        f"mean {winner_row['mean']:.3f} over {winner_row['count']:.0f} ratings."
    )


def claude_answers():
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    stats = question_1(ratings_df, movies_df)
    question_2(stats)
    question_3(ratings_df, movies_df)


if __name__ == "__main__":
    claude_answers()
