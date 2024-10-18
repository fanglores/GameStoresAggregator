#!/bin/bash

# Add repository key
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv E0C56BD4

# Add ClickHouse repository
echo "deb http://repo.yandex.ru/clickhouse/deb/stable/main/" | sudo tee /etc/apt/sources.list.d/clickhouse.list

# Update packages list
sudo apt update -y

# Install ClickHouse (password for server will be prompted!)
sudo apt install -y clickhouse-server clickhouse-client

# Start the service (default port is 8123)
sudo service clickhouse-server start