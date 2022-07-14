# Web-Crawler
web crawling by python, bs4

파이썬을 이용한 Web Crawling,

requests 와 BeautifulSoup 패키지 install 필요

  기본 구조
url 정보를 통해 html 문서를 받아오고
BeautifulSoup에 내장된 파싱 함수를 이용해 파싱.

(이렇게 파싱된 데이터는 
find 나 select 등 다른 함수를 이용해 
추가 정보 추출 가능)

  유의점
1. url 정보를 이용해 웹 페이지에 html 문서를 요청할 때
웹 사이트가 봇(bot)이 보낸 요청으로 인지하고
데이터를 주지 않는 경우가 있음
-> requests 함수의 추가 인자인 header 에 유저 정보를 전달하여 해결 가능

(http://www.useragentstring.com/ 사이트 내에 있는 Mozilla ~~ 부분)

2. 다수의 url을 크롤링하고 싶으면 해당 url 주소의 규칙을 추측해서
url로 전달해줘야 함
ex) url = "https://www.nocutnews.co.kr/news/" + str(5786521 + page * 10)
                                                      ↑ 이부분이 규칙
3. 간혹 url 에서 정보를 가져왔는 데 비어있는 때가 있음. (페이지가 삭제된 경우 등)
-> checkValue 함수로 객체 내 정보 검사, 하나라도 비어있으면 버림
 
4. 이외 발생할 가능성이 있는 모든 오류는 try catch 문으로 처리
 
5. 받아온 데이터를 전처리 하는 법은 테스트 중

이외에 모르겠거나, 더 필요한 점은 말할 것
