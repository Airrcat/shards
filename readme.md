使用版本小于6.0的pyinstaller(pip install pyinstaller==5.9.0)进行打包生成exe
```powershell
pyinstaller -F --key 'fffenoStranff' load.py
```
会在dist目录生成执行文件exe。

免杀自定义:
shell.py中的shellcode变量可存储64位CS shellcode
可通过修改shell.py中的magic变量稍微增强免杀性能。对于不免杀的情况，请尝试修改pyinstaller执行时的key值。（该key需16位）

注：请不要将样本提交到沙盒。