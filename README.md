# Project-Bot

--------------------setup--------------------

clone repository onto each machine

edit beacon.py 
  - add C2server IP Address in manager function

edit slave.py
  - add beacon IP Address
  
--------------------running botnet--------------------

Use command 'python3 C2server.py' on a command server or vm

Use command 'python3 beacon.py' on a relay server or vm

Use command 'python3 slave.py' on slave server/s or vm/s
