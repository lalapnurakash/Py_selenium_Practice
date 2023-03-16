from datetime import datetime

def time_delta(t1, t2):
    strpformat = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, strpformat)
    t2 = datetime.strptime(t2, strpformat)
    print(str(int(abs(t1 - t2).total_seconds())))
time_delta("Sun 10 May 2015 13:54:36 -0000","Sat 02 May 2015 19:54:36 +0530")
