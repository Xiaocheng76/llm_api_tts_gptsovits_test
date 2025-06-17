def decide_motivation(emotion, intent):
    if emotion == "高興":
        return "親近"
    if emotion == "生氣":
        return "自我防衛"
    return "理性回應"
