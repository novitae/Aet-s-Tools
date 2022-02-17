# TXT to (requests) HEADERS
**Turns**
```
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: fr-fr
Connection: keep-alive
Accept-Encoding: gzip, deflate, br
```
**to**
```
{
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "fr-fr",
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate, br",
}
```
**_(dict or str)_**
## Usage
```python
# Install with:
git clone https://github.com/novitae/tth && python tth/setup.py install

# Run from CLI:
tth

# Run as a module:
from tth.tth import txtToHeaders

myHeaders = txtToHeaders(text="""Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: fr-fr
Connection: keep-alive
Accept-Encoding: gzip, deflate, br""", toDict=True)
# toDict on True will return a dict instead of a str
```
