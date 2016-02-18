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


def selen(driver, url):
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
	
	urls_done = [
		#"https://hasjob.co/view/2kd5p",
		#"https://hasjob.co/view/65ccx",
		#"https://hasjob.co/view/uoemf",
		#"https://hasjob.co/view/0awzv",
		#"https://hasjob.co/canvs.in/vx50x",
		#"https://hasjob.co/upgrad.com/jyfjj",
		# "https://hasjob.co/bcjukebox.in/86rdh"
		#"https://hasjob.co/tangramme.com/ejt9v"
		#"https://hasjob.co/gmail.com/u0hxe"
		#"https://hasjob.co/intimetechlabs.com/n9uzc",
		#"https://hasjob.co/pixoc.com/s8yx4",
		#"https://hasjob.co/kotak.net/s5og0",
		#"https://hasjob.co/listup.co.in/0z9tl",
		#"https://hasjob.co/skyfilabs.com/k2q30",
		#"https://hasjob.co/beewise.in/28l84",
		#"https://hasjob.co/infratab.in/4mvom",
		#"https://hasjob.co/khyateh.com/w026u?b=0",
		#"https://hasjob.co/skoov.com/zi6kk",
		#"https://hasjob.co/bhiveworkspace.com/njc18",
		#"https://hasjob.co/doctorscircle.in/9f461",
		#"https://hasjob.co/mammoth.io/t4pub",
		#"https://hasjob.co/compile.com/9ffs0?b=1",
		#"https://hasjob.co/nightingales.in/46x8q",
		#"https://hasjob.co/urbanhunt.in/bc3kl",
		#"https://hasjob.co/dailycacy.in/ugoqk",
		#"https://hasjob.co/robocop.io/4m8jb",
		#"https://hasjob.co/callhub.io/enlej?b=1",
		#"https://hasjob.co/logos.social/vcar6",
		#"https://hasjob.co/nanolocal.in/9zv9t",
		#"https://hasjob.co/codingmart.com/4sva7",
		
		# BLore
		# Clearride
		#"https://hasjob.co/clearride.in/3l2m1",
		# Hoverr
		#"https://hasjob.co/hoverr.co/6gfy7",
		# Hiver
		#"https://hasjob.co/grexit.com/ava6y",
		#"https://hasjob.co/janacare.com/qoanl?b=1",
		
		#"https://hasjob.co/dishq.in/4piy8",
		#"https://hasjob.co/skyfilabs.com/jqfy6",
		#"https://hasjob.co/oyeplay.com/74hzy",
		
		
		#Any
		#"https://hasjob.co/krevive.solutions/m27pz",
		#"https://hasjob.co/tablehero.com/zb2eo",
		#"https://hasjob.co/skedool.it/v3olt",
		#MeTripping
		#"https://hasjob.co/metripping.com/pcief",
		
		#"https://hasjob.co/devois.com/360io",
		#"https://hasjob.co/opexanalytics.com/5hvg8",
		#"https://hasjob.co/jet.one/ck6fs",
		#"https://hasjob.co/phodphad.com/l51bu",
		#"https://hasjob.co/falkonry.com/94gqp",
		#"https://hasjob.co/sodainmind.com/vipf9?b=1",
		
		#"https://hasjob.co/vahan.co/rd5bx",
		#"https://hasjob.co/kuvera.in/f0a3m",
		#"https://hasjob.co/chaipoint.com/qxshw",
		
		# Mum
		#"https://hasjob.co/sportzinteractive.net/hff4n",
		#"https://hasjob.co/sutrajobs.com/e4kx4",
		#"https://hasjob.co/tacto.in/op9ir?b=1",
		#"https://hasjob.co/decorasystems.com/jpzgu",
		# CityFlo
		#"https://hasjob.co/cityflo.com/zizl2",
		# Canvs.in
		#"https://hasjob.co/canvs.in/oqvzj",
		#"https://hasjob.co/right-click.in/ulj3u",
		# Craftsvilla
		#"https://hasjob.co/sutrajobs.com/e4kx4",
		# Breakout
		#"https://hasjob.co/gobreakout.com/br76k",
		# Ithaka
		#"https://hasjob.co/ithaka.travel/ocnh1",
		# BCJukebox
		#"https://hasjob.co/bcjukebox.in/e02pb",
		# Truce
		#"https://hasjob.co/truce.in/oupsr?b=1",
		# Nexplor
		#"https://hasjob.co/nexplor.io/bvv9i",
		
		#"https://hasjob.co/urbanhunt.in/ibhpd",
		#"https://hasjob.co/shopzeko.in/fbcwl",
		
		#"https://hasjob.co/inayo.in/66edt?b=0",
		#"https://hasjob.co/fulfil.io/a1t52",
		
		
		
	]
	# urls_done
	
	urls_left = [
		# Blore
		#"https://hasjob.co/relatas.com/um0xf",
		#"https://hasjob.co/whyable.com/as0ce",
		#"https://hasjob.co/doctorscircle.in/3a1dx",
		#"https://hasjob.co/eclinic247.com/zdv8x",
		#"https://hasjob.co/buzzhire.in/nzjd9",
		#"https://hasjob.co/kingslearning.in/h8xh0",
		#"https://hasjob.co/buzzfactr.co/16u2y",
		#"https://hasjob.co/redmonstergames.com/o2ga5",
		#"https://hasjob.co/mytempleapp.com/wgnpm?b=1",
		#"https://hasjob.co/nanolocal.in/3akp5",
		#"https://hasjob.co/tecsolsoftware.com/8pdp8",
		#"https://hasjob.co/innovsystech.com/ze6q7",
		#"https://hasjob.co/kritiwitty.co/k4psn?b=0",
		#"https://hasjob.co/clickypanel.com/g86ss",
		#"https://hasjob.co/mebelkart.com/jgb6r",
		
		# Pune
		#"https://hasjob.co/jombay.com/pbf3e",
		
		
		# FlatPi
		#"https://hasjob.co/flatpi.com/ikbav",
		
		
		
		
	]
	#urls_left
	
	for url in urls_left:
		print url
		d = selen(driver, url)
	
	d.quit()
	#driver.quit()
	return True


# dom=document.getElementById('id_of_the_tinymce_frame').contentDocument.body



