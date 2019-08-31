from xml.dom import minidom

def getFileDetailsXml(fileName):
	parseData = minidom.parse("..\config\Pyconfig.xml")
	configData = parseData.getElementsByTagName('programeentry')
	progConfigXml = ""
	progConfigXmlPath = ""
	for i in configData:
		if fileName == i.childNodes[1].firstChild.data:
			progConfigXml = i.childNodes[3].firstChild.data
			progConfigXmlPath = i.childNodes[5].firstChild.data
	if progConfigXml != "":
		mapping = {"XMLName" : progConfigXml}
		mapping['XMLPath'] = progConfigXmlPath
		relativePath = ".." + progConfigXmlPath
		parseDataSub = minidom.parse(relativePath)
		progData = parseDataSub.getElementsByTagName('datapath')
		mapping['InputPath'] = progData[0].getElementsByTagName('subrootin')[0].firstChild.data
		mapping['OutputPath'] = progData[0].getElementsByTagName('subrootout')[0].firstChild.data
	return (mapping)