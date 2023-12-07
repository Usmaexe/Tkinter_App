import subprocess

def open(event,frame,file):
    try :
        subprocess.Popen(["start",file],shell=True)
    except Exception as e:
        print(f"Error: {e}")
    
