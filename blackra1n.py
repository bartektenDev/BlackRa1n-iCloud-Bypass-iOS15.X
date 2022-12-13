import re
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import time
from PIL import ImageTk, Image
from subprocess import run
import subprocess

root = tk.Tk()
frame = tk.Frame(root)

#root.iconbitmap('blackrain.ico')
root.iconphoto(False, tk.PhotoImage(file='newbricon.png'))



LAST_CONNECTED_UDID = ""
LAST_CONNECTED_IOS_VER = ""

def detectDevice():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER
    #step 1 technically
    print("Searching for connected device...")
    os.system("ideviceinfo > lastdevice.txt")

    f = open("lastdevice.txt", "r")
    fileData = f.read()
    f.close()

    if("ERROR: No device found!" in fileData):
        #no device was detected, so retry user!
        print("ERROR: No device found!")

        messagebox.showinfo("No device detected! 0x404","Try disconnecting and reconnecting your device.")
    else:
        #we definitely have something connected...

        #find the UDID
        start = 'UniqueDeviceID: '
        end = 'UseRaptorCerts:'
        s = str(fileData)

        foundData = s[s.find(start)+len(start):s.rfind(end)]
        UDID = str(foundData)
        LAST_CONNECTED_UDID = str(UDID)

        #find the iOS
        #we definitely have something connected...
        start2 = 'ProductVersion: '
        end2 = 'ProductionSOC:'
        s2 = str(fileData)

        foundData2 = s2[s.find(start2)+len(start2):s2.rfind(end2)]
        deviceIOS = str(foundData2)
        LAST_CONNECTED_IOS_VER = str(deviceIOS)

        if(len(UDID) > 38):
            #stop automatic detection
            timerStatus = 0

            print("Found UDID: "+LAST_CONNECTED_UDID)
            messagebox.showinfo("iDevice is detected!","Found iDevice on iOS "+LAST_CONNECTED_IOS_VER)
            cbeginExploit10["state"] = "normal"
            cbeginExploit2["state"] = "normal"
            
            messagebox.showinfo("Ready to begin!","We are ready to exploit. You can now use BlackRa1n!")

        else:
            print("Couldn't find your device")

def startDFUCountdown():
    print("Get ready to put device into DFU mode...")


def enterRecMode():
    print("Kicking device into recovery mode...")
    os.system("./extras/euphoria_scripts/enterrecovery.sh")

def exitRecMode():
    print("Kicking device out of recovery mode...")
    os.system("./extras/euphoria_scripts/exitrecovery.sh")

def showDFUMessage():
    messagebox.showinfo("Step 1","Put your iDevice into DFU mode.\n\nClick Ok once its ready in DFU mode to proceed.")


def jailbreakIOS15():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER
    
    VER = str(LAST_CONNECTED_IOS_VER)

    print("Starting palera1n-mod jailbreak...")
    os.system(f"cd ./palera1n-mod/ && ./palera1n.sh --tweaks {VER}")
    #palera1n code is modified to always pass verbose command with this tool so no need to add verbose at the end
    print("Device is jailbroken!\n")
    
def buildSSHRD():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER
    #clean files for new build
    print("Cleaning SSHRD...")
    os.system("bash ./SSHRD_Script/sshrd.sh clean")
    # download and build necessary files for custom ramdisk checkm8 exploit
    print("Building SSHRD...")
    os.system("bash ./SSHRD_Script/sshrd.sh 15.6")#+str(LAST_CONNECTED_IOS_VER))
    print("Built SSHRD!\n")
    messagebox.showinfo("Built IPSW!","IPSW is built and ready to boot!")
    
def loadSSHRD():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER
    # download and build necessary files for custom ramdisk checkm8 exploit
    print("Booting SSHRD...")
    os.system("bash ./SSHRD_Script/sshrd.sh boot")#+str(LAST_CONNECTED_IOS_VER))
    print("Booted SSHRD!\n")
    messagebox.showinfo("Booting IPSW...","Device is booting custom IPSW!")
    
def exploitBlackRa1n():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER
    # download and build necessary files for custom ramdisk checkm8 exploit
    print("Loading bypass script...")
    #os.system("bash ./br_bypass.sh")#+str(LAST_CONNECTED_IOS_VER))
