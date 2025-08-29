root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# dig ANY sevenkingdoms.local @192.168.20.10

; <<>> DiG 9.18.30-0ubuntu0.24.04.2-Ubuntu <<>> ANY sevenkingdoms.local @192.168.20.10
;; global options: +cmd
;; Got answer:
;; WARNING: .local is reserved for Multicast DNS
;; You are currently testing what happens when an mDNS query is leaked to DNS
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 53651
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 2

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;sevenkingdoms.local.		IN	ANY

;; ANSWER SECTION:
sevenkingdoms.local.	600	IN	A	192.168.20.10
sevenkingdoms.local.	3600	IN	NS	kingslanding.sevenkingdoms.local.
sevenkingdoms.local.	3600	IN	SOA	kingslanding.sevenkingdoms.local. hostmaster.sevenkingdoms.local. 297 900 600 86400 3600

;; ADDITIONAL SECTION:
kingslanding.sevenkingdoms.local. 3600 IN A	192.168.20.10

;; Query time: 20 msec
;; SERVER: 192.168.20.10#53(192.168.20.10) (TCP)
;; WHEN: Mon Aug 25 11:26:52 CEST 2025
;; MSG SIZE  rcvd: 154
