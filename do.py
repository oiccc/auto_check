#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import time
import datetime
import requests



def set_page_timeout():
	x = 1

def login_refresh_ression(login_username,login_password):
	x=1
	print (login_username,login_password)
	headersss_admin = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Length':'115',
        'Content-Type':'application/x-www-form-urlencoded',
        #'Cookie':'SESSION=daf7aebf-f3ec-4302-ad2c-ed311cb1e7b2',
        'Host':'authwe.cwrcloud.huawei.com',
        'Origin':'https://authwe.cwrcloud.huawei.com',
        'Referer':'https://authwe.cwrcloud.huawei.com/cas/login?service=https://authwe.cwrcloud.huawei.com/cwr-user-web/shiro-cas?targetUrl=/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
        'Upgrade-Insecure-Requests':'1'
        }
	headersss_admin222 = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',

        #'Cookie':'SESSION=daf7aebf-f3ec-4302-ad2c-ed311cb1e7b2',
        'Host':'we.cwrcloud.huawei.com',
        'Referer':'https://authwe.cwrcloud.huawei.com/cas/login?service=https://authwe.cwrcloud.huawei.com/cwr-user-web/shiro-cas',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
        'Upgrade-Insecure-Requests':'1'
        }

	page_url = 'https://authwe.cwrcloud.huawei.com/cas/login?service=https://we.cwrcloud.huawei.com/cwr-user-web/shiro-cas'
	loginurl = 'https://authwe.cwrcloud.huawei.com/cas/login'
	login_data = {
                'username':login_username,
                'password':login_password,
                'securityCode':'1111',
                'language':'zh-cn',
                'execution':'e1s1',
                '_eventId':'submit',
                'geolocation':''}  
	yzm_data = {
                'userName':login_username,
                'password':login_password,
                'code':'1111',
                'languageType':'zh-cn'}  
	yzm_string = 'userName=sxzdhUser01&password=Aa123456&code=1111&languageType=zh-cn'
	s = requests.Session()
	res111 = s.get(page_url)
	res222 = s.get("https://authwe.cwrcloud.huawei.com/cas/defaultKaptcha")
	res333 = s.get("https://authwe.cwrcloud.huawei.com/cas/getUserWebSite?GET")
            #headersss_admin['SESSION'] = s.cookies.get_dict()['SESSION']
	print (res333.content)
	print (yzm_data)
	xxx = s.cookies.get_dict()['SESSION']
	print (xxx)
	res133 = s.post("https://authwe.cwrcloud.huawei.com/cas/compareKaptcha",headers=headersss_admin,data=yzm_data,verify=False)
            #headersss_admin['SESSION'] = s.cookies.get_dict()['SESSION']
	print (headersss_admin)
	print (res133.content)
	print (res133.headers)
	headersss_admin['SESSION'] = xxx
	print (headersss_admin)

	loginstring='username=sxzdhUser01&password=Aa123456&securityCode=1111&execution=e1s1&_eventId=submit&geolocation=&language=zh-cn'
	res134 = s.post("https://authwe.cwrcloud.huawei.com/cas/login",data=loginstring,headers=headersss_admin,verify=False)
	print ('ssosss',res134.content)
	print ('httpcode',res134.status_code)
	print (res133.headers)
	print (s.cookies.get_dict())
	headersss_admin222['Cookie'] = 'shiro.sesssion2'+'='+str(s.cookies.get_dict()['shiro.sesssion2'])+';nickName=sxzdhUser01; language=zh-cn'
	print (headersss_admin222)
	res444 = s.get("https://we.cwrcloud.huawei.com/cwr-user-web/pages/cwr-entry-new.html",headers=headersss_admin222,verify=False)
            
	print (res444.content)
	res555 = s.get("https://we.cwrcloud.huawei.com/cwr-user-web/anticsrf.js",headers=headersss_admin222,verify=False)
	print (res555.content)

	result = re.findall(".token:\"(.*)\"\}",str(res555.content))
	for i in s.cookies.get_dict():
		print (i,s.cookies.get_dict()[i])
		newcookies = i+"="+s.cookies.get_dict()[i]
	X_CSRF_TOKEN = result[0]
	print (res444.status_code)
	print( newcookies,X_CSRF_TOKEN)






