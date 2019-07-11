# blockchain 앱

* Block, Blockchain 구현

## 주요 문제

### 탈중앙화(decentralization) 이전 블록체인을 어떻게 유지할까.

* SQLite
* Session
* Memcached
* Redis

# network 앱

* P2P 구현
* 웹소켓 통신

## 주요 문제

### 소켓 연결 객체
#### 소켓 연결 객체를 어디에 저장할까.

* SQLite
* Session
* Memcached
* Redis

#### 서버 소켓
consumer, channel로 연다

#### 클라이언트 소켓
웹소켓 클라이언트

* websockets
* websocket-client


# chat 앱