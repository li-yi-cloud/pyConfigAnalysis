#coding:utf-8
import re,os

class ConfigAnalysis():
    def __init__(self):
        self.__config = None
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
            raise IOError('No such file or directory."%s"'%configfilename)
    def keys(self):
        return [ckey for ckey,_ in self.__config]
    def get(self,key):
        for ckey,cvalue in self.__config:
            if ckey == key:
                return cvalue
        raise KeyError("Maping key not found.('%s')"%key)

if __name__=="__main__":
    pass

