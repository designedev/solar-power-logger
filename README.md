# solar-power-logger
금비전자 인버터를 사용한 태양광 발전시스템에서, 발전량 데이터를 얻는 코드.

데이터는 MQTT를 이용해 얻고, 이를 위해 Elfin EW11모델을 사용함. (사용법은 여기에서 설명하지 않습니다.)
인버터로 다음 신호를 전송하면, EW11이 상태값을 publish 해줍니다.
```7E0101D188```
>상태 요청은 query.py를 참고합니다.

전송받은 신호를 각 비트값에 따라 파싱해서, 사용합니다.
>신호 순서 및 의미는, 신재생에너지 표준 프로토콜 가이드라인(v1.3)을 참고(구글검색)

### DB, MQTT 연결을 위해 config디렉토리를 만들고, database.json 과 mqtt.json 파일을 정의해야 합니다.
>database.json
```json
{
	"host" : "000.000.000.000",
	"port" : "3307",
	"database" : "database_name",
	"user" : "user_id",
	"password" :"user_password"
}

```
>mqtt.json
```json
{
	"host" : "000.000.000.000",
	"port" : "1883",
	"user" : "user_id",
	"password" :"password"
}

```