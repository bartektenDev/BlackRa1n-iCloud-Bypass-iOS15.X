

# @ios_euphoria BlackRa1n
# iOS 15.X-16 iCloud Bypass

if ! which curl >> /dev/null; then
    echo "Error: curl not found"
    exit 1
fi
if ! which iproxy >> /dev/null; then
    echo "Error: iproxy not found"
    exit 1
fi
#stop asking me if i want to fucking save the damn key
rm -rf ~/.ssh/known_hosts
clear

# Change the current working directory
cd "`dirname "$0"`"

# Check for Homebrew, install if we don't have it
if test ! $(which brew); then
    echo "Installing homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" > /dev/null 2>&1
    echo ''
fi

# Check for sshpass, install if we don't have it
if test ! $(which sshpass); then
    echo "Installing sshpass..."
    brew install esolitos/ipa/sshpass > /dev/null 2>&1
    echo ''
fi

# Check for iproxy, install if we don't have it
if test ! $(which iproxy); then
    echo "Installing iproxy..."
    brew install libimobiledevice > /dev/null 2>&1
    echo ''
fi


echo 'Starting iproxy...'

killall iproxy
idevicepair pair
iproxy 2222:22 > /dev/null 2>&1 &

echo ""
echo "
 ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀ ██▀███   ▄▄▄       ██▓ ███▄    █
▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██ ▒ ██▒▒████▄    ▓██▒ ██ ▀█   █
▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒▓██  ▀█ ██▒
▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒██▀▀█▄  ░██▄▄▄▄██ ░██░▓██▒  ▐▌██▒
░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░██▓ ▒██▒ ▓█   ▓██▒░██░▒██░   ▓██░
░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓  ░ ▒░   ▒ ▒
▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░  ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░░ ░░   ░ ▒░
 ░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░   ░░   ░   ░   ▒    ▒ ░   ░   ░ ░
 ░          ░  ░     ░  ░░ ░      ░  ░      ░           ░  ░ ░           ░
      ░                  ░
"
echo ""
echo "MAKE IT RAIN!!!"

sleep 2
    
echo 'Mounting filesystem as read-write'
sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@localhost -p2222 'mount_filesystems'

echo 'Running iOS 15-16 iCloud Bypass...'
sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@localhost -p2222 'mv -v /mnt1/usr/libexec/mobileactivationd /mnt1/usr/libexec/mobileactivationdBackup'
sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@localhost -p2222 'ldid -e /mnt1/usr/libexec/mobileactivationdBackup > /mnt1/usr/libexec/mob.plist'
#upload new mobileactivationd
sshpass -p 'alpine' scp -rP 2222 -o StrictHostKeyChecking=no ./mobileactivationd_iOS15 root@localhost:/mnt1/usr/libexec/mobileactivationd
sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@localhost -p2222 'chmod 755 /mnt1/usr/libexec/mobileactivationd'
sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@localhost -p2222 'ldid -S/mnt1/usr/libexec/mob.plist /mnt1/usr/libexec/mobileactivationd'
sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@localhost -p2222 'rm -v /mnt1/usr/libexec/mob.plist'
sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@localhost -p2222 '/usr/sbin/nvram allow-root-hash-mismatch=1'


#UPDATE BY EUPHORIA work-in-proress for FaceTime enabler! hehe if you found this, message me <3 @ios_euphoria on twitter
#echo "Pushing new data_ark.plist..."
#sshpass -p 'alpine' scp -rP 2222 -o StrictHostKeyChecking=no ./uploadAFTER_ACTIVATION/data_ark.plist root@localhost:/var/root/Library/Lockdown/data_ark.plist
#sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -p 2222 "root@localhost" 'chmod 755 /var/root/Library/Lockdown/data_ark.plist'
#sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -p 2222 "root@localhost" 'chflags uchg /var/root/Library/Lockdown/data_ark.plist'
#echo "Euphoria patch made!"

echo 'iCloud Files Modified!'

echo 'Telling device to boot...'
sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@localhost -p2222 /sbin/reboot
echo 'Device is now booting...'


sleep 2

# Kill iproxy
kill %1 > /dev/null 2>&1

echo 'BlackRa1n Done!'

echo ''
