"""
projekt_3.py: 3 projekt: Engeto Online Python Akademie
author: Michal Slabý
email: michalslaby1@gmail.com => v Engeto založeno pod jakub.rutkowski@allegro.pl
discord: michals._68964
"""

import sys
import csv
from bs4 import BeautifulSoup
import requests


def get_codes_links(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    links = ["https://volby.cz/pls/ps2017nss/" + link["href"]
             for link in soup.find_all("a") if link.text.isnumeric() and len(link.text) == 6]
    codes = [link.split("/")[-1].split(".")[0] for link in links]
    return codes, links


def header_ww(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    header = ["code", "location", "registered", "envelopes", "valid"]
    header += [subject.text for subject in soup.find_all("td")[10::5] if subject.text != "-"]
    return header

def get_units(links, codes):
    data = []
    for link, code in zip(links, codes):
        unit_data = requests.get(link)
        unit_data_bs = BeautifulSoup(unit_data.text, "html.parser")
        unit = [code]
        unit.append(str(unit_data_bs.find_all("h3")[2].text).split(":")[1].strip())  # location
        unit.append("".join(str(unit_data_bs.find_all("td")[3].text).split()))  # registered
        unit.append("".join(str(unit_data_bs.find_all("td")[4].text).split()))  # envelopes
        unit.append("".join(str(unit_data_bs.find_all("td")[7].text).split()))  # valid
        unit += [party.text for party in unit_data_bs.find_all("td")[11::5]]
        data.append(unit)
    return data

def scrape_data(url, output_file):
    codes, links = get_codes_links(url)
    header = header_ww(links[0])
    data = get_units(links, codes)
    export_data(output_file, header, data)
    print("Dokončeno.")

def export_data(output_file, header, data):
    with open(output_file, "w", newline="") as file:
        print("Export do csv", file.name)
        file_writer = csv.writer(file, delimiter=";")
        file_writer.writerow(header)
        file_writer.writerows(data)


def main():
    if len(sys.argv) != 3:
        print("Zadané chybné parametry. Použijte: python projekt_3.py [adresa] [název_souboru]")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2] + ".csv"

    scrape_data(url, output_file)


if __name__ == "__main__":
    main()
