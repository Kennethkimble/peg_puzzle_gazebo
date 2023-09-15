# Goal: Generate a urdf file for the pegboard puzzle
# Configurable parameters:
#   Mesh dir path, mesh name-type mapping
#   in-plane link spacing
#   wall plane positions/orientations
# Interface:
#   create base (empty) pegboard walls (inputs: Config)
#   create filled wall (inputs: Config, Array of slot-type instances)

from odio_urdf import *
import peg_board as pb

config = {
        "mesh_dir_path": "model://puzzle/meshes/", #string
        "mesh_types_dict": {
            "HC":"highCircleHole.STL",
            "LC":"lowCircleHole.STL",
            "HS":"highSquareHole.STL",
            "LS":"lowSquareHole.STL",
            "HH":"highHexHole.STL",
            "LH":"lowHexHole.STL",
            },
        "mesh_scale": 1.0,                      #scalar
        "slot_spacing": 0.075,                  #scalar
        "slot_pattern_origin": [0,0],           #xy
        "left_wall_origin": [0.15,-0.037,0.387,-1.57,1.57,0.00],   #xyz rpy
        "right_wall_origin": [-0.037,0,0.387,0,1.57,0],  #xyz rpy
        "floor_origin": [0,0,0.2,0,0,0],          #xyz rpy
        "output_file": "/tmp/my_puzzle.urdf"
        }

def populate_plane(slots, parent_link):
    urdf_group = []
    for i, slot in enumerate(slots):
        pattern_origin = config['slot_pattern_origin']
        spacing = config['slot_spacing']
        pattern_index_x = int(i / 3)
        pattern_index_y = i % 3
        offset_x =  pattern_index_x * spacing
        offset_y =  pattern_index_y * spacing
        slot_origin = [pattern_origin[0] + offset_x, pattern_origin[1] + offset_y, 0, 1.57,0,0]
        mesh_name = config['mesh_dir_path'] + config['mesh_types_dict'][slot]
        slot_link =  Link(
            Inertial(
                Origin(slot_origin),
                Mass(value=1.0),
                Inertia([1.,1.,1.,1.,1.,1.,])),
            Visual(
                Origin(slot_origin),
                Geometry(Mesh(filename = mesh_name))),
            Collision(
                Origin(slot_origin),
                Geometry(Mesh(filename = mesh_name))),
        name = parent_link.name + "_slot_" + str(i))
        slot_joint = Joint(Parent(parent_link.name), Child(slot_link.name), Origin([0]*6), type="fixed")
        urdf_group += [slot_link, slot_joint]
    urdf(Group(*urdf_group))

if __name__ == "__main__":
    pegboard = pb.Pegboard()

    urdf = Robot('pegboard_puzzle')
    base = Link('base_link')
    lw = Link('left_wall')
    rw = Link('right_wall')
    fl = Link('floor')

    jbl = Joint(Parent(base.name), Child(lw.name), Origin(config['left_wall_origin']), type="fixed")
    jbr = Joint(Parent(base.name), Child(rw.name), Origin(config['right_wall_origin']), type="fixed")
    jbf = Joint(Parent(base.name), Child(fl.name), Origin(config['floor_origin']), type="fixed")
    
    urdf(base, lw, rw, fl)
    urdf(jbl, jbr, jbf)

    populate_plane(pegboard.to_dict()['LEFT'], lw)
    populate_plane(pegboard.to_dict()['RIGHT'], rw)
    populate_plane(pegboard.to_dict()['BASE'], fl)

    pegboard.print_board(pegboard.planes)

    with open(config['output_file'], 'w') as f:
        f.write(str(urdf))
