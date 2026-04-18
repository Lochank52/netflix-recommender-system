from sklearn.feature_extraction.text import TfidfVectorizer

def get_tfidf_matrix(df):
    tfidf = TfidfVectorizer(stop_words='english')
    return tfidf.fit_transform(df['description'])