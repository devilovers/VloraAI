import speech_recognition as sr
from gtts import gTTS
import pygame
import webbrowser
import os
import sys
import time
import subprocess

pygame.mixer.init()

def vlora_bicara(teks):
    print(f"\n[Vlora]: {teks}")
    file_audio = "vlora_temp.mp3"
    try:
        tts = gTTS(text=teks, lang='id', slow=False)
        tts.save(file_audio)
        
        pygame.mixer.music.load(file_audio)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            
        pygame.mixer.music.unload()
        if os.path.exists(file_audio):
            os.remove(file_audio)
    except Exception as e:
        print(f"[Error Suara]: {e}")

SITES = {
    "https://www.youtube.com": {
        "nama": "YouTube",
        "keywords": ["youtube", "yutub", "yu tub", "utub", "yt", "yutup", "tub", "you tube", "yutob", "yutubku", "pideo", "video", "nonton"]
    },
    "https://www.github.com": {
        "nama": "GitHub",
        "keywords": ["github", "git hab", "git", "githab", "git hub", "githubku", "repo", "repository", "gethuk", "getuk"]
    },
    "https://chatgpt.com": {
        "nama": "ChatGPT",
        "keywords": ["chat gpt", "chatgpt", "cat gpt", "gpt", "gepete", "cet gpt", "capete", "chat jipiti", "jipiti", "ai"]
    },
    "https://gemini.google.com": {
        "nama": "Gemini",
        "keywords": ["gemini", "geminai", "gemni", "jiminy", "gemini google", "jemini", "jimani"]
    },
    "https://www.google.com": {
        "nama": "Google",
        "keywords": ["chrome", "krom", "google", "gugel", "gugl", "browser", "browsing", "internet", "search", "cari"]
    },
    "https://web.whatsapp.com": {
        "nama": "WhatsApp Web",
        "keywords": ["whatsapp web", "wa web", "web wa", "wasap web", "watsap web", "web whatsapp"]
    },
    "https://www.pinterest.com": {
        "nama": "Pinterest",
        "keywords": ["pinterest", "pinteres", "pin", "pinter", "pinters", "finteres", "gambar", "foto", "referensi"]
    },
    "https://pmb.poliban.ac.id/login": {
        "nama": "web poliban",
        "keywords": ["poliban", "pmb poliban", "kampus", "kuliah", "pmb", "poliban pmb", "web poliban", "login poliban", "polybag", "polibag", "poli bag", "poly bag", "polibak", "volleyball", "vollyball", "voleyball", "volyball"]
    },
    "http://localhost/myfinance/pages/dashboard.php": {
        "nama": "My Finance",
        "keywords": ["my finance", "myfinance", "finance", "keuangan", "finan", "mai finance", "mai finan", "my finan", "dashboard keuangan"]
    }
}

