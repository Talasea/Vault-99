
#!/usr/bin/env python3
# WiFi-basiertes räumliches Scanning mit Pineapple
# Dieses Skript implementiert die grundlegende Funktionalität für CSI-Extraktion
# und KI-basierte räumliche Erkennung mit einem WiFi Pineapple

import numpy as np
import time
import subprocess
import threading
import torch
import torch.nn as nn
import torch.optim as optim
from scipy.io import savemat, loadmat
from matplotlib import pyplot as plt

# ------------------------------------------------------------------------
# Pineapple CSI Extraktion
# ------------------------------------------------------------------------

class PineappleCSIExtractor:
    """Klasse zum Extrahieren von Channel State Information (CSI) vom WiFi Pineapple"""
    
    def __init__(self, interface="wlan0", sample_rate=100):
        """
        Initialisiert den CSI-Extraktor
        
        Args:
            interface: Die WiFi-Schnittstelle des Pineapple
            sample_rate: Anzahl der Samples pro Sekunde
        """
        self.interface = interface
        self.sample_rate = sample_rate
        self.running = False
        self.csi_data = []
        self.connected = False
        
    def connect_to_pineapple(self, ip="172.16.42.1", username="root", password="pineapplesecret"):
        """Verbindung zum Pineapple herstellen"""
        try:
            # In einer realen Implementierung würde hier SSH oder eine API-Verbindung hergestellt
            print(f"Verbinde mit Pineapple auf {ip}...")
            # Simulation einer erfolgreichen Verbindung
            self.connected = True
            print("Verbindung hergestellt!")
            return True
        except Exception as e:
            print(f"Verbindungsfehler: {e}")
            return False
    
    def configure_monitor_mode(self):
        """Konfiguriert den Pineapple für den Monitor-Modus"""
        if not self.connected:
            print("Keine Verbindung zum Pineapple!")
            return False
            
        try:
            # In der Praxis würden hier Befehle über SSH gesendet
            cmd = f"ifconfig {self.interface} down && iwconfig {self.interface} mode monitor && ifconfig {self.interface} up"
            print(f"Führe aus: {cmd}")
            # Simulation der Befehlsausführung
            time.sleep(1)
            print("Monitor-Modus aktiviert")
            return True
        except Exception as e:
            print(f"Fehler beim Konfigurieren des Monitor-Modus: {e}")
            return False
    
    def start_capture(self, duration=30):
        """Startet die CSI-Datenerfassung"""
        if not self.connected:
            print("Keine Verbindung zum Pineapple!")
            return
            
        self.running = True
        self.csi_data = []
        
        # In einer realen Implementierung würde hier ein spezielles Tool auf dem Pineapple gestartet
        # Hier simulieren wir die CSI-Datenerfassung
        def capture_thread():
            print(f"Starte CSI-Erfassung für {duration} Sekunden...")
            start_time = time.time()
            sample_interval = 1.0 / self.sample_rate
            
            while self.running and (time.time() - start_time) < duration:
                # Simuliere CSI-Daten (30 Unterträger mit komplexen Werten)
                timestamp = time.time() - start_time
                # Erzeuge 3x3 MIMO-Kanal (3 Sende- und 3 Empfangsantennen) für 30 Unterträger
                csi_sample = np.random.randn(30, 3, 3) + 1j * np.random.randn(30, 3, 3)
                self.csi_data.append({
                    'timestamp': timestamp,
                    'csi': csi_sample
                })
                time.sleep(sample_interval)
                
            self.running = False
            print(f"CSI-Erfassung beendet. {len(self.csi_data)} Samples aufgenommen.")
        
        thread = threading.Thread(target=capture_thread)
        thread.start()
        return thread
    
    def stop_capture(self):
        """Stoppt die laufende CSI-Datenerfassung"""
        self.running = False
    
    def save_data(self, filename="csi_data.mat"):
        """Speichert die erfassten CSI-Daten"""
        if not self.csi_data:
            print("Keine Daten zum Speichern!")
            return
            
        # Konvertiere die Daten in ein Format für Matlab/SciPy
        timestamps = np.array([sample['timestamp'] for sample in self.csi_data])
        csi_array = np.array([sample['csi'] for sample in self.csi_data])
        
        # Speichere als .mat-Datei für die Kompatibilität mit MATLAB
        savemat(filename, {
            'timestamps': timestamps,
            'csi_data': csi_array
        })
        print(f"Daten gespeichert in {filename}")
        
    def process_csi_data(self):
        """Verarbeitet die rohen CSI-Daten für das KI-Modell"""
        if not self.csi_data:
            print("Keine Daten zur Verarbeitung!")
            return None
            
        # Extrahiere Amplituden und Phasen aus den komplexen CSI-Werten
        csi_array = np.array([sample['csi'] for sample in self.csi_data])
        amplitudes = np.abs(csi_array)
        phases = np.angle(csi_array)
        
        # Normalisiere die Daten
        amp_normalized = (amplitudes - np.mean(amplitudes)) / np.std(amplitudes)
        phase_normalized = phases / np.pi  # Normalisierung auf [-1, 1]
        
        # Stelle die Daten für das neuronale Netz bereit
        # Format: [Samples, Features (30 Unterträger * 3 Tx * 3 Rx * 2 (Amp+Phase))]
        samples = amp_normalized.shape[0]
        features = np.zeros((samples, 30, 3, 3, 2))
        features[:, :, :, :, 0] = amp_normalized
        features[:, :, :, :, 1] = phase_normalized
        
        return features

