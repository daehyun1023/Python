import requests
from bs4 import BeautifulSoup

"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

# stackover = 'https://stackoverflow.com/jobs?r=true&q='
# wework = 'https://weworkremotely.com/remote-jobs/search?term='
# remoteok = 'https://remoteok.io/remote-dev+'

# remoteok = 'https://remoteok.io/remote-dev+'
# keyword= 'python'
# url = f'{remoteok}{keyword}-jobs'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def extract_job(html):
    title = html.find("h2").get_text(strip=True)
    company = html.find("h3").get_text(strip=True)
    apply = "https://remoteok.io" + \
        html.find("a", {"class": "preventLink"})["href"]
    return {"title": title, "company": company, "apply_link": apply}


def extract_jobs(url):
    jobs = []
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("tr", {"class": "job"})
    for result in results:
        job = extract_job(result)
        jobs.append(job)

    return jobs


def get_db(url):
    jobs = extract_jobs(url)
    return jobs