def check_status(cookies_set,log_file_path,case_content,time_warning_limit,login_url,monitor_url,hub_url,result_file_path,ignore_in_url_list,username,password):
	try:
		print ('==obv portal check '+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		task_status = 'pass'
		task_http_code = 200
		res = 'check pass'
		#print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		#print ("Check "+case_content)
		chrome_options = webdriver.ChromeOptions()
		caps = DesiredCapabilities.CHROME
		caps['loggingPrefs'] = {'performance': 'ALL'}
		caps['perfLoggingPrefs']={'enableNetwork': True}
		#logincookiew =[{'value': 'c1dad3cd-6ea7-4bd0-9bff-34ceaf22ba60', 'httpOnly': True, 'domain': 'alpha2.cwrcloud.huawei.com', 'name': 'shiro.sesssion2', 'secure': False, 'path': '/cwr-user-web'},{'value': 'sdAdmin01', 'httpOnly': False, 'domain': '.huawei.com', 'name': 'nickName', 'secure': False, 'path': '/'},{'value': 'h-cn', 'httpOnly': False, 'domain': '.huawei.com', 'name': 'language', 'secure': False, 'path': '/'}]
		driver = webdriver.Remote(command_executor=hub_url,
		desired_capabilities = caps)
		driver.get(login_url)
		for i in cookies_set:
			#print (i)
			if i['secure'] =='False':
				i['secure'] = False
			elif i['secure'] =='True':
				i['secure'] = True
			if i['httpOnly'] =='False':
				i['httpOnly'] = False
			elif i['httpOnly'] =='True':
				i['httpOnly'] = True
			driver.add_cookie(i)


		driver.get(monitor_url)
		try:
			driver.implicitly_wait(10)   
			title = driver.title
			print (title)
		except Exception as e:
			title = 'cwr entry'
			print (e)
		if title != 'cwr entry':
			task_status = 'failed'
			res='sessionfailed'
			login_refresh_ression(username,password)
			exit()
			#go to login and refresh session
		#print ("等待30s，页面加载")
		time.sleep(10)
		#print ("after 30s")
		xxx =driver.get_log('performance')
		#print (xxx[0])
		cost_start = time.strftime(("%Y-%m-%d %H:%M:%S"), time.localtime(xxx[0]['timestamp']/1000))
		cost_end = time.strftime(("%Y-%m-%d %H:%M:%S"), time.localtime(xxx[-1]['timestamp']/1000))
		cost_time = (xxx[-1]['timestamp']-xxx[0]['timestamp'])/1000
		http_status_200_count = 0
		http_status_500_count = 0
		http_status_000_count = 0
		result_000_string =''
		with open(log_file_path,'a') as f:
			for i in xxx:
				try:
					if json.loads(i['message'])['message']['method'] == 'Network.responseReceived':
						url = json.loads(i['message'])['message']['params']['response']['url'][:100]
						otherStyleTime = time.strftime(("%Y-%m-%d %H:%M:%S"), time.localtime(i['timestamp']/1000))
						datasize = str(float(json.loads(i['message'])['message']['params']['response']['encodedDataLength'])/1024)[:4]
						try:
							timetime = str(float(json.loads(i['message'])['message']['params']['response']['timing']['sendEnd'])-float(json.loads(i['message'])['message']['params']['response']['timing']['sendStart']))[:4]
						except Exception as e:
							timetime = 0
						status = json.loads(i['message'])['message']['params']['response']['status']
						statusText = json.loads(i['message'])['message']['params']['response']['statusText']
						r_type = json.loads(i['message'])['message']['params']['type']
						log_string = str(otherStyleTime)+'|'+url+'|'+str(status)+'|'+str(r_type)+'|'+str(datasize)+'kb|'+str(timetime)+'\n\r'
						f.write(log_string)
						if status ==500 and r_type =='XHR':
							task_status = 'failed'
							task_http_code = 500
							res = 'XHR failed>0'
							for i in ignore_in_url_list:
								if i in url:
									#print ('igore')
									task_status = 'pass'
									task_http_code = 200
									res = 'check pass'

									break



						if status == 200:
							http_status_200_count += 1
						#	if float(timetime) >time_warning_limit:
						#		print (str(otherStyleTime)+'|'+url+'|\033[1;32m'+str(status)+'\033[0m|'+str(r_type)+'|'+str(datasize)+'kb|\033[1;33m'+str(timetime)+'\033[0mms')
						#	else:
						#		print (str(otherStyleTime)+'|'+url+'|\033[1;32m'+str(status)+'\033[0m|'+str(r_type)+'|'+str(datasize)+'kb|\033[1;32m'+str(timetime)+'\033[0mms')
						elif status == 500:
							result_000_string = result_000_string +log_string
						#	http_status_500_count += 1
						#	if float(timetime) >time_warning_limit:
						#		print (str(otherStyleTime)+'|'+url+'|\033[1;31m'+str(status)+'\033[0m|'+str(r_type)+'|'+str(datasize)+'kb|\033[1;33m'+str(timetime)+'\033[0mms')
						#	else:
						#		print (str(otherStyleTime)+'|'+url+'|\033[1;31m'+str(status)+'\033[0m|'+str(r_type)+'|'+str(datasize)+'kb|\033[1;32m'+str(timetime)+'\033[0mms')
						else:
							result_000_string = result_000_string +log_string
							http_status_000_count += 1
						#	if float(timetime) >time_warning_limit:
						#		print (str(otherStyleTime)+'|'+url+'|\033[1;31m'+str(status)+'\033[0m|'+str(r_type)+'|'+str(datasize)+'kb|\033[1;33m'+str(timetime)+'\033[0mms')
						#	else:
						#		print (str(otherStyleTime)+'|'+url+'|\033[1;31m'+str(status)+'\033[0m|'+str(r_type)+'|'+str(datasize)+'kb|\033[1;32m'+str(timetime)+'\033[0mms')
				except Exception as e:
					print (e)
		
		if int(cost_time) >60:
			task_status = 'failed'
			res = 'CostTime>60'

		infostring =  ('checkitem=obv portal,name={},status={},http_code={},time_total={},desc={}'.format(case_content,task_status,task_http_code,cost_time,res))
		print (infostring)


		with open(result_file_path,'a') as dd:
			result_string = (str(otherStyleTime)+"|OK:"+str(http_status_200_count)+'|500:'+str(http_status_500_count)+'|000:'+str(http_status_000_count)+'|cost_time:'+str(cost_time)+'\n\r'+result_000_string)		
			dd.write(result_string)

	except Exception as e:
		print (e)
	finally:
		driver.quit()







def main_do():
	with open('test.conf','r') as f:
		load_dict = json.load(f)
		second_wait = (load_dict['second_wait'])
		time_warning_limit =(load_dict['time_warning_limit']) 
		login_url = (load_dict['login_url']) 
		monitor_url = (load_dict['monitor_url']) 
		hub_url = (load_dict['hub_url']) 

		ignore_in_url_list = (load_dict['ignore_in_url']).split(',')

		for i in load_dict['config_set']:
			cookies_set =i['config']['cookies']
			log_file_path = (i['config']['log_file_path'])
			result_file_path = (i['config']['result_file_path'])
			case_content = (i['config']['case_content'])
			username =(i['config']['username'])
			password = (i['config']['password']) 
			check_status(cookies_set,log_file_path,case_content,time_warning_limit,login_url,monitor_url,hub_url,result_file_path,ignore_in_url_list,username,password)		
	if int(second_wait)==-1:
		exit()
	else:
		time.sleep(int(second_wait))

while True:
	main_do()
#check_status()

