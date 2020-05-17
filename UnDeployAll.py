import os
import sys
import java.util.Properties
import java.io.FileInputStream


############## connecting to weblogic admin server #############
def connectAdmin() :
	
	wlurl = 't3://'+wllistenaddress+':'+wllistenport
	print('connecting to the url:'+ wlurl)

	try:
		connect(wlusr, wlpwd, wlurl)
		print('Successfully connected')
	except:
		print 'Unable to find admin server...'

def undeployApplications() :
	cd ('AppDeployments')
	myapps=cmo.getAppDeployments()
	for appName in myapps:
	   try:
		  appPath = "/AppDeployments/" + appName.getName()
		  cd(appPath)
		  print "Stopping deployment " + appName.getName()
		  stopApplication(appName.getName())
		  print "Undeploying " + appName.getName()
		  undeploy(appName.getName(), timeout=60000)
	   except Exception , e:
		  print "Deployment " + appName.getName() + " removal failed."
	  
############# main method #####################
if __name__== "main":
	fileStream=java.io.FileInputStream('WLSProperties.py')
	properties=java.util.Properties()
	properties.load(fileStream)
	wlusr=properties.getProperty('wlusr')
	wlpwd=properties.getProperty('wlpwd')
	wllistenaddress=properties.getProperty('wllistenaddress')
	wllistenport=properties.getProperty('wllistenport')
	
	connectAdmin()
	undeployApplications()
