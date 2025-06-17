def predict_emotion(text, intent):
    if intent == "讚美":
        return "高興"
    if intent == "冒犯":
        return "羞愧" if "我" in text else "生氣"
    return "中性"
