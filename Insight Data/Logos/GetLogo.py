import clearbit
import json
import urllib
import requests 
import shutil

def downloadlogo(response):
	try:
		if response is not None:
			if response is not "":
				print(json.dumps(response))
				with open(x.replace("\n","").replace(" ","") + '.json', 'w') as outfile:
					json.dump(response, outfile)

				print(response['logo'])
				urllib.urlretrieve(response['logo'], x.replace("\n","") + ".jpg")

				r = requests.get(response['logo'], stream=True)
				if r.status_code == 200:
					with open(x.replace("\n","") + ".png", 'wb') as f:
						r.raw.decode_content = True
						shutil.copyfileobj(r.raw, f)
				
				#from selenium import webdriver;
				#from selenium import WebElement;
				#driver = webdriver.Ie();
				#driver.get(response['logo']);
				#image_element = driver.find_element_by_name('img')
				#src = image_element.get_attribute("src")
				#if src:
				#	driver.get(src)
				#	driver.save_screenshot(x.replace("\n","") + '.png')
	except AssertionError as error:
		print(error)
			
clearbit.key = 'sk_460eb096462bb99c960bfbaad2db9ff3'

f = open("C:\Work\Code\Logos\Clients.csv", "r")
for x in f:
	print(x)

	response = clearbit.NameToDomain.find(name=x)
	combined = clearbit.Enrichment.find(domain=x.replace(" ","").replace("&","") + ".com",stream=True)
	print(json.dumps(combined))
	downloadlogo(combined)	
			
