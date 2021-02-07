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

# wework = 'https://weworkremotely.com/remote-jobs/search?term='
# keyword= 'python'
# url = wework + keyword


def extract_job(html):
    title = html.find("span", {"class": "title"}).get_text(strip=True)
    company = html.find("span", {"class": "company"}).get_text(strip=True)
    apply = "https://weworkremotely.com" + \
        html.find("a", recursive=False)["href"]
    return {"title": title, "company": company, "apply_link": apply}


def extract_jobs(url):
    jobs = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("li", {"class": "feature"})
    for result in results:
        job = extract_job(result)
        jobs.append(job)

    return jobs


def get_db(url):
    jobs = extract_jobs(url)
    return jobs
