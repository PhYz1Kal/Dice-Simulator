from pathlib import Path
import time
import os

dpath=str(Path.home() / "Desktop")
expath=str(Path.home() / "DCsim")
mvpath=str(Path.home() / "Downloads/DCsim")
targpath=str(Path.home())

os.system('mv '+mvpath+' '+targpath)
time.sleep(0.1)
os.system('chmod +x '+expath+'/uninstall.sh')
time.sleep(0.1)
os.system('chmod +x '+expath+'/uninstall.py')
time.sleep(0.1)
os.system('chmod +x '+expath+'/DiceRoller.py')
time.sleep(0.1)
os.system('chmod +x '+expath+'/DiceRoller.py')
inp=str(Path.home())
file=open(expath+'/Dice_simulator.desktop',"r")
line3=file.readlines()
line3[2]="Exec=python3 "+inp+'/DCsim/DiceRoller.py\n'
file=open(expath+'/Dice_simulator.desktop',"w")
file.writelines(line3)
file.close()
file=open(expath+'/Dice_simulator.desktop',"r")
line3=file.readlines()
line3[3]="Icon="+inp+'/DCsim/icon\n'
file=open(expath+'/Dice_simulator.desktop',"w")
file.writelines(line3)
file.close()
os.system('mv '+expath+'/Dice_simulator.desktop '+dpath+'/')
if os.path.isdir(expath)==True:
    os.system('echo Dice simulator successfully installed!\necho Closing in 5 seconds...')
    time.sleep(5)
    os.system('exit')
else:
    os.system('echo Somethhing went wrong with the installation\necho Closing in 30 seconds...')
    time.sleep(30)
    os.system('exit')
