# brain.py

from modules.perception import classify_intent
from modules.emotion import predict_emotion
from modules.motivation import decide_motivation
from modules.prompt_gen import build_prompt
from modules.llm_interface import call_llm
from modules.tts_interface import synthesize_voice

def main(user_input):
    intent = classify_intent(user_input)
    emotion = predict_emotion(user_input, intent)
    motivation = decide_motivation(emotion, intent)
    prompt = build_prompt(user_input, emotion, motivation)
    reply = call_llm(prompt)
    print(f"🤖：{reply}")

    # 這裡改成固定參考音頻路徑，請改成你本地有效的音頻檔路徑
    ref_audio_path = "audio/SG0_01_01_CRS0015.wav"
    
    synthesize_voice(reply, ref_audio_path, prompt_text=prompt)
