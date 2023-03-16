import os
import sys
import datetime

print(os.path.dirname(sys.executable))
s=datetime.date.today().strftime("%d%b%Y")
print(f'headline-{s}.csv')

