class XMLParser:

    def __init__(self, xml_string):
        self.parsedString = ""
        self.xml_iterator_parser(xml_string)

    def xml_iterator_parser(self, input_node):
        if input_node.hasChildNodes():
            for Node in input_node.childNodes:
                self.xml_iterator_parser(Node)
        elif input_node.nodeType == input_node.TEXT_NODE:
            self.parsedString += input_node.nodeValue.encode('utf-8').strip(' ')

    def get_string(self):
        return self.parsedString.strip()
