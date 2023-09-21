#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

gz sdf -p /tmp/my_puzzle.urdf > $SCRIPT_DIR/../models/puzzle/model.sdf
