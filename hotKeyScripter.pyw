import random
import platform
import subprocess
import string

startupinfo = None
if platform.system() == 'Windows':
    import _subprocess  # @bug with python 2.7 ?
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= _subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = _subprocess.SW_HIDE

def createScript(alphabet):
    file = open("scramble.ahk",'w')
    for i in range(len(alphabet)-1):
        file.write(alphabet[i])
        file.write("::")
        file.write(alphabet[i+1])
        file.write("\n")
    file.write("#SingleInstance force")
    file.close()
    
def shuffleLetters(alphabet):
    for i in range(len(alphabet)):
        x = random.randrange(0,len(alphabet)-1)
        temp = alphabet[i]
        alphabet[i] = alphabet[x]
        alphabet[x] = temp
    return alphabet

alphabet = [char for char in string.ascii_lowercase]

alphabet = shuffleLetters(alphabet)
createScript(alphabet)
args = ["autohotkey.exe scramble.ahk"]
out = subprocess.check_output(args, startupinfo=startupinfo)

