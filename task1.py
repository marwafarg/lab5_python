import webbrowser
from random import choice
random_page_generator = ['http://www.randomwebsite.com/cgi-bin/random.pl',
                         'https://www.google.com/',
                         'https://www.facebook.com/'''
                         'https://www.youtube.com/'
                         ]
webbrowser.open(choice(random_page_generator))