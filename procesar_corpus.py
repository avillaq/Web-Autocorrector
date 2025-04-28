from autocorrect.word_count import count_words, extraer_texto

extraer_texto(ruta_carpeta="cess_esp_corpus", archivo_salida="data/cess_esp_texto.txt")
count_words(src_filename="data/cess_esp_texto.txt", lang="es", encd="utf-8", out_filename="data/cess_esp_word_count.json")