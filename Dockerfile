FROM linuxserver/rdesktop:ubuntu-xfce-version-8e125ca8

RUN apt update && apt install locales && \
locale-gen en_US en_US.UTF-8 && \
update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
export LANG=en_US.UTF-8

RUN apt install -y software-properties-common
RUN add-apt-repository universe
RUN apt update && apt install -y curl -y
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null
RUN apt update && apt upgrade -y

RUN apt install -y ros-humble-ros-base
RUN apt install -y ros-humble-examples-rclcpp-minimal-subscriber ros-humble-examples-rclcpp-minimal-publisher 
#RUN source /opt/ros/humble/setup.bash
RUN apt install -y python3-rosdep
RUN rosdep init && rosdep update
RUN apt install -y ros-humble-rmw-cyclonedds-cpp ros-humble-rmw-fastrtps-cpp
RUN apt install -y ros-humble-desktop
RUN apt install -y \
  build-essential \
  cmake \
  git \
  python3-colcon-common-extensions \
  python3-flake8 \
  python3-pip \
  python3-pytest-cov \
  python3-rosdep \
  python3-setuptools \
  python3-vcstool \
  nano \
  wget
  
RUN rosdep update

# extra stuff for andrew's tutorial
# RUN apt install -y \
  #   ros-humble-joint-state-publisher ros-humble-joint-state-publisher-gui  

# RUN echo "export ROS_DOMAIN_ID=0" >> /root/.bashrc && \
# echo "export ROS_LOCALHOST_ONLY=0" >> /root/.bashrc && \
# echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

# RUN apt update && apt install ros-humble-ur -y
# EXPOSE 50002
# RUN apt install -y ros-humble-ros2controlcli

