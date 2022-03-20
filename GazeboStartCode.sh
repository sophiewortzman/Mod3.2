#Setup for Gazebo code

#Open Xlaunch, enable "start no client", disable "Native opengl" and enable "Disable access control".
#Open Ubuntu and paste the following by right clicking in the terminal.
#To test xeyes, past the following into the terminal before launching gazebo.

echo 'export LIBGL_ALWAYS_INDIRECT=0' >> ~/.bashrc
echo "export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0" >> ~/.bashrc
source ~/.bashrc

sudo apt update
sudo apt install x11-apps
xeyes
#close xeyes

roslaunch simulation gazebo.launch


#Enter the following into a separate terminal from the one used to launch gazebo.

git clone https://github.com/sophiewortzman/Mod3.2.git
cd ~/Mod3.2


#When ready, run the following code in the Ubuntu terminal that is not running git hub. 
#Right after you have run the second line of code, hit the play button in gazebo.

git pull
python Test.py


#For testing of a different file, replace "Test.py" with the file name you are trying to run.
#After updating code in the repository, run the "git pull" command to sync the files in Ubuntu.