# ------------------------------------------------------------------------
# Modell für räumliche Wahrnehmung
# ------------------------------------------------------------------------

class SpatialPerceptionUNet(nn.Module):
    """Vereinfachtes U-Net für räumliche Wahrnehmung basierend auf WiFi-CSI"""
    
    def __init__(self, in_channels=540):  # 30 Unterträger * 3 Tx * 3 Rx * 2 (Amp+Phase)
        super(SpatialPerceptionUNet, self).__init__()
        
        # Encoder
        self.enc1 = self._conv_block(in_channels, 64)
        self.pool1 = nn.MaxPool2d(2)
        self.enc2 = self._conv_block(64, 128)
        self.pool2 = nn.MaxPool2d(2)
        self.enc3 = self._conv_block(128, 256)
        
        # Bottleneck
        self.bottleneck = self._conv_block(256, 512)
        
        # Decoder
        self.upconv3 = nn.ConvTranspose2d(512, 256, kernel_size=2, stride=2)
        self.dec3 = self._conv_block(512, 256)  # 512 = 256 + 256 (skip connection)
        self.upconv2 = nn.ConvTranspose2d(256, 128, kernel_size=2, stride=2)
        self.dec2 = self._conv_block(256, 128)  # 256 = 128 + 128 (skip connection)
        
        # Output - Räumliche Karte (64x64) und Personenerkennung
        self.spatial_output = nn.Conv2d(128, 1, kernel_size=1)
        self.person_output = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
            nn.Linear(128, 1),
            nn.Sigmoid()
        )
        
    def _conv_block(self, in_channels, out_channels):
        """Standardblock mit zwei Faltungen und ReLU"""
        return nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1),
            nn.ReLU(inplace=True)
        )
    
    def forward(self, x):
        """Forward-Pass durch das Netzwerk"""
        # Encoder
        e1 = self.enc1(x)
        e2 = self.enc2(self.pool1(e1))
        e3 = self.enc3(self.pool2(e2))
        
        # Bottleneck
        b = self.bottleneck(e3)
        
        # Decoder mit Skip-Connections
        d3 = self.dec3(torch.cat([self.upconv3(b), e3], dim=1))
        d2 = self.dec2(torch.cat([self.upconv2(d3), e2], dim=1))
        
        # Ausgabe
        spatial_map = self.spatial_output(d2)
        person_detection = self.person_output(d2)
        
        return spatial_map, person_detection

