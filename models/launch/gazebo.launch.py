import os
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    OpaqueFunction,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Set the path to this package.
    package_path = get_package_share_directory("peg_puzzle_gazebo")
    
    # Set the path to the world file
    world_file_name = 'peg_puzzle.world'
    world_path = os.path.join(package_path, 'worlds', world_file_name)

    gazebo_models_path = os.path.join(package_path, 'models')
    os.environ["GAZEBO_MODEL_PATH"] = gazebo_models_path
    
    # Gazebo node
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [FindPackageShare("gazebo_ros"), "/launch", "/gazebo.launch.py"]
        ),
        launch_arguments={
            'world': world_path,
            }.items()
    )

    nodes_to_start = [
        gazebo,
    ]

    return LaunchDescription(nodes_to_start)