#!/usr/bin/env python3

import os
import rclpy
from rclpy.node import Node

from gazebo_msgs.srv import SpawnEntity
from peg_puzzle_gazebo.spawn_params import SpawnParams

from ament_index_python.packages import get_package_share_directory

class PartSpawner(Node):
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

    def spawn_puzzle(self, xyz) -> bool:
        path = os.path.join(get_package_share_directory("peg_puzzle_gazebo"), 'models', 'puzzle', 'model.sdf')
        params = SpawnParams('puzzle', path, xyz=xyz)
        return self.spawn_entity(params)

    def spawn_hex(self, xyz) -> bool:
        path = os.path.join(get_package_share_directory("peg_puzzle_gazebo"), 'models', 'hex_peg', 'model.sdf')
        params = SpawnParams('hex_peg', path, xyz=xyz)
        return self.spawn_entity(params)

    def spawn_circle(self, xyz) -> bool:
        path = os.path.join(get_package_share_directory("peg_puzzle_gazebo"), 'models', 'circle_peg', 'model.sdf')
        params = SpawnParams('circle_peg', path, xyz=xyz)
        return self.spawn_entity(params)

    def spawn_square(self, xyz) -> bool:
        path = os.path.join(get_package_share_directory("peg_puzzle_gazebo"), 'models', 'square_peg', 'model.sdf')
        params = SpawnParams('square_peg', path, xyz=xyz)
        return self.spawn_entity(params)


def main():
    rclpy.init()

    spawner = PartSpawner()

    spawner.spawn_puzzle([0,0,0])
    spawner.spawn_hex([0.4,-0.05,0])
    spawner.spawn_circle([0.4,0,0])
    spawner.spawn_square([0.4,0.05,0])

    spawner.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
    
