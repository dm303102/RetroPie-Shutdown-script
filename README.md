# Retropie python shutdown script
Filename: shutdown_pi.py

Description: This script will allow you to press a RESET button attached to the Pi board to safetly shutdown if RetroPie freezes. This avoids corrupting the SD card.

Installation:
1. SSH to Linux Pi
2. Enter cd ~
3. Use Winscp to upload shutdown.py or use git at the SSH terminal with the command:
git clone https://github.com/dm303102/Retropie.git
4. Enter sudo vi /etc/rc.local 
5. Scroll to 1 line before the #fi at the end of the file(with j)
6. Add the text below(with a):
sudo python /home/pi/shutdown_pi.py &
7. Press Esc Esc :wq to save and quit

Usage:
While RetroPie is running, hold the right RESET button on the game console for 2 to 4 seconds to restart the console; THE LIGHT WILL BLINK RAPIDLY. If this fails, holding the buttons for more than 4 seconds will issue a HARD SHUTDOWN command; THE LIGHT WILL BLINK SLOWLY. Once all the light on the board are off. It is safe to press the power button.
