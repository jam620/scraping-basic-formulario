#!/usr/local/bin/python3
# _*_ coding: utf8 _*_

import mechanize
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--buscar", help="Opción a buscar")
parser = parser.parse_args()


def main():
    if parser.buscar:
        bus = mechanize.Browser()
        bus.set_handle_robots(False)
        bus.set_handle_equiv(False)
        bus.addheaders = [("User-Agent",
                           "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3")]
        bus.open("https://www.google.com")

        #Permite encontrar los forms entro de la página
        '''for form in bus.forms():
            print(form)'''
        bus.select_form(nr = 0)
        bus["q"] = parser.buscar
        #fue modificado esta parte bus.submit asignando la variable
        #bus.submit()
        #
        responde = bus.submit()
        p = BeautifulSoup(responde.read(), "html5lib")
        for enlace in p.find_all("a"):
            #print(enlace.get("href"))
            url = enlace.get("href")
            url = url.replace("/url?q=", "")
            url = url.replace("/search?q=", "")
            print(url)
        #print(responde.read())

    else:
        print("Palabra a buscar")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("[-] Saliendo")
        exit()

