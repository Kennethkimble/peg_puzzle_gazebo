#!/usr/bin/env python3

import os
import rclpy
from rclpy.node import Node

from gazebo_msgs.srv import SpawnEntity
from peg_puzzle_gazebo.spawn_params import SpawnParams

from ament_index_python.packages import get_package_share_directory

class HoleSpawner(Node):
    def __init__(self):
        super().__init__('part_spawner')
        
        # Create service client to spawn objects into gazebo
        self.spawn_client = self.create_client(SpawnEntity, '/spawn_entity')
            
    def spawn_entity(self, params: SpawnParams) -> bool:
        self.spawn_client.wait_for_service()

        self.get_logger().info(f'Spawning: {params.name}')

        req = SpawnEntity.Request()

        req.name = params.name
        req.xml = params.xml
        req.initial_pose = params.initial_pose
        req.robot_namespace = params.robot_namespace
        req.reference_frame = params.reference_frame

        future = self.spawn_client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        
        return future.result().success


def main():
    rclpy.init()

    spawner = HoleSpawner()

    path = os.path.join(get_package_share_directory("peg_puzzle_gazebo"), 'models', 'high_circ_hole', 'model.sdf')

    params = SpawnParams('high_circ_hole', path, xyz=[0, 0, .1])

    spawner.spawn_entity(params)

    spawner.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
    