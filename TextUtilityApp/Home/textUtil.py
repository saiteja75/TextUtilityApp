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
    jsonVal = json.loads(text)
    return json.dumps(jsonVal, indent=3)