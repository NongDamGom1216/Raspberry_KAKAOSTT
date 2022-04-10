import requests
import json
import io, sys

from pydub import AudioSegment
from pydub.playback import play

URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
HEADERS = {
    "Content-Type" : "application/xml",
    "Authorization" : "KakaoAK 91993241356264156056f235e6563db3"
}
DATA=""

kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

# 샘플 다운로드 https://developers.kakao.com/docs/latest/ko/voice/rest-api

rest_api_key = '91993241356264156056f235e6563db3'
headers = {
    "Content-Type": "application/octet-stream",
    # 바이트 타입
    "X-DSS-Service": "DICTATION",
    "Authorization": "KakaoAK " + rest_api_key,
    # KakaoAK 다음 띄어쓰기 포함
}
def recognize(audio):
    # 음성 파일의 데이터 값
    with open('output.wav', 'rb') as fp:
        audio = fp.read()
        # res = requests.post(kakao_speech_url, headers=headers, data=audio)

    res = requests.post(kakao_speech_url, headers=headers, data=audio)

    is_success = True
    start = res.text.find('{"type":"finalResult"')
    end = res.text.rindex('}')+1

    if start == -1:
        start = res.text.find('{"type":"errorCalled"')
        is_success = False

    # res.text[:] 슬라이싱
    result_json_string = res.text[start:end]
    result = json.loads(result_json_string)

    return is_success, result

def order(DATA):
    res = requests.post(URL, headers = HEADERS, data = DATA.encode('utf-8'))
    if res.status_code != 200: # 에러를 확인하는 법
        print(res)
        print(res.text)
        sys.exit(0)

    sound = io.BytesIO(res.content)
    song = AudioSegment.from_mp3(sound)
    play(song)