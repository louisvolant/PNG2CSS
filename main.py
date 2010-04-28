#!/usr/bin/env python
#

## MAde by Louis Volant
## 2010-04-27

"""Main function of PNG2CSS."""

__version__ = '1'

import application_exceptions
import create_htmlcss
from itertools import imap
import logger
import os
import png
import settings
import sys
import urllib
import traceback


def main(argv):
    """Main function of PNG2CSS."""
    try:
        logger.info("Start.")
        
        r=png.Reader(file=urllib.urlopen(settings.INPUT_PNG_FILENAME))
        r = list(r.read())
        logger.info(str(r))
        width = r[0]
        height = r[1]
        h = 0
        img = []
        l=r[2]
        color_count = []
        logger.info(str(l))
        for e in l: #pour chaque ligne
            compteur = 0 
            line = []
            cell = ""
            #logger.info("length : "+str(len(e)))
            for c in range(0,(3*width)):
                #logger.info(str(range(0,(3*width)-1)))
                compteur += 1
                #logger.info(str("valeur de c : ")+str(c))
                #logger.info(hex(int(e[c])))
                color = str(hex(int(e[c]))[2:])
                if len(color) == 1:
                    cell += "0"
                cell += color
                if compteur == 3:
                    compteur = 0 #remise a zero tous les 3 passages
                    line.append(cell)
                    color_count.append(cell)
                    cell = ""
            h += 1
            img.append(line)
        #logger.info(str(img))
        
        #Si on souhaite virer la couleur dominante
        color_each = list(set(color_count))
        color_max = ''
        max_count = 0
        for c in color_each:
            count = color_count.count(c)
            if count > max_count:
                max_count = count
                color_max = c      
        
        
        #La, on a l'image en RAM. On debute la premiere passe
        r = 0 #row
        c = 0 #column
        w = 1 #width
        h = 1 #height
        ttl = [] #liste des proprietes CSS a ecrire #ttl = total
        create_htmlcss.debuts_html()
        for line in img:
            for cell in line:
                if c < (width-1):
                    if line[c+1] == cell:
                        w = w + 1 #compression 1D
                    else:
                        ttl.append([c-w+1,r,w,h,cell]) 
                        w = 1 #on remet le compteur a son etat initial
                else:
                    ttl.append([c-w+1,r,w,h,cell])
                    w = 1 #on remet le compteur a son etat initial
                c+=1
            r+=1 #on incremente la ligne
            c = 0 #on revient a la ligne pour les colonnes
        
        #compression 2D
        ttl.sort()
        i = 0
        last = len(ttl)-1
        while i < last: #'len(ttl)-2' car on ne touche pas au dernier pixel
            t = ttl[i]
            u = ttl[i+1]
            if t[0]==u[0] and t[1]+t[3]==u[1] and t[2]==u[2] and t[4]==u[4]:
                u[1] = t[1]
                u[3] += t[3]
                ttl.remove(t)
                last -= 1
            else:
                i += 1
            
            
        #Ecriture du CSS et HTML
            #Compression avec le background
        create_htmlcss.append_css(0,0,width,height,color_max)
        create_htmlcss.append_html(0,0)
        for i in ttl:
            if not(i[4] == color_max):
                create_htmlcss.append_css(i[0],i[1],i[2],i[3],i[4])
                create_htmlcss.append_html(i[0],i[1])
        create_htmlcss.finish_html()
        logger.info("End.")
    except:
        e = traceback.format_exc()
        logger.error("Error during execution," \
                     + " error is: " + str(e))


if __name__ == "__main__":
    main(sys.argv[1:])
