import crawledData


# 결과가 출력될 파일
f = open('C:\\Users\\KHS\\Desktop\\Study\\Python\\WebCrolling\\result.json', 'w')


dic = {}    # 만들어진 객체가 담길 딕셔너리
n = 0       # 딕셔너리 크기
num = 100   # Crawling 할 url 개수

f.write("[\n")
for page in range(num):
    # url 생성자 | Crawling 을 하려는 웹 주소의 규칙을 찾아야 함
    # 아래는 예시

    # 노컴뉴스
    # url = "https://www.nocutnews.co.kr/news/" + str(5786521 + page * 10)

    # 네이버 뉴스 - 아이 뉴스
    url = "https://n.news.naver.com/article/031/0000" + \
          str(685095 + page * 10) + "?sid=100"

    # 네이버 뉴스 - 한국경제
    # url = "https://n.news.naver.com/article/newspaper/015/000" \
    #       + str(4723902 + page) + "?date=20220712"

    # crawling 할 url 의 객체 생성
    newValue = crawledData.CrawledData(url)

    # url 내에 빠진 정보가 없을 때만 Crawling
    try:
        newValue.crawling()
        if crawledData.checkValue(newValue) is False:
            continue
    except:
        continue

    # 완료된 정보는 저장
    dic[n] = {url, newValue}
    n += 1
    f.write("    {\n")
    f.write('        "title":' + '"' + newValue.getTitle() + '",\n')
    f.write('        "category":' + '"' + newValue.getCategory() + '",\n')
    f.write('        "url":' + '"' + url + '",\n')
    f.write('        "summary":' + '"' + newValue.getSummary() + '",\n')
    f.write('        "contents":' + '"' + newValue.getContents() + '",\n')
    f.write("    },\n")

f.write("\n]")
f.close()

print("Processing complete\n")


