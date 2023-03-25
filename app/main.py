# Docs - https://api.c99.nl/api_overview
# Purchase an API Key - https://api.c99.nl/dashboard/shop

import requests
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
async def index():
    return Response("A FastAPI Wrapper used to access and return data from the C99.nl API")

c99_key = "your_c99_key"

# Subdomain Finder and CloudFlare Resolver
# Performs an advanced subdomain scan to find most subdomains of the given domain.
@app.get("/subdomain/{domain}")
async def get_subdomain(domain: str):
    url = f"https://api.c99.nl/subdomainfinder?key={c99_key}&domain={domain}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Phone Lookup
# Get more information about any phone number.
@app.get("/phone/{phone_number}")
async def get_phone_number(phone_number: str):
    url = f"https://api.c99.nl/phonelookup?key={c99_key}&number={phone_number}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Firewall Technology (WAF) Detector
# Scans to detect if a website is behind a firewall and determines what firewall it is.
@app.get("/firewalldetector/{url}")
async def get_firewall(url: str):
    url = f"https://api.c99.nl/firewalldetector?key={c99_key}&url={url}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Multiple Port Scanner
# Scans all ports of given host.
@app.get("/multi/portscanner/{host}")
async def get_multi_ports(host: str):
    url = f"https://api.c99.nl/portscanner?key={c99_key}&host={host}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Single Port Scanner
# Scans a single port of given host.
@app.get("/single/portscanner/{host}/{port}")
async def get_multi_ports(host: str, port: str):
    url = f"https://api.c99.nl/portscanner?key={c99_key}&host={host}&port={port}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}       

# Ping
# Pings a host 4 times and shows the result.
@app.get("/ping/{host}")
async def get_ping(host: str):
    url = f"https://api.c99.nl/ping?key={c99_key}&host={host}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# IP to Host
# Gets host of given IP address.
@app.get("/iptohost/{ip_address}")
async def get_host(ip_address: str):
    url = f"https://api.c99.nl/gethostname?key={c99_key}&host={ip_address}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Advanced DNS Checker
# Performs an advanced check on the specific URL. Parameter &server=[countrycode] is optional. 
# If left empty, all servers will be used. Possible check types: a, aaaa, cname, mx, ns, soa, txt
@app.get("/advanceddns/{url}/{check_type}")
async def get_dns_check(url: str, check_type: str):
    server = "us"  # Parameter &server=[countrycode] is optional
    url = f"https://api.c99.nl/dnschecker?key={c99_key}&url={url}&type={check_type}&json"
    if server:
        url = f"{url}&server={server}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Host to IP
# Gets server IP of given host.
@app.get("/hosttoip/{host}")
async def get_host_ip(host: str, server: str = ""):
    url = f"https://api.c99.nl/dnsresolver?key={c99_key}&host={host}&server={server}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Domain Checker
# Checks whether a domain is available or not, no matter what extension.
@app.get("/domainchecker/{domain}")
async def check_domain_availability(domain: str):
    url = f"https://api.c99.nl/domainchecker?key={c99_key}&domain={domain}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Domain History Check
# Checks available IP history of a domain with dates.
@app.get("/domainhistory/{domain}")
async def get_domain_history(domain: str):
    url = f"https://api.c99.nl/domainhistory?key={c99_key}&domain={domain}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# IP 2 Domains
# Attempts to find websites hosted on the specific IP address.
@app.get("/ip2domains/{ip}")
async def get_ip_domains(ip: str):
    url = f"https://api.c99.nl/ip2domains?key={c99_key}&ip={ip}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Alexa Rank Checker
# Grab the latest Alexa Rank information of any website, including backlinks and top country.
@app.get("/alexarank/{url}")
async def get_alexa_rank(url: str):
    url = f"https://api.c99.nl/alexarank?key={c99_key}&url={url}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Whois Checker
# Whois check on a domain to see who the domain owner is.
@app.get("/whois/{domain}")
async def get_whois(domain: str):
    url = f"https://api.c99.nl/whois?key={c99_key}&domain={domain}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Screenshot Tool
