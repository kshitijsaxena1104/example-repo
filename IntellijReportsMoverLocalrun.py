import random
import shutil


def intellijreports():
    sourceLocation = r'D:\Github\CucumberUIAutomation\com.CFrame\src\test\java\testresult\cucumber-report\index.html'
    DestinationLocation = r'C:\Users\Kshitij.Saxena\Desktop\NReports\Intellijreportfile' + str(
        random.randint(1, 100)) + ".html"
    shutil.copy(sourceLocation, DestinationLocation)

# # Below is for P1 Report when run
def Gitnewautomationui():
    sourceLocation1 = r'D:\GITOLATESTUIAUTOMATION\GITOUILatestcom.CFrame\src\test\java\testresult\cucumber-report\index.html'
    DestinationLocation1 = r'C:\Users\Kshitij.Saxena\Desktop\NReports\GITNEWAUTOMATIONUIreportfile' + str(
        random.randint(1, 100)) + ".html"
    shutil.copy(sourceLocation1, DestinationLocation1)

intellijreports()
#Gitnewautomationui()