#####Connect to Weblogic AdminServer#######################
def connectAdmin() :
	
	wlurl = 't3://'+wllistenaddress+':'+wllistenport
	print('connecting to the url:'+ wlurl)

	try:
		connect(wlusr, wlpwd, wlurl)
		print('Successfully connected')
	except:
		print 'Unable to find admin server...'
		exit()
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
	wlsfileStream=java.io.FileInputStream('WLSProperties.py')
	wlproperties=java.util.Properties()
	wlproperties.load(wlsfileStream)	
	wlusr=wlproperties.getProperty('wlusr')
	wlpwd=wlproperties.getProperty('wlpwd')
	wllistenaddress=wlproperties.getProperty('wllistenaddress')
	wllistenport=wlproperties.getProperty('wllistenport')