#    os.system("bash ./extras/bypassFiles/Activate.sh")
    os.system("bash ./br_bypass.sh")
    print("iCloud bypass complete!\n")
    messagebox.showinfo("BlackRa1n Done!","iOS 15.X Patch Done!\n\nFinal step, your device will boot into recovery mode, just run Jailbreak iOS 15.X again and your device should boot!")
    
def restoreBaseband():
    os.system("sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -p2222 'root@localhost' 'mv /mnt6/$(cat /mnt6/active)/usr/local/standalone/firmware/Baseband2 /mnt6/$(cat /mnt6/active)/usr/local/standalone/firmware/Baseband'")
    print("Restore Baseband command sent!")
    messagebox.showinfo("Restore Baseband","Restore Baseband command sent!")

def hideBaseband():
    os.system("sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -p2222 'root@localhost' 'mv /mnt6/$(cat /mnt6/active)/usr/local/standalone/firmware/Baseband /mnt6/$(cat /mnt6/active)/usr/local/standalone/firmware/Baseband2'")
    print("Hide Baseband command sent!")
    messagebox.showinfo("Hide Baseband","Hide Baseband command sent!")


def startSSHServer():
    os.system("iproxy 2222:22 2>&1 &")
    
def mountfilesystemsSSHCMD():
    os.system("sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -p2222 'root@localhost' 'mount_filesystems'")
    print("Mount Filesystems command sent!")
    messagebox.showinfo("Mount Filesystems","Mount Filesystems command sent!")

def exploitSSHReboot():
    print("Sending reboot command...")
    os.system("sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -p2222 'root@localhost' '/sbin/reboot'")
    print("Reboot command sent!")
    messagebox.showinfo("Reboot command sent!","Reboot command sent!")

def quitProgram():
    print("Exiting...")
    os.system("exit")


root.title('BlackRa1n v1.3 - iOS 15.X iCloud Activation Lock Bypass - @ios_euphoria')
frame.pack()

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("newbricon.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img,width=100)
label.pack()

cdetectDevice = tk.Button(frame,
                   text="Pair iDevice",
                   command=detectDevice)
cdetectDevice.pack(side=tk.TOP)

#cbeginExploit = tk.Button(frame,
#                   text="Start checkra1n",
#                   command=exploitCheckra1n,
#                   state="normal")
#cbeginExploit.pack(side=tk.TOP)

cbeginExploit10 = tk.Button(frame,
                   text="Jailbreak iOS 15.X",
                   command=jailbreakIOS15,
                   state="normal")
cbeginExploit10.pack(side=tk.TOP)

cbeginExploit5 = tk.Button(frame,
                   text="Build Custom IPSW",
                   command=buildSSHRD,
                   state="normal")
cbeginExploit5.pack(side=tk.TOP)

cbeginExploit6 = tk.Button(frame,
                   text="Boot Custom IPSW",
                   command=loadSSHRD,
                   state="normal")
cbeginExploit6.pack(side=tk.TOP)
 
#cbeginServer = tk.Button(frame,
#                    text="Start SSH Server",
#                    command=startSSHServer,
#                    state="normal")
#cbeginServer.pack(side=tk.TOP)
#
#cbeginServer2 = tk.Button(frame,
#                    text="Mount Filesystems",
#                    command=mountfilesystemsSSHCMD,
#                    state="normal")
#cbeginServer2.pack(side=tk.TOP)
#
#cbeginExploit8 = tk.Button(frame,
#                    text="Restore Baseband",
#                    command=restoreBaseband)
#cbeginExploit8.pack(side=tk.TOP)
#
#cbeginExploit9 = tk.Button(frame,
#                    text="Hide Baseband",
#                    command=hideBaseband)
#cbeginExploit9.pack(side=tk.TOP)
#
#cbeginExploit4 = tk.Button(frame,
#                    text="Send SSH Reboot",
#                    command=exploitSSHReboot)
#cbeginExploit4.pack(side=tk.TOP)

cbeginExploit2 = tk.Button(frame,
                   text="Start BlackRa1n",
                   command=exploitBlackRa1n,
                   state="normal")
cbeginExploit2.pack(side=tk.TOP)

cexitRecovery = tk.Button(frame,
                   text="Exit Recovery Mode",
                   command=exitRecMode)
cexitRecovery.pack(side=tk.TOP)

root.geometry("600x300")

root.eval('tk::PlaceWindow . center')

root.mainloop()
