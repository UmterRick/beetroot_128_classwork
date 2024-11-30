# beautifulsoup4
# scrapy

class Node:
    def __init__(self, tag, attributes=None, children=None):
        self.tag = tag
        self.attributes = attributes
        self.children = children if children else []

    def __repr__(self):
        return f"HtmlNode(<{self.tag}>, {self.attributes}, children={len(self.children)})"




class HtmlParser:
    def __init__(self, html_file_path):
        with open(html_file_path) as file:
            self.html = file.read()

        self.index = 0

    def parse(self):
        return self._parse_node()

    def _parse_node(self):
        if self.html[self.index] != "<":
            self.index += 1
            return None

        self.index += 1
        tag_name = []
        attributes = {}
        while self.html[self.index] not in [">", " "]:
            tag_name.append(self.html[self.index])
            self.index +=1

        tag_name = "".join(tag_name)

        while self.html[self.index] != ">":
            if self.html[self.index] == " ":
                self.index += 1
                attr_name = []
                while self.html[self.index] != '=':
                    attr_name.append(self.html[self.index])
                    self.index += 1
                self.index += 2 # skip = and  opening "
                attr_value = []
                while self.html[self.index] != '"':
                    attr_value.append(self.html[self.index])
                    self.index += 1

                self.index += 1 # skip closing "
                attributes["".join(attr_name)] = "".join(attr_value)
            else:
                self.index += 1


        self.index += 1
        children = []
        while not self.html.startswith(f"</{tag_name}>", self.index):
            child = self._parse_node()
            if child:
                children.append(child)

        self.index += len(f"</{tag_name}>")
        return Node(tag_name, children=children)


def find_nodes_by_tag(tree, tag_name):
    results = []

    def dfs(node):
        if node.tag == tag_name:
            results.append(node)
        for child in node.children:
            dfs(child)

    dfs(tree)
    return results

parser = HtmlParser("example.html")
parser.parse()


nodes = find_nodes_by_tag("li")
print(nodes, sep="\n")



