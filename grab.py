import requests


# Coded by Daywalker133

# Hacktoberfest2022
# Hackroberfun

from multiprocessing.dummy import Pool

from colorama import Fore

import os, sys, time

from platform import system

from colorama import Style

from colorama import init

init(autoreset=True)

fr = Fore.RED

fh = Fore.RED

fc = Fore.CYAN

fo = Fore.MAGENTA

fw = Fore.WHITE

fy = Fore.YELLOW

fbl = Fore.BLUE

fg = Fore.GREEN

sd = Style.DIM

fb = Fore.RESET

sn = Style.NORMAL

sb = Style.BRIGHT


try:

    os.system("title [+] Coded By Daywalker133 [+]")

except:

    pass


def checking():

    print("{}{} \n\t\tMass-WebScraping by Daywalker133".format(fr, sb))
    ips = raw_input("{}{} \n\t\tEnter Your List IPS: ".format(fg, sb))

    ips = open(ips, "r")

    for i in ips.readlines():

        done = i.rstrip()

        try:

            done = done.rstrip()

            bing = requests.get(
                "http://api.hackertarget.com/reverseiplookup/?q=" + done
            )

            if "." in bing.content:

                print("{}{}" + (bing.content)).format(fy, sb)

                with open("Snatched.txt", "a") as o:

                    o.writelines(bing.content + "\n")

            else:

                pass

        except:

            pass


checking()
