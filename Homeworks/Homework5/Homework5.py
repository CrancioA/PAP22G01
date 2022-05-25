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
from subprocess import Popen
import os


class GetPythonInfo:

    def first_method(self):
        result = Popen(['powershell', '-c', r"Invoke-WebRequest -Uri 'https://en.wikipedia.org/wiki/History_of_Python"
                                            r"' -OutFile 'D:\02_Adi\02_Curs "
                                            r"python\PAP22G01\Homeworks\Homework5\page.html'"])
        print(result)

    def second_method(self):
        result = Popen(['powershell', '-c', r"Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.10.4/python"
                                            r"-3.10.4-amd64.exe' -OutFile "
                                            r"'D:\02_Adi\02_Curs "
                                            r"python\PAP22G01\Homeworks\Homework5\python-3.10"
                                            r".4-amd64.exe'"])
        # stdout, stderr = result.communicate()
        # print(stdout, stderr)
        print(result)

    def third_method(self):
        result = os.popen('python --version')
        print(result.readline())


obj = GetPythonInfo()
print("First method: ")
obj.first_method()
print("Second method: ")
obj.second_method()
print("Third method: ")
obj.third_method()
