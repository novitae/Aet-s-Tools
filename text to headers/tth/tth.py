from json import dumps

def fromCLI() -> print and str:
    """Prints a very short tutorial text for people using from CLI."""
    print('[ TXT -> HEADERS ] Paste your text, then hit Enter two times to get the it in Dict.')
    text = []
    while True:
        In = input()
        if In == "":
            break
        text.append(In)
    return txtToHeaders("\n".join(text))

def txtToHeaders(text:str,toDict:bool=False) -> str or dict:
    """Returns in str or dict the input text
    - text: headers under str format (each line must be separeted with "\n" and key separated from value with ":\"
    - toDict: returns a dict instead of a str"""
    o = {}
    for line in text.split("\n"):
        s = line.split(": ",1)
        if type(s) is str:
            s = s.split(":",1)
        o[s[0]] = s[-1]
    return (o if toDict else dumps(o,indent=4))
