#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:44:31 2023

@author: carlosdm
"""
from pyspark import SparkContext
import sys



def main(infile, outfile):
    with SparkContext() as sc:
        sc.setLogLevel("ERROR")
        data = sc.textFile(infile)
        words_rdd = data.map(lambda x: len(x.split()))
        count = words_rdd.sum()
        with open(outfile, 'w') as outfile: 
            outfile.write("El numero total de palabras en el fichero {} es: {}".format(infile, count))
        

if __name__ == "__main__":
    if len(sys.argv)<3:
       print(f"Usage: {sys.arv[0]} <infile> <outfile> ")
       exit(1)
    infile = sys.argv[1]
    outfile = sys.argv[2]
    main(infile, outfile)