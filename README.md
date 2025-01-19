# A simple tool to switch between 14.3:9 and 16:9 using Qres

- In all but the Qres.exe file there are changes needed (resolution, refresh rate, file path), however if you copy the extracted files to "C:\Tools\Windows\ResSwitcher" you will have to edit less
- Ensure that you have python installed, I used 3.13.1 and it works, it should be the latest version at time of writing
- Replace all [abc] with the information stated in the [], and ensure to not leave the [] in

-- For Normal.bat -- 

- Change "C:\Tools\Windows\ResSwitcher" to where you wish for these files to be stored
- Change the 2560 and 1440 to "qres.exe /x [YOUR NATIVE MONITOR WIDTH] /y [YOUR NATIVE MONITOR HEIGHT] /r [YOUR MONITORS REFRESH RATE]"

-- For Stretched.bat -- 

- Change "C:\Tools\Windows\ResSwitcher" to where you want these files to be stored
- Change the 2560 and 1440 to "qres.exe /x [(YOUR NATIVE MONITOR WIDTH) * (1720/1920)] /y [YOUR NATIVE MONITOR HEIGHT] /r [YOUR MONITORS REFRESH RATE]"

-- For Switcher.py -- 

- Change the "os.system("[xyz]")" to the correct locations for the files
- Change the "width != 2560" to "width != [YOUR NATIVE MONITOR WIDTH]"

Once done, create a shortcut from "Switcher.py", rename it to Res Switcher and move it to the desktop
