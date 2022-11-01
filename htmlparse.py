from bs4 import BeautifulSoup

def clean_pct(s):
    return(float(s.replace('%', 'e-2')))

with open(f"electionresults/result_9_12.html", 'r', encoding="utf-8") as file:
    soup = BeautifulSoup(file.read())

contents = soup.find_all("div", "main_body")[0].contents[3].contents

election_name = contents[7]
race_name = contents[25]

ward_results_table = soup.find_all("table")[0]

ward_results = [td for td in ward_results_table.stripped_strings]

alder_results = {
    ward_results[1]: clean_pct(ward_results[7]),
    ward_results[3]: clean_pct(ward_results[9])}

print(alder_results)

#breakpoint()