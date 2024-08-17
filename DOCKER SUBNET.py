#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Created on Fri Aug 16 22:37:14 2024


#!/bin/bash

# Set the name of the network
NETWORK_NAME="mynetwork"

# Create a new network with a custom subnet if it doesn't exist
if [ ! $(docker network ls -q | grep $NETWORK_NAME) ]; then
  docker network create --subnet=192.168.1.0/24 $NETWORK_NAME
fi

# List all containers and their IP addresses
echo "Containers and their IP addresses:"
docker ps -aq --format="{{.Names}} {{range .NetworkSettings.Networks}}{{.IPAddress}}/{{.Gateway}}{{end}}"

# Connect a new container to the network
docker run -it --net $NETWORK_NAME --ip 192.168.1.100 myimage

# Disconnect a container from the network
docker network disconnect $NETWORK_NAME mycontainer

# Stop and restart a container with a new IP address
docker stop mycontainer
docker run -it --net $NETWORK_NAME --ip 192.168.1.200 myimage

# List all containers and their IP addresses again to see the changes
echo "Containers and their IP addresses after changes:"
docker ps -aq --format="{{.Names}} {{range .NetworkSettings.Networks}}{{.IPAddress}}/{{.Gateway}}{{end}}"