D:
cd workspace\renuka\scanner
echo "cmd - load...">logs\log.txt
echo "cmd - File running....">logs\log.txt
python start.py
echo "cmd - working...">logs\log.txt
@echo off
echo "cmd - done...">logs\log.txt
@pause
:END
cmd /k
