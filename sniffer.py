import threading
import sys
import os

# --- Robust Imports ---
try:
    import customtkinter as ctk
    # Explicitly importing from layers helps VS Code resolve names better
    from scapy.all import sniff
    from scapy.layers.inet import IP, TCP, UDP, ICMP
    from scapy.packet import Raw
except ImportError:
    print("Missing dependencies. Please run: pip install scapy customtkinter")
    sys.exit(1)

# Initialize the UI appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class PacketSnifferApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Educational Network Sniffer")
        self.geometry("1000x600")

        # Application State
        self.sniffing = False
        self.sniff_thread = None

        # --- UI Layout ---
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Control Panel
        self.control_frame = ctk.CTkFrame(self)
        self.control_frame.grid(row=0, column=0, padx=20, pady=15, sticky="ew")

        self.start_button = ctk.CTkButton(
            self.control_frame, 
            text="Start Sniffing", 
            command=self.toggle_sniffing,
            fg_color="#28a745", 
            hover_color="#218838"
        )
        self.start_button.pack(side="left", padx=10, pady=10)

        self.clear_button = ctk.CTkButton(
            self.control_frame, 
            text="Clear Logs", 
            command=self.clear_logs
        )
        self.clear_button.pack(side="left", padx=10, pady=10)

        self.status_label = ctk.CTkLabel(self.control_frame, text="Status: Ready", text_color="gray")
        self.status_label.pack(side="right", padx=20)

        # Output Log
        self.textbox = ctk.CTkTextbox(self, font=("Consolas", 13), activate_scrollbars=True)
        self.textbox.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
        
        self.textbox.insert("0.0", "LOG STARTED: Waiting for user action...\n" + "-"*50 + "\n")

    def toggle_sniffing(self):
        if not self.sniffing:
            self.sniffing = True
            self.start_button.configure(text="Stop Sniffing", fg_color="#dc3545", hover_color="#c82333")
            self.status_label.configure(text="Status: Sniffing...", text_color="#28a745")
            
            # Use daemon=True so the thread closes when the app closes
            self.sniff_thread = threading.Thread(target=self.run_sniffer, daemon=True)
            self.sniff_thread.start()
        else:
            self.sniffing = False
            self.start_button.configure(text="Start Sniffing", fg_color="#28a745", hover_color="#218838")
            self.status_label.configure(text="Status: Stopped", text_color="#ffc107")

    def run_sniffer(self):
        """Runs the Scapy sniffing loop."""
        try:
            # stop_filter checks the boolean; if it returns True, sniff() ends
            sniff(prn=self.packet_callback, stop_filter=lambda x: not self.sniffing, store=False)
        except Exception as e:
            self.after(0, self.show_error, str(e))

    def packet_callback(self, pkt):
        """Processes each captured packet."""
        if IP in pkt:
            src_ip = pkt[IP].src
            dst_ip = pkt[IP].dst
            proto_name = "OTHER"
            
            if TCP in pkt: proto_name = "TCP"
            elif UDP in pkt: proto_name = "UDP"
            elif ICMP in pkt: proto_name = "ICMP"

            # Clean raw payload data
            payload_preview = ""
            if pkt.haslayer(Raw):
                raw_payload = pkt[Raw].load
                # Convert bytes to string, replacing non-printable characters with '.'
                payload_preview = "".join([chr(b) if 32 <= b < 127 else "." for b in raw_payload[:50]])

            log_line = f"[{proto_name}] {src_ip} -> {dst_ip} | Data: {payload_preview}\n"
            
            # Safe UI update from thread
            self.after(0, self.update_textbox, log_line)

    def update_textbox(self, text):
        self.textbox.insert("end", text)
        self.textbox.see("end")

    def show_error(self, message):
        self.textbox.insert("end", f"\n[!] ERROR: {message}\n")
        self.toggle_sniffing()

    def clear_logs(self):
        self.textbox.delete("1.0", "end")

def is_admin():
    """Check for Admin (Windows) or Root (Unix) privileges."""
    try:
        if os.name == 'nt': # Windows
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        else: # Linux/macOS
            return os.getuid() == 0
    except AttributeError:
        return False

if __name__ == "__main__":
    if not is_admin():
        print("************************************************************")
        print("WARNING: This script requires Administrator/Root privileges.")
        print("On Windows: Run VS Code as Administrator.")
        print("On Linux: Run with 'sudo'.")
        print("************************************************************")

    app = PacketSnifferApp()
    app.mainloop()