#coding:utf-8
import re,os
from functools import reduce

class ConfigAnalysis():
    def __init__(self):
        self.__update_log = {}
        self.__add_log = {}
        self.__config = None
        self.__configfilename = None
    def __validitycheck(self,lines,configfilename):
        for line_number in range(len(lines)):
            if (not re.match(r'^#', lines[line_number])) and (not re.match(r'^(\r\n|\r|\n)',lines[line_number])) and (not re.match(r'^[a-zA-Z0-9](\w|\.| |\t)*\=( |\t)*(\S){1,}', lines[line_number])):
                raise SyntaxError("The configuration file (%s) have SyntaxError(%s) in line %s"%(configfilename,lines[line_number],line_number))
    def __analysisfile(self,configfilename):
        with open(configfilename,'r') as Contents:
            lines = Contents.readlines()
        self.__validitycheck(lines,configfilename)
        return [re.match(r'^[a-zA-Z0-9](\w|\.| |\t)*\=( |\t)*(\S){1,}', line).group() for line in lines if re.match(r'^[a-zA-Z0-9](\w|\.| |\t)*\=( |\t)*(\S){1,}', line)]
    def __analysislines(self,vaild_lines):
        return [re.split(r'( |\t)*\=( |\t)*',i,maxsplit=1) for i in vaild_lines]
    def read(self,configfilename):
        if os.path.exists(configfilename):
            if os.path.isfile(configfilename):
                self.__config = [(item[0],item[-1]) for item in  self.__analysislines(self.__analysisfile(configfilename))]
            else:
                raise IOError('"%s" is not a file.'%configfilename)
        else:
            raise FileNotFoundError('No such file or directory:"%s"'%configfilename)
    def keys(self):
        return [ckey for ckey,_ in self.__config]
    def get(self,key):
        for ckey,cvalue in self.__config:
            if ckey == key:
                return cvalue
        raise KeyError("Maping key not found.('%s')"%key)
    def update(self,key,newvalue):
        if re.match(r"(\S){1,}",newvalue) and if re.match(r"^(\S){1,}",newvalue).group()==newvalue:
            self.__update(key,newvalue)
        else:
            raise ValueError("Unsupported value.(Only support Non-blank characters)")
    def __update(self,key,newvalue):
        for i in len(self.__config):
            if self.__config[i][0]==key:
                self.__config[i]=(key,newvalue)
                self.__update_log[key]=newvalue
                return True
        raise KeyError("Maping key not found.('%s')"%key)
    def add(self,key,value):
        if re.match(r"(\S){1,}",value) and if re.match(r"^(\S){1,}",value).group()==value:
            if re.match(r'^[a-zA-Z0-9](\w|\.)*$',key):
                self.__add(key,value)
            else:
                raise KeyError("Unsupported Key.(The key must start with a number or letter and only support ['number','letter','_','.'])")
        else:
            raise ValueError("Unsupported value.(Only support Non-blank characters)")
    def __add(self,key,value):
        try:
            self.update(key, value)
            self.__update(key, value)
        except:
            self.__config.append(key,value)
            self.__add_log[key]=value
    def save(self):
        with open(self.__configfilename,"r") as cfile:
            clines = cfile.readlines()
            for n in range(len(clines)):
                for nkey in self.__update_log.keys():
                    if re.match(r"^%s( |\t)*\=( ||\t)*(\S){1,}"%nkey, clines[n]):
                        clines[n]=re.sub(r"^%s( |\t)*\=( ||\t)*(\S){1,}"%nkey, "%s = %s"%(nkey,self.__update_log[nkey]), clines[n])
            if not re.match(r'.*(\r\n|\r|\n)$', clines[-1]):
                clines[-1]=clines[-1]+"\n"
            clines=clines+["%s = %s\n"%(nkey,self.__add_log[nkey]) for nkey in self.__add_log.keys()]
        with open(self.__configfilename,"w") as wcfile:
            wcfile.write(reduce(lambda x,y:x+y, clines))
            
if __name__=="__main__":
    pass

