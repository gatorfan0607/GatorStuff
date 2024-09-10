# GatorStuff
Random Things I made - Feel free to use anything you like
Gator's Troubleshooting Utility
Overview
Gator's Troubleshooting Utility is a Python application designed to streamline IT troubleshooting and system maintenance tasks. The application provides a graphical user interface (GUI) that allows users to easily execute various system commands and utilities, view troubleshooting information, and run scan utilities. It features four main sections, each offering different functionalities to assist in diagnosing and resolving system issues.

Features
1. Troubleshooting Utilities
Available Commands: IPConfig, Ping Google, Traceroute Google, ARP Table, DHCP Leases, DNS Cache, Netstat, Get Mac, Route Print
Functionality: Select and run a set of predefined troubleshooting commands. Results are saved to C:\SFC_logs and displayed in a message box once the execution is complete.
2. System Utilities
Available Utilities: Computer Management, Settings, Network and Sharing Center, System Information, Print Management, Control Panel, System Properties, Task Scheduler, Empty MMC
Functionality: Launch system utilities and administrative tools directly from the GUI with admin privileges.
3. Scan Utilities
Available Scans: SFC Scan, DISM Scan, Check Disk /f, Check Disk /r
Functionality: Execute system scan commands with admin privileges to check and repair system files and disk issues.
4. Admin Utilities
Available Commands: NSLookup, CMD (Run as Admin), PowerShell (Run as Admin)
Functionality: Open NSLookup in a new command prompt window, and start Command Prompt or PowerShell with administrative rights.
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/your-username/gators-troubleshooting-utility.git
Install Dependencies Make sure you have Python installed, and then install the required libraries using pip:

bash
Copy code
pip install tk
Usage
Run the Application Navigate to the directory where you cloned the repository and run the application using Python:

bash
Copy code
python main.py
Select and Execute Utilities

Use the checkboxes to select the troubleshooting, system, or scan utilities you want to run.
Click the "Run Selected" buttons to execute the chosen commands or utilities.
Admin utilities can be opened directly using their respective buttons.
License
This project is licensed under the GNU General Public License v3.0 (GPLv3). See the LICENSE file for details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.


______________________________________________________________________________________________________________

Gator's Tshoot Tool
Overview
Gator's Reference Tool is a Python-based desktop application designed to provide detailed information and troubleshooting steps for various IT tools and commands. The application features a user-friendly graphical interface, allowing users to access a wide range of technical topics and commands with just a click.

Features
Interactive Menu: Access detailed information through a simple menu structure.
Dynamic Button List: Easily navigate through various IT topics and commands with dynamically created buttons.
Scrollable Interface: Enjoy a smooth user experience with scrollable sections for both the list of commands and the information display.
Functionality
Menu Options:

File Menu: Includes an "Exit" option to close the application.
About Menu: Displays a brief overview of the application with copyright information.
Left Panel:

Contains a scrollable list of buttons for different IT topics (e.g., IPConfig, Ping, Tracert, etc.).
Each button, when clicked, displays detailed information about the corresponding topic in the right panel.
Right Panel:

Shows detailed information and troubleshooting steps related to the selected topic.
Features a scrollbar for easy navigation through the content.
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/your-username/gators-reference-tool.git
Install Dependencies Ensure you have Python installed. This project requires the tkinter module, which is included with Python by default.

Usage
Run the Application Navigate to the directory where you cloned the repository and run the application using Python:

bash
Copy code
python main.py
Explore Topics

Click on the buttons in the left panel to view detailed information about various IT topics and commands.
Use the scrollbar in the right panel to navigate through the information.
License
This project is licensed under the GNU General Public License v3.0 (GPLv3). See the LICENSE file for details.

Contributing
Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

