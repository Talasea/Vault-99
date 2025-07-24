WIRESHARK:

==========

  

1. Wireshark installieren.

   Download von:

         [https://www.wireshark.org/download.html](https://www.wireshark.org/download.html)

  

2. Voraussetzungen schaffen:

   - Der Rechner, der protokolliert, muss im gleichen Netzwerk sein.

         - Überblick , über die benutzten Netzwerksadapter, verschaffen.

           (Damit im Wireshark das richtige Device ausgewählt werden kann.)

3. Wireshark starten und das Netzwerkdevice auswählen

  

4. Capture starten

  

5. Event abwarten

  

6. Capture stoppen

  

7. Event finden.

   - Zum Beispiel durch geschicktes konfigurieren eines Displayfilters.

     Beispiel: "ip.addr == 192.168.11.208 and http"

         - An den Farben orientieren

         - ggf. die Zeitanzeige nutzen (umstellen)

8. Packete/ Traffic interpretieren :)

  

# ###############################################################

  

  

Paketfilter konfugurieren:

  

-> Capture Filter

   -> Filtert die Pakete bereits bei der Aufzeichnung

  

-> Display Filter

   -> Es werden ALLE Pakete aufgezeichnet und 'später' ausgewählt, welche man betrachten möchte

# ####################################

  

Für die Übung:

  

1. Sicherstellen, daß ein Webserver (für http) erreichbar ist.

   (Wir wollen http Traffic capturen.)

   -> Kali Linus Starten und einloggen (kali//kali)

         -> Apache Webserver installieren:

            sudo apt install apache2  -> Dieser Befehl installiert einen Webserver)

                        systemctl start apache2

         -> Browser öffnen und "127.0.0.1"  aufrufen.

            -> Die Default Apache Seite sollte angezeigt werden.

         -> Die IP-Adresse des Webservers in Erfahrung bringen:

            -> Auf der Konsole "ifconfig" ausführen und nach dem richtigen Adapter schauen.

                           In unserem Fall ist es 192.168.11.208

         -> Auf den Host wechseln, Browser öffnen und hier die Adresse des Apache Servers eingeben.

            Beispiel: [http://192.168.11.208](http://192.168.11.208/)