#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    special_characters = ['.', '?', ':']
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in special_characters:
            result += "\n\n"

            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    

    print(result.strip())
