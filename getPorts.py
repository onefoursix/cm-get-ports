#!/usr/bin/python

## ********************************************************************************
## getPorts.py 
## 
## Example of how to retrieve Service ports using cm-api v6 for CM v5.0
##
## Usage: getPorts.py 
## 
##        (set CM connection properties in the script)
## 
## ********************************************************************************


## ** imports *******************************

import sys
from cm_api.api_client import ApiResource


##  ** CM Connection Settings ******************************

## Cloudera Manager Host and Port
cm_host = "localhost"
cm_port = "7180"

## Cloudera Manager login
cm_login = "admin"

## Cloudera Manager password
cm_password = "admin"

## Cluster Name
cluster_name = "Cluster 1"



## ** function defs ***************************

def getHostNameForHostId(api, hostId):

  for host in api.get_all_hosts():
    if host.hostId == hostId:
      return host.hostname
  return "hostname not found for hostId: " + hostId


def getRoleURLs(role):
  
  list = []
  config = role.get_config('full')

  for property_name in config:
  
    if "port" in property_name: 
      port = config[property_name].value
      if port == None:
        custom_port = False
        port = config[property_name].default
      else:
        custom_port = True

      hostname = getHostNameForHostId(api, role.hostRef.hostId)

      url = hostname + ":" + port
      property_name = property_name.replace('_', '.')
      item = role.type.ljust(20) + property_name.ljust(55) + url.ljust(40)
      if custom_port:
        item = item + "(custom port)"
      list.append(item)   
  return list   


## ** Connect to CM ***************************

print ""
print "Connecting to Cloudera Manager at : http://" + cm_host + ":" + cm_port
print ""
api = ApiResource(server_host=cm_host, server_port=cm_port, username=cm_login, password=cm_password)
cluster = api.get_cluster(cluster_name)


for service in cluster.get_all_services():

  print service.type + " Service " + "(" + service.displayName + ")"
  print "*****************************"
  list = []
  for role in service.get_all_roles():
    for url in getRoleURLs(role):
      list.append(url)
  list.sort()
  for item in list:
    print item
  print ""    
print ""
