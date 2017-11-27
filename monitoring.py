import larm
import shutil
import psutil # must be installed
import sys
import os

soft_disk_usage = 50
hard_disk_usage = 90
soft_memory_usage = 50
hard_memory_usage = 90

def parse_options():
    if len(sys.argv) == 1:
        disk_usage()
        memory_usage()
        exit(0)
    if len(sys.argv) == 3 and sys.argv[1] == "-o":
        if sys.argv[2] == "disk":
            disk_usage()
        elif sys.argv[2] == "mem":
            memory_usage()
        else:
            print("Invalid option: " + sys.argv[2])
            print("Allowed types are: disk, mem")
            exit(1)
        exit(0)
    print("Usage: " + sys.argv[0] + " (-o <type>)")
    print("Where type is: disk, mem")
    exit(1)

def disk_usage():
    print_disk_info()
    print("Checking disk usage...")
    if os.name == 'nt':
        usage = shutil.disk_usage("C:")
    else:
        usage = shutil.disk_usage("/")
    percentage = usage.used / usage.total * 100
    larm.larm("Dateisystem verwendeter Speicherplatz in %", round(percentage), soft_disk_usage, hard_disk_usage)

def memory_usage():
    print_memory_info()
    print("Checking memory usage...")
    mem = psutil.virtual_memory()
    larm.larm("Speicherverbrauch in %", round(mem.percent), soft_memory_usage, hard_memory_usage)

def print_disk_info():
    print("Disk Usage Threshold:")
    print("Softlimit Disk Usage: ", soft_disk_usage)
    print("Hardlimit Disk Usage: ", hard_disk_usage)
    print("--------------------------------------------------------")

def print_memory_info():
    print("Memory Usage Threshold:")
    print("Softlimit Memory Usage: ", soft_memory_usage)
    print("Hardlimit Memory Usage: ", hard_memory_usage)
    print("--------------------------------------------------------")

parse_options()