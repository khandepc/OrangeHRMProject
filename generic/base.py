from configparser import ConfigParser
from generic.seleniumbase import SeleniumBase

class Base(SeleniumBase):
    def read_config_file(self,file_name,section_name):
        cp=ConfigParser()
        cp.read("./configuration/"+file_name)

        ll=cp.items(section_name)
        dd={}
        for tt in ll:
            key=tt[0]
            value=tt[1]
            dd[key]=value
        return dd

