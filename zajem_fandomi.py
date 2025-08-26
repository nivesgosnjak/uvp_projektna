## funkcije potrebne za zapis prve csv datoteke

import re
from pisanje_datotek import url_to_string


link_vrsta=r"<li id=\"medium_.*?href=\"(.*?)\">(.*?)</a>"

def najdi_url(besedilo):
    """funkcija najde dodatek linka za dostop 
    do spletne strani posamezne vrste fandoma
    in njegovo ime, ki je še vedno nespremenjeno, ups"""
    seznam=re.findall(link_vrsta, besedilo)
    # pod imenom "Uncategorised fandoms" so zgolj dela, ne tudi njihova pripadnost
    return seznam[:-1]

fandom_st=r"<a class=\"tag\" href=\".*?\">(.*?)</a>.*?\((.*?)\)"


def seznam_fandomov(url):
    """funkcija najde vse fandome in 
    število del v njih, vrne seznam tuplov"""
    besedilo=url_to_string(url)
    seznam= re.findall(fandom_st, besedilo, flags=re.DOTALL)
    # for el in seznam:
    #     if int(el[1])<50:
    #         seznam.remove(el)
    return seznam

def fandom_to_dict(sez_url,url):
    """funkcija dobi seznam povezav do vrst fandomov,
    vrne seznam slovarjev z vrsto fandoma, naslovom fandoma in
    število del"""
    dicts=[]
    for el in sez_url:
        link=url+el[0]
        vrsta=el[1].replace("&amp;", "&")
        naslov_st=seznam_fandomov(link)
        for el1 in naslov_st:
            dict={}
            dict["vrsta_fandoma"]=vrsta
            dict["fandom"]=el1[0]
            dict["število_del"]=int(el1[1])
            dicts.append(dict)
    return dicts


