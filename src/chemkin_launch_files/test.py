from subprocess import Popen
import time
# from shutil import copyfile
# import os.path

def main():
    time.sleep(2)
    calcul = Popen("job2.sh")
    Popen.wait(calcul, timeout=None)

if __name__ == "__main__":
    main()