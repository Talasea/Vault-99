### **Schritt 1: Bestimmung der benötigten Subnetzbits**

- Um 3 Subnetze zu erstellen, benötigen wir mindestens **2 Bits** (da 22=4≥322=4≥3).
    
- Die neue Subnetzmaske wird **/26** (24 + 2).

### **Schritt 2: Subnetzberechnung**

Jedes Subnetz hat:

- **Subnetzmaske:** 255.255.255.192 (da 256−64=192256−64=192 im vierten Oktett).
    
- **Blockgröße:** 64 Adressen pro Subnetz (z. B. 0–63, 64–127, 128–191, 192–255).
    
- **Nutzbare Hosts pro Subnetz:** 2(32−26)−2=622(32−26)−2=62 Hosts.


### **Die 3 Subnetze**

|Subnetz|Netzwerkadresse|Erste nutzbare IP|Letzte nutzbare IP|Broadcastadresse|
|---|---|---|---|---|
|1|192.168.2.0/26|192.168.2.1|192.168.2.62|192.168.2.63|
|2|192.168.2.64/26|192.168.2.65|192.168.2.126|192.168.2.127|
|3|192.168.2.128/26|192.168.2.129|192.168.2.190|192.168.2.191|

- Das vierte Subnetz (192.168.2.192/26) bleibt **unbenutzt**, falls später benötigt.

- **Subnetzmaske:** 255.255.255.192 (/26).
    
- **Hosts pro Subnetz:** 62 nutzbare IPs.
    
- **Flexibilität:** Das vierte Subnetz kann für zukünftige Erweiterungen reserviert werden.



_____________________________________________________________________________________________

7 Subnetze 

1. Zuerst bestimmen wir die Anzahl der benötigten Bits für 7 Subnetze:  
    2^3 = 8 > 7, also benötigen wir 3 zusätzliche Bits.
    
2. Die neue Subnetzmaske wird:  
    255.255.255.224 oder /27 (24 + 3 = 27)
    
3. Die Subnetz-Größe berechnet sich wie folgt:  
    256 - 224 = 32 IP-Adressen pro Subnetz
    

## Subnetz-Aufteilung

Hier sind die 7 Subnetze mit ihren Netzwerk-IDs, Broadcast-Adressen und nutzbaren IP-Bereichen:

4. Subnetz 1:
    
    - Netzwerk-ID: 192.168.2.0/27
        
    - Erster Host: 192.168.2.1
        
    - Letzter Host: 192.168.2.30
        
    - Broadcast: 192.168.2.31
        
5. Subnetz 2:
    
    - Netzwerk-ID: 192.168.2.32/27
        
    - Erster Host: 192.168.2.33
        
    - Letzter Host: 192.168.2.62
        
    - Broadcast: 192.168.2.63
        
6. Subnetz 3:
    
    - Netzwerk-ID: 192.168.2.64/27
        
    - Erster Host: 192.168.2.65
        
    - Letzter Host: 192.168.2.94
        
    - Broadcast: 192.168.2.95
        
7. Subnetz 4:
    
    - Netzwerk-ID: 192.168.2.96/27
        
    - Erster Host: 192.168.2.97
        
    - Letzter Host: 192.168.2.126
        
    - Broadcast: 192.168.2.127
        
8. Subnetz 5:
    
    - Netzwerk-ID: 192.168.2.128/27
        
    - Erster Host: 192.168.2.129
        
    - Letzter Host: 192.168.2.158
        
    - Broadcast: 192.168.2.159
        
9. Subnetz 6:
    
    - Netzwerk-ID: 192.168.2.160/27
        
    - Erster Host: 192.168.2.161
        
    - Letzter Host: 192.168.2.190
        
    - Broadcast: 192.168.2.191
        
10. Subnetz 7:
    
    - Netzwerk-ID: 192.168.2.192/27
        
    - Erster Host: 192.168.2.193
        
    - Letzter Host: 192.168.2.222
        
    - Broadcast: 192.168.2.223

- Wir haben das ursprüngliche /24 Netzwerk in 7 gleich große /27 Subnetze aufgeteilt.
    
- Jedes Subnetz hat 32 IP-Adressen, von denen 30 für Hosts nutzbar sind.
    
- Die neue Subnetzmaske ist 255.255.255.224 oder /27.
    
- Es bleiben 32 IP-Adressen übrig (192.168.2.224 - 192.168.2.255), die für zukünftige Erweiterungen genutzt werden können.


----------------------------------- oder ---------------------------------------------------

### **Schritt 1: Bestimmung der benötigten Subnetzbits**

- Um **7 Subnetze** zu erstellen, benötigen wir mindestens **3 Bits** (da 23=8≥723=8≥7).
    
- Die neue Subnetzmaske wird **/27** (24 + 3).


### **Schritt 2: Subnetzberechnung**

Jedes Subnetz hat:

- **Subnetzmaske:** 255.255.255.224 (da 256−32=224256−32=224 im vierten Oktett).
    
- **Blockgröße:** 32 Adressen pro Subnetz (z. B. 0–31, 32–63, 64–95, usw.).
    
- **Nutzbare Hosts pro Subnetz:** 2(32−27)−2=302(32−27)−2=30 Hosts.
    

---

### **Die 7 Subnetze**

|Subnetz|Netzwerkadresse|Erste nutzbare IP|Letzte nutzbare IP|Broadcastadresse|
|---|---|---|---|---|
|1|192.168.2.0/27|192.168.2.1|192.168.2.30|192.168.2.31|
|2|192.168.2.32/27|192.168.2.33|192.168.2.62|192.168.2.63|
|3|192.168.2.64/27|192.168.2.65|192.168.2.94|192.168.2.95|
|4|192.168.2.96/27|192.168.2.97|192.168.2.126|192.168.2.127|
|5|192.168.2.128/27|192.168.2.129|192.168.2.158|192.168.2.159|
|6|192.168.2.160/27|192.168.2.161|192.168.2.190|192.168.2.191|
|7|192.168.2.192/27|192.168.2.193|192.168.2.222|192.168.2.223|

- Das achte Subnetz (192.168.2.224/27) bleibt **unbenutzt**, falls später benötigt.


- **Subnetzmaske:** 255.255.255.224 (/27).
    
- **Hosts pro Subnetz:** 30 nutzbare IPs.
    
- **Flexibilität:** Das achte Subnetz kann für zukünftige Erweiterungen reserviert werden.