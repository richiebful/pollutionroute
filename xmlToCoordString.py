import xml.etree.ElementTree as ET
import sys

tree = ET.parse(sys.argv[1])
root = tree.getroot()
print(root.tag)

ns = {'def':'http://www.topografix.com/GPX/1/1'}
points = root.findall('.//def:trkpt', ns)

def toTuple(e):
    return (e.get('lat'), e.get('lon'))

ptstring = [toTuple(p) for p in points]
print(list(ptstring))
