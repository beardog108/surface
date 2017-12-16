#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect('sites.db')
c = conn.cursor()

t = ('RHAT')
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)

schema = {'name': '', 'category': '', 'keywords': '', 'onion': '', 'zeronet': '', 'i2p': '', 'i2pHostname': '', 'freenet': '', 'ipfs': '', 'dat': ''}
newSite = schema
while True:
    print('''
    1. Add Site
    2. Remove site
    3. List sites
    4. Quit
    ''')
    choice = input('>').lower()
    if choice in ('4', 'quit'):
        break
    elif choice in ('1', 'add'):
        for i in schema.keys():
            print('Enter', i)
            entry = input('>')
            newSite[i] = entry

        c.execute("""INSERT INTO sites (name, onion, zeronet, i2p, i2pHostname, freenet, ipfs, dat, keywords, category) 
        VALUES('""" + newSite['name'] + "','" + newSite['onion'] + "','" + newSite['zeronet'] + "','" + newSite['i2p'] + "','" + newSite['i2pHostname'] + "','" + newSite['freenet'] + "','" + newSite['ipfs'] + "','" + newSite['dat'] + "','" + newSite['keywords'] + "','" + newSite['category'] + """')""")
        conn.commit()
    elif choice in ('2', 'remove'):
        id = input('Enter id: ')
        c.execute("Delete from sites where id=" + id)
        conn.commit()
    elif choice in ('3', 'list'):
        for row in c.execute('SELECT * FROM SITES ORDER BY ID'):
            print(str(row[0]) + ':' + row[1])