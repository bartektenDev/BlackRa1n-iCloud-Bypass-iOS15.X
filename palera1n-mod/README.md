# Palera1n mod by kitty915

> **Warning** PLEASE, DO NOT ASK FOR SUPPORT REGARDING ICLOUD BYPASS IN PALERA1N DISCORD SERVER! THIS IS NOT OFFICIALLY SUPPORTED AND WON'T EVER BE.

This palera1n mod adds a tethered iCloud Hello screen bypass for checkm8 devices, tested on an iPhone 6S.

The script works on macOS and Linux. Windows is NOT supported. VMs are NOT supported unless PCI USB Passthrough is used. LiveCD Linux can be used if you have enough RAM.

Only tested on tethered palera1n jailbreak, semi-tethered may need different mount directories but I don't have a compatible device to test.

This bypass will also jailbreak with palera1n, we do this to disable rootfs seal enforcement. This could be done without palera1n patching the kernel but I am too lazy to do that, and I want a JB anyways.

iOS 16 support may be a thing when palera1n's iOS 16 branch gets somewhat stable, but I don't have a device to test

# DISCLAIMER

This bypass must not be used on a device you don't legally own and have permission to modify, I am not responsible for any misuse of anyting in this repo.

# Usage
To bypass Hello screen we will first of all, restore to a clean iOS 15.x version. (15.0-15.7.1)

You should be in the Hello screen for the version you restored, now reboot into DFU mode.

Now in your PC, clone this git repo (recursively) and cd into it
```
git clone https://github.com/kitty915/palera1n-mod/ && cd ./palera1n-mod/
```

Make sure you have all palera1n dependencies installed, then we can start with the jailbreak and bypass process.

> If you are in linux you may need to run the following commands in a new terminal (and leave it open) before running palera1n:
>
> ``sudo systemctl stop usbmuxd && sudo usbmuxd -p -f``

We will jailbreak with palera1n first to prepare all files:
```
./palera1n.sh --tweaks <iOS version> --verbose
```
>You will need to replace "<iOS version>" with the iOS version currently installed in your device. For example:
>
>``./palera1n.sh --tweaks 15.7.1 --verbose``

Let the script run and follow any screen prompt if any. When it finishes you should be booted into iOS again. If for some reason you end up in recovery mode, try running the command again and it should boot you into iOS.

If everything was succesful and you booted into iOS, reboot to DFU again, we are going to start the bypass process.

Type the following command in the terminal:
```
./palera1n.sh --bypass <iOS version>
```
> Again, changing "<iOS version>" with your iOS version.

Let the process finish and your device should be in recovery mode

Once in recovery mode, we are already done with the bypass, just run the same palera1n command from before to boot.
```
./palera1n.sh --tweaks <iOS version> --verbose
```
> **Warning** You will have to run this command every time you want to boot your device!
>
> Remember to change "<iOS version>" with your iOS version too.

Now, proceed with setup as normal, you can skip Wi-Fi setup and won't be asked to activate your device.

You can now jailbreak with palera1n too with the Tips app, enjoy!

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
- @kitty915: Modified palera1n script to automate bypass and added instructions in the readme
