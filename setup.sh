sudo apt-get update --allow-releaseinfo-change
sudo apt-get upgrade -y
sudo apt-get install python3-dev python3-pip libffi-dev libssl-dev -y
sudo -H pip3 install --upgrade pip
sudo apt-get purge python3-pip
sudo -H pip3 install --upgrade luma.oled
sudo pip3 install smbus
sudo raspi-config -> Interfacing Options -> P4 SPI -> Yes -> OK -> Finish
sudo reboot now    (THEN WAIT and reconnect over SSH)
sudo apt-get install python3-numpy
sudo apt-get install libopenjp2-7
sudo apt install libtiff5

#sudo Python3 Demo