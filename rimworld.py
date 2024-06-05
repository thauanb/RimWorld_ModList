"""Reads information in a folder with RimWorld mods and saves it in a text file."""
import os
from lxml import etree as ET

class XmlReader:
    """Class to read information from XML files."""

    def __init__(self, path):
        """Initialize XmlReader with the path to the XML file."""
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()

    def read_about(self) -> list:
        """Read information from the XML file and return a list of name, author, and package_id."""
        name = self.root.find('name').text or "Sem Nome"
        author = self.root.find('author').text or "Sem Autor"
        package_id = self.root.find('packageId').text or "Sem ID"
        return [name, author, package_id]
    
    def get_xml_tree(self):
        """Return the XML tree."""
        return self.tree


RIMWORLD_PATH = r"D:\Programas\Steam\steamapps\workshop\content\294100"

def list_mods(path: str):
    """List all mods installed in the specified folder."""
    count = 0
    for pasta in os.listdir(path):
        mod_path = os.path.join(path, pasta)
        for root, _, files in os.walk(mod_path):
            for file in files:
                if file.endswith(".xml") and "About" in file:
                    count += 1
                    try:
                        xml_reader = XmlReader(os.path.join(root, file)).read_about()
                        name, author, package_id = xml_reader
                        folder = os.path.join(root, file).replace('\\\\About\\\\About.xml', '')
                        infos = f"{folder} -> {name} - {author} | {package_id}"
                        print(infos)
                        with open("mods.txt", "a", encoding="utf-8") as f:
                            f.write(f"{infos}\n")
                    except (FileNotFoundError, ET.ParseError) as e:
                        print(f"Erro ao processar o arquivo {file}: {e}")
    if count == 0:
        print("[-] Nenhum mod foi identificado")
    else:
        print(f"[+] {count} mods")

list_mods(RIMWORLD_PATH)
input()
