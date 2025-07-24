---
created: 2025-01-27T10:16
updated: 2025-01-28T10:10
---
```powershell
 docker run -dit --name my-apache-app -p 8080:80 httpd:2.4
```

Mit geteiltem Inhalt für HTTP Dateien

```powershell
docker run -dit --name Apache2 -p 8080:80 -v //c/users/andre/httpd:/usr/local/apache2/htdocs/ httpd
```

Mit aktuellem Ordner

```powershell
docker run -dit --name Apache2.1 -p 8000:80 -v ${PWD}:/usr/local/apache2/htdocs/ httpd
```