from bs4 import BeautifulSoup
import pandas as pd


def clean_pct(s):
    return(float(s.replace('%', 'e-2')))

def parsefile(fp):
    with open(fp, 'r', encoding="utf-8") as file:
        soup = BeautifulSoup(file.read(),
                    features="lxml")

    contents = soup.find_all("div", "main_body")[0].contents[3].contents

    election_name = contents[7].get_text(strip=True)
    race_name = contents[25].get_text(strip=True)

    ward_results_rows = soup.find_all("table")[0].find_all("tr")

    candidate_row = [td for td in ward_results_rows[0].stripped_strings]
    result_row = [td for td in ward_results_rows[1].stripped_strings] 

    n_candidates = (len(candidate_row) - 1) // 2

    d = []

    for i in range(n_candidates):
        indx = i * 2 + 1
        candidate = tuple([
            election_name,
            race_name,
            candidate_row[indx],
            int(result_row[indx].replace(',',''))
        ])
        d.append(candidate)

    d = pd.DataFrame.from_records(d, columns=["election", "race", "candidate", "votes"])
    
    return d

