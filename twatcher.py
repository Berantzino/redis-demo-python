from flask import Flask, render_template, request
from tweet_store import TweetStore

app = Flask(__name__)
store = TweetStore()


@app.route('/twitter-filter')
def index():
    tweets = store.tweets()
    return render_template('index.html', tweets=tweets)

@app.route('/redis-caching', methods=['GET', 'POST'])
def caching():
    if request.method == 'POST':
        pass
    return render_template('scrape_form.html')


if __name__ == '__main__':
    app.run(debug=True)
