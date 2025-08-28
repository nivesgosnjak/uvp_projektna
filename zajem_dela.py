# Funkcije za pisanje druge csv datoteke

import re
import time
from pomozne import *

#####################################################
# glavni vzorci
avtor=re.compile(r'<a rel="author" .*?>(.*?)</a>', re.DOTALL) 

vzorci_fanfic=re.compile(
    r'<h4 class="heading">.*?>(.*?)</a>.*?'
    r'<p class="datetime">(.*?)</p>.*?'
    r'<dd class="language" .*?>(.*?)</dd>.*?'
    r'<dd class="words">(.*?)</dd>.*?'
    r'<dd class="comments"><a href=".*?">(.*?)</a>.*?'
    r'<dd class="kudos"><a .*?>(.*?)</a>.*?'
    r'<dd class="bookmarks"><a .*?>(.*?)</a>.*?'
    r'<dd class="hits">(.*?)</dd>.',
    re.DOTALL
)

vzorci_poglavja=re.compile(
    r'<dd class="chapters".*?'
    r'>(\d+).*?'
    r'/(\d+|\?)'
)

#####################################################
# Da lahko zajamemo več kot prvih 20 del napisanih na prvi strani,
# se moremo sprehoditi čez strani, pri tem je a število strani,
# čez katere se bomo sprehodili.
a=50
osnovni_link="https://archiveofourown.org/works?commit=Sort+and+Filter&work_search%5Bsort_column%5D=kudos_count&work_search%5Bother_tag_names%5D=&work_search%5Bexcluded_tag_names%5D=&work_search%5Bcrossover%5D=&work_search%5Bcomplete%5D=&work_search%5Bwords_from%5D=&work_search%5Bwords_to%5D=&work_search%5Bdate_from%5D=&work_search%5Bdate_to%5D=&work_search%5Bquery%5D=&work_search%5Blanguage_id%5D=&tag_id=Harry+Potter+-+J*d*+K*d*+Rowling"


#####################################################


def vse_strani(url):
    """ Funkcija sprejme osnovni link spletne
    strani, ga dopolni, da se vrti skozi vse strani 
    na spletni strani, vrne množico posameznih del"""
    fanfici=set()
    i=1
    while i<=a:
        time.sleep(0.1) # varovalo, da nas stran ne začne zavračati
        link=url+"&page="+str(i)
        fanfici.update(set(na_dele(link)))
        i+=1
    return fanfici


def fanfic_podatki(seznam):
    """ Funkcija sprejme množico stringov - posameznih 
    fanficov, iz njih dobi podatke kot so naslov, avtor,
    število besed, komentarji, hits, bookmarks, kudos, poglavja,
    zadnja posodobitev, vse to vrne v obliki seznamov slovarjev"""
    dicts=[]
    for fanfic in seznam:
        dict={}
        najdba=vzorci_fanfic.search(fanfic)
        datum=pretvori_datum(najdba.group(2))
        dict['naslov']=najdba.group(1)
        dict['mesec']=datum[0]
        dict['leto']=datum[1] 
        dict['jezik']=najdba.group(3) 
        dict['število besed']=odstrani_vejico(najdba.group(4)) 
        dict['komentarji']=odstrani_vejico(najdba.group(5)) 
        dict['kudos']=odstrani_vejico(najdba.group(6)) 
        dict['bookmarks']=odstrani_vejico(najdba.group(7)) 
        dict['hits']=odstrani_vejico(najdba.group(8)) 
        poglavja=vzorci_poglavja.search(fanfic)
        dict['napisana poglavja']=poglavja.group(1)
        dict['vsa poglavja']=poglavja.group(2) if poglavja.group(2)!='?' else "ni podatka"
        avt=avtor.search(fanfic)
        if avt:
            dict['avtor']=avt.group(1)
        else:
            dict['avtor']='ni podatka'
        dicts.append(dict)
    return dicts


    