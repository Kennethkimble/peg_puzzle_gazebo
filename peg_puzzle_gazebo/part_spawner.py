#!/usr/bin/env python3

import os
import rclpy
from rclpy.node import Node

from gazebo_msgs.srv import SpawnEntity
from peg_puzzle_gazebo.spawn_params import SpawnParams

from ament_index_python.packages import get_package_share_directory

import json
import numpy

class PartSpawner(Node):
    def __init__(self):
        super().__init__('part_spawner')
        
        # Create service client to spawn objects into gazebo
        self.spawn_client = self.create_client(SpawnEntity, '/spawn_entity')
        self.peg_cnt = 0
            
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

    def spawn_hex(self, xyz, rf='') -> bool:
        path = os.path.join(get_package_share_directory("peg_puzzle_gazebo"), 'models', 'hex_peg', 'model.sdf')
        params = SpawnParams('hex_peg' + str(self.peg_cnt), path, xyz=xyz, rf=rf)
        self.peg_cnt+=1
        return self.spawn_entity(params)

    def spawn_circle(self, xyz, rf='') -> bool:
        path = os.path.join(get_package_share_directory("peg_puzzle_gazebo"), 'models', 'circle_peg', 'model.sdf')
        params = SpawnParams('circle_peg' + str(self.peg_cnt), path, xyz=xyz, rf=rf)
        self.peg_cnt+=1
        return self.spawn_entity(params)

    def spawn_square(self, xyz, rf='') -> bool:
        path = os.path.join(get_package_share_directory("peg_puzzle_gazebo"), 'models', 'square_peg', 'model.sdf')
        params = SpawnParams('square_peg' + str(self.peg_cnt), path, xyz=xyz, rf=rf)
        self.peg_cnt+=1
        return self.spawn_entity(params)

    def populate_puzzle(self):
        with open('/tmp/my_puzzle.json', 'r') as f:
            puzzle_state = json.load(f)

        spacing = 0.075
        for k,v in puzzle_state.items():
            if k == "LEFT":
                rf = "left_wall"
            if k == "RIGHT":
                rf = "right_wall"
            if k == "BASE":
                rf = "floor"
            for i,s in enumerate(v):
                x = int(i / 3)
                y = i % 3
                if s[0] == "H":
                    z = -0.15
                else:
                    z = -0.19
                xyz = [x * spacing, y * spacing, z]
                if s[1] == "C":
                    self.spawn_circle(xyz, rf=rf)
                if s[1] == "S":
                    self.spawn_square(xyz, rf=rf)
                if s[1] == "H":
                    self.spawn_hex(xyz, rf=rf)

def main():
    rclpy.init()

    spawner = PartSpawner()

    spawner.spawn_puzzle([0,0,0])
    spawner.populate_puzzle()
    spawner.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
    
