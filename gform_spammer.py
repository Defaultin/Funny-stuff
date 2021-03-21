from os import cpu_count
from requests import post
from random import choice
from multiprocessing import Pool


class GFormSpammer:
    def __init__(self, id, data):
        self.form_id = id
        self.form_choices = data
        self.procs = cpu_count()
        self.link = 'https://docs.google.com/forms/d/e/'
        self.url = self.link + id + '/formResponse'
        self.headers = {
            'Referer': self.link + id + '/viewform',
            'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36'
        }
        self.setup()


    def setup(self):
        self.form_data = {k: choice(v) for k, v in self.form_choices.items()}


    def spam(self, n):
        for i in range(n):
            self.setup()
            code = post(self.url, data=self.form_data, headers=self.headers).status_code
            status = 'OK' if code == 200 else 'FAIL'
            print(f'status: {status:^10} code: {code:^10} attempt: {i:^10}')


    def run(self, n=1_000_000):
        with Pool(processes=self.procs) as pool:
            pool.map(self.spam, [n] * self.procs)
        

def main():
    form_id = '1FAIpQLSeBuwLTYf0xo23JJHXjc19GppgqtOITfxnzfHkJfZQ7kBurbA'
    form_data = {
        'entry.40969488'    : ['Yes', 'No'],
        'entry.1277036222'  : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'entry.305730833'   : ['Just for fun!', 'Just because!', 'I want this!', 'I like this!']
    }
    GFormSpammer(form_id, form_data).run()
    


if __name__ == '__main__':
    main()