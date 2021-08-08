import xml.etree.ElementTree as ET
import os
import sys

_ENCODING = 'utf-8'

def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem

def readFile():
    
    tree = ET.parse('bookstore.xml')
    root = tree.getroot()
    print(root.tag)

    ##update change file here
    for e in root.iter():
        print(e.tag, e.attrib)

    print(ET.tostring(root, encoding=_ENCODING).decode('utf8'))
    #write to file

    print('------------------- \n')
    for m in root:
        print(m)
    for m in root.findall("./magazine/subscription/[@per='year']"):
        print(m.attrib, m.text)

    for m in root.findall("./magazine/subscription/[@price='24']..."):
        print(m.attrib, m.text)

    for s in root.iter('book'):
        print(s.attrib)

    bf2 = root.find("./magazine/subscription/[@price='24']")
    print(bf2)

    bf2.attrib["price"] = '34'
    print(bf2.attrib)
    #for node in root.iter('subscription'):
      #  print(node.attrib)
    
    #for node in root.iter('first-name'):
     #   print(node.text)

    #for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
      #  print(movie.attrib)


    bf2 = root.findall("./bookstore/book/author/[@first-name='Joe']")

    print(bf2)
    #tree = ET.ElementTree(indent(root))
    tree.write('stuff.xml', xml_declaration= True, encoding=_ENCODING)
    



if __name__ == '__main__':
    
    print(sys.argv[1])
    readFile()

    isMaster = True
    writeMode = True