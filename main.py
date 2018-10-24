from bs4 import BeautifulSoup
import httplib2
import datetime
FILE_PATH='D:/Documents/codes/python/lotto_histo/lotto.txt'

def getHTML(url):
    http = httplib2.Http()
    response, content = http.request(url)
    if response.status >= 200 or response.status < 400:
        return content
    else:
        raise Exception('URL returned the following code: ' + response.status)

def getNumbers():
    URL = 'https://www.philippinepcsolotto.com/history/6-58-lotto-result-history'
    soup = BeautifulSoup(getHTML(URL), 'html.parser')
    
    results = soup.select('div.post-content.box.mark-links.entry-content > ul > li')
    numbers= []
    for result in results:
        numbers.append(result.getText().split('-', 1)[1].strip())
    return numbers

def getLotto():
    lotto = open(FILE_PATH, 'r')
    lotto_numbers = lotto.read().split('\n')
    lotto.close()

    return lotto_numbers

def appendLotto(numbers):
    lotto = open(FILE_PATH, 'a')
    for number in numbers:
        lotto.write('\n' + number)

def cmpNumbers():
    numbers = getNumbers()
    lottos = getLotto()

    for lotto in lottos:
        for number in numbers:
            if number == '__-__-__-__-__-__':
                continue
            if lotto == number:
                numbers.remove(number)
                break

    if len(numbers) != 0:
        appendLotto(numbers)

def main():
    now = datetime.datetime.now()
    day = int(now.strftime('%w'))
    if day == 1 or day == 3 or day == 6:
        cmpNumbers()

main()