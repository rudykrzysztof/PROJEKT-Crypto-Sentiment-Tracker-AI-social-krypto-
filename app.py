from flask import Flask, jsonify
from sentiment import analyze_sentiment

app = Flask(__name__)

sample_posts = [
    "Bitcoin to the moon!",
    "Huge crash coming",
    "ETH looks strong",
    "Market is dead"
]

@app.route("/api/sentiment")
def sentiment():
    results = []

    for post in sample_posts:
        results.append({
            "text": post,
            "sentiment": analyze_sentiment(post)
        })

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
