import urllib2
from bs4 import BeautifulSoup
url       = urllib2.urlopen('http://www.polla.cl/cache/dgLastResultsForGame/es/Loto/1.xml')
contents  = url.read()
parse=BeautifulSoup(contents , "lxml")
fecha = parse.find("resulttime").text
loto = parse.findAll("mainvalues")
#Imprime Datos
print "Fecha: " + fecha[:10]
print "LOTO: " + loto[0].text
print "REVANCHA: " + loto[1].text
print "DESQUITE: " + loto[2].text
print "AHORA SI QUE SI: " + loto[4].text
print "JUBILAZO: " + loto[5].text
#Creado con todo el <3 ThebloodSys!
