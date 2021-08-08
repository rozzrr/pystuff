import os
import sys
import xml.etree.ElementTree as ET

def validateScriptParams(param):
    isValid = False
    if param in ['master', 'm', 'M', 'Master']:
        isValid = True
    return isValid


def xmlParser():
    tree = ET.parse(xmlDir + "\\" + 'bookstore.xml')
    root = tree.getroot()
    print(ET.tostring(root, encoding='utf-8').decode('utf8'))
   
    masterElementConfig = root.find("./magazine/subscription/[@price='36']")
    masterElementConfig.attrib['price'] = '36'
    
    print(root.tag)
    m2 = root.find("./book/author/first-name")
    print(m2.text)
    m2.text = "Steven"

    print(m2.text)

    print('changed slave mode to ', MasterMode)

    #tree.write(xmlDir + "\\" + 'bookstore.xml', xml_declaration= True, encoding='utf-8')
    
if __name__ == '__main__':
    try:
        MasterMode = False
        xmlDir = 'C:\Data'
        if len(sys.argv) > 1:
            masterInput = sys.argv[1]
            if validateScriptParams(sys.argv[1]):
                MasterMode = True
        if os.path.exists(xmlDir):
            print('Path is valid')
            print('Master mode set to ', MasterMode)

        else:
            print('invalid path to directory, change config file and retry')
        
        xmlParser()
    except Exception as e:
        print(e)
        sys.exit(0)

    

   
    