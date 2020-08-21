import os
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

os.system('git status')
os.system('git add outputs -A')
os.system('git commit -m \''+dt_string+'\'')
os.system('git push origin master -f')

