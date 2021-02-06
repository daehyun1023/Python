# Chapter4 Flask

## 4.0

scrapper를 웹서버에 넣는 작업을 할 예정
csv파일을 만드는 대신 웹사이트에 스크래퍼 결과를 바로보여줄 수 있게
다운로드를 원한다면 다운로드도 할수 있게 해줌


## 4.1

```python
app = Flask("SuperScrapper")

@app.route("/")
def home():
  return "Hello! Welcome to mi casa!"
a
@app.route("/contact")
def contact():
  return "Contact me!"

app.run(host="0.0.0.0")
```

는 기본 홈페이지, @app.route는 바로 밑에 있는 함수만을 찾아 실행시켜주는 것 (밑에 함수없으면 에러)

## 4.2

route에서 <>를 통해 무언가를 받으면 그것을 함수인자에 넣어줘야함 아래처럼해줘야댐

```python
@app.route("/<username>")
def contact(username):
  return f"Hello {username} how are you doing"
```

직접 html파일을 불러오는 법은
`from flask import Flask, render_template`  
`render_template("home.html")`을 통해 html 파일을 불러올 수 있음

## 4.3

새로운 주소에서 사용자가 입력한 정보를 받아오기 위해
`from flask import request`를 해주어야함

`request.args.get('word')` 를 통해 word의 value값을 가져올 수 있음

`render_template("report.html", searchingBy=word)` 이렇게 html에 인자를 넘겨줄 수도 있음 html에서는 이 인자를 {{searchingBy}} 로 받음

`redirect("/")` 사용자가 입력한 정보가 없거나 할때 다시 홈페이지로 가게 해줌

## 4.5

매번 사용자가 요청할때마다 scrapping을 100번넘게하면서 기다리기엔 시간이 너무 오래걸리기 때문에 fake DB를 만들 것임
fake DB는 라우트 외부(바깥)에 나와있어야됨

## 4.6
flask을 통해 파이썬 코드를 html에서 친다면, {%%}안에 쳐줘야함
```html
    {% for job in jobs %}
      <span>{{job.title}}</span>
      <span>{{job.company}}</span>
      <span>{{job.location}}</span>
      <a href="{{job.link}}" target="_blank">Apply</a>
    {% endfor %}
```


## 4.7
csv로 export와 저장하는 기능을 만들어보자   
try, except 문
```
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
  except:
    return redirect("/")
```
중간에 raise로 exception을 발생시켜서 except처리 하게 해주는 것




