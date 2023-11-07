# check current dateand time :

import datetime

now = datetime.datetime.now()

print("currnt date & time :- ",end = "")

print(now.strftime("%d-%m-%y %H : %M : %S "))
