import pandas as pd
import requests 
from bs4 import BeautifulSoup

accounting_job = []
for i in range(1,11):
  url = f'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Accounting%20Analyst&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=accounting%20analyst&pDate=I&sequence=1&startPage={i}'
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  new = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
  for n in new:
    Link = n.find('a')['href']
    Company = n.find('h3', class_="joblist-comp-name").text.replace('(More Jobs)', '').strip()
    Exprience = n.find('li').text.replace('card_travel','')
    Location = n.ul.find('span').text.strip()
    Job_Description = n.find('ul', class_="list-job-dtl clearfix").li.text.replace('Job Description:', '').strip().replace('More Details', '')
    key_skill = n.find('span', class_="srp-skills").text.strip()
    # exprience = 
    j = {
        'Compnay':Company,
        'Exprience':Exprience,
        'Location':Location,
        'Job_Description':Job_Description,
        'key_skill':key_skill,
        'Link':Link
    }
    accounting_job.append(j)
