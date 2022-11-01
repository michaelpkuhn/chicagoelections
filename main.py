import electiondata

def main():
    pass

def election_scrape():
    for i in electiondata.elections_ls:
        race_ls = electiondata.get_race_numbers(i)
        print(i, len(race_ls))
        #print(i, race_ls)
        #print(len(race_ls))
        
        for j in race_ls:
            r = electiondata.get_election_html(i, j)
            with open(f"electionresults/result_{i}_{j}.html", 'w', encoding="utf-8") as file:
                file.write(r.prettify())



if __name__ == '__main__':
    main()