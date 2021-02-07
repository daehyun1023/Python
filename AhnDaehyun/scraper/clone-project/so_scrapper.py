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

# stackover = 'https://stackoverflow.com/jobs?r=true&q='
# keyword= 'python'
# url = stackover + keyword


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job(html):
    title = html.find("h2", {"class": "mb4"}).find("a")["title"]
    company, location = html.find(
        "h3", {"class": "mb4"}).find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html["data-jobid"]
    return {"title": title, "company": company, "apply_link": f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping: SO: Page: {page+1}")
        result = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs


def get_db(url):
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)

    return jobs
