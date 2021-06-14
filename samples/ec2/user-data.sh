#!/bin/bash

yum update
yum install nginx

service nginx start
chkconfig nginx on