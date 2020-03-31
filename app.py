from flask import Flask, render_template, request
from tweet_store import TweetStore
from caching import get_github_profile
import json

app = Flask(__name__)
store = TweetStore()

@app.route('/')
def home():
    return render_template('base.html')


@app.route('/twitter-filter')
def twitter_filter():
    tweets = store.tweets()
    return render_template('index.html', tweets=tweets)


@app.route('/redis-caching', methods=['GET', 'POST'])
def caching():
    if request.method == 'POST':
        username = request.form['username']
        user_data = get_github_profile(username)
        # user_data = json.loads(user)
        print("im in post")
        print(type(user_data['profile']))
        return render_template('scrape_form.html', user_data=user_data)
    else:
        print("not in post")
        return render_template('scrape_form.html')


if __name__ == '__main__':
    app.run(debug=True)
