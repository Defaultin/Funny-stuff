import re
import requests
from bs4 import BeautifulSoup


__all__ = ('random_article')


def random_article(file, language='ru', limit=10):
    '''
    Finds part of a random wikipedia article 
    and saves it to a text file.

    Parameters
    ----------
    file : str
        Name or path of the output text file (data/file.txt).
    language : str, optional
        Language of the generated article {'en', 'ru', 'fr', 'de', 'es', 'it'}.
    limit : int, optional
        Limit on the number of paragraphs in the article.
        The number of paragraphs will not exceed the specified limit.
        
    Returns
    -------
    out : None
    '''
    langs = {'en', 'ru', 'fr', 'de', 'es', 'it'}
    if language not in langs:
        raise ValueError(f'Unsupported language! {langs} expected.')

    article = ''
    while not article:
        wiki = f'https://{language}.wikipedia.org/wiki/Special:Random'
        html_page = requests.get(wiki)
        content = BeautifulSoup(html_page.content, 'html.parser')
        paragraphs = content.select('p')[:limit]
        article = ''.join([s.text for s in paragraphs])
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(re.sub(r'\[\d{1,}\]', '', article))