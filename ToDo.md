# Add another contributor
username: spurihwr

# Schedule meeting
Schedule meeting with Saurabh and Praveen on Saturday at 9:00 pm CET.
Invite using below gmail ids:

```
kulprav1986@gmail.com
spurihwr@gmail.com
```

# GIT related
Create a feature branch named "feature/self-driving-car". Below are some of commands (in command line) that will help you do that
```
git branch <feature-branch-name>
git checkout <feature-branch-name>
git push ...
```

# Link to material
Look at ipynb file located at 
"https://github.com/Vinohith/Self_Driving_Car_specialization/blob/master/Introduction_to_Self-Driving_Cars/Week_4/Longitudinal_Vehicle_Model.ipynb"

Understand the code and run the `ipynb` file at your end. You have to install `ipython notebook` to run ipynb binary files.


# Install Robot Operating System (ROS)
Follow the tutorial in "http://wiki.ros.org/ROS/Tutorials"

# Main Tasks

## Create a rosnode "logitudinal_dynamic_model"

Rosnode "logitudinal_dynamic_model" subscribe to rosmessage containing following data:
```
throttle (float32) # accelarator pedel position (in radians)
alpha  (float32)  # road inclination in randians.
```
The rosnode outputs below rosmessage after processing above data
```
x (float 32) # position in x coordinate (currently one dimentional)
v (float32)  # translational velocity
a (float32) # angular accelaration
w_e (float32) # rotational velocity/angular velocity
w_e_dot (float32) # 