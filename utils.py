import pandas as pd
from scipy import sparse
# corrMatrix=pd.read_csv("corr_mar.csv")
movies=pd.read_csv("dataset/movies.csv")
links=pd.read_csv("dataset/links.csv")
image=pd.read_csv("dataset/movie_poster.csv",names=["movieId","Image"])

ratings = pd.read_csv('dataset/ratings.csv')


ratings = pd.merge(movies,ratings).drop(['genres','timestamp'],axis=1)
userRatings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating')
userRatings = userRatings.dropna(thresh=10, axis=1).fillna(0,axis=1)
corrMatrix = userRatings.corr(method='pearson')


def get_similar(movie_name,rating):
    similar_ratings = corrMatrix[movie_name]*(rating-2.5)
    # print(similar_ratings)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    #print(type(similar_ratings))
    return similar_ratings

action_lover = [("Four Rooms (1995)",4)]
def recommend(movies):
    similar_movies = pd.DataFrame()
    for movie,rating in movies:
        similar_movies = similar_movies.append(get_similar(movie,rating),ignore_index = True)
    return  similar_movies


# print(similar_movies.sum().sort_values(ascending=False).head(20))
# result=recommend(action_lover).sum().sort_values(ascending=False).head(50)
# result_data=pd.DataFrame(result)
# list_movies=result_data[0].index
# indexs=movies[movies["title"].isin(list_movies)]["movieId"].values
# genrce=movies[movies["movieId"].isin(indexs)]["genres"].values
# print(genrce)

# print(image["Image"][image["movieId"]==1].values[0])


