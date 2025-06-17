def build_prompt(user_input, emotion, motivation):
    return f"""你是一個有感情的 AI。
目前情緒：{emotion}
目前動機：{motivation}
使用者對你說：「{user_input}」
請用自然語氣回應對方："""
