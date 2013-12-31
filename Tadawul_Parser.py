import re
import time
import urllib

__Company={'1140': 'AL Bilad ', '4300': 'Dar Al Arkan ', '8250': 'AXA \
', '8150': 'ACIG ', '2090': 'Gypsum ', '4020': 'Real Estate ', '8300'
: 'Wataniya ', '3040': 'Qassim Cement ', '4220': 'Emaar E  ', '8012':
'Jazira Takaful ', '6080': 'Bishah Agriculture ', '8010': 'Tawuniya \
', '6004': 'Catering ', '2320': 'AL Babtain ', '6002': 'Herfy Foods '
, '8090': 'SANAD ', '7050': 'Almutakamela ', '4140': 'Saudi Export ',
'2150': 'Glass ', '8210': 'Bupa Arabia ', '2240': 'Zamil Industrial \
', '2010': 'SABIC ', '8220': 'Weqaya Takaful ', '1090': 'SAMBA ', 
'1310': 'MMG ', '8140': 'Al ', '1150': 'Alinma ', '4030': 'Bahri ', 
'7040': 'Atheeb Telecom ', '6090': 'Jazan Development ', '8020': 
'Malath Insurance ', '4230': 'Red Sea ', '6010': 'NADEC ', '8290': 
'Solidarity ', '4130': 'Al Baha ', '1060': 'SABB ', '3030': 'Saudi \
Cement ', '2310': 'Sipchem ', '2140': 'Al Ahsa for Dev ', '2060': 
'Industrialization ', '2250': 'SIIG ', '1320': 'SSP ', '8230': 'Al \
Rajhi Takaful ', '8030': 'MEDGULF ', '1080': 'Arab National ', '1120'
: 'Al Rajhi ', '4070': 'Tihama ', '7030': 'ZAIN KSA ', '4090': 
'Taiba ', '4200': 'Aldrees ', '8130': 'ATC ', '4280': 'Kingdom ', 
'4040': 'SAPTCO ', '2300': 'SPM ', '3020': 'Yamamah Cement ', '2380':
'Petro Rabigh ', '2170': 'Alujain ', '6060': 'Sharqiya Dev Co ', 
'2260': 'Sahara Petrochemical ', '2070': 'Pharmaceutical ', '1010': 
'RIBL ', '8040': 'ALLIANZ SF ', '4210': 'SRMG ', '2280': 'Almarai ', 
'4270': 'SPPC ', '1330': 'ALKHODARI ', '4190': 'Jarir ', '7020': 
'Etihad Etisalat ', '8200': 'Saudi Re ', '8280': 'Al Alamiya ', 
'8120': 'Gulf Union ', '2270': 'SADAFCO ', '2040': 'Ceramic ', '4050'
: 'SASCO ', '3010': 'Arab Cement ', '6001': 'H B ', '4290': 
'Alkhaleej Trng ', '3090': 'Tabuk Cement ', '3091': 'Jouf Cement ', 
'6070': 'Jouff Agriculture ', '2370': 'MESC ', '2160': 'Amiantit ', 
'4260': 'Budget Saudi ', '4080': 'Assir ', '8050': 'SALAMA ', '4110':
'Mubarrad ', '4180': 'Fitaihi Group ', '2290': 'YANSAB ', '2190': 
'SISCO ', '3004': 'Northern Cement ', '3001': 'HCC ', '3003': 'City \
Cement ', '3002': 'Najran Cement ', '8110': 'WAFA Insurance ', '7010'
: 'STC ', '2200': 'Pipes ', '2050': 'SAVOLA  Group ', '8190': 'U C A \
', '4061': 'Anaam Holding ', '1301': 'ASLAK ', '6040': 'Tabuk \
Agriculture ', '2110': 'Cables ', '1030': 'Saudi Investment ', '3080'
: 'Eastern Cement ', '2360': 'SVCP ', '1212': 'Astra Indust ', '1213'
: 'AlSorayai Group ', '1210': 'BCI ', '1211': 'MA ', '8100': 'SAICO '
, '1214': 'SHAKER ', '8060': 'Walaa Insurance ', '2180': 'FIPCO ', 
'8260': 'Gulf General ', '2210': 'Nama Chemicals ', '4170': 'Shams', 
'1020': 'BJAZ ', '8180': 'Sagr Insurance ', '2020': 'SAFCO ', '2350':
'Saudi Kayan ', '2100': 'Food ', '6050': 'Saudi Fisheries ', '8170':
'Trade Union ', '5110': 'Saudi Electricity ', '8070': 'Arabian \
Shield ', '1201': 'Takween ', '4240': 'AlHokair ', '3060': 'Yanbu \
Cement ', '8270': 'Buruj ', '1050': 'Saudi Fransi ', '1810': 
'ALTAYYAR ', '2340': 'AlAbdullatif ', '2130': 'Saudi Industrial ', 
'4160': 'Thim ', '4001': 'A ', '4002': 'Mouwasat ', '4003': 'Extra ',
'4004': 'Dallah Health ', '4005': 'Care ', '2220': 'Maadaniyah ', 
'2030': 'SARCO ', '6020': 'Qassim Agriculture ', '4310': 'KEC ', 
'8160': 'AICC ', '4250': 'Jabal Omar ', '4100': 'Makkah ', '8310': 
'AMANA Insurance ', '8311': 'Enaya ', '8312': 'Alinma Tokio M ', 
'8240': 'ACE ', '3050': 'Southern Cement ', '2330': 'Advanced ', 
'2120': 'Saudi Advanced ', '4150': 'Arriyadh Development ', '1040': 
'Saudi Hollandi ', '8080': 'SABB Takaful ', '2230': 'Saudi Chemical '
, '2080': 'Gas ', '4010': 'Hotels ', '2002': 'Petrochem ', '2001': 
'CHEMANOL '}

