◀ [[<% tp.user.getRelativeDay(tp.file.title, -3) %>]] - [[<% tp.user.getRelativeDay(tp.file.title, 1) %>]] ▶
## Summary 🦚
## Vormittag
#### Ablauf 🧭
###### ⛩ Bingoliste/Ergänzungen 🐾
###### Zusammenfassung 🦚 

## Nachmittag
###### Aufgaben📚
###### Zusammenfassung 🦚 

---
```dataview
TABLE file.ctime AS "Created", file.mtime AS "Updated", file.size AS "Size" 
WHERE file.cday = date(this.file.name) OR file.mday = date(this.file.name) 
```
