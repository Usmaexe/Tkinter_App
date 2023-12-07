import subprocess 

#check is used
lsProcess = subprocess.run(["ls"], stdout=subprocess.PIPE, text=True)
grepProcess = subprocess.Popen( 
	["grep", "sample"], stdin=lsProcess.stdout,
	stdout=subprocess.PIPE, text=True) 
output, error = grepProcess.communicate() 

print(output) 
print(error) 
