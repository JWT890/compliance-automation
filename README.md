# compliance-automation

Automation of scripts for regulations such as NIST and more

Bash NIST 800-53 checker_script.sh The purpose of this script is to check for system compliance with NIST 800-53 by automating select controls with Bash  
AC-6 (Least Priveledge): makes sure that all accounts have their respective permissions based on UID  
CM-6 (Password policies): makes sure that all passwords have a max, min, and warn range before expiration  
CS-28 (Sensitive file permissions): Makes sure only root has access to sensitive info  
SI-2 (Up to date system): Checks for system is up to date with latest patch or update  
SC-28 (Protection of Information at Rest): Checks for if the disk is encrypted. If not, manually enable it  

Bash NIST 800-171 checker_script.sh The purpose of this script is to check for system compliace with NIST 800-171 by automating select controls with Bash  
SI-2 (Automatic Updates): makes sture that system is patched with updates installed in timely manner  
AU-2 (Audit Logging): checks rsyslog for verification of authentication events and retains records  
AC-7, AC-2, IA-5 (Password Function): checks to see if password is compliant  
3.5.1, 3.5.2, IA-5 (Password policy): Complexity and lifetime  
SI-7, 3.14.9 (File Integrity): Monitors for unauthorized changes to files and integrity checks
CM-2 (Baselining Config): verifies baseline system config details
