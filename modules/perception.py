def classify_intent(text):
    if any(word in text for word in ["你真棒", "好厲害"]):
        return "讚美"
    if "幹" in text or "爛" in text:
        return "冒犯"
    return "一般交流"
