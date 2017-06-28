__author__ = 'Tena'

import os
from os.path import basename

path2 = os.path.abspath(r'/home/martina/STROJNO UČENJE/Strojno-ucenje/Inception v3 transfer learning/vectors') #mjesto gdje se nalaze svi vektori

#all_vectors je prazan file u koji se pisu svi vektori
with open(r'/home/martina/STROJNO UČENJE/Strojno-ucenje/Inception v3 transfer learning/all_vectors.txt', 'w') as outfile:
    for filename in os.listdir(path2):
        with open(os.path.join(path2, filename),encoding='utf-8', errors='replace') as infile:
            outfile.write(infile.read() + "\n")