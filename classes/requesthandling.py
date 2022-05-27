import requests

class RequestToSteam:
    
    def __init__(self, start: int = 0, count: int = 50):
        self.start = start
        self.count = count
        self.response = requests.get(f'https://store.steampowered.com/search/results/?query&start={self.start}&count={self.count}&dynamic_data=&sort_by=_ASC&snr=1_7_7_2300_7&specials=1&infinite=1')

    def html_from_json(self):
        return self.response.json()['results_html']
    
    
    