#!/usr/bin/env python
#

## MAde by Louis Volant
## 2010-04-27

import os
import settings

def append_css(c,l,w,h,color):
    message_css = "div.c"+str(c)+"l"+str(l)
    message_css += "{position:absolute;left:"+str(c)+"px;top:"+str(l)+"px;"
    message_css += "width:"+str(w)+"px;height:"+str(h)+"px;background:#"+str(color)+";}\n"
    file = open(settings.OUTPUT_CSS_FILENAME,'a')
    file.write(message_css)
    file.close()
    
def append_html(c,l):
    message_html = "<div class=\"c"+str(c)+"l"+str(l)+"\"> </div>\n"
    file = open(settings.OUTPUT_HTML_FILENAME,'a')
    file.write(message_html)
    file.close()
    
def debuts_html():
    message_html = "<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">\n"
    message_html += "<html>\n<head>\n"
    message_html += "<meta content=\"text/html; charset=ISO-8859-1\" http-equiv=\"content-type\">\n"
    message_html += "<title>Page de test</title><style type=\"text/css\"></style>"
    message_html += "<link rel='stylesheet'  href='"+str(settings.OUTPUT_CSS_FILENAME)+"' type='text/css' media='all' />"
    message_html += "</head>\n\n<body>\n"

    file = open(settings.OUTPUT_HTML_FILENAME,'w')
    file.write(message_html)
    file.close()   
    if os.path.exists(settings.OUTPUT_CSS_FILENAME):
        os.remove(settings.OUTPUT_CSS_FILENAME)  
    
def finish_html():
    message_html = "</body></html>"
    file = open(settings.OUTPUT_HTML_FILENAME,'a')
    file.write(message_html)
    file.close()    
