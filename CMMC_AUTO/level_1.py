import os
import platform
import subprocess
import socket
import datetime
import select
import shutil
import psutil
import time

print("Welcome to the CMMC Automation Script for CMMC Level l Compliance")

# function to check operating system information
def check_os_info():
    # retrieves and prints the operating system information, version and architecture
    os_name = platform.system()
    os_version = platform.release()
    os_arch = platform.machine()

    # prints the OS information
    print(f"Operating System: {os_name}")
    print(f"Version: {os_version}")
    print(f"Architecture: {os_arch}")

    generate_report(os_name=os_name, os_version=os_version, os_arch=os_arch)

# function to check the firewall status
def check_firewall_status():
    # checks the firewall status based on the operating system
    system = platform.system()
    try:
        # Windows Firewall check
        if system == 'Windows':
            # Checks using netsh, advfirewall, show, and allprofiles and captures the output
            result = subprocess.run(('netsh', 'advfirewall', 'show', 'allprofiles'), capture_output=True, text=True)
            # Checks the output for 'State' and 'ON'
            if 'State' in result.stdout and 'ON' in result.stdout.upper():
                print('Firewall is enabled')
            else:
                print("Firewall is disabled")
        # Linux firewall check
        elif system == 'Linux':
            # Checks the firewall status using ufw
            result = subprocess.run(['ufw', 'status'], capture_output=True, text=True)
            if 'Status: active' in result.stdout:
                print('Firewall (ufw) is enabled')
            else:
                print("Firewall (ufw) is disabled on Linux")
        else:
            print("Firewall status check not supported on this OS")
    except Exception as e:
        print(f"Error checking firewall status: {e}")

    

def monitor_system_metrics():
    start_time = time.time()
    while True:
        cpu_percent = psutil.cpu_percent()
        print(f"CPU Usage: {cpu_percent}%")
        
        memory_percent = psutil.virtual_memory().percent
        print(f"Memory Usage: {memory_percent}%")

        if cpu_percent > 80:
            print("High CPU usage above 80%")
        else:
            print("Below CPU threshold")
        
        if memory_percent > 80:
            print('Memory Usage is above 80%')
        else:
            print("Below Memory threshold")
        
        if platform.system() == 'Windows':
            result = subprocess.run(['tasklist'], capture_output=True, text=True)
            count = result.stdout.count('svchost.exe') + result.stdout.count('svchost')
            if count > 10:
                print("High number of svchost processes running on Windows")
        elif platform.system() == 'Linux':
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            count = len(result.stdout.splitlines())
            if count > 100:
                print("High number of processes running on Linux")
            else:
                print("Process count within normal range")
        
        generate_report(cpu_percent, memory_percent)
        

#def manage_user_access():
    

#def monitor_network():


#def check_system_time():


#def check_disk_space():
    #if platform.system() == 'Windows':
        
def generate_report(cpu_percent=None, memory_percent=None, os_name=None, os_version=None, os_arch=None):
    report_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name = f"CMMC_LEVEL_1_REPORT__{report_time}.txt"
    file_name = file_name.replace(" ", "_").replace(":", "-")
    with open(file_name, "w") as f:
        f.write(f"CMMC Level Basic Audit 1 Report\n")
        f.write(f"Generated on: " + report_time + "\n\n")
        if cpu_percent is not None:
            f.write(f"CPU Usage: {cpu_percent}%\n")
        if memory_percent is not None:
            f.write(f"Memory Usage: {memory_percent}%\n")
        if os_name is not None:
            f.write(f"Operating System:  {os_name}\n")
        if os_version is not None:
            f.write(f'Version: {os_version}\n')
        if os_arch is not None:
            f.write(f"Architecture: {os_arch}\n")
        f.write(f"This is a report that is assisted the audit. Still got to do it manually though")
    print("\nReport Generated")

def main_menu():
    while True:
        print("\n=== CMMC Level 1 Compliance Assistant ===")
        print("1. Check System Info (AC.L1-3.1.1)")
        print("2. Check Firewall Status (SI.L1-3.14.1)")
        print("3. Monitor System Metrics (AU.L1-3.3.2)")
        print('4. Check User Access (AC.L1-3.1.2)')
        print('5. Monitor Network (SI.L1-3.14.3)')
        print('6. Check System Time (AU.L1-3.3.1)')
        print('7. Check Disk Space (MA.L1-3.7.1)')
        print('8. Generate Report (AC.L1-3.1.1)')
        print('900. Exit')

        choice = input("Enter your choice: ")
        if choice == "1":
            check_os_info()
        elif choice == "2":
            check_firewall_status()
        elif choice == "3":
            monitor_system_metrics()
        elif choice == "4":
            check_user_access()
        elif choice == "5":
            monitor_network()
        elif choice == "6":
            check_system_time()
        elif choice == "7":
            check_disk_space()
        elif choice == '8':
            generate_report()
        elif choice == '900':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()