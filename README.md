# 🌐 Modern Network Packet Sniffer

A lightweight, modern graphical user interface (GUI) tool built with **Python** for real-time network traffic analysis. This tool captures network packets and displays essential information such as source/destination IP addresses, protocols, and raw payload data.

---

## ✨ Features
- **Real-time Capture:** Monitor live network traffic as it happens.
- **Protocol Identification:** Automatically detects **TCP**, **UDP**, and **ICMP** protocols.
- **Payload Inspection:** Extracts and displays a sanitized ASCII preview of raw packet data.
- **Modern UI:** A clean, dark-themed interface built with `CustomTkinter`.
- **Cross-Platform Support:** Includes privilege checks for both Windows (Administrator) and Linux (Root).

---

## 🛠️ Prerequisites

Before running the application, ensure you have the following installed:

1.  **Python 3.10+**: [Download Python](https://www.python.org/downloads/)
2.  **Npcap (Windows Users ONLY)**: 
    - Scapy requires a packet capture driver to interact with your network card.
    - Download and install **[Npcap](https://nmap.org/npcap/)**.
    - **CRITICAL:** During installation, check the box that says **"Install Npcap in WinPcap API-compatible Mode"**.
3.  **Administrative Privileges**: Packet sniffing requires direct access to network hardware, which requires Admin (Windows) or Sudo (Linux) rights.

---

## 🚀 Installation & Setup

1. **Clone or create your project folder.**
2. **Install the required Python libraries** via the terminal:
   ```bash
   pip install scapy customtkinter
   ```

---

## 💻 How to Run in Visual Studio Code

### On Windows:
1.  Close Visual Studio Code if it is open.
2.  Right-click the **VS Code icon** on your desktop or start menu and select **"Run as Administrator"**.
3.  Open your project folder.
4.  Open `sniffer.py`.
5.  Press `F5` to run or type `python sniffer.py` in the integrated terminal.

### On Linux:
1.  Open your terminal in the project folder.
2.  Run the script using `sudo`:
    ```bash
    sudo python3 sniffer.py
    ```

---

## 📖 How to Use
1.  **Launch the App**: Once the GUI appears, the status will show "Ready."
2.  **Start Sniffing**: Click the green **"Start Sniffing"** button. The status will change to "Sniffing..." and packets will begin appearing in the log window.
3.  **Analyze**:
    - **[TCP/UDP/ICMP]**: Shows the protocol used.
    - **IP Addresses**: Shows where the data is coming from and where it is going.
    - **Data**: Shows the first 50 characters of the raw packet content (non-readable characters are replaced with dots).
4.  **Stop**: Click the red **"Stop Sniffing"** button to halt the capture.
5.  **Clear**: Click **"Clear Logs"** to empty the display window.

---

## ⚖️ Ethical Use & Disclaimer

**This tool is for educational and self-testing purposes only.**

- **Authorization**: Never use this tool to capture traffic on a network you do not own or do not have explicit, written permission to monitor.
- **Privacy**: Intercepting network traffic in public or shared spaces may be illegal and is a violation of privacy.
- **Responsibility**: The developer is not responsible for any misuse of this software or for any legal consequences resulting from its use.

**Always practice "White Hat" ethics: Use your skills for good and with permission.**

---

## 📦 Project Structure
```text
packet-sniffer/
│
├── sniffer.py        # The main Python application code
└── README.md         # Documentation and instructions
```
