from configparser import ConfigParser

cf=ConfigParser()
cf.read("props.ini")
print(cf.sections())
print(cf.get('debug','pid-file'))
print ("Log Errors debugged ? : ", cf.getboolean('debug','log_errors'))
print ("Port Server : ", cf.getint('server','port'))
print ("Worker Server : ", cf.getint('server','nworkers'))

cf.set('server', 'port', '9000')
cf.set('debug', 'log_errors', 'False')

import sys

cf.write(sys.stdout)