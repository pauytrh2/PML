from sys import argv
from pml_to_html import pml_to_html
from os import makedirs as mkdir, path, system as run
from shutil import rmtree as rmdir
from time import sleep
import webbrowser
from pauyerror import PauyError

if len(argv) < 2:
    raise PauyError("Please provide an input file UwU")
pml_file = argv[1]

with open(pml_file, "r") as file:
    content = file.read()
    html = pml_to_html(content)

try:
    rmdir("temp")
except:
    pass
mkdir("temp", exist_ok=True)

with open("temp/temp.html", "w") as html_file:
    html_file.write(html)

webbrowser.open("file://" + path.abspath("temp/temp.html"))