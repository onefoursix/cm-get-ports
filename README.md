cm-get-ports
==================

A Python script that retrieves Service Port info from Cloudera Manager




####Requirements
- Cloudera Manager 4.1 or higher (I tested with CM 4.5.2) with a configured HDFS Service. 
- CM login with Administrator privileges
- CDH 4.1 or higher (I tested with CDH 4.2.1)
- Python (I tested on CentOS 6.4 which includes Python 2.6.6)
- Python setuptools (see below)
- CM API must be installed (see below)


####Install Python setuptools
On CentOS:

    # yum -y install python-setuptools


####Download and Install the Cloudera Manager API Client
Download the CM API Client:

    # wget https://github.com/cloudera/cm_api/tarball/master
    # tar -xvf master

This will give you a dir named something like <code>cloudera-cm_api-1f8dd19<code>

Change to the cm-api's python directory and install the CM-API module (see the README and SHELL_README for additional details):

    # cd cloudera-cm_api-1f8dd19/python
    # python setup.py install

