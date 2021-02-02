# Chapter2

## 2.0

웹스크래퍼: 웹사이트에서 정보를 가져오는 것

ex)구글은 위키피디아, 영화 출연한 정보 등 다양한 정보들을 추출해서 가져옴  
유명 신문사 웹사이트 100개의 기사를 매일 아침마다 볼 수 있음  
앞으로 이것들을 구현할 것임

---

## 2.1

스택오버플로우, 인디드에서 구인구직 정보를 가져와서 엑셀 시트에 옮기기  
-> scrapper로 해당페이지 일자리 정보 가져오고, 다음 링크로 가서 다시 정보 가져오고 엑셀시트에 옮기기

---

## 2.2

먼저, https://stackoverflow.com/jobs?q=python 여기랑  
https://indeed.com/jobs?q=python 이거 접속

강의랑 사이트가 똑같이 안되서 아래의 페이지로 리퀘스트 해볼것임  
https://kr.indeed.com/jobs?q=python&start=10

응답여부 확인: `print(indeed_result)`  
html전부(text)를 가져온 것: `print(indeed_result.text)`

---

## 2.3 ~ 2.5

BeautifulSoup을 이용해서 html text의 내용을 잘 찾아줌  
`find_all('tag-name')` 를 이용(이렇게 찾으면 리스트로 만들어짐)해서 해당 태그를 전부 찾아주거나 `find('tag-name)` 를 이용해서 해당 태그하나 찾을 수 있음

---

## 2.6

### 정리

1. 모든 a 태그 검색
   soup.find_all("a")
   soup("a")

2. string 이 있는 title 태그 모두 검색
   soup.title.find_all(string=True)
   soup.title(string=True)

3. a 태그를 두개만 가져옴
   soup.find_all("a", limit=2)

4. string 검색
   soup.find_all(string="Elsie") # string 이 Elsie 인 것 찾기
   soup.find_all(string=["Tillie", "Elsie", "Lacie"]) # or 검색
   soup.find_all(string=re.compile("Dormouse")) # 정규식 이용

5. p 태그와 속성 값이 title 이 있는거
   soup.find_all("p", "title")
   예)

6. a태그와 b태그 찾기
   soup.find_all(["a", "b"])

7. 속성 값 가져오기
   soup.p['class']
   soup.p['id']

8. string을 다른 string으로 교체
   tag.string.replace_with("새로운 값")

9. 보기 좋게 출력
   soup.b.prettify()

10. 간단한 검색
    soup.body.b # body 태그 아래의 첫번째 b 태그
    soup.a # 첫번째 a 태그

11. 속성 값 모두 출력
    tag.attrs

12. class 는 파이썬에서 예약어이므로 class* 로 쓴다.
    soup.find_all("a", class*="sister")

13. find
    find()
    find_next()
    find_all()

14. find 할 때 확인
    if soup.find("div", title=True) is not None:
    i = soup.find("div", title=True)

15. data-로 시작하는 속성 find
    soup.find("div", attrs={"data-value": True})

16. 태그명 얻기
    soup.find("div").name

17. 속성 얻기
    soup.find("div")['class'] # 만약 속성 값이 없다면 에러
    soup.find("div").get('class') # 속성 값이 없다면 None 반환

18. 속성이 있는지 확인
    tag.has_attr('class')
    tag.has_attr('id')
    있으면 True, 없으면 False

19. 태그 삭제
    a_tag.img.unwrap()

20. 태그 추가
    soup.p.string.wrap(soup.new_tag("b"))
    soup.p.wrap(soup.new_tag("div")

Step 1. 페이지 가져오기
Step 2. request 만들기
Step 3. job 추출하기

## 2.10 ~ 2.16

.string의 값이 None으로 나오면 .get_text()도 한번 해보면 잘 나올수도있음

```
    pages = soup.find('div', {'class': 's-pagination'}).find_all('a')
    last_page = pages[-2].get_text(strip=True)
    print(last_page)
```

```
file = open('jobs.csv', 'w', -1,"utf-8", newline="")
```

file을 write하는데 cp949 인코딩문제로 인해 bufferring을 -1로, encoding을 utf-8로 맞춰주었음  
또한, writer.writerow를 할때 한 행마다 빈행이 생성되어서 이를 없애주기 위해 newline=''로 설정해주었음
