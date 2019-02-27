#!/usr/bin/python3
import os
onnlist = open('dns_servers.txt')
def timetest(nameserver):
    names = ['ya.com', 'fb.com', 'cnn.com', '9gag.com', 'bbc.co.uk', 'habr.com', 'telesurtv.net', 'amazon.com', 'digitalocean.com', 'rt.com', 'my.com', 'ccc.de']
    sum = 0
    for n in names:
        com = 'dig @' + nameserver + ' ' + n
        out = os.popen(com).readlines()
        lineout = ''
        for o in out:
            if 'Query time' in o: lineout = o
        #print(n, '\t', lineout)
        sum += int(lineout.split(' ')[-2])
    midtime = sum / len(names)
    print(nameserver, '\t', 'Average time: ', int(midtime))   

line = 'not empty'
while line != '':
    line = onnlist.readline().rstrip()
    try:
        timetest(line)
    except IndexError: continue

