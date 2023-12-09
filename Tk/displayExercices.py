import subprocess
import regex
def open(event,frame,file):
    print(file)
    try :
        #the "" argument is necessary to allow the files that contain backspaces to open
        subprocess.Popen(["start", "" ,file],shell=True)
    except Exception as e:
        print(f"Error: {e}")
    
