#>>>>>>>>>>>>>IMPORTS<<<<<<<<<<<<<<<<<<<<<
import pyautogui
import webbrowser
from time import sleep
#>>>>>>>>>>>>FUNCTIONS<<<<<<<<<<<<<<<<<<<<<
def SndSms(Target_link,No_of_sms,message):
    webbrowser.open(Target_link)
    sleep(40)
    i = 1
    for i in range(No_of_sms):
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        i += 1
#>>>>>>>>>>>>>>>>>>>>>USAGE<<<<<<<<<<<<<<<<<
message = input('enter the message you want to snd: ')
link = "https://web.whatsapp.com/"
NO_OF_SMS = int(input("how many messages you want to snd: "))
SndSms(link,NO_OF_SMS,message)