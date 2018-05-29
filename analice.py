from sets import Set
import re
import math
import urlparse
import MySQLdb
db = MySQLdb.connect(host="localhost", user="", passwd="", db="APACHE_MODSEC")
cur=db.cursor()
query="Select * from logs;"
cur.execute(query)
num_char=re.compile('\d')
alp_char=re.compile('[A-Za-z]')
special_char=re.compile('[^a-zA-Z\d]')
def entropy4(st):
    stList = list(st)
    alphabet = list(Set(stList)) # list of symbols in the string
    freqList = []
    for symbol in alphabet:
        ctr = 0
        for sym in stList:
            if sym == symbol:
                ctr += 1
        freqList.append(float(ctr) / len(stList))
    ent = 0.0
    for freq in freqList:
        ent = ent + freq * math.log(freq, 2)
    ent = -ent
    return ent
file = open("./datos2.csv", "w")
params=[]
for i in cur.fetchall():
#    print urlparse.urlparse(i[1])
    parameters=[]
    if i[0] == "82.223.66.86":
        for z in urlparse.urlparse(i[1]).query.split("&"):
            parameter = z.split("=")[0]
            if parameter in params:
                indice=params.index(parameter)
            else:
                params.append(parameter)
                indice=params.index(parameter)
            query = z[len(parameter)+1:]
            file.write("{0},{1}\n".format(i[1],"good"))
#            file.write("{0},{1},{2},{3},{4},{5},{6}\n".format(indice, len(query), entropy4(query), len(num_char.findall(query)), len(alp_char.findall(query)), len(special_char.findall(query)),"good"))
#            print[(indice, len(query), entropy4(query), len(num_char.findall(query)), len(alp_char.findall(query)), len(special_char.findall(query))),"good"]

            parameters.append((indice, len(query), entropy4(query), len(num_char.findall(query)), len(alp_char.findall(query)), len(special_char.findall(query))))
#    print(urlparse.urlparse(i[1]).path, parameters)
#    print(parameters)

    if i[0] == "82.98.177.181":
        for z in urlparse.urlparse(i[1]).query.split("&"):
            parameter = z.split("=")[0]
            if parameter in params:
                indice=params.index(parameter)
            else:
                params.append(parameter)
                indice=params.index(parameter)
            query = z[len(parameter)+1:]
            file.write("{0},{1}\n".format(i[1],"bad"))
#            file.write("{0},{1},{2},{3},{4},{5},{6}\n".format(indice, len(query), entropy4(query), len(num_char.findall(query)), len(alp_char.findall(query)), len(special_char.findall(query)),"bad"))
#            print[(indice, len(query), entropy4(query), len(num_char.findall(query)), len(alp_char.findall(query)), len(special_char.findall(query))),"good"]
            parameters.append((indice, len(query), entropy4(query), len(num_char.findall(query)), len(alp_char.findall(query)), len(special_char.findall(query))))
    print params
