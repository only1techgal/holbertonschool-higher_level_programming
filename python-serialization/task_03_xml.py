#!/usr/bin/python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary into an XML file."""
    # Create the root element
    root = ET.Element("data")

    # Iterate over dictionary items and add them as child elements
    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)  # Converts the value to a string
        root.append(child)

    # Create an ElementTree object and write it to the specified file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserializes an XML file into a Python dictionary."""
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Iterate over the XML elements and reconstruct the dictionary
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text

        return dictionary

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

    except ET.ParseError:
        print(f"Error: Failed to parse XML from file '{filename}'.")
        return None
