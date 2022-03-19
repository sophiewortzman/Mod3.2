#Setup for Gazebo code

#Open Xlaunch, disable "Native opengl" and enable "Disable access control".

#Open Ubuntu and paste the following by right clicking in the terminal. 
roslaunch simulation gazebo.launch

#Enter the following into a separate terminal from the one used to launch gazebo.
git clone https://github.com/sophiewortzman/Mod3.2.git
cd ~/Mod3.2

#When ready, run the following code in the Ubuntu terminal that is not running git hub. After you have run the second line of code, hit the play button in gazebo.
git pull
python Test.py

#For testing of a different file, replace "Test.py" with the file name you are trying to run.
#After updating code in the repository, run the "git pull" command to sync the files in Ubuntu.
