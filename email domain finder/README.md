# emdofi
### Simple python program to uncensor email domains;
e.g. : For people using [toutatis](https://github.com/megadose/toutatis), the obfuscated email domain's can be uncovered with this program.
```
python emdofi.py ********@g****.**m

e***l@d*****.f***** ----> e***l@domain.finder
Domains matching with ********@g****.**m :
~ games.com
~ gamil.com
~ gawab.com
~ globo.com
~ gmail.com
~ gmial.com
~ gustr.com
```
## Usage:
Installation
```
git clone https://github.com/novitae/emdofi; cd emdofi; pip install -r requirements.txt
```
Usage
```
# Works for emails
python emdofi.py my@******censored.****email
# And domain
python emdofi.py o****e.**
```
