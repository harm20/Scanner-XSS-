import requests
Target = input("Target URL :")
payload = "<script>alert('XXS');</script>"
req = request.get(target+payload,"html.parser").text
if payload == req :
   print("Found vulnerability discovered")
else :
    print("Not Found") 
