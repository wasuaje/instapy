
# -*- coding: utf-8 -*-
#! /usr/bin/env python

import urllib
import urllib2
import uuid
import random
import datetime
import hashlib
import json

def totimestamp(dt):
	epoch=datetime(1970,1,1)
	td = dt - epoch
	# return td.total_seconds()
	return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6 

def  SendRequest(url,post_data, user_agent):
	url = 'https://instagram.com/api/v1/'+url		
	headers = { 'User-Agent' : user_agent }
	req = urllib2.Request(url, post_data, headers)
	print dir(req)
	print req.data
	response = urllib2.urlopen(req)	
	the_page = response.read()	
#     ch = curl_init();
# 	curl_setopt($ch, CURLOPT_URL, 'https:#instagram.com/api/v1/'+url);
# 	curl_setopt($ch, CURLOPT_USERAGENT, $user_agent);
# 	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
# 	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);

# 	if($post) {
# 		curl_setopt($ch, CURLOPT_POST, true);
# 		curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
# 	}
		
# 	if($cookies) {
# 		curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookies.txt');			
# 	} else {
# 		curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookies.txt');
# 	}
		
# 	$response = curl_exec($ch);
# 	$http = curl_getinfo($ch, CURLINFO_HTTP_CODE);
# 	curl_close($ch);
		
	return the_page

def GenerateGuid():
	return uuid.uuid1()

def  GenerateUserAgent():
	resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
	dpis = ['120', '160', '320', '240']

	ver = random.choice(versions)
	dpi = random.choice(dpis)
	res = random.choice(resolutions)
	
	return 'Instagram 6.'+str(random.randint(1,2))+'.'+str(random.randint(0,2))\
	       +' Android ('+str(random.randint(10,11))+'/'+str(random.randint(1,3))+'.'\
	       +str(random.randint(3,5))+'.'+str(random.randint(0,5))+'; '+dpi+'; '+res+\
	       '; samsung; '+ver+'; '+ver+'; smdkc210; en_US)'

def  GenerateSignature(data):
	#return hash_hmac('sha256', data, 'b4a23f5e39b5929e0666ac5de94c89d1618a2916');
	return hashlib.sha256(data).hexdigest()

def  GetPostData(filename):
	now = datetime.utcnow()
	_time=totimestamp(now)
	if not os.path.exists(filename):
		print "The image doesn't exist " + filename;
	else:
		post_data = {'device_timestamp' :_time, 
							'photo' : '@'+filename}
		return post_data

# Set the username and password of the account that you wish to post a photo to
username = 'vitasunset1';
password = 'vita456';

# Set the path to the file that you wish to post.
# This must be jpeg format and it must be a perfect square
filename = 'kids3.jpg'

# Set the caption for the photo
caption = "Kids Products"

# Define the user agent
agent = GenerateUserAgent()

# Define the GuID
guid = GenerateGuid()

# Set the devide ID
device_id = "android-%s" % guid

## LOG IN 
# You must be logged in to the account that you wish to post a photo too
# Set all of the parameters in the string, and then sign it with their API key using SHA-256
data = {"device_id":"%s" % device_id,"guid":"%s" % guid,"username":"%s" % username,\
		"password":"%s" % password, "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
		}
datastrjson = json.dumps(data)

dat = urllib.urlencode(data)
sig = GenerateSignature(dat)
#data= json.load(data)

data = 'signed_body='+sig+'.'+dat+'&ig_sig_key_version=6'
login = SendRequest('accounts/login/', data, agent);
print login