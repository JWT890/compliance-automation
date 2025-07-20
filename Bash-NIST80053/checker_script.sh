#!/bin/bash

# Automates certain aspects of NIST 800-53

# This script checks for Auditing, User account, updates and integrity, and configuration and tracking

# checks to see script is being run as root or without sudo
if [[ $EUID -ne 0 ]]; then
   #if true then exits
   echo "This script must be run as root. Exiting"
   # exits the script
   exit 1
fi

echo "Starting Compliance checking"

# AC-6 Least Privelege

# checks to see if users have the proper privledges
echo "[*] Checking for users with UID 0 other than root"
# checks through /etc/passwd for any one
awk -F: '($3 == 0) {print $1}' /etc/passwd | grep -v "^root$"

# CM -6 Password policies

echo "[*] Configuring password policy"
# checks the auth_file for password descrepancies
auth_file="/etc/login.defs"
# sets a password max day age of 90 days before changing
sed -i 's/^PASS_MAX_DAYS./*PASS_MAX_DAYS 90/' "$auth_file"
# sets a min day age of 1 before changing
sed -i 's/^PASS_MIN_DAYS./*PASS_MIN_DAYS 1/' "$auth_file"
# sets a warn age of 7 before changing
sed -i 's/^PASS_WARN_AGE./*PASS_WARN_AGE 7/' "$auth_file"

# CM-6 Disable unsused filesystems
echo "[*] Disabling uncommon or unused filesystems"
# checks to see for any systems that are unused
for fs in cramfs squashfs udf; do
 #edits the file if true
  echo "install $fs /bin/true" > /etc/modprobe.d/"$fs".conf
done

#SC-28 Permissions on sensitive files
echo "[*] Checking permissions on /etc/shadow"
# sets permission to be read only by root
chmod 000 /etc/shadow
# sets the permission to /etc/shadow
chown root:shadow /etc/shadow

echo "Checking permissions on boot"
# sets the permission to full access for root
chmod 700 /boot

# SI-2 Ensure system is up to date
echo "[*} Checking for and applying updates"
# checks to see if the system is up to date
if command -v apt &> /dev/null; then
# if yes then updates and upgrades
  apt update && apt upgrade -y
# if else then updates
elif command -v yum &> /dev/null; then
  yum update -y
else
# else you need to manually update
  echo "Package manager not supported. Manuel update required"
fi

# SC-28 Protection of Info at Rest
echo "Checking disk encryption"
# checks the disk for encryption notice
if lsblk | grep -q crypt; then
    echo "Disk appears encrypted"
else
    echo "No disk encryption detected. Enable manually"
fi

# Loggint activity
log_file="/var/log/nist_hardening.log"
echo "Hardening script completed on $(date)" >> "$log_file"
echo "Compliance tasks completed. Check $log_file for log"
