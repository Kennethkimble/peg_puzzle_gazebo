#!/usr/bin/env python3

from peg_puzzle_gazebo.utilities import pose_info

class SpawnParams:
    def __init__(self, name, file_path=None, xyz=[0,0,0], rpy=[0,0,0], ns='', rf=''):
        self.name = name
        self.initial_pose = pose_info(xyz, rpy)
        self.robot_namespace = ns
        self.reference_frame = rf

        self.xml = self.get_sdf(file_path)

    
    def get_sdf(self, file_path: str) -> str:
        try:
            f = open(file_path, 'r')
            entity_xml = f.read()
        except IOError:
            return ''
        
        return entity_xml