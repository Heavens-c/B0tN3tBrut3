#!/bin/bash

# Check if the script is being run with superuser privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root."
  exit 1
fi

# Update package repositories
apt update

# Install required dependencies
apt install -y build-essential cmake libgmp3-dev gengetopt libpcap-dev flex byacc libjson-c-dev pkg-config libunistring-dev

# Install ZMap from the default repository
apt install -y zmap

# Check if ZMap installation was successful
if [ $? -eq 0 ]; then
  echo "ZMap has been successfully installed."
  
  # Make the script executable
  chmod +x script_name.sh
else
  echo "ZMap installation failed."
fi
