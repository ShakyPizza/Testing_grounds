import tkinter as tk
from tkinter import scrolledtext
import random
import time

class HackerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Hacker Style Terminal")
        self.geometry("800x600")
        self.configure(bg='black')
        
        self.terminal = scrolledtext.ScrolledText(self, wrap=tk.WORD, bg='black', fg='green', insertbackground='green', font=('Courier', 12))
        self.terminal.pack(fill=tk.BOTH, expand=True)
        
        
        self.bind('<Return>', self.on_enter)
        
        self.fake_hacking_text()

    def create_hacker_window(self, title, x, y, width, height):
        window = tk.Toplevel(self)
        window.title(title)
        window.geometry(f"{width}x{height}+{x}+{y}")
        window.configure(bg='black')

        label = tk.Label(window, text=title, bg='black', fg='green', font=('Courier', 12))
        label.pack(pady=10)
    
    def on_enter(self, event):
        command = self.terminal.get("1.0", tk.END).strip()
        self.terminal.insert(tk.END, f"\nYou entered: {command}\n")
    
    def fake_hacking_text(self):
        hacking_texts = [
        "Accessing system files...\n",
        "Bypassing firewall...\n",
        "Decrypting passwords...\n",
        "Downloading data...\n",
        "Connecting to server...\n",
        "Injecting malicious code...\n",
        "Retrieving user credentials...\n",
        "Scanning for vulnerabilities...\n",
        "Compiling exploits...\n",
        "Establishing secure connection...\n",
        "Monitoring network traffic...\n",
        "Brute-forcing authentication...\n",
        "Escalating privileges...\n",
        "Extracting encryption keys...\n",
        "Hijacking session tokens...\n",
        "Disabling security protocols...\n",
        "Downloading sensitive files...\n",
        "Uploading payload...\n",
        "Cleaning logs...\n",
        "Covering tracks...\n",
        "Initializing hacking sequence...\n",
        "Compromising target IP...\n",
        "Fetching data from remote server...\n",
        "Decrypting database entries...\n",
        "Disabling security systems...\n",
        "Generating exploit payload...\n",
        "Exploiting buffer overflow...\n",
        "Accessing confidential files...\n",
        "Decrypting secured messages...\n",
        "Scanning ports...\n",
        "Mapping network topology...\n",
        "Enumerating system services...\n",
        "Injecting SQL commands...\n",
        "Exploiting zero-day vulnerability...\n",
        "Harvesting email addresses...\n",
        "Infecting system with malware...\n",
        "Hijacking DNS requests...\n",
        "Modifying registry values...\n",
        "Uploading backdoor...\n",
        "Downloading encryption keys...\n",
        "Analyzing traffic patterns...\n",
        "Injecting XSS payload...\n",
        "Manipulating HTTP headers...\n",
        "Gaining shell access...\n",
        "Establishing persistence...\n"
    ]
        for text in hacking_texts:
            self.terminal.insert(tk.END, text)
            self.terminal.see(tk.END)
            self.terminal.update_idletasks()
            time.sleep(random.uniform(0.5, 1.5))

if __name__ == "__main__":
    app = HackerGUI()
    app.mainloop()