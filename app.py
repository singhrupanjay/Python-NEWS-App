from flask import Flask,render_template,request 
import requests
from config import NEWS_API_KEY

#CREATE A FLASK APP
app = Flask(__name__)

# Homepage - Route
@app.route("/")
def index():
    query = request.args.get("query", "latest")
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}'
    #the {query} gets replaced with latest
    response = requests.get(url)
    news_data = response.json()

    articles = news_data.get('articles', [])

    filtered_articles = [article for article in articles if "yahoo" not in article["source"]["name"]  and 'removed'
    not in article["title"].lower()]

    return render_template("index.html", articles = filtered_articles, query=query)
    # first article is variable and 2nd article is value that we created above 

if __name__== "__main__":
    app.run(debug=True)