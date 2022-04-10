from signal import pause
import recorder
import kakao
import time
import device_control

def voice():
    global audio, is_success, result
    max_time_end = time.time() + (5)
    while True:
        audio = recorder.activate() # 버튼을 누르면 녹음 시작
        is_success, result = kakao.recognize(audio)  # 음성 인식 실행
        if time.time() > max_time_end:
            break

def main():
    while True:
        voice()

        if is_success:
            device_control.active(result)
            
        else:
            # 음성 합성으로 오디오 출력
            print('인식 실패:', result['value'])
            kakao.order("<speak>다시 말씀해주세요.</speak>")

        
        
main()