import subprocess

#check is used
lsProcess = subprocess.run(["ls"], stdout=subprocess.PIPE, text=True)
grepProcess = subprocess.Popen(["grep", "sample"], stdin=subprocess.PIPE,stdout=subprocess.PIPE, text=True)
output, error = grepProcess.communicate()

print("h"+output+"h")
