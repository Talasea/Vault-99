
Das Video beinhaltet eine Vortrag ums hacking und um die damit auftretenden Sicherheit Lücken.

So erläutert der Dozent mehre mögliche Angriffsvarianten.  Anfangs wurde nochmal auf die Rechtslage eingegangen. 

Paywall umgehen:
Quellcode untersuchen  
In seinem Beispiel um geht er die Paywall in dem er den quellcode der website sich anzeigen und ändert einen wert  in dem er disabeld in einer codezeile löscht . so wird die Paywall umgangen. Im Anschluss erläutert er wie man eine Solche schwachstelle schliest in dem die daten auf den server ausgelagert werden . 



Login hacking
mit hilfe von Passwortlisten ausprobieren  (die liste der häufigsten Passwörter )
er erläutert wie man die console des brwosers öffnet und Java cods imprementiert.  (trycombination) er nutz imprinzip eine ar Wörterbuchangriff aus seiner Datenbank





Brute Force Angriff :Dieser Angriff basiert auf dem Prinzip der “rohen Gewalt”, indem der Angreifer alle möglichen Kombinationen von Zeichen, Zahlen und Sonderzeichen ausprobiert, bis er das richtige Passwort findet. in dem Video versucht der mit Hilfe von libarys  die nach und nach Buchstaben Kombinationen ausprobieren  ein Passwort zu knacken .
1. Einfaches Brute Force: Der Angreifer probiert alle möglichen Kombinationen von Zeichen und Zahlen aus, bis er das richtige Passwort findet.
2. Wörterbuchangriff: Der Angreifer verwendet ein Wörterbuch und ergänzt Wörter mit Zahlen und Sonderzeichen, um längere Passwörter zu knacken.
3. Credential Stuffing: Der Angreifer verwendet ein bereits kompromittiertes Benutzerkonto und probiert verschiedene Kombinationen von Benutzernamen und Kennwörtern aus. Im Video benutzt er dafür eine Datenbank die die gängigsten Passwörtern aufzeigt und die dazugehörigen verschlüsselten Hash , da ein generierter hash nicht zurück gerechnet werden kann . Und wie man verhindern Kann das sein hash in ener Rainbowtabel augelistet werden kann 

Als lätztes Beispiel wird gezeigt wie eine Fiktive onlineShop Seite in Warenkorp über den Quellcode verändert wird in dem eine abfrage verandert wird und so eine gutschrift im warenkorb angezeigt wird .   / onclick="addToCart(´monitor´,298)  zu  addToCart (´Gutschrift,-999,990)




