from xml.dom import minidom
import os

def getProgrammeXml():
	parseData = minidom.parse("config\Pyconfig.xml")
	configData = parseData.getElementsByTagName('programeentry')
	progConfigXml = ""
	progConfigXmlPath = ""
	for i in configData:
		if os.path.basename(__file__) == i.childNodes[1].firstChild.data:
			progConfigXml = i.childNodes[3].firstChild.data
			progConfigXmlPath = i.childNodes[5].firstChild.data
	if progConfigXml != "":
		print (progConfigXml)
		print (progConfigXmlPath)
		
getProgrammeXml()