# 도로시 (도와줘 로드위의 CCTV) 
## 범죄 예방을 위한 딥러닝 기반의 스마트 도로 관제서비스 DOROCI : Deep-learning Road CCTV

### 서비스 개요
현재 여성안심귀갓길에 설치된 비상벨은 응급상황에 직접 비상벨의 위치를 찾아 눌러야 한다는 불편함과 장애물에 가려져 있으면 쉽게 접근할 수 없다는 한계가 있다.
도로시는 딥러닝을 통한 음성데이터와 CCTV를 활용해 자동으로 위급상황을 인지하고 경찰의 빠르고 정확한 판단과 출동을 돕는 스마트 도로 관제서비스이다.

### 시스템 구조
![image](https://user-images.githubusercontent.com/44834680/103102385-084c7d00-465f-11eb-99ad-60d1bf606005.png)


### ERD(Entity Relationship Diagram)
![image](https://user-images.githubusercontent.com/44834680/103102253-8a887180-465e-11eb-94f4-dc012d1652c1.png)

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
pip install requests
```

## 실행
```
$ python manage.py runserver
    
```
