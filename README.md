# is_control
This is a ROS indigo package for controlling the pioneer and communicating with the vision module. I developed this package as a part of my independent study with Marcello Balduccini.

Dependency
-----------
This ros package depends on the is_vision package which can be found [here](https://github.com/RyanYoung25/is_vision).

Install
-------------
To install this ros package simply place in the source folder in your catkin workspace, ususally found ~/catkin_ws/src/ then update your catkin settings by sourcing the bash script catkin_ws/devel/setup.bash then finally make the package using catkin_make at the toplevel catkin_ws directory. 

This package will not build unless the is_vision ros package is also in your catkin workspace. 

