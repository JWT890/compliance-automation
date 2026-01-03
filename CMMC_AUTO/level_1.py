import os
import platform
import subprocess
import socket
import datetime
import select

print("Welcome to the CMMC Automation Script for CMMC Level l Compliance")

def check_os_info():
    os_name = platform.system()
    os_version = platform.release()
    os_arch = platform.machine()

    print(f"Operating System: {os_name}")
    print(f"Version: {os_version}")
    print(f"Architecture: {os_arch}")

def check_firewall_status():
    if platform.system() == 'Windows':
        status = subprocess.run(['netsh', 'adufirewall', 'show', 'allprofiles'], capture_output=True, text=True)
        print(status.stdout)
    elif platform.system() == 'Linux':
        status = subprocess.run(['sudo', 'ufw', 'status'], capture_output=True, text=True)
        print(status.stdout)
    else:
        print("Firewall status check not supported on this OS.")

def check_antivirus_status():


def check_user_accounts():
    

def monitor_network():

def generate_report():
    report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(f"CMMC_LEVEL_1_REPORT_(report_time).txt", "w") as f:
        f.write(f"CMMC Level Basic Audit 1 Report\n")
        f.write(f"Generated on: " + report_time + "\n\n")
        f.write(f"This is a report that is assited the audit. Still got to do it manually though")
    print("\nReport Generated")

def main_menu():
    while True:
        print("\n=== CMMC Level 1 Compliance Assistant ===")
        print("1. Check System Info (AC.L1-3.1.1)")
        print("2. Check Firewall Status (SI.L1-3.14.1)")
        print("3. Check Antivirus Status (SI.L1-3.14.2)")

        choice = input("Enter your choice: ")
        if choice == "1":
            check_os_info()
        elif choice == "2":
            check_firewall_status()
        elif choice == "3":
            check_antivirus_status()
        elif choice == "4":
            check_user_accounts()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()