一个简单的免杀python shellcode加载样例，测试时python版本3.10，pyinstaller版本5.9.0
```powershell
pyinstaller -F --key 'fffenoStranff' load.py
```
直到2023.12.24为止，该方式对火绒、360、windows defender是免杀的。

pip install pyinstaller==5.9.0

pyinstaller -F --key 'fffenoStranff' load.py

