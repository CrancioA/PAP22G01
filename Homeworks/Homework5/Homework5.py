"""
Create a class for an object that implement three methods.

- first method gets the latest stable version of python by downloading and looking in the content of this page:
https://en.wikipedia.org/wiki/History_of_Python To download the page try using the following command for windows
powershell -c "Invoke-WebRequest -Uri 'https://en.wikipedia.org/wiki/History_of_Python' -OutFile 'C:\temp\page.html'"
or curl, wget, or some other tools you may have in case of mac.

- the second method downloads the latest version of python and starts the installer no installation steps are
required just start the downloaded executable file

- compare the retrieved version with the first 2 digits of your installed version and show a message to the user with
current and available version.
you can get the python version by using the command python3 --version
"""
import subprocess
from subprocess import Popen
from time import sleep

class GetPythonInfo:

    def first_method(self):
        result = Popen(['powershell', '-c', r"Invoke-WebRequest -Uri 'https://en.wikipedia.org/wiki/History_of_Python"
                                            r"'-OutFile 'D:\02_Adi\02_Curs "
                                            r"python/PAP22G01/Homeworks/Homework5/page.html'"], text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        print(stdout, stderr)
        print(result)


    def second_method(self):
        result = Popen(['powershell', '-c', r"https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe'"
                        r"-OutFile 'D:\02_Adi\02_Curs"
                        r"python/PAP22G01/Homeworks/Homework5/python-3.10.4-amd64.exe'"], text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # stdout, stderr = result.communicate()
        # print(stdout, stderr)
        # print(result)
        result1 = Popen([r"D:\02_Adi\02_Curs python\PAP22G01\Homeworks\Homework5\python-3.10.4-amd64.exe"], text=True, stderr=subprocess.PIPE)

        # result1.communicate(b'Cancel')
        # result1.terminate()
        # sleep(1)
        # result.communicate(b'Yes')


    def third_method(self):
        result = Popen(['cmd', 'python --version' ],shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result)


obj = GetPythonInfo()
# obj.first_method()
# obj.second_method()
obj.third_method()
