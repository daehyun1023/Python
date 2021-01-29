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

## 2.2

먼저, https://stackoverflow.com/jobs?q=python 여기랑  
https://indeed.com/jobs?q=python 이거 접속

강의랑 사이트가 똑같이 안되서 아래의 페이지로 리퀘스트 해볼것임  
https://kr.indeed.com/jobs?q=python&start=10

응답여부 확인: `print(indeed_result)`  
html전부(text)를 가져온 것: `print(indeed_result.text)`
