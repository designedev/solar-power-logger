import paho.mqtt.client as mqtt
import converter
import database
import config_loader as conf
import json
 
# 콜백 함수 정의하기
#  (mqttc.connect를 잘 되면) 서버 연결이 잘되면 on_connect 실행 (이벤트가 발생하면 호출)
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))
 
# 브로커에게 메시지가 도착하면 on_message 실행 (이벤트가 발생하면 호출)
def on_message(client, obj, msg):
    print(msg.payload.hex())
    hex = msg.payload.hex()
    output = converter.hex_to_decimal(hex[30:34]) *0.001
    accumulated_output = converter.hex_to_decimal(hex[42:58]) *0.001
    database.save_data(output, accumulated_output)
 
def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribe complete : " + str(mid) + " " + str(granted_qos))
 
# 클라이언트 생성
mqttc = mqtt.Client()
 
# 콜백 함수 할당하기
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
 
 
# 브로커 연결 설정
# 참고로 브로커를 Cloudmqtt 홈페이지를 사용할 경우
# 미리 username과 password, topic이 등록 되어있어야함.
mqtt_info = conf.get_mqtt_info()
url = mqtt_info["host"]
port = int(mqtt_info["port"])
username = mqtt_info["user"]
password = mqtt_info["password"]
 
subscribe_topic = "volt-result"
 
# 클라이언트 설정 후 연결 시도
mqttc.username_pw_set(username, password)
mqttc.connect(host=url, port=port)
 
# QoS level 0으로 구독 설정, 정상적으로 subscribe 되면 on_subscribe 호출됨
mqttc.subscribe(subscribe_topic, 0)
 
 
# 네트워크 loop를 계속 실행. 종료 에러가 발생하기 전까지 계속 실행
rc = 0
while rc == 0:
    rc = mqttc.loop()
 
print("rc: " + str(rc))
 