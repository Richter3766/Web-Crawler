import requests
import string
from bs4 import BeautifulSoup


class CrawledData:
    def __init__(self, url):
        self.url = url
        self.title = None
        self.category = None
        self.summary = None
        self.contents = None

    def setTitle(self, title):
        self.title = title

    def setCategory(self, category):
        self.category = category

    def setSummary(self, summary):
        self.summary = summary

    def setContents(self, contents):
        self.contents = contents

    def crawling(self):
        # Crawling 하고 싶은 사이트에게 유저 정보를 넘겨 접근 거부를 방지
        # http://www.useragentstring.com/ 사이트 내에 있는 Mozilla ~~ 부분
        headers = {'User-Agent':
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

        response = requests.get(self.url, headers=headers)    # url 정보를 가져옴

        if response.status_code == 200:  # url 정보를 받는 데 성공한 경우
            html = response.text  # 소스를 문자열로 바꿔주고
            soup = BeautifulSoup(html, 'html.parser')  # html 문서로 파싱

            """
            # html 문서 내에서 필요한 내용 찾기 (웹 개발자 도구 활용)
                1. 원하는 웹 페이지에서 F12를 눌러 개발자 도구를 띄운다
                2. ctrl + shift + c 를 누른다
                3. 웹 페이지 내 알고 싶은 부분을 클릭한다
                4. 개발자 도구에 방금 클릭한 부분이 강조될텐데 그 부분을
                   마우스 우클릭 -> Copy -> Copy Selector
                이후 ctrl + v 로 " " 내에 붙여넣기
                기본적으로 soup.find 나 select, select_one 함수 활용
            """

            # 예시
            # 노컴 뉴스
            # title = soup.find('title').get_text()
            # category = soup.select_one('#divSubCategory > p > strong').get_text()
            # summary = soup.select_one('#pnlViewBox > div.summary_l > div > p').get_text()
            # contents = soup.select_one("div#pnlContent")

            # 네이버 뉴스 - 아이 뉴스
            title = soup.select_one('#ct > div.media_end_head.go_trans > div.media_end_head_title > h2').get_text()
            category = soup.select_one('#contents > div.media_end_categorize > a > em').get_text()
            summary = soup.select_one('#dic_area > strong').get_text()
            contents = soup.select_one("#dic_area")

            # 네이버 뉴스 - 한국 경제
            # title = soup.find('').get_text()
            # category = soup.select_one('').get_text()
            # summary = soup.select_one('').get_text()
            # contents = soup.select_one("")

            # 제대로 가져왔는 지 확인
            # print(title)
            # print(category)
            # print(summary)
            # print(contents.getText)
            """
                무시 가능
            # 전처리 테스트용
            # spanstr = contents.select("span.fr-inner")
            # strlist = spanstr
            # print(spanstr)
            # contents = contents.get_text()
            
            # 전처리
            # title = self.preprocessing(title)
            # category = self.preprocessing(category)
            # summary = self.preprocessing(summary)
            # contents = self.preprocessing(contents)      # span 내부에 있는 텍스트 제거 필요(이미지 밑에 적힌 작은 글)

            # 객체에 데이터 저장 (전처리 된 데이터)
            # self.setTitle(title)
            # self.setCategory(category)
            # self.setSummary(summary)
            # self.setContents(contents)
            """

            # 객체에 데이터 저장
            self.setTitle(title.strip())
            self.setCategory(category)
            self.setSummary(summary)
            self.setContents(contents.getText()
                             .replace(u'\xa0', u'').replace(u'\u200b', u'').replace("\n", " ").strip())
        else:
            print(response.status_code)     # url 이 없을 경우 상태 코드 출력

    # 클래스 기본 함수
    def getTitle(self):
        return self.title

    def getCategory(self):
        return self.category

    def getSummary(self):
        return self.summary

    def getContents(self):
        return self.contents

    # 전처리 함수 (테스트 중)
    def preprocessing(self, data: str) ->str:
        # 문자열 공백 제거
        data.replace(u'\xa0', u'').replace(u'\u200b', u'').replace("\n", " ")
        data.strip()
        subData = data.split()

        for s in subData:
            if s.isalpha():
                idx = data.find(s)
                data = data[:idx] + data[idx + len(s):]

            if s.find("@") != -1:
                idx = data.find(s)
                data = data[:idx] + data[idx + len(s):]

            s.translate(str.maketrans('', '', string.punctuation))

        return data


def checkValue(newValue: CrawledData) -> bool:
    if newValue.getTitle() is None:
        return False
    if newValue.getCategory() is None:
        return False
    if newValue.getSummary() is None:
        return False
    if newValue.getContents() is None:
        return False
    return True
