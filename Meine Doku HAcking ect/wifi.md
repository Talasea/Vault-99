https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.123.253901
[ine-grained Person Perception using WiFi (ICCV 2019)](https://www.ri.cmu.edu/app/uploads/2019/09/Person_in_WiFi_ICCV2019.pdf)


# WiFi für räumliches Scannen mit KI

Basierend auf dem Forschungspapier "Person-in-WiFi: Fine-grained Person Perception using WiFi" beschreibe ich, was Sie benötigen würden, um ein ähnliches Projekt zur räumlichen Erfassung mit WiFi und KI nachzustellen.

## Benötigte Hardware

1. **WiFi-Adapter/Antennen**:
    - Intel 5300 WiFi-Netzwerkkarten (NICs) oder vergleichbare Geräte
    - Mindestens zwei Sets von Antennen: ein Sender-Set und ein Empfänger-Set
    - Jedes Set sollte drei Antennen haben, die horizontal in einer Linie angeordnet sind (ähnlich wie bei einem Standard-WiFi-Router)
    - Die Antennen sollten innerhalb einer Wellenlänge (ca. 12,5 cm bei 2,4 GHz) gleichmäßig verteilt sein
2. **Computer/Server**:
    - Mindestens zwei Computer: einer für die Signalübertragung, einer für den Empfang
    - Ausreichend Rechenleistung für die spätere KI-Verarbeitung (idealerweise mit guter GPU)
3. **Kamera für Trainingsdaten** (optional):
    - RGB-Kamera zur Erfassung von Referenzbildern
    - Diese wird nur für das Training benötigt, um Annotationen zu erstellen

## Benötigte Software

1. **Channel State Information (CSI) Extraction Tool**:
    - Open-Source-Tool wie das von Halperin et al. erwähnte für Intel 5300 NICs
    - Software zur Erfassung der CSI bei 30 EM-Frequenzen mit einer Bandbreite von 20 MHz um 2,4 GHz
2. **Datenverarbeitungs-Pipeline**:
    - Software zur Synchronisierung von WiFi-Signalen mit Kamerabildern (falls verwendet)
    - Tools zur Vorverarbeitung der WiFi-Signale
3. **KI-Framework**:
    - PyTorch, TensorFlow oder ähnliche Deep-Learning-Frameworks
    - U-Net-ähnliche Architekturen für die Bildrekonstruktion
    - Implementierung von benutzerdefinierten Verlustfunktionen wie der im Paper beschriebenen Matthew Weight (MW)
4. **Trainingsannotationen**:
    - Software zur Erzeugung von Segmentierungsmasken (z.B. Mask R-CNN)
    - Software zur Körperposenschätzung (z.B. OpenPose)

## Erforderliche Kenntnisse und Fähigkeiten

1. **Signalverarbeitungskenntnisse**:
    - Verständnis von elektromagnetischer Wellenausbreitung
    - Kenntnisse über WiFi-Protokolle und Channel State Information (CSI)
2. **Deep Learning**:
    - Erfahrung mit CNN-Architekturen, insbesondere U-Net
    - Kenntnisse in der Entwicklung und Optimierung von Verlustfunktionen
    - Verständnis von Multi-Task-Lernen
3. **Programmierung**:
    - Python für ML-Implementierungen
    - C/C++ möglicherweise für Hardware-Interaktionen
    - Datenverarbeitung und -visualisierung

## Durchführungsschritte

1. **Hardware-Setup**:
    - Konfiguration der WiFi-Adapter zur Extraktion von CSI
    - Positionierung der Antennen in der richtigen Geometrie
2. **Datenerfassung**:
    - Sammlung von CSI-Daten bei verschiedenen Raumkonfigurationen
    - Falls für Training benötigt: parallele Aufnahme von RGB-Bildern
3. **Datenverarbeitung**:
    - Synchronisierung und Vorverarbeitung der WiFi-Signale
    - Erzeugung von Annotationen aus Kamerabildern (wenn verwendet)
4. **Modelltraining**:
    - Implementierung der U-Net-Architektur mit angepassten Verlustfunktionen
    - Training mit ausreichenden Datensätzen für verschiedene Raumszenarien
5. **Evaluation und Optimierung**:
    - Testen des Modells in neuen Umgebungen
    - Anpassung für verschiedene Anwendungsfälle

## Herausforderungen und Einschränkungen

1. **Räumliche Auflösung**:
    - WiFi-Signale bei 2,4 GHz haben eine Wellenlänge von ca. 12,5 cm
    - Kleine Objekte unter dieser Größe könnten schwer zu erkennen sein
2. **Mehrdeutigkeiten**:
    - Das Mapping von 1D-WiFi-Signalen zu 2D/3D-Rauminformationen ist ein schwieriges, unterbestimmtes Problem
    - Multiwegausbreitungseffekte können zu Interferenzen führen
3. **Umgebungsabhängigkeit**:
    - Das System muss möglicherweise für jede neue Umgebung neu trainiert werden
    - Im Paper wird ein GAN-Ansatz vorgeschlagen, um umgebungsunabhängige Merkmale zu lernen
4. **Datenmenge**:
    - Für robuste KI-Modelle werden große Datenmengen benötigt
    - Die Annotation ist zeitaufwendig und ressourcenintensiv

Dieses Projekt ist technisch anspruchsvoll, bietet aber gegenüber kamerabasierten Systemen den Vorteil, dass es beleuchtungsunabhängig ist, durch Wände "sehen" kann und weniger Datenschutzbedenken aufwirft als Videoüberwachung.



# Schritt-für-Schritt-Anleitung: WiFi-basiertes räumliches Scanning mit KI

Hier ist eine praktische Anleitung, wie Sie mit der Entwicklung eines WiFi-basierten Raumscanning-Systems beginnen können:

## Phase 1: Hardware-Setup

### 1. Beschaffung der Hardware

- **WiFi-Adapter**: Kaufen Sie mindestens zwei Intel 5300 WiFi-Netzwerkkarten (etwa 15-30€ pro Stück)
- **Antennen**: Besorgen Sie drei Antennen für jede Karte (insgesamt 6 Antennen)
- **Computer**: Zwei Linux-Computer (Ubuntu empfohlen) mit PCI-Express-Slots für die Karten
- **Optional**: Eine RGB-Kamera für das Training (z.B. eine Webcam oder besser)

### 2. Hardware-Installation

1. Installieren Sie die Intel 5300 NICs in die Computer
2. Verbinden Sie die drei Antennen mit jeder Karte
3. Platzieren Sie die drei Antennen jeder Karte horizontal in einer Linie mit etwa 4-5 cm Abstand

### 3. Software-Einrichtung für CSI-Erfassung

1. Installieren Sie Linux (Ubuntu 18.04 oder neuer empfohlen)
2. Installieren Sie den modifizierten Intel 5300 NIC-Treiber:
    
    bash
    
    ```bash
    git clone https://github.com/dhalperi/linux-80211n-csitool-supplementary.git
    cd linux-80211n-csitool-supplementary
    sudo apt-get install build-essential linux-headers-$(uname -r)
    make
    sudo make install
    ```
    
3. Laden Sie die erforderlichen Kernel-Module:
    
    bash
    
    ```bash
    sudo modprobe -r iwlwifi mac80211
    sudo modprobe iwlwifi connector_log=0x1
    ```
    

## Phase 2: Datenerfassung

### 1. CSI-Logging-Software einrichten

1. Kompilieren Sie die CSI-Logging-Tools:
    
    bash
    
    ```bash
    cd linux-80211n-csitool-supplementary/netlink
    make
    ```
    
2. Erstellen Sie ein Skript zum Erfassen der CSI-Daten:
    
    bash
    
    ```bash
    ./log_to_file csi.dat
    ```
    

### 2. WiFi-Setup

1. Konfigurieren Sie einen Computer als Sender:
    
    bash
    
    ```bash
    sudo ifconfig wlan0 up
    sudo iw dev wlan0 connect your_network
    ```
    
2. Konfigurieren Sie den anderen Computer als Empfänger im Monitor-Modus:
    
    bash
    
    ```bash
    sudo ifconfig wlan0 down
    sudo iwconfig wlan0 mode monitor
    sudo ifconfig wlan0 up
    ```
    

### 3. Datenerfassung

1. Starten Sie die Datenerfassung am Empfänger:
    
    bash
    
    ```bash
    sudo ./log_to_file csi_data.dat
    ```
    
2. Generieren Sie Netzwerkverkehr vom Sender:
    
    bash
    
    ```bash
    ping [Empfänger-IP] -i 0.01
    ```
    
3. Nehmen Sie parallel dazu (falls gewünscht) Videodaten für das Training auf:
    
    bash
    
    ```bash
    ffmpeg -f v4l2 -framerate 20 -video_size 640x480 -i /dev/video0 output.mp4
    ```
    

## Phase 3: Datenverarbeitung

### 1. CSI-Daten extrahieren

1. Installieren Sie MATLAB oder Python mit den erforderlichen Bibliotheken:
    
    bash
    
    ```bash
    pip install numpy scipy matplotlib pandas
    ```
    
2. Verwenden Sie das folgende Python-Skript zur Extraktion der CSI-Daten:
    
    python
    
    ```python
    import numpy as np
    
    def read_bf_file(filename):
        # Implementieren Sie CSI-Lesefunktion
        # (Eine vollständige Implementierung würde den Rahmen sprengen)
        pass
    
    csi_data = read_bf_file("csi_data.dat")
    ```
    

### 2. Datenvorverarbeitung

1. Synchronisieren Sie CSI- und Videodaten (falls vorhanden):
    
    python
    
    ```python
    # Code zur Synchronisierung basierend auf Zeitstempeln
    ```
    
2. Normalisieren Sie die CSI-Daten:
    
    python
    
    ```python
    csi_normalized = (csi_data - np.mean(csi_data)) / np.std(csi_data)
    ```
    

## Phase 4: KI-Modellentwicklung

### 1. Einrichtung der Trainingsumgebung

1. Installieren Sie PyTorch:
    
    bash
    
    ```bash
    pip install torch torchvision
    ```
    
2. Installieren Sie optional weitere Bibliotheken für Annotationen:
    
    bash
    
    ```bash
    pip install opencv-python detectron2
    ```
    

### 2. Implementierung des U-Net-Modells

python

```python
import torch
import torch.nn as nn

class UNet(nn.Module):
    def __init__(self):
        super(UNet, self).__init__()
        # Encoder
        self.enc1 = self.conv_block(150, 64)
        self.enc2 = self.conv_block(64, 128)
        # [Weitere Encoder-Schichten...]
        
        # Decoder
        self.dec1 = self.conv_block(128, 64)
        # [Weitere Decoder-Schichten...]
        
        # Ausgabeschicht
        self.output = nn.Conv2d(64, 1, kernel_size=1)
        
    def conv_block(self, in_ch, out_ch):
        return nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_ch, out_ch, 3, padding=1),
            nn.ReLU(inplace=True)
        )
        
    def forward(self, x):
        # Implementierung des Forward-Passes
        # [...]
        return self.output(x)

model = UNet()
```

### 3. Implementierung der Matthew Weight-Verlustfunktion

python

```python
def matthew_weight_loss(pred, target, k=1, b=1):
    # Implementierung der im Paper beschriebenen Matthew Weight-Funktion
    weight = k * target + b * torch.sign(target)
    loss = weight * torch.pow(pred - target, 2)
    return loss.mean()
```

### 4. Training des Modells

python

```python
def train(model, train_loader, optimizer, epochs=20):
    for epoch in range(epochs):
        for batch_idx, (data, target) in enumerate(train_loader):
            optimizer.zero_grad()
            output = model(data)
            loss = matthew_weight_loss(output, target)
            loss.backward()
            optimizer.step()
            # [Ausgabe des Fortschritts...]
```

## Phase 5: Erste Tests und Iterative Verbesserung

### 1. Einfaches Testszenario

1. Platzieren Sie Ihre WiFi-Geräte in einem Raum
2. Erfassen Sie CSI-Daten in einem kontrollierten Szenario
3. Führen Sie Ihr Modell auf den Testdaten aus:
    
    python
    
    ```python
    with torch.no_grad():
        predictions = model(test_data)
    ```
    
4. Visualisieren Sie die Ergebnisse:
    
    python
    
    ```python
    import matplotlib.pyplot as plt
    plt.imshow(predictions[0, 0].cpu().numpy())
    plt.show()
    ```
    

### 2. Iterative Verbesserung

1. Identifizieren Sie Probleme und Einschränkungen
2. Sammeln Sie mehr Daten oder passen Sie die Netzwerkarchitektur an
3. Trainieren Sie das Modell erneut und wiederholen Sie den Testprozess

## Praktische Tipps

1. **Starten Sie klein**: Beginnen Sie mit einer einfachen Konfiguration (z.B. leerer Raum vs. Raum mit einer Person)
2. **Inkrementeller Ansatz**: Arbeiten Sie schrittweise von der Erkennung großer Objekte bis hin zu feineren Details
3. **Benutzen Sie Simulationen**: Für erste Tests können Sie WiFi-Signalausbreitung simulieren
4. **Community-Ressourcen**: Suchen Sie nach Open-Source-Implementierungen und Diskussionen in Foren wie GitHub

Diese Anleitung bietet einen Startpunkt. Je nach Ihren spezifischen Zielen und verfügbaren Ressourcen müssen Sie möglicherweise bestimmte Aspekte anpassen oder erweitern.


Bei der Verwendung eines Pineapple-Geräts anstelle von Standard-Routern in diesem WiFi-basierten räumlichen Scanning-System würden sich einige wichtige Veränderungen ergeben.

Ein WiFi Pineapple ist ein spezialisiertes Gerät für Netzwerksicherheitstests, das ursprünglich für Penetrationstests entwickelt wurde. Es hat einige Eigenschaften, die für ein räumliches Scanning-System sowohl Vorteile als auch Herausforderungen bieten könnten:

### Vorteile der Verwendung eines WiFi Pineapple:

1. **Erweiterte Funkfunktionen**: Pineapples verfügen über fortschrittliche Funknetzwerk-Manipulation, die präzisere Signaleinstellungen ermöglichen könnte.
2. **Integrierte Tools**: Viele eingebaute Funktionen für Paketerfassung und Signalanalyse, die die Erfassung von Channel State Information (CSI) erleichtern könnten.
3. **Mobilität**: Pineapples sind kompakt und oftmals batteriebetrieben, was die Mobilität des Systems verbessern würde.
4. **Simultane Verbindungen**: Kann gleichzeitig als Sender und Empfänger fungieren, was potenziell die Hardware-Anforderungen reduzieren könnte.

### Herausforderungen:

1. **Treiber-Kompatibilität**: Die im Dokument erwähnten Intel 5300 NICs verwenden spezielle Treiber für die CSI-Extraktion. Es müsste geprüft werden, ob der Pineapple ähnliche CSI-Extraktionsfähigkeiten unterstützt oder ob die entsprechenden Treiber angepasst werden können.
2. **Antennen-Konfiguration**: Die Forschungsarbeit nutzt eine spezifische Anordnung von drei Antennen mit bestimmten Abständen. Sie müssten sicherstellen, dass der Pineapple vergleichbare Antennen-Konfigurationsmöglichkeiten bietet.
3. **Signalqualität**: Pineapples sind für Sicherheitstests optimiert, nicht für die präzise Signalverarbeitung, die für KI-basierte räumliche Wahrnehmung benötigt wird.
4. **Entwicklungsumgebung**: Die Anpassung der Software-Tools zur CSI-Extraktion könnte aufgrund der proprietären Natur des Pineapple-Systems komplexer sein.

### Notwendige Anpassungen:

1. Entwicklung oder Anpassung von CSI-Extraktionstools speziell für die Pineapple-Hardware.
2. Modifikation der Signalverarbeitungspipeline, um mit dem möglicherweise anderen Datenformat oder der Signalcharakteristik umzugehen.
3. Kalibrierung des Systems unter Berücksichtigung der besonderen Eigenschaften der Pineapple-Hardware.

Ein WiFi Pineapple könnte das System potenziell kompakter und mobiler machen, jedoch mit dem Kompromiss einer komplexeren Entwicklung und möglicherweise niedrigerer Signalpräzision. Für Forschungs- oder Proof-of-Concept-Zwecke könnte es dennoch eine interessante Alternative darstellen.