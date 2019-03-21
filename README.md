# Whatsapp-Post-Python
This is a python project to send a whatsapp message.

It consist of two python files:
1. whatsapp.py :
                This is a primary code to get idea about how the program will work. After running this first you have to scan the QR code. Then enter the user/group
                name to which you wants to send the message.Then enter the message and then enter how many times you wants to send the same message. Press Enter this will send the
                message to specified user.
2. multi_user.py :
                This is the updated code. With the help of this we can send multiple messages to multiple users/groups for multiple times by scanning QR code only 
                once. After running the code first scan the QR code. Then it will ask for name of user or group, enter the user or group name to which you wants to send 
                the message. Then it will ask "Do you wants to add another user?" if you wants to add another user then press 1 else press 0. If you press 1
                it will ask for user name and it will continue till you press 1. If you press 0 it will ask to enter the message. Enter the message, now it will
                send the message to users you specified, if user name not found it will specify that the user name you entered is not found. Then it wiil ask
                "Do you wants to send another message?" if you wants to send message press 1 else press 0. If you press 1, it will ask for message and it will continue
                till you press 1. If you press 0 it will send the message and ask "Do you wants to use this again?" if you wants to send the message to another
                users then press 1, it will ask for user/group name and again same procedure as above. If you don't wants to use this program press 0, it will
                exit from program.
