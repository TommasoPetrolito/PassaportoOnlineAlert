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
    'https://www.passaportonline.poliziadistato.it/GestioneDisponibilitaAction.do?codop=getDisponibilitaCittadino'

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
wrong_dates = ["06/03/2023", "07/03/2023", "08/03/2023", "13/03/2023", "29/03/2023", "03/04/2023", "05/04/2023"]
wrong_questura = "50"


def main():
    cookies = {'JSESSIONID': 'ah1-T3cyJZF-FFqsstEJImj2;Secure;HttpOnly'}
    while True:
        page = requests.get(URL, cookies=cookies)
        dom = html.fromstring(page.content)

        # LOGGER.info(f"Checking {str(key)}: {commissariati[key]}")
        naviga_disponibilita = ""
        try:
            naviga_disponibilita = \
                dom.xpath(f"//table[@class='naviga_disponibilita']//tr//td")[1].text
            naviga_disponibilita = naviga_disponibilita.strip()
            LOGGER.info(f"Data: {naviga_disponibilita}")
        except:
            LOGGER.info(f"ERRORE: nessuna data nel navigatore di disponibilitè, forse il glitch è rientrato.")

        if naviga_disponibilita != "" and datetime.strptime(naviga_disponibilita, '%d/%m/%Y') < data_in_cui_ho_una_prenotazione:
            list_disponibilita = \
                dom.xpath(f"//table[@class='list_disponibilita']/tbody/tr/td[@headers='descrizione']/a/@href")
            for disponibilita in list_disponibilita[1:]:
                if f"idRegista={wrong_questura}&" in disponibilita and naviga_disponibilita in wrong_dates:
                    continue
                else:
                    LOGGER.info(f"Data disponibile; URL: https://www.passaportonline.poliziadistato.it/{disponibilita}")
        time.sleep(7)


if __name__ == '__main__':
    start_time = time.time()
    main()
    elapsed_time = time.time()
    print("Total elapsed: %.2f" % elapsed_time)
