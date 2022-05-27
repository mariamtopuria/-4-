from classes.requesthandling import RequestToSteam
from classes.parsinghandling import SteamParsing
from console.consolefuncs import *


def main():
    req = RequestToSteam(count=100)
    parsing = SteamParsing(req.html_from_json(), 'steamsales.db', 'steamspecials')
    
    while True:
        print(f'There are {parsing.number_of_records()} records in database')
        display_info()
        enter_choice = int(input('>>>'))
        
        if enter_choice == 0:
            exit()
        elif enter_choice == 1:
            print(parsing.to_dataframe())
            ask_for_save(parsing)
            
        elif enter_choice == 2:
            custom_starting_page(RequestToSteam, SteamParsing)
        
        elif enter_choice == 3:
            ask_for_trunc(parsing)
        elif enter_choice == 4:
            query_table(parsing)
        

if __name__ == '__main__':
    main()