# 

[https://regexr.com/](https://regexr.com/)


Reguläre Ausdräcke

Reguläre Muster, auch als reguläre Ausdrücke (Regular Expressions, Regex) bekannt, sind Zeichenketten, die bestimmte Kombinationen von Zeichen in Texten filtern oder ersetzen können.236 Sie basieren auf der formalen Sprachtheorie und werden häufig in der Textbearbeitung und Programmierung eingesetzt.23

Reguläre Ausdrücke folgen bestimmten Regeln und verwenden besondere Zeichen, um Muster zu definieren. Zum Beispiel kann das Muster "T.*g" alle Wörter in einem Text finden, die mit "T" beginnen und auf "g" enden, wie "Tag", "Trag" oder "Türgriff".3

Ein regulärer Ausdruck kann aus einzelnen Zeichen, Klassen von Zeichen, Klammern und Sonderzeichen bestehen. Hier sind einige Beispiele:

- `gray|grey` passt auf "gray" und "grey".2
    
- `gr(a|e)y` passt auf "gray" und "grey", indem es eine Alternative zwischen "a" und "e" definiert.2
    
- `gr[ae]y` passt auf "gray" und "grey", indem es eine Klasse von Zeichen definiert.2
    
- `b[aeiou]bble` passt auf "babble", "bebble", "bibble", "bobble" und "bubble".2
    
- `colou?r` passt auf "color" und "colour", wobei das Fragezeichen das vorhergehende Zeichen optional macht.23
    
- `Hello\\nworld` passt auf "Hello world", wobei der umgekehrte Schrägstrich das folgende Zeichen als Literal interpretiert.6
    

Reguläre Ausdrücke können sehr komplex sein und bieten eine effiziente Methode, um Texte nach bestimmten Mustern zu durchsuchen oder zu ersetzen.