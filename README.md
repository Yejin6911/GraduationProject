# 도로시 (도와줘 로드위의 CCTV) 
## 범죄 예방을 위한 딥러닝 기반의 스마트 도로 관제서비스 DOROCI : Deep-learning Road CCTV

### 서비스 개요
현재 여성안심귀갓길에 설치된 비상벨은 응급상황에 직접 비상벨의 위치를 찾아 눌러야 한다는 불편함과 장애물에 가려져 있으면 쉽게 접근할 수 없다는 한계가 있다.
도로시는 딥러닝을 통한 음성데이터와 CCTV를 활용해 자동으로 위급상황을 인지하고 경찰의 빠르고 정확한 판단과 출동을 돕는 스마트 도로 관제서비스이다.

### 시스템 구조
![image](https://user-images.githubusercontent.com/44834680/103102385-084c7d00-465f-11eb-99ad-60d1bf606005.png)


### ERD(Entity Relationship Diagram)
![image](https://user-images.githubusercontent.com/44834680/103102253-8a887180-465e-11eb-94f4-dc012d1652c1.png)

## 구현 App 종류 별 기능
### 1. Account
|url|기능|
|---|---|
|/account/login|사용자 로그인|
|/account/logout|사용자 로그아웃|

### 2. Map
|url|기능|
|---|---|
|/map|알람발생(마커 생성)|
|/map/cctv/<int:location_pk>|알람발생 위치 cctv 화면 불러오기|
|/map/cctv/<int:pk>|해당 알람 확인완료 처리|
|/map/record|알람 발생 기록 조회|
|/map/lists/police|담당 경찰관 조회|
|/map/lists/gurard|담당 지킴이 조회|
|/map/send/<int:alarm_pk>|메세지 보내기 기능|

### 3. Alarm
|url|기능|
|---|---|
|/alarm|알람생성
|/alarm/siren/<int:location_pk>|사이렌 요청 전송

## 준비 사항

1. 가상환경 생성
```
$ cd [프로젝트 디렉토리]
$ python -m venv .myvenv
```
2. 가상환경 실행
```
$ source .myvenv/bin/activate
```
3. myvenv 디렉터리 안에 있는 bin/python이 사용되는지 확인.
```
$ which python
```

4. 가상 환경에 패키지 설치
```
$ pip install -r requirements.txt
```

5. Graduation/map 아래에 keys.py 생성
```
service_id = "{Naver SENS service_id}"
access_key = "{API 인증키 Access Key ID}"
secret_key = "{API 인증키 Secret Key}"
```
6. migration
```
$ python manage.py makemigrations
$ python manage.py migrate
```

## 실행
```
$ python manage.py runserver
    
```

### OTP 발급 디바이스 등록
*dadmin : 기존 admin 페이지
*admin: 디바이스 정보를 등록할 수 있는 어드민 페이지.

1. [admin 페이지](http://localhost:8000/admin)에서 기기 등록을 위한 TOTP Device 정보 등록(admin)
![image](https://user-images.githubusercontent.com/44834680/103103880-772dd400-4667-11eb-87cf-f95ae7ede670.png)

2. [dadmin 페이지](http://localhost:8000/dadmin/otp_totp/totpdevice/)에서 QRCode를 발급하고 사용자가 앱(OTPAuth)으로 QRCode를 등록함으로써 OTP 발급을 위한 준비 완료.
![image](https://user-images.githubusercontent.com/44834680/103104006-2cf92280-4668-11eb-8986-e37c640ad269.png)

### 데이터 등록

1. [dadmin-> map->location](http://localhost:8000/dadmin/account/station/)페이지에서 '경찰서 목록'을 Import 해줌.
![image](https://user-images.githubusercontent.com/44834680/103104285-9e85a080-4669-11eb-8c61-f78cccd216ff.png)
파일 선택 -> "map->static->data" 아래의 '경찰서 목록' 파일 선택 -> csv Format 설정 -> Submit
![image](https://user-images.githubusercontent.com/44834680/103104307-b78e5180-4669-11eb-931a-5b92003e6820.png)

2. [dadmin-> map->location](http://localhost:8000/dadmin/map/location/)페이지에서 data를 import 해줘야 함.

![image](https://user-images.githubusercontent.com/44834680/103104081-a264f300-4668-11eb-8de6-7784d536f463.png)

파일 선택 -> "map->static->data" 아래의 해당 경찰서 파일 선택 -> csv Format 설정 -> Submit

![image](https://user-images.githubusercontent.com/44834680/103104574-70a15b80-466b-11eb-84a6-2cfd67db3eb4.png)


## [딥러닝 모델 보러가기](https://github.com/jessica9685/DOROCI)


