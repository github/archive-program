
![6qi0IOfvib](https://user-images.githubusercontent.com/34923485/216248305-d8bafc1e-8910-4cf1-9e6a-d7697e3db4ff.gif)

Featured on https://api.c99.nl/integrations

# Setup
Make sure you have a c99.nl key, you can't use this without one

Make sure you have python installed

Run the install.bat file then run the run.bat file

Go to the endpoint you want to access.

## Features

### Subdomain Finder and CloudFlare Resolver
Performs an advanced subdomain scan to find most subdomains of the given domain.
```python
Endpoint: /subdomain/{domain}
```

### Phone Lookup
Get more information about any phone number.
```python
Endpoint: /phone/{phone_number}
```

### Firewall Technology (WAF) Detector
Scans to detect if a website is behind a firewall and determines what firewall it is.
```python
Endpoint: /firewalldetector/{url}
```

### Multiple Port Scanner
Scans all ports of given host.
```python
Endpoint: /multi/portscanner/{host}
```

### Single Port Scanner
Scans a single port of given host.
```python
Endpoint: /single/portscanner/{host}/{port}
```

### Ping
Pings a host 4 times and shows the result.
```python
Endpoint: /ping/{host}
```

### IP to Host
Gets host of given IP address.
```python
Endpoint: /iptohost/{ip_address}
```

### Advanced DNS Checker
Performs an advanced check on the specific URL. Parameter &server=[countrycode] is optional. If left empty, all servers will be used. Possible check types: a, aaaa, cname, mx, ns, soa, txt
```python
Endpoint: /advanceddns/{url}/{check_type}
```

### Host to IP
Gets server IP of given host.
```python
Endpoint: /hosttoip/{host}
```

### Domain Checker
Checks whether a domain is available or not, no matter what extension.
```python
Endpoint: /domainchecker/{domain}
```

### Domain History Check
Checks available IP history of a domain with dates.
```python
Endpoint: /domainhistory/{domain}
```

### IP 2 Domains
Attempts to find websites hosted on the specific IP address.
```python
Endpoint: /ip2domains/{ip}
```

### Alexa Rank Checker
Grab the latest Alexa Rank information of any website, including backlinks and top country.
```python
Endpoint: /alexarank/{url}
```

### Whois Checker
Whois check on a domain to see who the domain owner is.
```python
Endpoint: /whois/{domain}
```

### Screenshot Tool
Creates a screenshot of any website/url you want.
```python
Endpoint: /screenshot/{url:path}
```

### GeoIP
Locates the given host/ip address.
```python
Endpoint: /geoip/{host}
```

### Website Up or Down Checker
Checks if a host is up or down.
```python
Endpoint: /upordown/{host}
```

### Site/URL Reputation Checker
Checks whether a specific site/url is suspicious and might contain malware, phishing or other potential harmful software.
```python
Endpoint: /reputationchecker/{url}
```

### Get Website Headers
Gets the headers of a website.
```python
Endpoint: /getheaders/{host}
```

### Link Backup
Makes an online backup of a link.
```python
Endpoint: /linkbackup/{url:path}
```

### URL Shortener
Shorts every long URL.
```python
Endpoint: /urlshortener/{long_url:path}
```

### Dictionary
Gets the definition of any word.
```python
Endpoint: /dictionary/{word}
```

### Synonym Finder
Gets the alternative words/synonyms for any legitimate english word you fill in.
```python
Endpoint: /synonym/{word}
```

### Email Validator
Checks if given up e-mail exists.
```python
Endpoint: /emailvalidator/{email}
```

### Disposable Mail Check
Checks if given up e-mail is disposable/temporarily or not.
```python
Endpoint: /disposablemailchecker/{email}
```

### IP Validator
Checks if IP address format is valid.
```python
Endpoint: /ipvalidator/{ip}
```

### TOR Checker
Checks whether an IP is from a TOR network or not.
```python
Endpoint: /torchecker/{ip}
```

### Translator
Translates your text (autodetected) to any language.
```python
Endpoint: /translate/{text}/{tolanguage}
```

### Random Info Generator
Generates random name address etc. (genders: male/female/all).
```python
Endpoint: /randomperson/{gender}
```

### Youtube Video Details
Gets all details of a specific YouTube video.
```python
Endpoint: /youtubedetails/{videoid}
```

### Youtube to MP3
Converts any song up to 10 minutes to MP3.
```python
Endpoint: /youtubemp3/{videoid}
```

### IP Logger
Creates you various links which you can send to anyone to log their IP.
```python
Endpoint: /iplogger
```

### Bitcoin Balance Checker
Checks the current balance of any Bitcoin address.
```python
Endpoint: /bitcoinbalance/{address}
```

### Ethereum Balance Checker
Checks the current balance of any Ethereum address.
```python
Endpoint: /ethereumbalance/{address}
```

### Currency Converter
Converts normal and cryptocurrencies to any other currency.
```python
Endpoint: /currency/{amount}/{from_currency}/{to_currency}
```

### Currency Rates
Shows the rate of every currency in the world based on the unit price of the given source.
```python
Endpoint: /currencyrates/{source}
```

### Weather Checker
Checks the weather of every city or postal code you give up. Change &unit= to F for Fahrenheit and C for Celcius.
```python
Endpoint: /weather/{location}/{unit}
```

### QR Code Generator
Generates a QR code and uploads it to imgur, useful to quickly share a piece of text or URL.
```python
Endpoint: /qrgenerator/{string}/{size}
```

### Text Parser
Extracts text from any image. It works best on English text.
```python
Endpoint: /textparser/{url}
```

### Proxy Detector
Detects whether an IP address is a proxy/vpn or not. High accuracy!
```python
Endpoint: /proxydetector/{ip}
```

### Either or
Provides a random "would you rather" question/dilemma, giving two hard options. (We recommend using JSON)
```python
Endpoint: /eitheror
```

### GIF Finder
Gives you a list of animated GIF's based on the given keyword.
```python
Endpoint: /gif/{keyword}
```
