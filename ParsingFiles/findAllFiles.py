'''
Approach: Fetching the response of the url using requests library.
          Utilize beautifulsoup library to parse html contents and
          finding all files or paths and logging the file paths
          while recursively looping over other directories to find
          out the files contained by the directory. Asyc methods can
          be utilized to improve the latency.
'''


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def findAllFiles(url, baseUrl=None):
    if baseUrl is None:
        baseUrl = url
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Unable to find url')
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) >= 2:
            content = cols[1].find('a')
            if content:
                name = content.text
                if name in ['.', '..', 'Parent Directory']:
                    continue

                href = content.get('href')
                fullUrl = urljoin(url, href)

                if href.endswith('/'):
                    findAllFiles(fullUrl, baseUrl)
                else:
                    relativeUrl = fullUrl.replace(baseUrl, '')
                    print(relativeUrl)


url = "https://gentoo.osuosl.org/distfiles/"
findAllFiles(url)