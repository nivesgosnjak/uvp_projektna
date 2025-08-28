# Dodatne funkcije, ki pomagajo pri zapisu druge csv datoteke

import re
from pisanje_datotek import url_to_string



vzorec_deli=re.compile(r'<!--title, author, fandom-->(.*?)</dl>', re.DOTALL)

def na_dele(url):
    """Funkcija dobi povezavo do spletne strani,
    vrne seznam besedil ločenih glede na posamezna dela"""
    besedilo=url_to_string(url)
    return vzorec_deli.findall(besedilo)

def pretvori_datum(datum):
    """Funkcija sprejme string, ki predstavlja
    datum v obliki npr. 13 Apr 2045 in vrne 
    tuple (4,2045) s številskimi vrednostmi,
    ki predstavljata leto in mesec"""
    deli=datum.split()
    i=None
    match deli[1]:
        case "Jan":
            i=1
        case "Feb":
            i=2
        case "Mar":
            i=3
        case "Apr":
            i=4
        case "May":
            i=5
        case "Jun":
            i=6
        case "Jul":
            i=7
        case "Aug":
            i=8
        case "Sep":
            i=9
        case "Oct":
            i=10
        case "Nov":
            i=11
        case "Dec":
            i=12
    return (i,int(deli[2]))

def odstrani_vejico(s):
    """ Funkcija sprejme string, ki predstavlja število,
    številu odstrani vejico in vrne int"""
    return int(s.replace(',',''))