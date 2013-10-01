cm-get-ports
==================

A Python script that retrieves Service URL info from Cloudera Manager.

A bit of a hack; the script simply walks through all service roles and prints a line for each configuration property that has the string "port" in its property name.

For more information see: [Cloudera Manager](http://www.cloudera.com/content/cloudera/en/products/cloudera-manager.html), [CM API Client](http://cloudera.github.io/cm_api/)





####Requirements
- Cloudera Manager 4.5 or higher (I'm guessing about that; I tested with CM 4.7.1) 
- CM login with Administrator privileges
- Python (I tested on CentOS 6.4 which includes Python 2.6.6)
- Python setuptools (see below)
- CM API must be installed (see below)


####Install Python setuptools
On CentOS:

    # yum -y install python-setuptools


####Download and Install the Cloudera Manager API Client
Download the CM API Client on any machine that allows you to make HTTP calls to Cloudera Manager (the script can run remotely from the cluster):

    # wget https://github.com/cloudera/cm_api/tarball/master
    # tar -xvf master

This will give you a dir named something like <code>cloudera-cm_api-8dea57a<code>

Change to the cm-api's python directory and install the CM-API module (see the README and SHELL_README for additional details):

    # cd cloudera-cm_api-8dea57a/python
    # python setup.py install


####Set Cloudera Manager Connection Settings

Edit the file getPorts.py.  Set the following:
- cm_host
- cm_port
- cm_login
- cm_password
- cluster_name


####Run the script

    # getPorts.py

The output 




