# Glavna datoteka in zagon

from zajem_fandomi import *
from zajem_dela import *
from pisanje_datotek import *

##############################################################3
# Glavni podatki

mapa='podatki'
datoteka_html='ao3.html'
csv_fandomi='fandomi.csv'
csv_dela='dela.csv'
spletna_stran='https://archiveofourown.org/'
spletna_stran2="https://archiveofourown.org/works?commit=Sort+and+Filter&work_search%5Bsort_column%5D=kudos_count&work_search%5Bother_tag_names%5D=&work_search%5Bexcluded_tag_names%5D=&work_search%5Bcrossover%5D=&work_search%5Bcomplete%5D=&work_search%5Bwords_from%5D=&work_search%5Bwords_to%5D=&work_search%5Bdate_from%5D=&work_search%5Bdate_to%5D=&work_search%5Bquery%5D=&work_search%5Blanguage_id%5D=&tag_id=Harry+Potter+-+J*d*+K*d*+Rowling"

##########################################################################

# ZAGON

def main():
    besedilo=url_to_string(spletna_stran)
    najdi_url(besedilo)
    seznam1=najdi_url(besedilo)
    slovarji=fandom_to_dict(seznam1,spletna_stran)
    zapisi_v_csv(slovarji, mapa, csv_fandomi)
    print('konec1')
    seznam2=vse_strani(spletna_stran2)
    slovarji2=fanfic_podatki(seznam2)
    zapisi_v_csv(slovarji2, mapa, csv_dela)
    print('konec2')


if __name__=='__main__':
    main()
