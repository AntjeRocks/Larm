import larm
import shutil
import psutil # must be installed
import sys
import os

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
            exit(1)
        exit(0)
    print("Usage: " + sys.argv[0] + " (-o <type>)")
    print("Where type is: disk, memory")
    exit(1)

def disk_usage():
    print("Checking disk usage...")
    if os.name == 'nt':
        usage = shutil.disk_usage("C:")
    else:
        usage = shutil.disk_usage("/")
    percentage = usage.used / usage.total * 100
    larm.larm("Dateisystem verwendeter Speicherplatz in %", round(percentage), 80, 90)

def memory_usage():
    print("Checking memory usage...")
    mem = psutil.virtual_memory()
    larm.larm("Speicherverbrauch in %", round(mem.percent), 50, 60)

parse_options()