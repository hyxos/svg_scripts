from yattag import Doc
from lxml import etree
from io import StringIO, BytesIO
import os

def gen_svg_wrapper(keys = {}, *arg):
    svg_id = keys['id']
    width = keys['width']
    height = keys['height']
    viewbox = keys['viewbox']
    doc, tag, text, line = Doc().ttl()
    with tag('svg',('version', '1.1'),('baseProfile','full'),
             ('id', svg_id),
             ('xmlns', 'http://www.w3.org/2000/svg'),
             ('xmlns:xlink', 'http://www.w3.org/1999/xlink'),
             ('width', width), ('height', height),
             ('viewBox', viewbox)):
        with tag('defs'):
            doc.asis(keys['defs'])
        doc.asis(keys['body'])
    document_root = etree.fromstring(doc.getvalue())
    pretty_svg =  etree.tostring(document_root, encoding='unicode',
                                  pretty_print=True)
    svg = """%s""" % (pretty_svg)
    return svg

def save_svg(keys = {}, *arg):
    path = keys['path']
    file_name = keys['file_name']
    svg = keys['svg']
    complete_name = os.path.join(path, file_name)
    with open(complete_name, "w") as file:
        file.write(svg)

test_svg = gen_svg_wrapper({'width': 100, 'height': 100, 'id': 'Spangler',
                 'defs': '', 'viewbox': '0 0 100 100',
                 'body': "<rect x='0' y='0' width='100' height='100' fill='black'></rect>"})

save_svg({'path': '.', 'file_name': 'test.svg', 'svg': test_svg})
