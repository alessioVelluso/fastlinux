#!/usr/bin/python3
import os
import subprocess
import shutil
from urllib.request import urlretrieve


class KaliCustomizer:
    image_url = "https://raw.githubusercontent.com/dorianpro/kaliwallpapers/master/kali-linux-wallpaper-v4.png"
    username = ""

    def __init__(self):
        self.download_wallpaper()
        self.user_panel_config()
        self.set_keyboard_layout()

    def download_wallpaper(self):
        try:
            local_path =  f'/home/{self.username}/Pictures/wallpaper.png'

            # Scarica l'immagine con timeout di 15 secondi
            urlretrieve(self.image_url, local_path)
            print(f"Immagine scaricata in: {local_path}")
        except Exception as e:
            print(e)

    def user_panel_config(self):
        try:
            os.system("xfce4-panel — quit")
            local_path =  f'/home/{self.username}/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml'
            shutil.copy("./panelconfig.xml", local_path)
            os.system("xfce4-panel -r")
        except Exception as e:
            print(e)

    def set_keyboard_layout(self):
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
