#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# dns.py

"""
Esse arquivo enumera servidores de DNS

"""

import socket
dominio = "google.com.br"
nomes = ["ns1", "ns2", "www", "ftp", "intranet"]

for nome in nomes:
    DNS = nome + "." + dominio
    try:
        print(DNS + ": " + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass