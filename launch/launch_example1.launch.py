from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_status_monitor',
            executable='status_broadcaster_node',
            name='status_broadcaster'
        ),
        Node(
            package='robot_status_monitor',
            executable='status_logger_node',
            name='status_logger'
        ),
    ])