# ------------------------------------------------------------------------
# Verlustfunktion mit Matthew-Gewichtung (aus dem Paper)
# ------------------------------------------------------------------------

def matthew_weight_loss(pred, target, k=1.0, b=1.0):
    """
    Verlustfunktion mit Matthew-Gewichtung wie im Paper beschrieben
    
    Args:
        pred: Vorhersage des Modells
        target: Zielwerte
        k, b: Parameter der Matthew-Gewichtungsfunktion
    """
    weight = k * target + b * torch.sign(target)
    loss = weight * torch.pow(pred - target, 2)
    return loss.mean()

# ------------------------------------------------------------------------
# Hauptfunktion für das komplette System
# ------------------------------------------------------------------------

def main():
    """Hauptfunktion für das räumliche Scanning-System"""
    print("WiFi-basiertes räumliches Scanning mit Pineapple\n")
    
    # Initialisiere den CSI-Extraktor
    csi_extractor = PineappleCSIExtractor(interface="wlan1", sample_rate=50)
    
    # Verbindung zum Pineapple herstellen
    if not csi_extractor.connect_to_pineapple():
        print("Konnte keine Verbindung zum Pineapple herstellen. Beende.")
        return
    
    # Konfiguriere den Monitor-Modus
    if not csi_extractor.configure_monitor_mode():
        print("Konnte Monitor-Modus nicht aktivieren. Beende.")
        return
    
    # Starte die CSI-Datenerfassung
    capture_thread = csi_extractor.start_capture(duration=10)
    capture_thread.join()  # Warte auf Abschluss der Datenerfassung
    
    # Speichere die Rohdaten
    csi_extractor.save_data("raw_csi_data.mat")
    
    # Verarbeite die CSI-Daten für das KI-Modell
    processed_data = csi_extractor.process_csi_data()
    if processed_data is None:
        print("Keine verarbeiteten Daten verfügbar. Beende.")
        return
    
    # Reshape für das Modell: [Samples, Channels, Height, Width]
    # Hier transformieren wir unsere CSI-Daten in ein Bild-ähnliches Format
    # Samples, 30, 3, 3, 2 -> Samples, 540, 8, 8
    samples = processed_data.shape[0]
    model_input = processed_data.reshape(samples, -1, 1, 1)
    model_input = torch.from_numpy(model_input.astype(np.float32))
    model_input = nn.functional.interpolate(model_input, size=(8, 8), mode='bilinear')
    
    # Initialisiere das Modell
    print("Initialisiere das räumliche Wahrnehmungsmodell...")
    model = SpatialPerceptionUNet(in_channels=model_input.shape[1])
    
    # Bei einem realen System würde hier das vortrainierte Modell geladen
    # model.load_state_dict(torch.load('trained_model.pth'))
    
    # Führe Inferenz durch (im Trainingsbetrieb würde hier trainiert werden)
    model.eval()
    with torch.no_grad():
        spatial_maps, person_detections = model(model_input)
        
    # Zeige die Ergebnisse
    print("\nErgebnisse der räumlichen Wahrnehmung:")
    print(f"Anzahl verarbeiteter Samples: {samples}")
    
    # Zeige den Durchschnitt der räumlichen Karten
    avg_spatial_map = spatial_maps.mean(0).squeeze().numpy()
    plt.figure(figsize=(10, 8))
    plt.imshow(avg_spatial_map, cmap='viridis')
    plt.colorbar(label='Intensität')
    plt.title('Durchschnittliche räumliche Wahrnehmung')
    plt.savefig('spatial_perception.png')
    print(f"Räumliche Wahrnehmungskarte gespeichert als 'spatial_perception.png'")
    
    # Zeige die Personenerkennung
    avg_person_detection = person_detections.mean().item()
    print(f"Durchschnittliche Personenerkennungswahrscheinlichkeit: {avg_person_detection:.2f}")
    
    print("\nSystem-Ausführung abgeschlossen.")

if __name__ == "__main__":
    main()