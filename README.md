Filename: shutdown_pi.py

Description: This script will allow you to press a RESET button attached to the Pi board to safetly shutdown if RetroPie freezes. This avoids corrupting the SD card.

Installation:
1. SSH to Linux Pi
2. Enter cd ~
3. Install RPI.GPIO with command

      sudo apt-get install python-dev python-rpi.gpio
      
4. Use Winscp to upload shutdown.py or use git at the SSH terminal with the command:

      git clone https://github.com/dm303102/Retropie.git

5. Enter sudo vi /etc/rc.local 
6. Scroll to 1 line before the #fi at the end of the file(with j)
7. Add the text below(with a):
sudo python /home/pi/shutdown_pi.py &
8. Press Esc Esc :wq to save and quit

If you ever have issues with corrupt SD cards, you can try to enable auto-repair every restart with:

1. cd /
2. sudo touch /forcefsck
3. sudo reboot

OR

1. sudo tune2fs -c 1 /dev/mmcblk0p2

Usage:
While RetroPie is running, hold the right RESET button on the game console for 2 to 4 seconds to restart the console; THE LIGHT WILL BLINK RAPIDLY. If this fails, holding the buttons for more than 4 seconds will issue a HARD SHUTDOWN command; THE LIGHT WILL BLINK SLOWLY. Once all the light on the board are off. It is safe to press the power button.
