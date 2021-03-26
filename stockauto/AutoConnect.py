from pywinauto import application
import time
import os

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('taskkill /IM DibServer* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
os.system('wmic process where "name like \'%DibServer%\'" call terminate')
time.sleep(5)

app = application.Application()
# junil 계정정보(id, pw, 공인인증서pw)
app.start('C:\CREON\STARTER\coStarter.exe /prj:cp /id:joon2344 /pwd:altkzk2! /pwdcert:altkzk2gh! /autostart')
time.sleep(60)
