import xml.dom.minidom

# use the parse() function to load and parse an XML file
doc = xml.dom.minidom.parse("/tmp/files/Reports.xml");

# print out the document node and the name of the first child tag
print(doc.nodeName)
print(doc.firstChild.tagName)
# get a list of XML tags from the document and print each one
ScanReport = doc.getElementsByTagName("name")
print("%d Issues Detected" % ScanReport.length)

for name in ScanReport:
    name = doc.getElementsByTagName("name")[1]
    name1 = doc.getElementsByTagName("cweid")[1]
    name2 = doc.getElementsByTagName("count")[1]
    name3 = doc.getElementsByTagName("wascid")[1]
    name4 = doc.getElementsByTagName("riskdesc")[1]
    name5 = doc.getElementsByTagName("desc")[1]
    print('\n' + 'Threat Detected: ' + name.firstChild.data)
    print('Cwe ID: ' + name1.firstChild.data)
    print('Count: ' + name2.firstChild.data)
    print('wascid: ' + name3.firstChild.data)
    print('riskdesc: ' + name4.firstChild.data)
    print('desc: ' + name5.firstChild.data)
