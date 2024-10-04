from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='path_planner_server',
            executable='Nav_To_Pose_Action_Client',
            output='screen'),
    ])