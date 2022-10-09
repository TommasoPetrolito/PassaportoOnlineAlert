import time
import logging
import requests
from lxml import html
import winsound

logging.basicConfig(format='%(asctime)s [%(module)s][%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

LOGGER = logging.getLogger("main")

URL = 'https://www.passaportonline.poliziadistato.it/GestioneDisponibilitaAction.do?codop=getDisponibilitaCittadino'


def main():
    cookies = {'JSESSIONID': 'DyD1G8k9MlQ8DfrU6VR0sMqc;Secure;HttpOnly'}
    while True:
        page = requests.get(URL, cookies=cookies)
        dom = html.fromstring(page.content)
        try:
            res = dom.xpath('//*[@id="message_box_xl_dispo"]/table[1]/tr/td[2]/p')[0].text
        except:
            res = ""
        finally:
            if not "Non ci sono" in res:
                winsound.Beep(440, 500)
                LOGGER.info("Qualcosa è cambiato")
            else:
                LOGGER.info("no dispo")
        time.sleep(7)


if __name__ == '__main__':
    start_time = time.time()
    main()
    elapsed_time = time.time()
    print("Total elapsed: %.2f" % elapsed_time)
