# Advanced-Keylogger-in-Python

Important Disclaimer: The author will not be held responsible for the abuse of this program. This is only intended for educational purposes.

## How to use:

1) Install Python version 3 on your computer from https://python.org. Make sure you install the pip package manager (it should be an option that the Python installer gives).
2) Download the file and open it up in a text editor.
3) Change `YOUREMAIL@gmail.com` and `YOURPASSWORD` to your preferred email/password that you want the keylogger to email the keylogs to. 
4) You can change `self.emailInterval` to the interval the keylogger should send the email with keylogs (in seconds). It is currently set to 3600 seconds which is 1 hour.
5) You can also change the name of the file that contains the keylogs. By default, it is called "keylogs.txt".
6) At this point, you can run the keylogger program as a python program `.py`
7) If you want to convert this to an executable file that can be run on any computer with Windows Operating System, check out: https://stackoverflow.com/questions/41570359/how-can-i-convert-a-py-to-exe-for-python

## Features:

1) Automatically stores keylogs with date and time to `keylogs.txt` file.
2) Automatically emails the keylogs file to the specified email with SMTPLIB and TLS encryption and exception handling.

![image](https://user-images.githubusercontent.com/76885647/151258322-f3d1792e-7a4f-462f-b795-9330a092172c.png)



# MORE FEATURES TO COME SOME, INCLUDING:

1) Automatically exceute on computer startup
2) Screen Recording and Clipboard Logging
3) Support for other email service providers
