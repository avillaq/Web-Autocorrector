import json
import re
import os
from collections import Counter, OrderedDict

from autocorrect.constants import word_regexes


def get_words(filename, lang, encd):
    word_regex = word_regexes[lang]
    capitalized_regex = r'(\.|^|<|"|\'|\(|\[|\{)\s*' + word_regexes[lang]
    with open(filename, encoding=encd) as file:
        for line in file:
            line = re.sub(capitalized_regex, "", line)
            yield from re.findall(word_regex, line)


def count_words(src_filename, lang, encd="utf-8", out_filename="word_count.json"):
    words = get_words(src_filename, lang, encd)
    counts = Counter(words)
    # make output file human readable
    counts_list = list(counts.items())
    counts_list.sort(key=lambda i: i[1], reverse=True)
    counts_ord_dict = OrderedDict(counts_list)
    with open(out_filename, "w") as outfile:
        json.dump(counts_ord_dict, outfile, indent=4)


def extraer_texto(ruta_carpeta, archivo_salida):
    # Se crea el archivo de salida
    with open(archivo_salida, "w", encoding="utf-8") as salida:
       for entry in os.scandir(ruta_carpeta):
            if entry.is_file() and entry.name.endswith(".tbf"):

                # Se abre un archivo del corpus 
                with open(entry.path, "r", encoding="windows-1252") as f:
                    palabras = []
                    texto = f.readlines()
                    for linea in texto:
                        match = re.search(r"\(\w+\s+([a-zA-ZáéíóúñÁÉÍÓÚÑ][\wáéíóúñÁÉÍÓÚÑ]*)\s+[\wáéíóúñÁÉÍÓÚÑ]+\)", linea)
                        if match:
                            palabra = match.group(1).replace("_", " ")
                            palabras.append(palabra)
                    
                    salida.write(" ".join(palabras) + "\n")