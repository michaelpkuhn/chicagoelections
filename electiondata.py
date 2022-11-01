import requests
from bs4 import BeautifulSoup

election_num = 220
race_num = 12

elections = {
    "2007" : (65, 60),
    "2011" : (25, 24),
    "2015" : (10, 9),
    "2019" : (210, 220)
}

elections_ls = (65, 60, 25, 24, 10, 9, 210, 220)

class ChiElectionRequest:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://chicagoelections.gov',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': f'https://chicagoelections.gov/en/election-results.asp',
            # 'Cookie': 'ASPSESSIONIDQGQCARBT=NOJCOHOBNOGDDMGIPFNELPII',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Sec-GPC': '1',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        self.data = {
            'election': '',
            'race': '',
            'ward': '',
            'precinct': '',
        }

        self.url = ''
    
    def post(self):
        r = requests.post(self.url,
            headers=self.headers, 
            data=self.data)
        if r.status_code != 200:
            return None
        
        soup = BeautifulSoup(r.content, 'html.parser')
        #breakpoint()
        return soup

def get_race_numbers(election_num):
    race_request = ChiElectionRequest()

    race_request.url = f'https://chicagoelections.gov/en/election-results.asp?election={election_num}'

    race_request.headers['Referer'] = f'https://chicagoelections.gov/en/election-results.asp?election={election_num}'
    
    race_request.data['election'] = f'{election_num}'
    
    s = race_request.post()
    #breakpoint()
    race_ls = []
    for o in s.find_all("option"):
        v = o['value']
        if v == '':
            continue
        race_ls.append(int(v))

    return race_ls

def get_election_html(election_num, race_num):
    election_request = ChiElectionRequest()

    election_request.url = 'https://chicagoelections.gov/en/election-results-specifics.asp'

    election_request.headers['Referer'] = f'https://chicagoelections.gov/en/election-results.asp?election={election_num}&race={race_num}'

    election_request.data['election'] =f'{election_num}'
    election_request.data['race'] =f'{race_num}'

    return election_request.post()

# with open("file.html", 'w', encoding="utf-8") as file:
#     file.write(soup.prettify())

#     
#     
#     "method": "POST",
#     
# });