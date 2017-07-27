# Retropie
Retropie custom scripts and utilities

shutdown_pi.py
Description: This script will allow you to press a RESET button attached to the Pi board to safetly shutdown if RetroPie freezes. This avoids corrupting the SD card. The script also repairs the SD card with every HARD SHUTDOWN.

Installation:

SSH
To Login to the Linux kernel, with the Raspberry Pi connected to your network,
1. Download putty: https://the.earth.li/~sgtatham/putty/latest/x86/putty.exe
2. Enter Retropie as the HostName
3. Click Open
4. If prompted, Click Yes
5. Login with Username: pi and Password: root

cd ~

sudo nano /etc/rc.local  

Usage:
While RetroPie is running, hold the right RESET button on the game console for 2 to 4 seconds to restart the console; THE LIGHT WILL BLINK RAPIDLY. If this fails, holding the buttons for more than 4 seconds will issue a HARD SHUTDOWN command; THE LIGHT WILL BLINK SLOWLY. Once all the light on the board are off. It is safe to press the power button.
