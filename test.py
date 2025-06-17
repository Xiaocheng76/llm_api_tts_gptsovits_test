import requests

def synthesize_voice(text, ref_audio_path, prompt_text):
    payload = {
        "text": text,
        "text_lang": "ja",
        "ref_audio_path": ref_audio_path,
        "prompt_text": prompt_text,
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
        with open("output.wav", "wb") as f:
            f.write(response.content)
        print("[TTS] 語音生成成功：output.wav")
    except Exception as e:
        print("[TTS] 發生錯誤：", e)

def main():
    text = "你好，這是測試文字。"
    ref_audio_path = "audio/SG0_01_01_CRS0015.wav"
    prompt_text = ""  # 可以空字串

    synthesize_voice(text, ref_audio_path, prompt_text)

if __name__ == "__main__":
    main()
