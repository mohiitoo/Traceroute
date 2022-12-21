import os 
import subprocess
"""
first $→ source runing.txt 
    (for active env file )                                          
"""
class tracerouteError(Exception):
    pass

class tracerouteValueError(tracerouteError):
    pass

class TracerouteMissingError(tracerouteError):
    pass

class traceroute:
    def __init__(self,address):
        self.address = address
        self.out = []

    def run(self):
        mac = 'traceroute -m 10 ' + self.address
        proc = subprocess.Popen(mac, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        out = out.decode('UTF-8')
        out = out.split('\n')
        return out
  
class fille:
    def __init__(self , d1):
        self.out = d1
    def write(self):
        f = open("myfile.csv","w")
        for i in self.out:
            f.write(i+"\n")
        f.close()
address = (os.getenv('address'))
if address == None:
    raise TracerouteMissingError("you miss active .env file follow readme file")
d1 = traceroute(address).run()
fille(d1).write()