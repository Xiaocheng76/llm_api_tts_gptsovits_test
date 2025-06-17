import requests

def call_llm(user_input):
    # 這裡替換成你呼叫對話模型的程式碼，回傳字串 reply
    # 範例：
    reply = "這是模擬的回答：" + user_input
    return reply

def synthesize_voice(text, ref_audio_path, prompt_text):
    payload = {
        "text": text,
        "text_lang": "ja",
        "ref_audio_path": ref_audio_path,
        "prompt_text":"",
        "prompt_lang": "ja",
        "text_split_method": "cut0",
        "batch_size": 1,
        "streaming_mode": False,
        "top_k": 5,
        "top_p": 1,
        "temperature": 1,
        "batch_threshold": 0.75,
        "split_bucket": True,
        "speed_factor": 1.0,
        "seed": -1,
        "parallel_infer": True,
        "repetition_penalty": 1.35,
        "sample_steps": 32,
        "super_sampling": False
    }


    print("[TTS] 發送請求到 GPT-SoVITS")
    try:
        response = requests.post("http://localhost:9880/tts", json=payload)
        response.raise_for_status()

        # 把返回的語音檔案寫到本地
        with open("output.wav", "wb") as f:
            f.write(response.content)
        print("[TTS] 語音生成成功：output.wav")
    except Exception as e:
        print("[TTS] 發生錯誤：", e)
        print("[TTS] 請確保 GPT-SoVITS 服務正在運行，並檢查網路連線。")

def main(user_input):
    # 呼叫對話模型取得回答
    reply = call_llm(user_input)

    # 參考音檔與提示文字，依你的環境調整路徑與內容
    ref_audio_path = "audio/SG0_01_01_CRS0015.wav"
    prompt = ""

    # 呼叫 TTS 合成語音
    synthesize_voice(reply, ref_audio_path)

if __name__ == "__main__":
    user_input = input("請輸入文字: ")
    main(user_input)