# Creates a screenshot of any website/url you want.
@app.get("/screenshot/{url:path}")
async def get_screenshot(url: str):
    screenshot_url = f"https://api.c99.nl/createscreenshot?key={c99_key}&url={url}&json"
    response = requests.get(screenshot_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# GeoIP
# Locates the given host/ip address.
@app.get("/geoip/{host}")
async def get_geoip(host: str):
    url = f"https://api.c99.nl/geoip?key={c99_key}&host={host}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Website Up or Down Checker
# Checks if a host is up or down.
@app.get("/upordown/{host}")
async def get_up_or_down(host: str):
    url = f"https://api.c99.nl/upordown?key={c99_key}&host={host}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Site/URL Reputation Checker
# Checks whether a specific site/url is suspicious and might contain malware, phishing or other potential harmful software.
@app.get("/reputationchecker/{url}")
async def get_reputation(url: str):
    full_url = f"https://api.c99.nl/reputationchecker?key={c99_key}&url={url}&json"
    response = requests.get(full_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Get Website Headers
# Gets the headers of a website.
@app.get("/getheaders/{host}")
async def get_headers(host: str):
    url = f"https://api.c99.nl/getheaders?key={c99_key}&host={host}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Link Backup
# Makes an online backup of a link.
@app.get("/linkbackup/{url:path}")
async def get_link_backup(url: str):
    full_url = f"https://api.c99.nl/linkbackup?key={c99_key}&url={url}&json"
    response = requests.get(full_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# URL Shortener
# Shorts every long URL.
@app.get("/urlshortener/{long_url:path}")
async def get_short_url(long_url: str):
    url = f"https://api.c99.nl/urlshortener?key={c99_key}&url={long_url}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return {"error": "Could not retrieve information"}


# Dictionary
# Gets the definition of any word.
@app.get("/dictionary/{word}")
async def get_definition(word: str):
    url = f"https://api.c99.nl/dictionary?key={c99_key}&word={word}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Synonym Finder
# Gets the alternative words/synonyms for any legitimate english word you fill in.
@app.get("/synonym/{word}")
async def get_synonym(word: str):
    url = f"https://api.c99.nl/synonym?key={c99_key}&word={word}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Email Validator
# Checks if given up e-mail exists.
@app.get("/emailvalidator/{email}")
async def get_email_validator(email: str):
    url = f"https://api.c99.nl/emailvalidator?key={c99_key}&email={email}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Disposable Mail Check
# Checks if given up e-mail is disposable/temporarily or not.
@app.get("/disposablemailchecker/{email}")
async def get_disposable_mail_checker(email: str):
    url = f"https://api.c99.nl/disposablemailchecker?key={c99_key}&email={email}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# IP Validator
# Checks if IP address format is valid.
@app.get("/ipvalidator/{ip}")
async def get_ip_validator(ip: str):
    url = f"https://api.c99.nl/ipvalidator?key={c99_key}&ip={ip}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# TOR Checker
# Checks whether an IP is from a TOR network or not.
@app.get("/torchecker/{ip}")
async def get_tor_checker(ip: str):
    url = f"https://api.c99.nl/torchecker?key={c99_key}&ip={ip}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Translator
# Translates your text (autodetected) to any language.
@app.get("/translate/{text}/{tolanguage}")
async def translate_text(text: str, tolanguage: str):
    url = f"https://api.c99.nl/translate?key={c99_key}&text={text}&tolanguage={tolanguage}&json&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Random Info Generator
@app.get("/randomperson/{gender}")
async def random_info(gender: str):
    url = f"https://api.c99.nl/randomperson?key={c99_key}&gender={gender}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Youtube Video Details
@app.get("/youtubedetails/{videoid}")
async def youtube_details(videoid: str):
    url = f"https://api.c99.nl/youtubedetails?key={c99_key}&videoid={videoid}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

#buggy asf
# Youtube to MP3
@app.get("/youtubemp3/{videoid}")
async def youtube_to_mp3(videoid: str):
    url = f"https://api.c99.nl/youtubemp3?key={c99_key}&videoid={videoid}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# IP Logger
@app.get("/iplogger")
async def ip_logger():
    url = f"https://api.c99.nl/iplogger?key={c99_key}&action=viewloggers&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

#buggy asf
# Bitcoin Balance Checker
@app.get("/bitcoinbalance/{address}")
async def bitcoin_balance(address: str):
    url = f"https://api.c99.nl/bitcoinbalance?key={c99_key}&address={address}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Ethereum Balance Checker
@app.get("/ethereumbalance/{address}")
async def ethereum_balance(address: str):
    url = f"https://api.c99.nl/ethereumbalance?key={c99_key}&address={address}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Currency Converter
@app.get("/currency/{amount}/{from_currency}/{to_currency}")
async def currency_converter(amount: float, from_currency: str, to_currency: str):
    url = f"https://api.c99.nl/currency?key={c99_key}&amount={amount}&from={from_currency}&to={to_currency}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Currency Rates
@app.get("/currencyrates/{source}")
async def currency_rates(source: str):
    url = f"https://api.c99.nl/currencyrates?key={c99_key}&source={source}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Weather Checker
@app.get("/weather/{location}/{unit}")
async def weather_checker(location: str, unit: str):
    url = f"https://api.c99.nl/weather?key={c99_key}&location={location}&unit={unit}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# QR Code Generator
@app.get("/qrgenerator/{string}/{size}")
async def qr_code_generator(string: str, size: int):
    url = f"https://api.c99.nl/qrgenerator?key={c99_key}&string={string}&size={size}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Text Parser
@app.get("/textparser/{url}")
async def text_parser(url: str):
    url = f"https://api.c99.nl/textparser?key={c99_key}&url={url}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

# Proxy Detector
@app.get("/proxydetector/{ip}")
async def text_parser(ip: str):
    url = f"https://api.c99.nl/proxydetector?key={c99_key}&ip={ip}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}

@app.get("/eitheror")
async def either_or():
    url = f"https://api.c99.nl/eitheror?key={c99_key}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}


@app.get("/gif/{keyword}")
async def gif_finder(keyword: str):
    url = f"https://api.c99.nl/gif?key={c99_key}&keyword={keyword}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve information"}


if __name__ == "__main__":
    app.run(debug=False)