import csv
import requests
import os
import re
from zajem_fandomi import *
from zajem_dela import *
from pisanje_datotek import *



mapa='podatki'
datoteka_html='ao3.html'
csv_fandomi='fandomi.csv'
csv_dela='dela.csv'
spletna_stran='https://archiveofourown.org/'

##########################################################################

# ZAGON

def main():
    besedilo=url_to_string(spletna_stran)
    najdi_url(besedilo)
    seznam1=najdi_url(besedilo)
    slovarji=fandom_to_dict(seznam1,spletna_stran)
    zapisi_v_csv(slovarji, mapa, csv_dela)
    print('konec')


if __name__=='__main__':
    main()
