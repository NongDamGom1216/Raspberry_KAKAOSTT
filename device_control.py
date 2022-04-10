from gpiozero import LED, Servo
import urllib.request as urllib
import json
import kakao
import time

led = LED(16)
servo = Servo(23)

API_key = '&appid=yout weather api'
apiurl = 'https://api.openweathermap.org/data/2.5/weather?q='

def weather(city):
    url = urllib.urlopen(apiurl + city + API_key + '&lang=kr&units=metric')
    apid = url.read()
    data = json.loads(apid)

    cityname = data['name']
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    humi = data['main']['humidity']

    result = f'{cityname} 의 날씨는 {weather} 이며 온도는 {str(temp)} 도, 습도는 {str(humi)} 입니다.'

    return result

def active(result):
    if result['value'] == '전등 켜':
        led.on()
    if result['value'] == '전등 꺼':
        led.off()
    if result['value'] == '문 열어':
        servo.max()
    if result['value'] == '문 닫아':
        servo.min()
    if result['value'] == '날씨 알려줘':
        func_result = weather('Incheon')
        kakao.order(f"<speak>{func_result}</speak>")
        time.sleep(10)