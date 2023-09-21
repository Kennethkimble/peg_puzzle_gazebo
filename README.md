# Pegboard Puzzle
ROS 2 Package for simulating the NIST pegboard assembly puzzle.

# Installation
The following instructions has been tested using an [althack Docker container](https://hub.docker.com/layers/althack/ros2/iron-cuda-gazebo-nvidia-2023-09-15/images/sha256-2a720812bcb19b4bcbd6b705ffb1b3dbcb2e4cd83d1cdc605c9c19db8abe2e77?context=explore), but should in-principle work on any system running Gazebo 11 Classic and ROS 2. The following instructions assume you will be using Docker with an NVIDIA GPU.

1. Install [Docker](https://docs.docker.com/engine/install/) and the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
2. Download a docker image with ROS2 and gazebo:
	```
	docker pull althack/ros2:iron-cuda-gazebo-nvidia-2023-09-15
 	```
	and run the container:
	```
	docker run -it \
	        -e DISPLAY=${DISPLAY} \
	        --privileged \
	        -v /tmp/.X11-unix:/tmp/.X11-unix \
	        --device=/dev/video0:/dev/video0 \
	        --runtime=nvidia \
	        --gpus all \
	        --network host \
	        --ipc=host althack/ros2:iron-cuda-gazebo-nvidia-2023-09-15
	```
4. Inside the container, clone [this](https://github.com/Pavel-P/odio_urdf) fork of [Odio URDF](https://github.com/hauptmech/odio_urdf), and install it with pip:
	```
	git clone https://github.com/Pavel-P/odio_urdf
	cd odio_urdf
	pip install -e .
	```
5. Create a colcon workspace containing this repository and build it:
	```
	mkdir -p /colcon_ws/src && cd /colcon_ws/src
	git clone https://github.com/Kennethkimble/peg_puzzle_gazebo.git
	cd .. && colcon build
	```
6. Launch Gazebo (using a ROS2 launch file to enable ROS spawning services):
	```
	ros2 launch peg_puzzle_gazebo gazebo.launch.py
	```
7. In a second shell, run the model spawning script inside the container:
	```
	docker exec -it bash <your-container-name>
	cd /colcon_ws/src/peg_puzzle_gazebo
	python3 peg_puzzle_gazebo/part_spawner.py
	```
8. To regenerate a new puzzle layout, generate a new URDF and update the Gazebo SDF:
	```
	python3 peg_puzzle_gazebo/generate_urdf.py
	bash peg_puzzle_gazebo/update_puzzle_sdf.bash
	```
9. In the first shell, rebuild the colcon workspace and re-launch Gazebo:
	```
	colcon build
	ros2 launch peg_puzzle_gazebo gazebo.launch.py
	```
