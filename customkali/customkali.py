#!/usr/bin/python3
import os
import subprocess
import tempfile
import shutil
from urllib.request import urlretrieve


class KaliCustomizer:
    image_url = "https://raw.githubusercontent.com/dorianpro/kaliwallpapers/master/kali-linux-wallpaper-v4.png"

    def __init__(self):
        self.change_wallpaper()

    def detect_desktop_environment(self):
        # Rileva l'ambiente desktop in uso
        if os.environ.get('DESKTOP_SESSION') == 'xfce': return 'xfce'
        elif os.environ.get('DESKTOP_SESSION') == 'gnome': return 'gnome'
        return 'unknown'

    def change_wallpaper(self):
        # Cambia lo sfondo usando un URL remoto
        de = self.detect_desktop_environment()

        # Crea una cartella temporanea dedicata
        temp_dir = os.path.join(tempfile.gettempdir(), "kali_customizer_wallpapers")
        os.makedirs(temp_dir, exist_ok=True)

        # Estrae il nome file dall'URL
        filename = os.path.basename(self.image_url.split("?")[0])
        local_path = os.path.join(temp_dir, filename)

        try:
            # Scarica l'immagine con timeout di 15 secondi
            urlretrieve(self.image_url, local_path)
            print(f"Immagine scaricata in: {local_path}")
        except Exception as e:
            print(f"Errore durante il download: {str(e)}")
            return

        # Applica lo sfondo
        if de == 'xfce':
            subprocess.run([
                "xfconf-query", "-c", "xfce4-desktop",
                "-p", "/backdrop/screen0/monitor0/workspace0/last-image",
                "-s", local_path
            ], check=True)
        elif de == 'gnome':
            subprocess.run([
                "gsettings", "set", "org.gnome.desktop.background",
                "picture-uri", f"file://{local_path}"
            ], check=True)

    def user_panel_config():
        user_config_path = os.path.expanduser("~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml")
        shutil.copy("./panelconfig.xml", user_config_path)
        os.system("xfce4-panel -r")

    def set_keyboard_layout(self):
        """Cambia il layout della tastiera da US a IT in modo permanente"""
        try:
            # 1. Cambio immediato per la sessione corrente
            subprocess.run(["setxkbmap", "it"], check=True)

            # 2. Modifica configurazione di sistema
            subprocess.run([
                "sed", "-i",
                's/^XKBLAYOUT=.*/XKBLAYOUT="it"/',
                "/etc/default/keyboard"
            ], check=True)

            # 3. Riconfigurazione automatica
            subprocess.run([
                "dpkg-reconfigure", "-f", "noninteractive",
                "keyboard-configuration"
            ], check=True)

            # 4. Riavvio servizi
            subprocess.run(["service", "keyboard-setup", "restart"], check=True)
            subprocess.run(["setupcon", "--force"], check=True)

            print("✅ Layout tastiera IT configurato con successo")

        except subprocess.CalledProcessError as e:
            print(f"❌ Errore: {str(e)}")
            print("Verifica i permessi e che il file /etc/default/keyboard esista")





KaliCustomizer()
