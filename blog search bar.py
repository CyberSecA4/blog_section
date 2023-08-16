from flask import Flask, render_template, request
from googlesearch import search

app = Flask(__name__)

# Function to search for the top articles from a specific website based on a query
def search_top_articles(site, query, num_results=10):
    try:
        results = search(query + " site:" + site, num_results=num_results)
        return list(results)
    except Exception as e:
        print("Error searching:", e)
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form['query']
        websites = [
            "https://medium.com/",
            "https://www.analyticsvidhya.com/",
            "https://twitter.com/",
            "https://owasp.org/",
            "https://thehackernews.com/",
            "https://www.hackingarticles.in/",
            "https://null-byte.wonderhowto.com/"
        ]
        for website in websites:
            top_articles = search_top_articles(website, query, num_results=5)
            results.extend(top_articles)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
