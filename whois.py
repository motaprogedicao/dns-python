#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# whois.py

import sys
try: 
    import whois
except:
    sys.exit("[!] Instale a biblio nmap com: pip install python-whois")

dominio = "teste.com.br"
consultaWhois = whois.whois(dominio)

print (consultaWhois.email) #1
print (consultaWhois["email"]) #2
print (consultaWhois.text) #3