APPS = {
    "VS Code": {
        "target": "code",
        "keywords": ["vscode", "vs code", "pescode", "viescode", "visual studio code", "koding", "kod", "code", "bescode", "vsc", "pes code", "vescode", "biscode", "coding", "editor"]
    },
    "Spotify": {
        "target": [f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Spotify\\Spotify.exe", "spotify:"],
        "keywords": ["spotify", "spotifi", "lagu", "musik", "spoti", "supotifi", "espotifi", "potifi", "pemutar musik"]
    },
    "WhatsApp": {
        "target": ["whatsapp:", f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\WhatsApp\\WhatsApp.exe"],
        "keywords": ["whatsapp", "wa", "watsap", "wasap", "chat", "watsup", "pesan", "wa desktop"]
    },
    "Word": {
        "target": "winword",
        "keywords": ["word", "ms word", "werd", "mikey word", "microsoft word", "ngetik", "dokumen word"]
    },
    "Excel": {
        "target": "excel",
        "keywords": ["excel", "ms excel", "eksel", "microsoft excel", "eskel", "tabel"]
    },
    "PowerPoint": {
        "target": "powerpnt",
        "keywords": ["powerpoint", "power point", "ppt", "paling poos", "pwer point", "presentasi", "merek slide"]
    },
    "XAMPP": {
        "target": ["C:\\xampp\\xampp-control.exe", "xampp-control"],
        "keywords": ["xampp", "ksamp", "examp", "samp", "xam", "server", "xampp control", "sams", "sam"]
    },
    "Roblox": {
        "target": [f"C:\\Users\\{os.getlogin()}\\OneDrive\\Desktop\\Roblox Player.lnk", f"C:\\Users\\{os.getlogin()}\\Desktop\\Roblox Player.lnk", "roblox:"],
        "keywords": ["roblox", "roblok", "roblos", "game", "robloks", "main game"]
    },
    "Canva": {
        "target": [f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Canva\\Canva.exe", "https://www.canva.com"],
        "keywords": ["canva", "kanva", "desain", "canba", "edit foto"]
    },
    "File Explorer": {
        "target": "explorer",
        "keywords": ["file saya", "file", "explorer", "file manager", "folder", "dokumen", "berkas", "buka folder", "buka file", "my computer", "komputer"]
    },
    "Kamera": {
        "target": "microsoft.windows.camera:",
        "keywords": ["kamera", "camera", "cam", "foto kamera", "kamera laptop", "webcam"]
    }
}

def buka_aplikasi(app_target):
    if isinstance(app_target, list):
        for path in app_target:
            try:
                if path.startswith("http://") or path.startswith("https://"):
                    webbrowser.open(path)
                    return True
                elif os.path.exists(path):
                    os.startfile(path)
                    return True
                elif ":" in path and not os.path.isabs(path):
                    os.startfile(path)
                    return True
            except Exception:
                continue
        return False
    else:
        try:
            if app_target.startswith("http://") or app_target.startswith("https://"):
                webbrowser.open(app_target)
            elif ":" in app_target and not os.path.isabs(app_target):
                os.startfile(app_target)
            else:
                os.system(f"start {app_target}")
            return True
        except Exception:
            return False

def tutup_terminal():
    pid = os.getpid()
    subprocess.Popen(f"taskkill /F /PID {pid}", shell=True)

def eksekusi_perintah(perintah):
    perintah = perintah.lower().replace(".", "").replace(",", "").strip()
    
    KATA_NONAKTIF = [
        "nonaktifkan", "non aktifkan", "matikan", "keluar", "berhenti", 
        "stop", "off", "tutup", "dada", "bye", "daah", "dadah", "close", "sleep"
    ]
    if any(k in perintah for k in KATA_NONAKTIF):
        vlora_bicara("Sistem Vlora dinonaktifkan. Sampai jumpa.")
        time.sleep(0.5)
        tutup_terminal()
        return

    for nama_aplikasi, data in APPS.items():
        for kw in data["keywords"]:
            if kw in perintah:
                vlora_bicara(f"Siap! Membuka aplikasi {nama_aplikasi}.")
                berhasil = buka_aplikasi(data["target"])
                if not berhasil:
                    vlora_bicara(f"Maaf, gagal membuka {nama_aplikasi}. Jalur aplikasi tidak ditemukan.")
                return

    for url, data in SITES.items():
        for kw in data["keywords"]:
            if kw in perintah:
                vlora_bicara(f"Siap! Berhasil membuka {data['nama']} di browser.")
                webbrowser.open(url)
                return

    vlora_bicara("Maaf, perintah tidak terdaftar dalam sistem.")

def dengarkan_suara():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 120
    recognizer.dynamic_energy_threshold = False
    recognizer.pause_threshold = 0.8

    with sr.Microphone() as source:
        print("\n[Mendengarkan...] Katakan perintahmu...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        
        try:
            audio = recognizer.listen(source, timeout=None, phrase_time_limit=7)
            teks = recognizer.recognize_google(audio, language="id-ID")
            print(f"[Input Suara Terdeteksi]: '{teks}'")
            return teks.lower()
        except sr.UnknownValueError:
            print("[Sistem]: Suara kurang jelas, mencoba mendengarkan lagi...")
            return ""
        except sr.RequestError:
            vlora_bicara("Koneksi internet bermasalah. Layanan pengenal suara tidak merespons.")
            return ""

if __name__ == "__main__":
    vlora_bicara("Sistem Vlora aktif dan siap menerima perintah.")
    
    NAME_VARIATIONS = [
        "vlora", "flora", "velora", "plora", "blora", "lora", "folra", "bora", 
        "vora", "mora", "ra", "lor", "flo", "la", "oi", "hey", "hei", "bro", "sis",
        "halo", "hallo", "wong", "mang", "bang", "kak", "mbak", "lur", "slur"
    ]

    while True:
        input_teks = dengarkan_suara()
        
        if input_teks:
            input_bersih = input_teks.replace(".", "").replace(",", "").strip()
            
            ditemukan_panggilan = any(nama in input_bersih for nama in NAME_VARIATIONS)
            
            if ditemukan_panggilan:
                perintah = input_bersih
                for nama in NAME_VARIATIONS:
                    if nama in perintah:
                        perintah = perintah.split(nama)[-1].strip()
                        break
                
                if perintah:
                    eksekusi_perintah(perintah)
                else:
                    vlora_bicara("Ya, ada yang bisa Vlora bantu?")
            else:
                eksekusi_perintah(input_bersih)