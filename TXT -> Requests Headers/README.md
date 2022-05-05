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
git clone https://github.com/novitae/Aet-s-Tools && cd Aet-s-Tools/'TXT -> Requests Headers'/ && pip install .

# Run from CLI:
tth
```
