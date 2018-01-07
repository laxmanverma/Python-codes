import json
import xmltodict
 
def convert(xml_attribs=True):
    with open("eduNewsfeed.xml", "rb") as f:    # notice the "rb" mode
        data = xmltodict.parse(f, xml_attribs=xml_attribs)
    with open("json_file.json", "w") as f:
        f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))	#separators=(item_separator, key_separator)
        #f.write(json.dumps(data))

convert()
