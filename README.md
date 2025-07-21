# compliance-automation

Automation of scripts for regulations such as NIST and more

Bash NIST 800-53 checker_script.sh The purpose of this script is to check for system compliance with NIST 800-53 by automating select controls with Bash  
AC-6 (Least Priveledge): makes sure that all accounts have their respective permissions based on UID  
CM-6 (Password policies): makes sure that all passwords have a max, min, and warn range before expiration  
CS-28 (Sensitive file permissions): Makes sure only root has access to sensitive info  
SI-2 (Up to date system): Checks for system is up to date with latest patch or update  
SC-28 (Protection of Information at Rest): Checks for if the disk is encrypted. If not, manually enable it  
