# Python Codes and Scripts
These are python scripts I am either working on, borrowed from others and improved (with citing), or developing currently.

## [Calculator](https://github.com/initcyber/Python/tree/master/Calculator)
### [Simple_Calculator.py](https://github.com/initcyber/Python/tree/master/Calculator/Simple%20Calculator.py)
Calculator I wrote around 2019. Need to refactor the code a bit and lint it.

## Cybersecurity Related Tools
###  [Nessus](https://github.com/initcyber/Python/blob/master/CybersecurityTools/Nessus/)
#### [nessus-csv-api.py](https://github.com/initcyber/Python/blob/master/CybersecurityTools/Nessus/nessus-csv-api.py)
Borrowed from [515tech](https://www.515tech.com/post/how-to-collect-data-from-the-tenable-nessus-api) - Line near or at 102 in [nessus-csv-api.py](https://github.com/initcyber/Python/blob/master/CybersecurityTools/Nessus/nessus-csv-api.py) 
 originally stated: 
	 `scan_request = session.get(scanverify=False)`
 I replaced some lined to make the script work. It now states:
 	 `scan_request = session.get(url=scan_url, scanverify=False)`


### [Python Scanner](https://github.com/initcyber/Python/blob/master/CybersecurityTools/Python%20Scanner/)
#### [scanner.py](https://github.com/initcyber/Python/blob/master/CybersecurityTools/Python%20Scanner/scanner.py)
Written around 2020 - This is a basic Python3 port scanner. 
