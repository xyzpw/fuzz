#!/usr/bin/env python3
import requests

ua = input("User-agent: ")


opt = int(input('''
Options:
1) dir
2) js
3) css
4) image
5) manifest
6) admin
'''))
uri = input("URI: ")

def start_fuzz(link, _type=opt):
  successStatusCodes = 0; scannedDirs = 0; forbiddenStatusCodes = 0
  scanDir = 'dir-wordlist.txt'
  if _type == 2: scanDir = 'js-wordlist.txt'
  elif _type == 3: scanDir = 'css-wordlist.txt'
  elif _type == 4: scanDir = 'image-wordlist.txt'
  elif _type == 5: scanDir = 'manifest-wordlist.txt'
  elif _type == 6: scanDir = 'admin-wordlist.txt'
  f = open(f'src/{scanDir}', 'r')
  for line in f.readlines():
    try:
      if _type != 4:
        r = requests.get(f"{link}{line.strip()}", headers={'user-agent': ua}, timeout=3)
        if r.status_code == 200: successStatusCodes += 1
        if r.status_code == 403: forbiddenStatusCodes += 1
        scannedDirs += 1
        print(f"\n{link}{line.strip()} => {r.url} returned status code {r.status_code}\n")
      elif _type == 4:
        r = requests.get(f"{link}{line.strip()}.png", headers={'user-agent': ua}, timeout=3) #scan png image
        if r.status_code == 200: successStatusCodes += 1
        if r.status_code == 403: forbiddenStatusCodes += 1
        scannedDirs += 1
        print(f"\n{link}{line.strip()}.png => {r.url} returned status code {r.status_code}\n")

        r = requests.get(f"{link}{line.strip()}.jpg", headers={'user-agent': ua}, timeout=3) #scan jpg image
        if r.status_code == 200: successStatusCodes += 1
        if r.status_code == 403: forbiddenStatusCodes += 1
        scannedDirs += 1
        print(f"\n{link}{line.strip()}.jpg => {r.url} returned status code {r.status_code}\n")

        r = requests.get(f"{link}{line.strip()}.jpeg", headers={'user-agent': ua}, timeout=3) #scan jpeg image
        if r.status_code == 200: successStatusCodes += 1
        if r.status_code == 403: forbiddenStatusCodes += 1
        scannedDirs += 1
        print(f"\n{link}{line.strip()}.jpeg => {r.url} returned status code {r.status_code}\n")

        r = requests.get(f"{link}{line.strip()}.ico", headers={'user-agent': ua}, timeout=3) #scan ico image
        if r.status_code == 200: successStatusCodes += 1
        if r.status_code == 403: forbiddenStatusCodes += 1
        scannedDirs += 1
        print(f"\n{link}{line.strip()}.ico => {r.url} returned status code {r.status_code}\n")

        r = requests.get(f"{link}{line.strip()}.gif", headers={'user-agent': ua}, timeout=3)
        if r.status_code == 200: successStatusCodes += 1
        if r.status_code == 403: forbiddenStatusCodes += 1
        scannedDirs += 1
        print(f"\n{link}{line.strip()}.gif => {r.url} returned status code {r.status_code}\n")
    except KeyboardInterrupt:
      successStatusCodePercentage = successStatusCodes / scannedDirs * 100
      print(f"\n\n{successStatusCodes} / {scannedDirs} returned 200 status code ({successStatusCodePercentage} %)\n\n")
      print("\n\nExiting\n\n")
      exit()
    except Exception as e:
      print(f"Exception caught {e}")
  successStatusCodePercentage = successStatusCodes / scannedDirs * 100
  successAndForbidden = forbiddenStatusCodes + successStatusCodes
  succesAndForbiddenPercentage = successAndForbidden / scannedDirs * 100
  print(f"\n\n{successStatusCodes} / {scannedDirs} returned 200 status code ({successStatusCodePercentage} %)\n\n")
  print(f"{successAndForbidden} / {scannedDirs} are open or forbidden ({succesAndForbiddenPercentage} %)\n\n")

start_fuzz(uri, opt)

del(opt, uri, start_fuzz); exit()
