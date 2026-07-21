import speech_recognition as sr
from gtts import gTTS
import pygame
import webbrowser
import os
import sys
import time

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
    "youtube": "https://www.youtube.com",
    "yutub": "https://www.youtube.com",
    "yu tub": "https://www.youtube.com",
    "utub": "https://www.youtube.com",
    "github": "https://www.github.com",
    "git hab": "https://www.github.com",
    "chat gpt": "https://chatgpt.com",
    "chatgpt": "https://chatgpt.com",
    "cat gpt": "https://chatgpt.com",
    "gemini": "https://gemini.google.com",
    "geminai": "https://gemini.google.com",
    "chrome": "https://www.google.com",
    "krom": "https://www.google.com",
    "google": "https://www.google.com",
    "whatsapp web": "https://web.whatsapp.com",
    "wa web": "https://web.whatsapp.com"
}

APPS = {
    "vscode": "code",
    "vs code": "code",
    "pescode": "code",
    "viescode": "code",
    "visual studio code": "code",
    "spotify": f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Spotify\\Spotify.exe",
    "spotifi": f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Spotify\\Spotify.exe",
    "discord": f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe",
    "diskor": f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe",
    "whatsapp": f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\WhatsApp\\WhatsApp.exe",
    "wa": f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
}

def eksekusi_perintah(perintah):
    perintah = perintah.lower().replace(".", "").replace(",", "").strip()
    
    for site_keyword, url in SITES.items():
        if site_keyword in perintah:
            vlora_bicara(f"Siap! Berhasil membuka {site_keyword} di browser.")
            webbrowser.open(url)
            return

    for app_keyword, path in APPS.items():
        if app_keyword in perintah:
            try:
                vlora_bicara(f"Siap! Berhasil menjalankan aplikasi {app_keyword}.")
                os.system(f'start "" "{path}"')
            except Exception as e:
                vlora_bicara(f"Maaf, gagal membuka {app_keyword}. Jalur aplikasi tidak ditemukan.")
            return

    if "matikan" in perintah or "keluar" in perintah or "berhenti" in perintah or "stop" in perintah:
        vlora_bicara("Sistem Vlora dinonaktifkan. Sampai jumpa.")
        sys.exit()

    vlora_bicara("Maaf, perintah tidak terdaftar dalam sistem.")

def dengarkan_suara():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.8

    with sr.Microphone() as source:
        print("\n[Mendengarkan...] Katakan 'Halo Vlora' lalu perintahmu")
        
        try:
            audio = recognizer.listen(source, timeout=None, phrase_time_limit=6)
            teks = recognizer.recognize_google(audio, language="id-ID")
            print(f"[Input Suara Terdeteksi]: '{teks}'")
            return teks.lower()
        except sr.UnknownValueError:
            print("[Sistem]: Suara tidak terdeteksi dengan jelas.")
            return ""
        except sr.RequestError:
            vlora_bicara("Koneksi internet bermasalah. Layanan pengenal suara tidak merespons.")
            return ""

if __name__ == "__main__":
    vlora_bicara("Sistem Vlora online dan siap menerima perintah.")
    
    HALO_VARIATIONS = ["halo", "hallo", "helo", "hello", "hi", "hai", "aloh", "alo"]
    NAME_VARIATIONS = ["vlora", "flora", "velora", "plora", "blora", "lora", "folra"]

    WAKE_WORDS = []
    for halo in HALO_VARIATIONS:
        for name in NAME_VARIATIONS:
            WAKE_WORDS.append(f"{halo} {name}")
    
    WAKE_WORDS.extend(NAME_VARIATIONS)

    while True:
        input_teks = dengarkan_suara()
        
        if input_teks:
            input_bersih = input_teks.replace(".", "").replace(",", "")
            ditemukan = False
            
            for wake_word in WAKE_WORDS:
                if wake_word in input_bersih:
                    perintah = input_bersih.split(wake_word)[-1].strip()
                    ditemukan = True
                    
                    if perintah:
                        eksekusi_perintah(perintah)
                    else:
                        vlora_bicara("Ya, ada yang bisa Vlora bantu?")
                    break
            
            if not ditemukan and len(input_bersih) > 0:
                print(f"[Info]: Panggilan tidak terdeteksi dari ucapan: '{input_bersih}'")