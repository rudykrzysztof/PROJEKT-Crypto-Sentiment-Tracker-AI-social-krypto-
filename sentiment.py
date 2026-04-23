def analyze_sentiment(text):
    positive_words = ["moon", "bull", "pump", "win"]
    negative_words = ["dump", "crash", "loss", "bear"]

    score = 0

    for word in positive_words:
        if word in text.lower():
            score += 1

    for word in negative_words:
        if word in text.lower():
            score -= 1

    if score > 0:
        return "BULLISH 🟢"
    elif score < 0:
        return "BEARISH 🔴"
    else:
        return "NEUTRAL ⚪"
