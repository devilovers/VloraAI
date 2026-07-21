import keyboard
import subprocess
import os
import sys

FOLDER_SAAT_INI = os.path.dirname(os.path.abspath(__file__))
SCRIPT_VLORA = os.path.join(FOLDER_SAAT_INI, "vlora.py")
PYTHON_EXE = sys.executable

def jalankan_vlora():
    print("\n[Hotkey Terdeteksi]: Menjalankan Vlora Assistant...")
    
    if not os.path.exists(SCRIPT_VLORA):
        print(f"[Error]: File tidak ditemukan di {SCRIPT_VLORA}")
        return

    perintah_cmd = f'start cmd /k "title Vlora Assistant && cd /d \"{FOLDER_SAAT_INI}\" && \"{PYTHON_EXE}\" \"{SCRIPT_VLORA}\""'
    subprocess.Popen(perintah_cmd, shell=True)

if __name__ == "__main__":
    print("==============================================")
    print(" Vlora Hotkey Listener Active")
    print(" Tekan [ Ctrl + Alt + V ] untuk memanggil Vlora")
    print("==============================================")
    
    keyboard.add_hotkey('ctrl+alt+v', jalankan_vlora)
    keyboard.wait()