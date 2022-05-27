
def display_info():
    print('1. Scrape from website first page\n2. Scrape from custom start\n3. Truncade table\n4. Query table\n0. Exit')
    

def ask_for_save(steamparsing_obj):
    while True:
        try:
            command = input('Do you want to save the information? y/n: ').lower()
            if command == 'y':
                steamparsing_obj.to_sql()
                print('Information was saved successfully')
                break
            elif command == 'n':
                break
            
        except ValueError:
            print('Invalid Value')
        except KeyboardInterrupt:
            break


def custom_starting_page(response_class, parser_class):
    while True:
        try:
            start_page = int(input('Start page: '))
            res = response_class(start=start_page, count=100)
            par = parser_class(res.html_from_json(), 'steamsales.db', 'steamspecials')
            print(par.to_dataframe())
            ask_for_save(par)
            break
        except KeyboardInterrupt:
            break
        except AttributeError:
            print('Starting page not found')


def ask_for_trunc(steamparsing_obj):
    while True:
        try:
            command = input('Do you want to truncade records? y/n: ').lower()
            if command == 'y':
                steamparsing_obj.trunc_table()
                print('Information was deleted successfully')
                break
            elif command == 'n':
                break
            
        except ValueError:
            print('Invalid Value')
        except KeyboardInterrupt:
            break


def query_table(steamparsing_obj):
    print(steamparsing_obj.query())
