import pyautogui
import sys

def show_reminder():
    reminders = "1. Check Plan of Attack list\n2.Check to-do list \n3. Journal ( if you haven't)\n4. Find somethiing Simple to do today\n5. Drink Water\n6. You will never do what Musk can if you're distracted, if you're emotionally weak, lack disiplinne, and don't FINSIH WHAT YOU START" 
    pyautogui.alert(text=reminders, title='Reminder', button='OK')
    sys.exit()  # This ensures the script exits after the OK button is pressed

if __name__ == "__main__":
    show_reminder()


    
