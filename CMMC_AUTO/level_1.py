import os
import platform
import subprocess
import socket
import datetime
import select

print("Welcome to the CMMC Automation Script for CMMC Level l Compliance")

def check_os_info():


def check_firewall_status():


def check_antivirus_status():


def check_user_accounts():


def genreate_report():
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

if __name__ == "__main__":
    main_menu()