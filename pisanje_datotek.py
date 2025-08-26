import requests
import os
import csv


def url_to_string(link):
    """ Funkcija prevede vsebino spletne strani
    v besedilo """
    return requests.get(link).text

def text_to_file(text, directory, filename):
    """ Funkcija zapiše besedilo v datoteko """
    os.makedirs(directory, exist_ok=True)
    pot=os.path.join(directory, filename)
    with open(pot, 'w', encoding='UTF-8') as file_out:
        file_out.write(text)
    return None


def zapisi_v_csv(seznam, directory, filename):
    """ Funkcija sprejme seznam slovarjev in jih 
    v obliki csv datoteke zapiše v dan daoteko in mapo,
    pri tem so stolpci ključi slovarjev"""
    stolpci=list(seznam[0].keys())
    os.makedirs(directory, exist_ok=True)
    pot=os.path.join(directory, filename)
    with open(pot, 'w', encoding='UTF-8', newline='') as csv_file:
        writer=csv.DictWriter(csv_file, fieldnames=stolpci)
        writer.writeheader()
        writer.writerows(seznam)
    return 