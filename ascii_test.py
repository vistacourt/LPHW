import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

def logo():
    cprint(figlet_format('Dodo Quest!', font='speed'),
           'yellow',  attrs=['bold'])
