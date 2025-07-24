Realtek Semiconductor Corp. RTL88x2bu [AC1200 Techkey]

  

Bus 001 Device 003: ID 0bda:b812 Realtek Semiconductor Corp. RTL88x2bu [AC1200 Techkey]

// ===========================================================================

  

T:  Bus=01 Lev=02 Prnt=02 Port=00 Cnt=01 Dev#=  3 Spd=480 MxCh= 0

D:  Ver= 2.10 Cls=00(>ifc ) Sub=00 Prot=00 MxPS=64 #Cfgs=  1

P:  Vendor=0bda ProdID=b812 Rev=02.10

S:  Manufacturer=Realtek

S:  Product=USB3.0 802.11ac 1200M Adapter

S:  SerialNumber=123456

C:  #Ifs= 1 Cfg#= 1 Atr=80 MxPwr=500mA

I:  If#= 0 Alt= 0 #EPs= 5 Cls=ff(vend.) Sub=ff Prot=ff Driver=(none)

E:  Ad=05(O) Atr=02(Bulk) MxPS= 512 Ivl=0ms

E:  Ad=06(O) Atr=02(Bulk) MxPS= 512 Ivl=0ms

E:  Ad=08(O) Atr=02(Bulk) MxPS= 512 Ivl=0ms

E:  Ad=84(I) Atr=02(Bulk) MxPS= 512 Ivl=0ms

E:  Ad=87(I) Atr=03(Int.) MxPS=  64 Ivl=500us

  

// ===========================================================================

  

  

  

Einrichten eines wireless USB-Sticks vom Typ RTL88x2bu:

=======================================================

  

Zweck:

- Besserer Empfang durch externe Antenne

- Geschwindigkeit: 5GHz-Band ist dadurch benutzbar

  

Die folgenden Befehle ggf in einem Script laufen lassen:

  

                #!/bin/sh

  

                sudo apt update

                sudo apt upgrade

  

                # Install prereqs

                sudo apt install git

                sudo apt install dnsmasq

                sudo apt install hostapd

                sudo apt install bc

                sudo apt install build-essential

                sudo apt install dkms

                sudo apt install raspberrypi-kernel-headers

  

# Reboot just in case there were any kernel updates

                sudo reboot

  

# Pull down the driver source

                sudo git clone [https://github.com/cilynx/rtl88x2bu](https://github.com/cilynx/rtl88x2bu)

                cd rtl88x2bu/

  

# Configure 'Makefile' for RasPi

                sudo sed -i 's/I386_PC = y/I386_PC = n/' Makefile

                sudo sed -i 's/ARM_RPI = n/ARM_RPI = y/' Makefile

  

# DKMS as above

                VER=$(sed -n 's/\PACKAGE_VERSION="\(.*\)"/\1/p' dkms.conf)                // kein sudo !

                sudo rsync -rvhP ./ /usr/src/rtl88x2bu-${VER}

                sudo dkms add -m rtl88x2bu -v ${VER}

                sudo dkms build -m rtl88x2bu -v ${VER}                                                         // dauert etwa 5 Minuten auf meinem Raspi 4b

                sudo dkms install -m rtl88x2bu -v ${VER}

                sudo reboot

                sudo nmtui                                                                                                                                                                 // Damit werden die (Wireless-) Verbindungen editiert (Network Manager)

                                                                                                                                                                                                                         // -> Device Wlan1 in das gewünschte Netzwerk einbinden

                [sudo nmcli]                                                                                                                                                         // Network Manager auf CLI

// =======================================================================================================================

  

Remote Desktop auf Raspberry einrichten:

  

                sudo apt install xrdp

                sudo systemctel start xrdp

In Windows 'mstsc' -> Im grafischen UI Raspi-Config aufgerufen und die Locales konfiguriert

sudo reboot

  

// =======================================================================================================================

  

Nun wird, wenn gewünscht, das Routing zwischen den beiden Netzen eingerichtet:

  

1. Voraussetzung:

        eth0 und wlan1 sind korrekt eingerichtet

        - eth0 ist im Netz 192.168.8.0/24 (Wird später an einen 8-Port-Switch angeschlossen / Zweites Netzwerk.)

        - wlan1 ist im Netz 192.168.11.0/24 (wireless USB-Adapter, 5GHz / stellt die Verbindung zum Hauptrouter her.)

  

2. System auf den aktuellsten Stand bringen:

        - sudo update

        - sudo upgrade

3. IP-Forwarding aktivieren:

        - sudo nano /etc/sysctl.conf

        - net.ipv4.ip_forward = 1                // Diese Zeile hinzufügen

        - sudo sysctl -p                                // Einstellungen aktualisieren

4. (IP-Tables Konfiguration. Falls es verwendet wird.)

        - sudo iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT

        - sudo iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT

5. (UFW konfigurieren. Je nachdem was benutzt wird.)

  

6. Routing konfigurieren:

        - sudo ip route add 192.168.11.0/24 via 192.168.8.1 dev eth0

        - sudo ip route add 192.168.8.0/24 via 192.168.11.1 dev eth1

        - Kontrolle mit 'ip route show'

        - Neustart des Routing: 'sudo systemctl restart networking'

7. Test mit Ping in beide Richtungen.