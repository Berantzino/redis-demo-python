from flask import Flask, render_template, request
from tweet_store import TweetStore
from caching import get_github_profile
import json

app = Flask(__name__)
store = TweetStore()


@app.route('/twitter-filter')
def index():
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


@app.route('/redis-caching/user', methods=['GET', 'POST'])
def github_user():
    if request.method == 'POST':
        username = request.form['username']
        user = get_github_profile(username)
        print("im in post")
        return render_template('github_profile.html', user=user)
    else:
        print("im not in post")
        return render_template('github_profile.html')


if __name__ == '__main__':
    app.run(debug=True)
