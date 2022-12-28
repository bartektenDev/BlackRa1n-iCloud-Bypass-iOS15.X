# BlackRa1n-iCloud-Bypass-iOS15.X
BlackRa1n is a Tethered iCloud Bypass Tool for iOS 15.X (checkm8 devices only)

![alt text](https://github.com/bartektenDev/BlackRa1n-iCloud-Bypass-iOS15.X/blob/main/Screen%20Shot%202022-12-13%20at%202.25.12%20AM.png)

It's really late and I have school tomorrow. I wanted to push this out as soon as I could so here it is for iOS 15.X. Not iOS 16 just yet...

Install tkinter, python3, sshpass, and whatever dependencies come with Sliver from appletech752.com

Instructions:
1. Connect iDevice
2. Open BlackRa1n folder and terminal on mac. 
3. In terminal enter the following command:
```
cd DRAG AND DROP BLACKRA1N FOLDER HERE
```
4. In terminal enter the following command:
```
python3 blackra1n.py
```
5. Pair iDevice in normal mode
6. Jailbreak iOS 15.X 
(Watch the terminal for information if anything fails or what happens. Follow DFU steps that will pop up.)
7. After your device is jailbroken and boots iOS you can continue to next step.
8. Put device into DFU mode.
8. Build Custom IPSW
9. Boot Custom IPSW (You did this step right if you see SSHRD, verbose mode, text on the screen)
10. Finally, Start BlackRa1n.
11. Device will reboot and you're done! 

If you get to recovery mode, just run Jailbreak step again and thats it device will boot bypassing iCloud Lock Activation.


I will update this asap. I have finals this week.
@ios_euphoria <3


# Credits

Original palera1n credits:
- [Nathan](https://github.com/verygenericname)
    - The ramdisk that dumps blobs, installs pogo to tips app, and duplicates rootfs is a slimmed down version of [SSHRD_Script](https://github.com/verygenericname/SSHRD_Script)
    - For modified [restored_external](https://github.com/verygenericname/sshrd_SSHRD_Script)
    - Also helped Mineek getting the kernel up and running and with the patches
    - Helping with adding multiple device support
    - Fixing issues relating to camera.. etc by switching to fsboot
    - [iBoot64Patcher fork](https://github.com/verygenericname/iBoot64Patcher)
- [Mineek](https://github.com/mineek)
    - For the patching and booting commands
    - Adding tweak support
    - For patchfinders for RELEASE kernels
    - [Kernel15Patcher](https://github.com/mineek/PongoOS/tree/iOS15/checkra1n/Kernel15Patcher)
    - [Kernel64Patcher](https://github.com/mineek/Kernel64Patcher)
- [Amy](https://github.com/elihwyma) for the [Pogo](https://github.com/elihwyma/Pogo) app
- [checkra1n](https://github.com/checkra1n) for the base of the kpf
- [nyuszika7h](https://github.com/nyuszika7h) for the script to help get into DFU
- [the Procursus Team](https://github.com/ProcursusTeam) for the amazing [bootstrap](https://github.com/ProcursusTeam/Procursus)
- [F121](https://github.com/F121Live) for helping test
- [m1sta](https://github.com/m1stadev) for [pyimg4](https://github.com/m1stadev/PyIMG4)
- [tihmstar](https://github.com/tihmstar) for [pzb](https://github.com/tihmstar/partialZipBrowser)/original [iBoot64Patcher](https://github.com/tihmstar/iBoot64Patcher)/original [liboffsetfinder64](https://github.com/tihmstar/liboffsetfinder64)/[img4tool](https://github.com/tihmstar/img4tool)
- [xerub](https://github.com/xerub) for [img4lib](https://github.com/xerub/img4lib) and [restored_external](https://github.com/xerub/sshrd) in the ramdisk
- [Cryptic](https://github.com/Cryptiiiic) for [iBoot64Patcher](https://github.com/Cryptiiiic/iBoot64Patcher) fork, and [liboffsetfinder64](https://github.com/Cryptiiiic/liboffsetfinder64) fork
- [libimobiledevice](https://github.com/libimobiledevice) for several tools used in this project (irecovery, ideviceenterrecovery etc), and [nikias](https://github.com/nikias) for keeping it up to date
- [Nick Chan](https://github.com/asdfugil) general help with patches.
- [Sam Bingner](https://github.com/sbingner) for [Substitute](https://github.com/sbingner/substitute)
- [Serena](https://github.com/SerenaKit) for helping with boot ramdisk.

Mod credits:
- @MatthewPierson: Patched mobileactivationd
- @edwin170: Some code inspired from [dualboot-ios-15-with-14-script](https://github.com/edwin170/dualboot-ios-15-with-14-script/)'s repo
- @kitty915: Modified palera1n script to automate bypass and added instructions in the readme. 
- @ios_euphoria: GUI Design
- @debbeddebbed: SSHRD tool. Super handy ssh ramdisking.
