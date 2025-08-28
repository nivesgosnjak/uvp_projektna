## funkcije potrebne za zapis prve csv datoteke

import re
from pisanje_datotek import url_to_string

#########################################################
# vzorci

# poišče link in vrsto
link_vrsta=re.compile(r"<li id=\"medium_.*?href=\"(.*?)\">(.*?)</a>",re.DOTALL)

# poišče ime fandoma in število del v njem
fandom_st=re.compile(r"<a class=\"tag\" href=\".*?\">(.*?)</a>.*?\((.*?)\)",re.DOTALL)


##########################################################


def najdi_url(besedilo):
    """ Funkcija najde dodatek linka za dostop 
    do spletne strani posamezne vrste fandoma
    in njegovo ime, izpusti kategorijo 'Uncategorised
    Fandoms' """
    seznam=link_vrsta.findall(besedilo)
    return seznam[:-1]

def seznam_fandomov(url):
    """ Funkcija najde vse fandome in 
    število del v njih, vrne seznam tuplov"""
    besedilo=url_to_string(url)
    seznam= fandom_st.findall(besedilo)
    return seznam

def fandom_to_dict(sez_url,url):
    """ Funkcija sprejme seznam povezav do vrst fandomov,
    vrne seznam slovarjev z vrsto fandoma, naslovom fandoma in
    številom del"""
    dicts=[]
    for el in sez_url:
        link=url+el[0]
        vrsta=el[1].replace("&amp;", "&")
        naslov_st=seznam_fandomov(link)
        for el1 in naslov_st:
            dict={}
            dict["vrsta fandoma"]=vrsta
            dict["fandom"]=el1[0]
            dict["število del"]=int(el1[1])
            dicts.append(dict)
    return dicts


