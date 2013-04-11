#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys
import codecs

# Paramètres pour les mots outils
delimiter = '/'

# Variables d'entrée/sortie
input_file = sys.argv[1]
output_file = sys.argv[2]

# Lecture du fichier de phrases étiquetées
buffer_ecriture = ''
for line in codecs.open(input_file, 'r', 'utf-8'):

    # Découpage de la ligne en tokens_pos
    tuples = line.strip().split(' ')
    nb_mots = len(tuples)

    # Test si la ligne n'est pas vide
    if nb_mots > 0:
        buffer_phrase = '\t<sentence nb_words="'+str(nb_mots)+'"><![CDATA['

        for i in range(nb_mots):

            matches = re.match('^(.+)/([^/]+)$', tuples[i])

            if not matches:
                print "problème : ", tuples[i]
            else:
                token = matches.group(1)
                pos = matches.group(2)
                buffer_phrase += token + delimiter + pos + ' '

        # Nettoyage de la phrase et ajout dans le buffer
        buffer_phrase = buffer_phrase.strip() + ']]></sentence>\n'
        buffer_ecriture += buffer_phrase

# Ecriture du fichier de sortie
handle = codecs.open(output_file, 'w', 'utf-8')
handle.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
handle.write('<cluster>\n')
handle.write(buffer_ecriture)
handle.write('</cluster>')
handle.close()












    