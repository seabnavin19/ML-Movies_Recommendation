from flask import Flask,jsonify,json,request
from utils import *
app=Flask(__name__)


@app.route("/",methods=["GET"])
def home():
    base_link = "https://www.themoviedb.org/movie/"
    image_link="https://st3.depositphotos.com/1005979/13618/i/600/depositphotos_136182400-stock-photo-coming-soon-words-movie-clapper.jpg"
    movies_re=movies.head(50)
    links_re=links["tmdbId"][movies_re["movieId"].index]
    # print(links_re.values[0])

    movies_result = [{"Title": movies_re["title"].values[i], "genres": movies_re["genres"].values[i], "link":base_link+str(int(links_re[i])),"image":image["Image"][image["movieId"]==i].values[0] if len(image["Image"][image["movieId"]==i].values)>0 else image_link} for i
                     in range(len(movies_re))]
    return jsonify(Movies=movies_result)
@app.route("/predict", methods=['GET',"POST"])
def predict():
        image_link="https://st3.depositphotos.com/1005979/13618/i/600/depositphotos_136182400-stock-photo-coming-soon-words-movie-clapper.jpg"
        base_link="https://www.themoviedb.org/movie/"
        mo=request.get_json()["movies"]
        mo1=[tuple(i) for i in mo]
        # print(mo1)
        result = recommend(mo).sum().sort_values(ascending=False).head(50)
        result_data = pd.DataFrame(result)
        list_movies = result_data[0].index

        indexs = movies[movies["title"].isin(list_movies)]["movieId"].values
        genres=[]
        link_movies=[]
        image_movies=[]
        for i in indexs:
            genres.append(movies["genres"][movies["movieId"]==i].values[0])
            link_movies.append(links["tmdbId"][links["movieId"]==i].values[0])
            if len(image["Image"][image["movieId"]==i].values)>0:
                image_movies.append(image["Image"][image["movieId"]==i].values[0])
            else:
                image_movies.append(image_link)

        movies_result=[{"Title":list_movies[i],"genres":genres[i],"link":base_link+str(int(link_movies[i])),"Image":image_movies[i]} for i in range(len(list_movies))]
        return jsonify(Movies=movies_result)


if __name__=="__main__":
    app.run(debug=True)