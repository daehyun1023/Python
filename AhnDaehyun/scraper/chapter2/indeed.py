import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('div', {'class': 'pagination'})
    links = pagination.find_all('a')

    pages = []
    for link in links[:-1]:
        pages.append(int(link.find('span').string))
    max_page = pages[-1]
    return max_page

def extract_job(html):
    title = html.find('a')['title']
    company = html.find('span', {'class': 'company'})
    company_anchor = company.find('a')
    if company:
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
    else:
        company = None

    company = company.strip()
    location = html.find('div', {'class': 'recJobLoc'})['data-rc-loc']
    job_id = html['data-jk']

    return {'title': title, 'company': company, 'location': location ,
            'apply_link': f"https://www.indeed.com/viewjobs?jk={job_id}"}

def extract_jobs(last_pages):
    jobs = []
    for page in range(last_pages):
        result = requests.get(f'{URL}&start={page*LIMIT}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class': 'jobsearch-SerpJobCard'})
        # print(results)
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs