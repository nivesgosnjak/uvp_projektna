# Funkcije za pisanje druge csv datoteke

import re
from pisanje_datotek import url_to_string


vzorec_deli=r'<!--title, author, fandom-->(.*?)</dl>'

def na_dele(url):
    """Funkcija dobi povezavo do spletne strani,
    vrne seznam besedil ločenih glede na posamezne fanfice"""
    besedilo=url_to_string(url)
    seznam_fanficov=re.findall(vzorec_deli, besedilo, flags=re.DOTALL)
    return seznam_fanficov


# main vzorci
naslov=r'<h4 class="heading">.*?>(.*?)</a>'
avtor=r'<a rel="author" .*?>(.*?)</a>'

jezik=r'<dd class="language" .*?>(.*?)</dd>'
besede=r'<dd class="words">(.*?)</dd>'
chapters1=r'<dd class="chapters"><.*?>(.*?)</a>/(.*?)</dd>' #dela za večino
chapters2=r'<dd class="chapters">(.*?)/(.*?)</dd>' # zgolj če chapters1 ne dela

kolekcije=r'<dd class="collections"><a .*?>(.*?)</a>'
komentarji=r'<dd class="comments"><a href=".*?">(.*?)</a>'
kudos=r'<dd class="kudos"><a .*?>(.*?)</a>'
bookmarks=r'<dd class="bookmarks"><a .*?>(.*?)</a>'
hits=r'<dd class="hits">(.*?)</dd>'

datum=r'<p class="datetime">(.*?)</p>'

vzorci=[naslov,avtor,jezik,besede,kolekcije,komentarji,kudos,bookmarks, hits, datum]
imena_vzorci=['naslov', 'avtor', 'jezik','število besed','kolekcije', 'komentarji', 'kudos', 'bookmarks', 'hits', 'datum']
# required tags se še morjo zgodit lolll

def pretvori_datum(datum):
    """Funkcija sprejme string, ki predstavlja
    datum v obliki npr 13 Apr 2045 in vrne 
    tuple (13,4,2045), kjer so vrednosti števila"""
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
        case "Okt":
            i=10
        case "Nov":
            i=11
        case "Dec":
            i=12
    return (int(deli[0]),i,int(deli[2]))






def fanfic_podatki(seznam):
    """ Funkcija sprejme seznam stringov - posameznih 
    fanficov, iz njih dobi podatke kot so naslov, avtor,
    število besed, komentrji, hits, bookmarks, kudos, poglavja,
    zadnja posodobitev, required warnings and shite,
    vse to vrne v obliki seznamov slovarjev, bajeeee"""
    dicts=[]
    for fanfic in seznam:
        dict={}
        # za vse razen poglavij
        for i, vzorec in enumerate(vzorci): 
            a=re.findall(vzorec, fanfic, flags=re.DOTALL)
            if len(a)>0:
                dict[imena_vzorci[i]]=a[0]
            else:
                dict[imena_vzorci[i]]="ni podatka"
        #popravimo datum
        stevilsko=pretvori_datum(dict['datum'])
        dict['datum']=stevilsko
        # poglavja
        poglavja=re.findall(chapters1, fanfic, flags=re.DOTALL)
        if len(poglavja)>0:
            dict["poglavja"]=poglavja[0]
        else:
            poglavja=re.findall(chapters2, fanfic, flags=re.DOTALL)
            dict["poglavja"]=poglavja[0]
        dicts.append(dict)
    return dicts
