import argparse
import os
from stringcolor import *

RPATH = os.path.dirname(__file__)+'/r.txt'

def make_int_ref(s):
    return '.'.join([str(len(e)) for e in s.split('.')])

def make_ref_list(up):
    import requests
    d = requests.get('https://gist.githubusercontent.com/ammarshah/f5c2624d767f91a7cbdc4e54db8dd0bf/raw/660fd949eba09c0b86574d9d3aa0f2137161fc7c/all_email_provider_domains.txt').text
    open(RPATH, 'w').close()
    for r in d.split('\n'):
        s = make_int_ref(r)
        c = '#'.join([f'{l}={str(i)}' for i, l in enumerate(r)])
        open(RPATH, 'a').write(f'{s};{r};{c}\n')
    print('-', bold('Updated')+' domain list' if up else bold('Downloaded')+' domain list')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('E', help='censored email or domain')
    parser.add_argument('-c', '--censor-char', type=str, help='the character designed to hide the other chars, by default "*"')
    parser.add_argument('-u', '--update', action='store_true', help='will update the list of domain the program is refering itself to')
    args = parser.parse_args()

    print(cs('e***l@d*****.f*****', 'LightSalmon3').underline()+cs(' ----> ', 'LightGrey14')+cs('e***l@domain.finder', 'SpringGreen5').underline())
    if not os.path.exists(RPATH) or args.update: make_ref_list(args.update)

    censoring_char = '*' if args.censor_char is None else args.censor_char
    censored_domain = args.E.split('@')[-1] if '@' in args.E else args.E
    censored_int_ref = make_int_ref(censored_domain)
    censored_ref = '#'.join([f'{l}={str(i)}' for i, l in enumerate(censored_domain) if not l in [censoring_char]])
    matching = []

    with open(RPATH, 'r') as R:
        for r in R.read().split('\n'):
            infos = r.split(';')
            if infos[0] == censored_int_ref:
                is_in = True
                ref = infos[2].split('#')
                for e in censored_ref.split('#'):
                    if not e in ref and is_in:
                        is_in = False
                if is_in:
                    matching.append(infos[1])
    
    if matching != []:
        print('Domains '+bold('matching')+' with '+args.E+' :')
        for match in matching:
            print(cs('~', 'SpringGreen5'), match)
    else:
        print(cs('No match found', 'Grey5').bold())

if __name__ == '__main__':
    main()