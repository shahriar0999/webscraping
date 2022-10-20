import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

url = 'https://jobs.bdjobs.com/jobsearch.asp?fcatId=1&icatId=-1'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'xml')

j = soup.find_all("div", class_="norm-jobs-wrapper")

accounting_finance_job = []
link = []
for i in j:
  jobtitle = i.find('div', class_="job-title-text").text.strip()
  company = i.find('div', class_='comp-name-text').text.strip()
  location = i.find('div', class_="locon-text-d").text.strip()
  education = i.find('div', class_="edu-text-d").text.strip()
  Experience_Requirements = i.find('div', class_="exp-text-d").text.strip()
  Deadline = i.find('div', class_="dead-text-s").text.strip()[11:]
  Link = i.find('a')['href'][18:25]
  Link = f"https://jobs.bdjobs.com/jobdetails.asp?id={Link}&fcatId=1&ln=1"
  
  job = {
      "Job_Title":jobtitle,
      "Company":company,
      "Location":location,
      "Education":education,
      "Experience_Requirements":Experience_Requirements,
      "Deadline": Deadline
}
  link.append(Link)
  accounting_finance_job.append(job)

pd.DataFrame(accounting_finance_job)
