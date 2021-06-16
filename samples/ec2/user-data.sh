#!/bin/bash

sudo yum update -y
sudo amazon-linux-extras install nginx1 -y
sudo yum install aws-kinesis-agent -y

sudo service nginx start
sudo chkconfig nginx on
sudo service aws-kinesis-agent start
sudo chkconfig aws-kinesis-agent on