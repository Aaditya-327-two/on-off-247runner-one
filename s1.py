#for on-off-247runner-one

first = ["on-off-247runner-one", ]
second = ["on-off-247runner-two", ]

#---------------------------------------------------------------

import heroku3
import time

gapOfCheck = 1728000
HEROKU_API = "ea15b1ea-40b6-47a1-9eb9-41a5a67df4a0"
heroku_conn = heroku3.from_key(HEROKU_API)

#---------------------------------------------------------------
def findMyApp(apps, appName):
    for _ in apps: 
        if _.name == appName: 
            return _

def enableApps(applist, appListText):
    for _ in appListText:
        print("A")
        findMyApp(applist, _).enable_maintenance_mode()

def disableApps(applist, appListText):
    for _ in appListText:
        print("B")
        findMyApp(applist, _).disable_maintenance_mode()

#---------------------------------------------------------------
last_time = time.time()%gapOfCheck
while True:
    time.sleep(1)
    now = time.time()%gapOfCheck

    print(last_time, now, now-last_time)
    if last_time< gapOfCheck and now> 0 and now-last_time<0:
        if last_time-now>gapOfCheck/4:  
            apps = heroku_conn.apps()   
            enableApps(apps, second)
            disableApps(apps, first)
            
    last_time = now