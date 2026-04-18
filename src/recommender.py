import pandas as pd

def create_index(df):
    return pd.Series(df.index, index=df['title']).drop_duplicates()

def recommend_movie(title, df, cos_sim, indices, top_n=10):

    if title not in indices:
        return "Movie not found"

    idx = indices[title]

    sim_scores = list(enumerate(cos_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:top_n+1]

    movie_indices = [i[0] for i in sim_scores]

    return df['title'].iloc[movie_indices]