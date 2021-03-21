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


    def run(self, n=100_000):
        with Pool(processes=self.procs) as pool:
            pool.map(self.spam, [n] * self.procs)
        

def main():
    form_id = '1FAIpQLScZobf46aSDpBwOv2_IdtI8KvkvZfd0aokww9nXpzGfSML90g'
    form_data = {
        'entry.921031262':      ['Женский', 'Мужской'],
        'entry.1140758884':     [1,2,3,4,5,6,7,8,9,10],
        'entry.446215675':      [1,2,3,4,5,6,7,8,9,10],
        'entry.474048133':      [1,2,3,4,5,6,7,8,9,10],
        'entry.18641284':       [1,2,3,4,5,6,7,8,9,10],
        'entry.1883718834':     [1,2,3,4,5,6,7,8,9,10],
        'entry.111081883':      [1,2,3,4,5,6,7,8,9,10],
        'entry.2126364118':     [1,2,3,4,5,6,7,8,9,10],
        'entry.483777673':      [1,2,3,4,5,6,7,8,9,10],
        'entry.102807615':      [1,2,3,4,5,6,7,8,9,10],
        'entry.1081321635':     [1,2,3,4,5,6,7,8,9,10],
        'entry.2018477058':     [1,2,3,4,5,6,7,8,9,10],
        'entry.1346942557':     [1,2,3,4,5,6,7,8,9,10],
        'entry.1370493519':     [1,2,3,4,5,6,7,8,9,10],
        'entry.75520167':       [1,2,3,4,5,6,7,8,9,10],
        'entry.2071664774':     [1,2,3,4,5,6,7,8,9,10],
        'entry.216057065':      [1,2,3,4,5,6,7,8,9,10],
        'entry.1333027542':     [1,2,3,4,5,6,7,8,9,10],
        'entry.761505026':      [1,2,3,4,5,6,7,8,9,10],
        'entry.214673452':      [1,2,3,4,5,6,7,8,9,10],
        'entry.858511167':      [1,2,3,4,5,6,7,8,9,10],
        'entry.1656968931':     [1,2,3,4],
        'entry.1199883668':     ['БГУ', 'БГМУ', 'БГУИР', 'БНТУ', 'БГЭУ', 'БГАТУ'],
        'entry.1010282196':     [19,20,21,22]
    }
    GFormSpammer(form_id, form_data).run()
    


if __name__ == '__main__':
    main()