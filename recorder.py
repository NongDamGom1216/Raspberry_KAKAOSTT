import speech_recognition as sr
from gpiozero import Button
import RPi.GPIO as GPIO

import time

button = Button(21, bounce_time=0.03)

WAVE_OUTPUT_FILENAME = "output.wav"

def record_audio():
    global audio
    recognizer = sr.Recognizer()


    # 마이크 설정
    microphone = sr.Microphone(sample_rate=16000)

    with microphone as source:
        print("Start to record the audio.")
        result = recognizer.listen(source)
        audio = result.get_wav_data()
    
    button.when_released = audio_save
        
def audio_save():
    global audio
    # 음성을 받아서 wav 파일로 저장
    print("Recording is finished.")

    with open(WAVE_OUTPUT_FILENAME, "wb") as f:
        f.write(audio)

    return audio
    

def activate():
    # 버튼을 누른 경우 녹음 시작
    button.when_pressed = record_audio



