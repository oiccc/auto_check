from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import time
import datetime




def set_page_timeout():
	x = 1



def check_status(cookies_set,log_file_path,case_content,time_warning_limit,login_url,monitor_url,hub_url,result_file_path):
	try:
		print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		print ("Check "+case_content)
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
		#print (driver.page_source)
		print ("等待30s，页面加载")
		time.sleep(30)
		print ("after 30s")
		xxx =driver.get_log('performance')
		http_status_200_count = 0
		http_status_500_count = 0
		http_status_000_count = 0
		with open(log_file_path,'a') as f:
			for i in xxx:
				try:
					if json.loads(i['message'])['message']['method'] == 'Network.responseReceived':
						url = json.loads(i['message'])['message']['params']['response']['url']
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
						if status == 200:
							http_status_200_count += 1
							if float(timetime) >time_warning_limit:
								print (str(otherStyleTime)+'|'+url+'|\033[1;32m'+str(status)+'\033[0m|'+str(r_type)+'|'+str(datasize)+'kb|\033[1;33m'+str(timetime)+'\033[0mms')
							else:
								print (str(otherStyleTime)+'|'+url+'|\033[1;32m'+str(status)+'\033[0m|'+str(r_type)+'|'+str(datasize)+'kb|\033[1;32m'+str(timetime)+'\033[0mms')
						elif status == 500:
							http_status_500_count += 1
							if float(timetime) >time_warning_limit:
								print (str(otherStyleTime)+'|'+url+'|\033[1;31m'+str(status)+'\033[0m|'+str(r_type)+'|'+str(datasize)+'kb|\033[1;33m'+str(timetime)+'\033[0mms')
							else:
								print (str(otherStyleTime)+'|'+url+'|\033[1;31m'+str(status)+'\033[0m|'+str(r_type)+'|'+str(datasize)+'kb|\033[1;32m'+str(timetime)+'\033[0mms')
						else:
							http_status_000_count += 1
							if float(timetime) >time_warning_limit:
								print (str(otherStyleTime)+'|'+url+'|\033[1;31m'+str(status)+'\033[0m|'+str(r_type)+'|'+str(datasize)+'kb|\033[1;33m'+str(timetime)+'\033[0mms')
							else:
								print (str(otherStyleTime)+'|'+url+'|\033[1;31m'+str(status)+'\033[0m|'+str(r_type)+'|'+str(datasize)+'kb|\033[1;32m'+str(timetime)+'\033[0mms')
				except Exception as e:
					print (e)
		print (str(http_status_200_count)+'|'+str(http_status_500_count)+'|'+str(http_status_000_count))		

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

		for i in load_dict['config_set']:
			cookies_set =i['config']['cookies']
			log_file_path = (i['config']['log_file_path'])
			result_file_path = (i['config']['result_file_path'])
			case_content = (i['config']['case_content'])
			check_status(cookies_set,log_file_path,case_content,time_warning_limit,login_url,monitor_url,hub_url,result_file_path)

	time.sleep(int(second_wait))

while True:
	main_do()
#check_status()

