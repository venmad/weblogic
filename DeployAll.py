import sys
import java
import java.util.Properties
import java.io.FileInputStream


############## Connect to weblogic admin server #############
def connectAdmin() :
	
	wlurl = 't3://'+wllistenaddress+':'+wllistenport
	print('connecting to the url:'+ wlurl)

	try:
		connect(wlusr, wlpwd, wlurl)
		print('Successfully connected')
	except:
		print 'Unable to find admin server...'
		exit()


################## deploy the application ###############
def deployApplication1() :
	try:
		connectAdmin()
		edit()
		startEdit()
		earname = applicationpath + '/' + earname1
		print ('Path to ear is' + earname)
		progress= deploy(earname1,earname,upload=false,targets=servr)
		progress.printStatus()
		activate()
		disconnect()
	except:
		print 'Unable to find EAR...'
	
	################## deploy the application ###############
def deployApplication2() :
	try:
		connectAdmin()
		edit()
		startEdit()
		earname = applicationpath + '/' + earname2
		print ('Path to ear is' + earname)
		progress= deploy(earname2,earname,upload=false,targets=servr)
		progress.printStatus()
		activate()
		disconnect()
	except:
		print 'Unable to find EAR...'
 
############Getting the Application Status########################		
def Applicationstatus() :
    connectAdmin()
    myapps=cmo.getAppDeployments()
    outputbuffer=[]
    outputbuffer.append("**"*50)
    outputbuffer.append(" \t\t\tAPPLICATION STATUS WEBLOGIC\t\t")
    outputbuffer.append("**"*50)
    outputbuffer.append (" %-50s%20s%20s" %("APPLICATION NAME","STATUS","TARGET"))
    outputbuffer.append("**"*50)
    for app in myapps:
            bean=getMBean('/AppDeployments/'+app.getName()+'/Targets/')
            targetsbean=bean.getTargets()
            for target in targetsbean:
                    domainRuntime()
                    cd('AppRuntimeStateRuntime/AppRuntimeStateRuntime')
                    appstatus=cmo.getCurrentState(app.getName(),target.getName())
                    outputbuffer.append(" %-50s%20s%20s" %(app.getName(),appstatus,target.getName()))
                    serverConfig()
    outputbuffer.append("**"*50)
    print'\n'.join(outputbuffer)
    file=open("DeploymentStatus.txt","w")
    output='\n'.join(outputbuffer)
    file.writelines(output)
    for line in file:
        print(line)
    file.close()
	############# main method #####################
  if __name__== "main":
	print('This will enable you to deploy the application ')
	deployfileStream=java.io.FileInputStream('DeployProperties.py')
	properties=java.util.Properties()
	properties.load(deployfileStream)
	
	wlsfileStream=java.io.FileInputStream('WLSProperties.py')
	wlproperties=java.util.Properties()
	wlproperties.load(wlsfileStream)
	
	
	wlusr=wlproperties.getProperty('wlusr')
	wlpwd=wlproperties.getProperty('wlpwd')
	wllistenaddress=wlproperties.getProperty('wllistenaddress')
	wllistenport=wlproperties.getProperty('wllistenport')
	applicationpath=wlproperties.getProperty('applicationpath')
	
	earname1=properties.getProperty('ear.name1')
	earname2=properties.getProperty('ear.name2')
	servr=wlproperties.getProperty('server')

	#validateProperties()
	deployApplication1()
	deployApplication2()
	Applicationstatus()
