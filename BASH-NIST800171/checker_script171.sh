#!/bin/bash

# function to enable automatic updates
function enable_automatic_updates() {
    echo "Enabling automatic security updates.."

    # checks to see if there are any upgrades available
    if ! command -v unattended-upgrades &> /dev/null; then
	# installs the updates
	sudo apt-get update && sudo apt-get install -y unattended-upgrades apt-listchanges
    fi

    # sets a minimun time for the updates to occur
    sudo bash -c 'cat > /etc/apt/apt.conf.d/20auto-upgrades << EOF
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Download-Upgradeable-Packages "1";
APT::Periodic::AutoclearnInterval "7";
APT::Periodic::Unattended-Upgrade "1";
EOF'

    echo "Automatic security updates enabled"
}

# function to check rsyslog for logging events and more
function check_logging() {
   echo "Checking rsyslog to check authentication event logging"
   # function to check rsyslog.conf for compliance
   if grep -q "auth.*" /etc/rsyslog.conf; then
	# prints is compliant
	echo "Authentication logging is configured (compliant)."
   else
	# prints is non-compliant
	echo "Authentication logging might not be fully configured (non-compliant)."
   fi
}

# function that checks to see if SSH is secure
function ssh_password() {
   echo "Checking SSH password..."
   # function to check if sshd_config is compliant
   if grep -q "PasswordAuthentication no" /etc/ssh/sshd_config; then
	# prints is compliant if disabled
	echo "SSH password authentication is disabled (compliant)."
   else
	# prints is non-compliant if enabled
	echo "SSH Password authentication is enabled (non-complant)."
   fi
}

# function to check the baseline of the system
function baseline_config() {
   echo "Hostname: $(hostnamectl hostname)"
   echo "Operating system: $(lsb_release -d | cut -f 2)"
   echo "Kernel Version: $(uname -r)"
}

# function that enforces a password policy
function set_password_policy() {
   echo "Setting password complexity and expiration..."
   # appends the file for a max password time of 90 days before changing
   sudo sed -i 's/^PASS_MAX_DAYS.*/PASS_MAX_DAYS 90/' /etc/login.defs
   # appends the file for a min password time of 7 days
   sudo sed -i 's/^PASS_MIN_DAYS.*/PASS_MIN_DAYS 7/' /etc/login.defs
   # appends the file to warn the the user 14 days expiration
   sudo sed -i 's/^PASS_WARN_AGE.*/PASS_WARN_AGE 14/' /etc/login.defs

   # checks to see the common-passowrd file exists
   if ! grep -q "pam_pwquality.so" /etc/pam.d/common-password; then
	# if not, it adds complexity to the file for password
	echo "Adding password complexity to PAM..."
	sudo sed -i '/pam_unix.so/ s/$/ retry=3 minlen=12 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1' /etc/pam.d/common-password
   fi
}

# function that checks for file integrity
function file_integrity() {
    # prints installing AIDE
    echo "Installing and starting AIDE"
    # if AIDE is not installed, it will be installed
    if ! command -v aide &> dev/null; then
	# installs it
	sudo apt-get install -y aide
    fi
    sudo aideinit
    sudo cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db
    echo "AIDE started"
}

# runs the functions one at a time
enable_automatic_updates
check_logging
ssh_password
baseline_config
set_password_policy
file_integrity

echo "NIST 800-171 basic controls automation completed"
