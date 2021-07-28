# ML-Movies_Recommendation
## Inspiration
Have you ever wonder how **Netflex, Facebook, Amazon** and other social media recommend the content that very fit to your personalize and and preference?
That's is Recommendation engine.They use machine learning algorithm to learn from  experience of the user that interact with the content so they can give user more personalize and satisfaction.
 80% of video views in Netflex is from Netflex's recommendation engine .Netflix’s personalized recommendation algorithms produce $1 billion a year in value from customer retention. So i think it is a good idea if i can built a movie recommendation engine that can give a recommendation to the user in real time that very fit to their taste.

## What it does
 **Recommeder.ai** is a system that we provide **API**  as a Movie recommendation system which mean base on user experience that they have watch and rate to the movie our **API** can understand their preference and give them personalize of taste in real time.  When users make any changes  to their preference then the users taste also update in our API in real time. use this [Link](https://www.postman.com/gold-flare-600073/workspace/postman-visualizer/request/12880035-876d4c61-270f-48e0-a0d9-3c0775f97e5e) to test our **API** in **POSTMAN** and see the result in **Postman Visualizer** in real time when you rate to specific movies. 
## How we built it
  In Order to built that API we have done some importance step like:
- Data Collection: we use datasets from [movielen datasets](https://grouplens.org/datasets/movielens/) 
- Web Scrapping : we use  **beautifulsoaup library** to scrap the poster of the movie to show in postman visualizer.This  [Note Book](https://gist.github.com/seabnavin19/887350abe981f95e7ebd2a922507a06e) I use to scrap the poster of specific movie.
- Data preprocessing and preparation: The most importance part of this recommendation engine is that we need to find the correlation between user rating and movies.
```python
ratings = pd.merge(movies,ratings).drop(['genres','timestamp'],axis=1)
userRatings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating')
userRatings = userRatings.dropna(thresh=10, axis=1).fillna(0,axis=1)
corrMatrix = userRatings.corr(method='pearson')
```
See all the code in [GitHub Repo](https://github.com/seabnavin19/ML-Movies_Recommendation/blob/main/utils.py) .And after that we can make a recommendation to user base on the correlation table between user and movies.

- Model Deployment: It is also one of the most importance step in this project. After we build a model we really need to deploy our model as an API that can be use and test by other webapp or mobile application.we choose **Flask**to deploy the model for this project because  is an easy and fastest way to deploy any ML model as an API.  [code of flask server](https://github.com/seabnavin19/ML-Movies_Recommendation/blob/main/server.py)
- API testing and Visualizing: After we deploy our model as an **API** we need to test it in real time to see the performance of our model **Postman** is the best tool that we can use for free. Like a quote said  "Picture speak louder than words" so it is very importance to visualize our model we use **Postman Visualizer**.


## Challenges we ran into
The 2 main problems for us are speed and the size of our model and API. Speed is very importance if we want to make a recommendation system but for us we have some problem with the speed of the model because with millions of data we try to find the correlation each time. But we can solve it by save the correlation table as csv file so don't need to run the correlation each time we recommend for user.

## Accomplishments that we're proud of
 The biggest success of this project we can hand on machine leaning algorithm and learn a lot about recommendation engine.
**Recommendation engine**  is a billion dollars project so I am really proud that I can have an experience on that and looking forward to  improve the knowledge on that and also machine learning field.
## What we learned
What we have learned from this project are:
- We can hand on to built a ML model from Data collection to Model deployment and API testing
- we have learn Recommendation engine which is a billion dollars project
- We have learn that in order to make an AI product is not just about model building but we need to deploy it and test it to see the performance.
- we learn and work on Visualizer tools in postman

## What's next for Recommender.ai
Our future plan we want to expand our system to implement in real business which we provide the recommendation engine as an API to our customer to implement that on their ecomerce,websites to improve their content and user experience. 
