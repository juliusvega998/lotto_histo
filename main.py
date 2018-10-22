from bs4 import BeautifulSoup
import httplib2
import datetime
import json
import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch

def getHTML(url):
    http = httplib2.Http()
    response, content = http.request(url)
    if response.status >= 200 or response.status < 400:
        return content
    else:
        raise Exception('URL returned the following code: ' + response.status)

def getNumber():
    URL = 'https://www.philippinepcsolotto.com/history/6-58-lotto-result-history'
    soup = BeautifulSoup(getHTML(URL), 'html.parser')
    #main_div = soup.select("div", {"class": "post-content box mark-links entry-content"})
    result = soup.select('div.post-content.box.mark-links.entry-content > ul > li')[0].getText()
    return result.split('-', 1)[1].strip()

def main():
    now = datetime.datetime.now()
    day = int(now.strftime('%w'))
    if day == 1 or day == 2 or day == 6:
        print(getNumber())

main()