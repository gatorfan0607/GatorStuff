import subprocess
import os
import tkinter as tk
from tkinter import messagebox, ttk
import ctypes

# Function to run a command as admin
def run_as_admin(command):
    # Using ctypes to prompt for admin privileges
    ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/c {command}", None, 1)

# Function to run a command in a normal command prompt (non-admin)
def run_command(command):
    subprocess.run(command, shell=True)

# Troubleshooting utilities handler
def run_troubleshooting_utilities():
    troubleshooting_commands = {
        "IPconfig": "ipconfig /all",
        "Ping Google": "ping google.com -n 10",
        "Traceroute Google": "tracert google.com",
        "ARP Table": "arp -a",
        "Renew DHCP": "ipconfig /renew",
        "Flush DNS": "ipconfig /flushdns",
        "Netstat": "netstat",
        "Get Mac": "getmac",
        "Route Print": "route print"
    }

    selected_commands = [cmd for cmd, var in troubleshooting_vars.items() if var.get()]
    if selected_commands:
        output_dir = r"C:\SFC_logs"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        results = ""
        for cmd in selected_commands:
            command = troubleshooting_commands[cmd]
            result_file = os.path.join(output_dir, f"{cmd.replace(' ', '_')}.txt")
            execute_command(command, result_file)
            results += f"\n{cmd}:\n{'='*len(cmd)}\n{open(result_file).read()}\n"

        messagebox.showinfo("Success", "Troubleshooting commands executed. Results saved in C:\\SFC_logs")
    else:
        messagebox.showwarning("No Selection", "No troubleshooting utilities selected.")

# System utilities handler
def run_system_utilities():
    system_utilities_commands = {
        "Computer Management": "compmgmt.msc",
        "Settings": "start ms-settings:",
        "Network and Sharing Center": "control /name Microsoft.NetworkAndSharingCenter",
        "System Information": "msinfo32",
        "Print Management": "printmanagement.msc",
        "Control Panel": "control",
        "System Properties": "sysdm.cpl",
        "Task Scheduler": "taskschd.msc",
        "Empty MMC": "mmc"
    }

    selected_commands = [cmd for cmd, var in system_utilities_vars.items() if var.get()]
    if selected_commands:
        for cmd in selected_commands:
            command = system_utilities_commands[cmd]
            run_as_admin(command)
    else:
        messagebox.showwarning("No Selection", "No system utilities selected.")

# Scan utilities handler
def run_scan_utilities():
    scan_commands = {
        "SFC Scan": "sfc /scannow",
        "DISM Scan": "DISM /Online /Cleanup-Image /RestoreHealth",
        "Check Disk /f": "chkdsk /f",
        "Check Disk /r": "chkdsk /r"
    }

    selected_scans = [cmd for cmd, var in scan_vars.items() if var.get()]
    if selected_scans:
        for cmd in selected_scans:
            command = scan_commands[cmd]
            run_as_admin(command)
    else:
        messagebox.showwarning("No Selection", "No scan utilities selected.")

# Function to open NSLookup prompt
def open_nslookup():
    run_command("start cmd /k nslookup")

# Add PowerShell and CMD buttons
def open_powershell_as_admin():
    run_as_admin("powershell")

def open_cmd_as_admin():
    run_as_admin("cmd")

# Layout adjustments to align quadrants properly
root = tk.Tk()
root.title("Gator's Troubleshooting Utility")
root.geometry("1200x800")  # Increase window size for better proportion

# Frames for the quadrants
frame_left_top = ttk.Frame(root, padding="10")
frame_left_top.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
frame_left_bottom = ttk.Frame(root, padding="10")
frame_left_bottom.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
frame_right_top = ttk.Frame(root, padding="10")
frame_right_top.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
frame_right_bottom = ttk.Frame(root, padding="10")
frame_right_bottom.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Configure row/column weights for proportional resizing
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Troubleshooting Utilities
tk.Label(frame_left_top, text="Troubleshooting Utilities").grid(row=0, column=0, columnspan=2, pady=5)
troubleshooting_vars = {}
for i, (name, _) in enumerate({
    "IPconfig": None,
    "Ping Google": None,
    "Traceroute Google": None,
    "ARP Table": None,
    "DHCP Leases": None,
    "DNS Cache": None,
    "Netstat": None,
    "Get Mac": None,
    "Route Print": None
}.items()):
    var = tk.BooleanVar()
    chk = tk.Checkbutton(frame_left_top, text=name, variable=var)
    chk.grid(row=i+1, column=0, sticky=tk.W, padx=5)
    troubleshooting_vars[name] = var
tk.Button(frame_left_top, text="Run Selected", command=run_troubleshooting_utilities).grid(row=i+2, column=0, pady=5, sticky=tk.W)

# System Utilities
tk.Label(frame_right_top, text="System Utilities").grid(row=0, column=0, columnspan=2, pady=5)
system_utilities_vars = {}
for i, (name, _) in enumerate({
    "Computer Management": None,
    "Settings": None,
    "Network and Sharing Center": None,
    "System Information": None,
    "Print Management": None,
    "Control Panel": None,
    "System Properties": None,
    "Task Scheduler": None,
    "Empty MMC": None
}.items()):
    var = tk.BooleanVar()
    chk = tk.Checkbutton(frame_right_top, text=name, variable=var)
    chk.grid(row=i+1, column=0, sticky=tk.W, padx=5)
    system_utilities_vars[name] = var
tk.Button(frame_right_top, text="Run Selected", command=run_system_utilities).grid(row=i+2, column=0, pady=5, sticky=tk.W)

# Bottom-right quadrant for CMD, PowerShell, and NSLookup
tk.Label(frame_right_bottom, text="Admin Utilities").grid(row=0, column=0, pady=5)
tk.Button(frame_right_bottom, text="NSLookup", command=open_nslookup).grid(row=1, column=0, pady=5, sticky=tk.W)
tk.Button(frame_right_bottom, text="CMD (Run as Admin)", command=open_cmd_as_admin).grid(row=2, column=0, pady=5, sticky=tk.W)
tk.Button(frame_right_bottom, text="PowerShell (Run as Admin)", command=open_powershell_as_admin).grid(row=3, column=0, pady=5, sticky=tk.W)

# Scan Utilities
tk.Label(frame_left_bottom, text="Scan Utilities").grid(row=0, column=0, columnspan=2, pady=5)
scan_vars = {}
for i, (name, _) in enumerate({
    "SFC Scan": None,
    "DISM Scan": None,
    "Check Disk /f": None,
    "Check Disk /r": None
}.items()):
    var = tk.BooleanVar()
    chk = tk.Checkbutton(frame_left_bottom, text=name, variable=var)
    chk.grid(row=i+1, column=0, sticky=tk.W, padx=5)
    scan_vars[name] = var
tk.Button(frame_left_bottom, text="Run Selected", command=run_scan_utilities).grid(row=i+2, column=0, pady=5, sticky=tk.W)

# Run the GUI
root.mainloop()
