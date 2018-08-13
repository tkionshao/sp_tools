from pprint import pprint
res_list = []

def getDiff(list):
    res_list = []
    for i in list[0]:
        count = 0
        for j in list[1]:
            if i.find(j) != -1:
                count += 1
        if count == 0:
            res_list.append(i)
    if len(res_list) == 0:
        print('THERE IS NOTHING DIFFERENCE BETWEEN THEM')
    return res_list

def getColNameFromSchema(schema_list):
    schema_list_ = [col.split(' ')[0] for col in schema_list]
    return schema_list

def read_cre_ins_sql(filename):
    schema_from_file = open(filename,'r',encoding='utf-8')
    lines = schema_from_file.read()
    schema_list = lines.split('\n')
    schema_list_ = [line.replace(',','').strip() for line in schema_list if line != '']
    return schema_list_

def read_slt_sql(filename):
    schema_from_file = open(filename,'r',encoding='utf-8')
    lines = schema_from_file.read()
    schema_list = lines.split('\n')
    schema_list_ = [line.strip() for line in schema_list if line != '']
    return schema_list_

def read_document_xlsx():pass
