import time
import logging
import requests
from lxml import html
import winsound
from datetime import datetime

logging.basicConfig(format='%(asctime)s [%(module)s][%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

LOGGER = logging.getLogger("main")

URL = \
    'https://www.passaportonline.poliziadistato.it/CittadinoAction.do?codop=resultRicercaRegistiProvincia&provincia=TO'

commissariati = {
    51: "Torino Barriera di Milano",
    53: "Torino Barriera Nizza",
    54: "Torino San Donato",
    55: "Torino San Paolo",
    58: "Torino San Secondo",
    59: "Torino Dora",
    60: "Torino Madonna di Campagna",
    42: "Bardonecchia",
    47: "Ivrea",
    49: "Rivoli",
    57: "Torino Centro",
    56: "Torino Borgo Po",
    61: "Torino Mirafiori",
#    40: "Questura di Torino"
                }
# questura buggata: id = 40; "Questura di Torino"

data_in_cui_ho_una_prenotazione = datetime.strptime('07-04-2023', '%d-%m-%Y')


def main():
    cookies = {'JSESSIONID': 'kW4HtskwOx8G3-aPt+nWDaip;Secure;HttpOnly'}
    while True:
        page = requests.get(URL, cookies=cookies)
        dom = html.fromstring(page.content)
        for key in commissariati.keys():
            # LOGGER.info(f"Checking {str(key)}: {commissariati[key]}")
            disponibilita = "No"
            seleziona_struttura = ""
            try:
                disponibilita = \
                    dom.xpath(f"//table[1]/tbody/tr[@id='{str(key)}']/td[@headers='disponibilita']")[0].text
                # LOGGER.info(f"Disponibilità: {disponibilita}")
                seleziona_struttura = \
                    dom.xpath(f"//table[1]/tbody/tr[@id='{str(key)}']/td[@headers='selezionaStruttura']/a/@href")[0]
                # LOGGER.info(f"HREF: {seleziona_struttura}")
            except:
                disponibilita = "No"

            if "si" in disponibilita.lower():
                # esempio https://www.passaportonline.poliziadistato.it/GestioneCalendarioCittadinoAction.do?codop=mostraCalendario&idRegista=40&data=06-03-2023
                check_page_URL = f"https://www.passaportonline.poliziadistato.it/{seleziona_struttura}"
                # LOGGER.info(f"Page to be checked: {check_page_URL}")
                splitter_string = "&data="
                data = seleziona_struttura.split(splitter_string)[1]
                # LOGGER.info(f"Date: {data}")
                datetime_object = datetime.strptime(data, '%d-%m-%Y')
                if datetime_object < data_in_cui_ho_una_prenotazione:
                    winsound.Beep(440, 500)
                    LOGGER.info(f"Date e orari disponibili a {commissariati[key]}")
                    LOGGER.info(f"URL: {check_page_URL}")
        time.sleep(7)


if __name__ == '__main__':
    start_time = time.time()
    main()
    elapsed_time = time.time()
    print("Total elapsed: %.2f" % elapsed_time)
