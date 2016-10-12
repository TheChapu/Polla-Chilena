import urllib2
from lxml import etree
import os

url       = urllib2.urlopen('http://www.polla.cl/cache/dgLastResultsForGame/es/Loto/1.xml')
contents  = url.read()
file = open("1.xml","w")
file.write(contents)
file.close()
doc       = etree.parse('1.xml')

fecha = doc.findtext("gameevents/gameevent/resulttime")
loto    = doc.findtext("gameevents/gameevent/gamedraws/gamedraw/name")
lotoresul = doc.findtext("gameevents/gameevent/gamedraws/gamedraw/resultsets/resultset/mainvalues")
revancha = doc.findtext("gameevents/gameevent/gamedraws/gamedraw[2]/name")
revancharesul = doc.findtext("gameevents/gameevent/gamedraws/gamedraw[2]/resultsets/resultset/mainvalues")
desquite = doc.findtext("gameevents/gameevent/gamedraws/gamedraw[3]/name")
desquiteresul = doc.findtext("gameevents/gameevent/gamedraws/gamedraw[3]/resultsets/resultset/mainvalues")
ahorasiquesi = doc.findtext("gameevents/gameevent/gamedraws/gamedraw[5]/name")
ahorasiquesiresul = doc.findtext("gameevents/gameevent/gamedraws/gamedraw[5]/resultsets/resultset/mainvalues")
jubilazo = doc.findtext("gameevents/gameevent/gamedraws/gamedraw[6]/name")
jubilazoresul =  doc.findtext("gameevents/gameevent/gamedraws/gamedraw[6]/resultsets/resultset/mainvalues")

print "Resultados Juegos de Azar " + fecha[:10]
print loto +" "+ lotoresul
print revancha + " "+ revancharesul
print desquite + " "+ desquiteresul
print ahorasiquesi + " " + ahorasiquesiresul
print jubilazo[:-2] + " "+ jubilazoresul
os.system("rm 1.xml")
