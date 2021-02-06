import json

def removePunctuations(text):
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
  
    for ele in text:  
        if ele in punc:  
            text = text.replace(ele, "") 
    
    return text

def ConverUpperCase(text):
    return text.upper()

def beautifyJson(text):
    text.replace('{',"{\n")
    text.replace(',',",\n")
    text.replace('}',"\n}")
    return text

def ConvertLowerCase(text):
    return text.lower()