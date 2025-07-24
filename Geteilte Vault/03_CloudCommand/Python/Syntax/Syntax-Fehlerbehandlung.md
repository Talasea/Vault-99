---
created: 2025-02-21T10:02
updated: 2025-02-21T10:02
---

```python
try:
    eingabe = int(input("Die nenne mir eine Zahl"))
    print("Deine Zahl war die: ")
    print(eingabe)
except:
    print("Nutzer du bist doof, bitte nenne mir doch eine Zahl")

#Falls der Nutzer nach dem er gefragt wurd statt einer Zahl nun
#Buchstaben eingibt, löst dies einen Fehler aus
#dadurch wird der Code im except Block ausgeführt, ohne das 
#es einen Programmabsturz gibt. 

```