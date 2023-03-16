
import logging
##loging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename= 'log.txt',
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# add the handler to the root logger
logger=logging.getLogger().addHandler(console)
log=logging.getLogger()

for i in range(10):
    logging.info(i)
logging.info("end!")