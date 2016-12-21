import re
import pickle

folders = open('folders.txt','r')

L = [] #list of all the matches in a file
D = {} # the dictionary that contains the data for each brand
d = {} #the dictionary comtaining the data for each model of each brand
keys = [] #keys for  d
values = []# values for d
b_key = [] #key for D
output_file = 'dict.pkl'

for folder in folders:
    D = {}
    b_key = re.findall(r'\/\w+\/',folder)
    fol = re.sub(r'\n','',folder)
    files = open(fol+'files.txt','r')
    for fl in files:
        fl_stripped = re.sub(r'\n','',fl)

        f = open(fol+fl_stripped,'r')

        r = re.compile(r'productObj\d+\s+\=\s+\{[\w\W]+\}\;?')
       # L = []
        #D = {}
        #d = {}
        #keys = []
        #values = []
        for line in f:
            keys=[]
            values=[]
            d_key = ''
            m = r.findall(line)
            if m:
                L.append(m)
#        print(m) 
                x = re.findall(r'\{[\w\W]+\}',m[0])
                y = re.sub(r'\{|\}','',x[0])
                c = re.split(r',',y)
        #print(c)
                for e in c:
                    f = re.sub(r'\"','',e)
                    n = re.sub(r'\s+$','',f)
                    z = n.split(':')
                    keys.append(z[0])
                    values.append(z[1])
                    if(z[0]=='id'):
                        d_key = z[1]
            if(not len(keys)==0 and not len(values)==0):
                d[d_key] = dict(zip(keys,values))

#print(d)
        #f.close()
        if b_key[0] not in D:
            D[b_key[0]] = [d]
        else:
            D[b_key[0]].append(d)
    output = open(fol+output_file,'wb')
    pickle.dump(D,output)
    output.close()
   # files.close()

folders.close()

#D['longines'].append(d)
#print(D)



