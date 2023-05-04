# quijote_entrega

Este repositorio consta de 2 ficheros de python:
  - quijote_con_dado.py: Genera una programa que estraiga de forma aleatoria un porcentaje de las líneas de un fichere: se leen el fichero por líneas y se "tira un dado". Si el dado es menor que el porcentaje la línea se graba en el fichero de salida. Mediante este programa y con el ratio 0.3 obtenemos el fichero "quijote_s05.txt"
  - conteo_palabras.py: Cuenta las palabras de un "fichero.txt". Ejecutamos este programa con el fichero "quijote_s05.txt" y nos guarda el resultado en el fichero "out_quijote_s05.txt". Más tarde, ejecutaremos este programa con el fichero completo "quijote.txt" y nos guardará el resultado en el fichero "out_quijote.txt".

Finalmente, probaremos el programa en el cluster. Copiaremos el fichero "quijote.txt" en hadoop y ejecutaremos de nuevo el programa conteo_palabras.py. El resultado se almacena en el fichero  "out_hdfs.txt".

Adicionalmente, está adjuntada una captura de pantalla que demuestra el uso del cluster con mi usuario cdiez05 en cdiez05@wild.mat.ucm.es