__SITE="http://www.tadawul.com.sa/wps/portal/!ut/p/c1/04_SB8K8xLLM9MSSzPy8xBz9CP0os3g_A-ewIE8TIwODYFMDA08Tn7AQZx93YwMjM6B8JG55AwOSdLsHhJmC5IONggO8jA08jQjoDk7N0_fzyM9N1S_IDY0od1RUBABj6OCs/dl2/d1/L2dJQSEvUUt3QS9ZQnB3LzZfTjBDVlJJNDIwRzE5MTBJS1NROVUyQTIwSjc!/?tabOrder=1&symbol=%s"#notic the %s for string replacement

class Analyze(object):
	def __init__(self,listOfCompanyCode):
		''' should pass a list  of company code , at least one element (for individual company !)'''
		self.CompanyCodes = listOfCompanyCode
	def __isMarketOpen(self):
		''' check the current time and compare it with time for Market to be open [from 11am to 3:30pm] 
		    return True when the current time at this interval[11am,3:30pm] ,else false
		'''
		#TODO:Next Version Add Eid's and Saudi national Day To be Closed
		CurrentTime = time.localtime()
		if (11<=CurrentTime[3]<15):
			return True
		elif (CurrentTime==CurrentTime[3] == 15 and CurrentTime[4]<=30):
			return True
		return False
		
	
	def Print(self,inputs):
		'''
		print formatted text to secren // you could change it to return formatted String in case wana integrate this module with your own project (maybe gui ..etc)
		'''
	def Fetch(self):
		'''
		will loop over all company you've choosed and fetch Data and parse it
		'''
	def FetchWhileMarketOpen(self,Sleep=0.5):
		'''
		Fetch then parse data while the Market is open
		Sleep:time for sleep between two fetch 
		'''


if __name__=='__main__':
	#if your run that pyfile as main file
	print "\t\t** Tdawul Monitor **"
	print "1-Show all Company Name with their Code"
	print "2-Enter Company Code (seprated with comma )"
	select = raw_input("Enter Your Choice:")
	
	if select =='1':
		for code,name in zip(__Company.keys(),__Company.values()):
			print "%-25s : %-4s"%(name,code)
	elif select == '2':
		Codes = raw_input("ENTER CODES:")
		Codes = Codes.replace(" ","").split(",")
		#checking if all Codes are valid
		if False  in [__Company.has_key(SingleCode) for SingleCode in Codes]:
			#NOTE !! print should be changed !
			print "\033[1;41m[-]One of your Codes is invalid make sure that all your entered code is correct\033[1;m\nBye!"
		else:
			#create object ..etc
			pass
			
		
	else:
		print "invalid input , Bye !"
	

