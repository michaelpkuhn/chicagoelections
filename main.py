from ast import parse
import electiondata
import htmlparse
import os
import pandas as pd


def main():
    #htmlparse.parsefile("electionresults/result_9_12.html")
    #htmlparse.parsefile("electionresults/result_210_10.html")
    parsefolder()

def parsefolder():
    dp = "electionresults/"
    file_list = os.listdir(dp)
    df = ''
    for fp in file_list:
        if "html" not in fp:
            continue
        d = htmlparse.parsefile(dp + fp)
        if type(df) is str:
            df = d
        else:
            df = pd.concat([df, d])
    
    df.to_csv('chicagomunicipal.csv')


def election_scrape():
    for i in electiondata.elections_ls:
        race_ls = electiondata.get_race_numbers(i)
        print(i, len(race_ls))
        for j in race_ls:
            r = electiondata.get_election_html(i, j)
            with open(f"electionresults/result_{i}_{j}.html", 
                        'w', encoding="utf-8") as file:
                file.write(r.prettify())



if __name__ == '__main__':
    main()