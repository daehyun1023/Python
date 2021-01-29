import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'

def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')
  pagination = soup.find("div", {"class": "pagination"})
  links = pagination.find_all('a')

  pages = []
  # pagination의 'a'에 있는 모든 span 가져오기
  for link in links[:-1]:
    pages.append(int(link.find('span').string))

  max_page = pages[-1]
  
  return max_page


def extract_indeed_jobs(last_pages):
  jobs = []
  for page in range(last_pages):
    result = requests.get(f'{URL}&start={page*LIMIT}')
    
  return jobs