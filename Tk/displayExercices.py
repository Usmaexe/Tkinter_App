import subprocess
def CryptageExo1(event, frame):
    file_path = "TP2-Cryptographie/LettreOcc(6).py"
    try:
        #the Popen method is a low level interface for running subprocess
        #it allows you to create a subproces from the existing one and interact with its I/O and ERRORS
        subprocess.Popen(["start", "", file_path], shell=True)
        #shell set to true so the entire command is passed to the system's SHELL
    except Exception as e:
        print(f"Error: {e}")


def CryptageExo2(event, frame):
    print("hello 2")


def CryptageExo3(event, frame):
    print("hello 3")