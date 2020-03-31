import re


class Tweet:

    def __init__(self, data):
        self.data = data

    def user_link(self):
        return f"http://twitter.com/{self.data['username']}"

    def filtered_text(self):
        return self.filter_brands(self.filter_urls(self.data['text']))

    def filter_brands(self, text):
        brands = ["COVID19", "BTC", "USD", "@CocaCola", "@realDonaldTrump"]

        for brand in brands:
            if brand.lower() in text.lower():
                text = text.replace(brand, f"<mark>{brand}</mark>")
            else:
                continue

        return text

    def filter_urls(self, text):
        return re.sub("(https?:\/\/\w+(\.\w+)+(\/[\w\+\-\,\%]+)*(\?[\w\[\]]+(=\w*)?(&\w+(=\w*)?)*)?(#\w+)?)",
                      r'<a href="\1" target="_blank">\1</a>', text)