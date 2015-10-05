from django.shortcuts import render

# Create your views here.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

def get_driver():
	driver = webdriver.Firefox()
	return driver

### FROM HERE Auto Poster starts ###
# AUTO-APPLIER AUTO-POSTER
def login_into_hasjob(driver):
	"""Open login page of hasjob, inpput your email/pass & login
	then call ur particular job details urlin selen function
	"""
	login_url = "https://hasjob.co/login"
	# login_url = "https://auth.hasgeek.com/login"
	driver.get(login_url)

	time.sleep(2)
	try:
		a = driver.find_element_by_id("showmore")
		a.click()
		time.sleep(1)
	except:
		# Log here, the element was not present
		print "Element with id `showmore` was not present"
		pass

	i = driver.find_element_by_id("username")
	i.send_keys("vickyojha2@yahoo.com")
	p = driver.find_element_by_id("password")
	p.send_keys("ashposeidon!!1")
	f = driver.find_element_by_id("passwordlogin")
	f.submit()
	time.sleep(7)


def selen(driver):
	urls_done = [
		"https://hasjob.co/view/2kd5p",
		"https://hasjob.co/view/65ccx",
		"https://hasjob.co/view/uoemf",
		"https://hasjob.co/view/0awzv",
	]
	urls_left = [ 
	]

	# url = "https://hasjob.co/bcjukebox.in/86rdh"
	#url = "https://hasjob.co/tangramme.com/ejt9v"
	#url = "https://hasjob.co/gmail.com/u0hxe"
	url = "https://hasjob.co/canvs.in/vx50x"
	url = "https://hasjob.co/upgrad.com/jyfjj"
	
	driver.get(url)
	time.sleep(5)

	# If `reveal-button` id present then do this else don't
	try:
		a = driver.find_element_by_id("reveal-button")
		a.click()
		# driver.get(url)
		time.sleep(3)
	except:
		# Log here, the element was not present
		print "Element with id `reveal-button` was not present"
		pass

	inp = driver.find_element_by_id("apply_email-0")
	inp.click()
	# Get phone number input field & fill it
	# same way for all other fields like email & job application
	# and then click Apply button
	ph = driver.find_element_by_id("apply_phone")
	ph.send_keys('9867922007')

	time.sleep(3)

	job_application_string = '<p>Hi Sir,</p><p>I am applying for the mentioned job.</p><p>The following is the link to my resume.</p><p><a data-mce-href=https://github.com/ashish2/r/blob/master/A4_2.doc?raw=true href=https://github.com/ashish2/r/blob/master/A4_2.doc?raw=true>https://github.com/ashish2/r/blob/master/A4_2.doc?raw=true</a><br data-mce-bogus=1></br> </p><p>Thanks & Regards,</p><p>Ashish.</p>'

	## tinyMCE.activeEditor.setContent(job_application_string)
	driver.execute_script("job_application_string = '<p>Hi Sir,</p><p>I am applying for the mentioned job.</p><p>The following is the link to my resume.</p><p><a data-mce-href=https://github.com/ashish2/r/blob/master/A4_2.doc?raw=true href=https://github.com/ashish2/r/blob/master/A4_2.doc?raw=true>https://github.com/ashish2/r/blob/master/A4_2.doc?raw=true</a><br data-mce-bogus=1></br> </p><p>Thanks & Regards,</p><p>Ashish.</p>';")
	# driver.execute_script("tinymce.activeEditor.setContent(job_application_string)")
	driver.execute_script("tinyMCE.get('apply_message').setContent(job_application_string)")
	driver.execute_script("tinymce.triggerSave()")

	# driver.switch_to_frame( driver.find_element_by_id("apply_message_ifr") )
	# bo = driver.find_element_by_id("tinymce")
	# bo.click()
	# bo.send_keys(job_application_string)
	# bo.send_keys(Keys.CONTROL, 'a') # highlight all in box
	# bo.send_keys(Keys.CONTROL, 'x') # cut
	# bo.send_keys(Keys.CONTROL, 'v') # paste

	# time.sleep(5)

	# driver.switch_to_default_content()


	f = driver.find_element_by_id("applyform")
	# print f
	# print f.id
	# print f.get_attribute("action")
	# print f.get_attribute("method")
	if f.id and f.get_attribute("method") == 'post':
		print "YES in Form"
		f.submit()

	time.sleep(5)

	# driver.quit()
	return driver

def poster_run():
	driver = get_driver()
	login_into_hasjob(driver)
	selen(driver)
	return driver


# dom=document.getElementById('id_of_the_tinymce_frame').contentDocument.body



