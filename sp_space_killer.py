#!/bin/python
'''
set the import file as named 'sample.sql' in the same folder with main moduleself.
Then execute commandline 'python sp_space_killer.py'
There will be an file named 'output.sql' in the sane placeself.
'''
from pprint import pprint as pp
with open('sample.sql','r',encoding='utf-8') as f:
    res_list = []
    not_include_list = []

    sample_list = f.read().split('\n')
    lines = f.readline()
    for col in sample_list:
        if col != '':
            res_list.append(col)
        else:
            not_include_list.append(col)

    pp(res_list)
    print(len(res_list))
    print(not_include_list)

with open('output.sql','w',encoding='utf-8') as f:
    for col in res_list:
        f.write(col+'\n')
        print(col)
