# Appium Demo
1.Need to install:<br>
Python (add to env) <br> 
Appium Desktop (add to env)<br> if you won't app you can install by nodejs _npm install -g appium_
Appium Inspector <br>
Android Studio <br>
Java JDK (add to env) <br>
Pycharm (add to env) <br>

2.In AS -> pip install Appium-Python-Client
# Start
0. Run Emulator PIXEL 3 XL API 22 on Android Studio
1. Run Appium server GUI -> Settings -> 
1st ANDROID_HOME == C:\Users\user\AppData\Local\Android\Sdk\ <br>
2nd JAVA_HOME == C:\tools\jdk\jdk-version  (in my destination)
2. Save and restart
3. hostname 0.0.0.0:4723 == localhost (127.0.0.1:4723) -> startServer
4. Run Appium inspector
Remote Host = localhost:4723
Remote Path = /wd/hub
JSON = {
   "appPackage": "com.code2lead.kwad",
   "appActivity": "com.code2lead.kwad.MainActivity",
   "platformName": "Android",
   "deviceName": "Pixel"
   }
start session -> DONE