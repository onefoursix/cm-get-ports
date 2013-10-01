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
Download and untar the CM API Client on any machine that allows you to make HTTP calls to Cloudera Manager (the script can run remotely from the cluster):

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

The output might look something like this (note that non-default parts are flagged):

    # [root@brooklyn ~]# ./getPorts.py

    
    Connecting to Cloudera Manager at : http://brooklyn.onefoursix.com:7180

    FLUME Service (flume1)
    *****************************
    AGENT               agent.http.port                         brooklyn.onefoursix.com:41414           
    AGENT               agent.http.port                         brooklyn0.onefoursix.com:41414          
    AGENT               agent.http.port                         brooklyn1.onefoursix.com:41414   
    
    SOLR Service (solr1)
    *****************************
    SOLR_SERVER         solr.admin.port                         brooklyn.onefoursix.com:8984            
    SOLR_SERVER         solr.admin.port                         brooklyn0.onefoursix.com:8984           
    SOLR_SERVER         solr.admin.port                         brooklyn1.onefoursix.com:18984          (custom port)
    SOLR_SERVER         solr.http.port                          brooklyn.onefoursix.com:8983            
    SOLR_SERVER         solr.http.port                          brooklyn0.onefoursix.com:8983           
    SOLR_SERVER         solr.http.port                          brooklyn1.onefoursix.com:18983          (custom port)

    HIVE Service (hive-service)
    *****************************
    HIVEMETASTORE       hive.metastore.port                     brooklyn.onefoursix.com:9083            
    HIVESERVER2         hs2.thrift.address.port                 brooklyn.onefoursix.com:10000           
    WEBHCAT             hive.webhcat.address.port               brooklyn0.onefoursix.com:50111 
     
    ZOOKEEPER Service (zookeeper1)
    *****************************
    SERVER              server.jmx.agent.port                   brooklyn.onefoursix.com:9010            
    SERVER              server.jmx.agent.port                   brooklyn0.onefoursix.com:9010           
    SERVER              server.jmx.agent.port                   brooklyn1.onefoursix.com:9010           

    HDFS Service (hdfs1)
    *****************************
    DATANODE            dfs.datanode.http.port                  brooklyn.onefoursix.com:1006            (custom port)
    DATANODE            dfs.datanode.http.port                  brooklyn0.onefoursix.com:1006           (custom port)
    DATANODE            dfs.datanode.http.port                  brooklyn1.onefoursix.com:1006           (custom port)
    DATANODE            dfs.datanode.https.port                 brooklyn.onefoursix.com:50475           
    DATANODE            dfs.datanode.https.port                 brooklyn0.onefoursix.com:50475          
    DATANODE            dfs.datanode.https.port                 brooklyn1.onefoursix.com:50475          
    DATANODE            dfs.datanode.ipc.port                   brooklyn.onefoursix.com:50020           
    DATANODE            dfs.datanode.ipc.port                   brooklyn0.onefoursix.com:50020          
    DATANODE            dfs.datanode.ipc.port                   brooklyn1.onefoursix.com:50020          
    DATANODE            dfs.datanode.port                       brooklyn.onefoursix.com:1004            (custom port)
    DATANODE            dfs.datanode.port                       brooklyn0.onefoursix.com:1004           (custom port)
    DATANODE            dfs.datanode.port                       brooklyn1.onefoursix.com:1004           (custom port)
    HTTPFS              hdfs.httpfs.admin.port                  brooklyn.onefoursix.com:14001           
    HTTPFS              hdfs.httpfs.http.port                   brooklyn.onefoursix.com:14000           
    JOURNALNODE         dfs.journalnode.http.port               brooklyn.onefoursix.com:8480            
    JOURNALNODE         dfs.journalnode.http.port               brooklyn0.onefoursix.com:8480           
    JOURNALNODE         dfs.journalnode.http.port               brooklyn1.onefoursix.com:8480           
    JOURNALNODE         dfs.journalnode.rpc.port                brooklyn.onefoursix.com:8485            
    JOURNALNODE         dfs.journalnode.rpc.port                brooklyn0.onefoursix.com:8485           
    JOURNALNODE         dfs.journalnode.rpc.port                brooklyn1.onefoursix.com:8485           
    NAMENODE            dfs.http.port                           brooklyn0.onefoursix.com:50070          
    NAMENODE            dfs.http.port                           brooklyn1.onefoursix.com:50070          
    NAMENODE            dfs.https.port                          brooklyn0.onefoursix.com:50470          
    NAMENODE            dfs.https.port                          brooklyn1.onefoursix.com:50470          
    NAMENODE            namenode.port                           brooklyn0.onefoursix.com:8020           
    NAMENODE            namenode.port                           brooklyn1.onefoursix.com:8020           

    HBASE Service (hbase1)
    *****************************
    MASTER              hbase.master.info.port                  brooklyn.onefoursix.com:60010           
    MASTER              hbase.master.port                       brooklyn.onefoursix.com:60000           
    REGIONSERVER        hbase.regionserver.info.port            brooklyn.onefoursix.com:60030           
    REGIONSERVER        hbase.regionserver.info.port            brooklyn0.onefoursix.com:60030          
    REGIONSERVER        hbase.regionserver.info.port            brooklyn1.onefoursix.com:60030          
    REGIONSERVER        hbase.regionserver.port                 brooklyn.onefoursix.com:60020           
    REGIONSERVER        hbase.regionserver.port                 brooklyn0.onefoursix.com:60020          
    REGIONSERVER        hbase.regionserver.port                 brooklyn1.onefoursix.com:60020          

    MAPREDUCE Service (mapreduce1)
    *****************************
    JOBTRACKER          ha.job.tracker.port                                 brooklyn.onefoursix.com:8023            
    JOBTRACKER          job.tracker.port                                    brooklyn.onefoursix.com:8021            
    JOBTRACKER          mapred.job.tracker.http.port                        brooklyn.onefoursix.com:50030           
    JOBTRACKER          mapred.jobtracker.hue.thrift.plugin.port            brooklyn.onefoursix.com:9290            
    TASKTRACKER         mapred.tasktracker.instrumentation.cmon.jettyport   brooklyn.onefoursix.com:4867            
    TASKTRACKER         mapred.tasktracker.instrumentation.cmon.jettyport   brooklyn0.onefoursix.com:4867           
    TASKTRACKER         mapred.tasktracker.instrumentation.cmon.jettyport   brooklyn1.onefoursix.com:4867           
    TASKTRACKER         task.tracker.http.port                              brooklyn.onefoursix.com:50060           
    TASKTRACKER         task.tracker.http.port                              brooklyn0.onefoursix.com:50060          
    TASKTRACKER         task.tracker.http.port                              brooklyn1.onefoursix.com:50060          

     OOZIE Service (oozie1)
     *****************************
     OOZIE_SERVER        oozie.admin.port                        brooklyn.onefoursix.com:11001           
     OOZIE_SERVER        oozie.http.port                         brooklyn.onefoursix.com:11000           
     OOZIE_SERVER        oozie.https.port                        brooklyn.onefoursix.com:11443           

     HUE Service (hue1)
     *****************************
     BEESWAX_SERVER      beeswax.meta.server.port                brooklyn.onefoursix.com:8003            
     BEESWAX_SERVER      beeswax.server.port                     brooklyn.onefoursix.com:8002            
     HUE_SERVER          hue.http.port                           brooklyn.onefoursix.com:8888            

     IMPALA Service (impala-service)
     *****************************
     IMPALAD             be.port                                 brooklyn.onefoursix.com:22000           
     IMPALAD             be.port                                 brooklyn0.onefoursix.com:22000          
     IMPALAD             be.port                                 brooklyn1.onefoursix.com:22000          
     IMPALAD             beeswax.port                            brooklyn.onefoursix.com:21001           (custom port)
     IMPALAD             beeswax.port                            brooklyn0.onefoursix.com:21001          (custom port)
     IMPALAD             beeswax.port                            brooklyn1.onefoursix.com:21001          (custom port)
     IMPALAD             hs2.port                                brooklyn.onefoursix.com:21050           
     IMPALAD             hs2.port                                brooklyn0.onefoursix.com:21050          
     IMPALAD             hs2.port                                brooklyn1.onefoursix.com:21050          
     IMPALAD             impalad.webserver.port                  brooklyn.onefoursix.com:25000           
     IMPALAD             impalad.webserver.port                  brooklyn0.onefoursix.com:25000          
     IMPALAD             impalad.webserver.port                  brooklyn1.onefoursix.com:25000          
     IMPALAD             state.store.subscriber.port             brooklyn.onefoursix.com:23000           
     IMPALAD             state.store.subscriber.port             brooklyn0.onefoursix.com:23000          
     IMPALAD             state.store.subscriber.port             brooklyn1.onefoursix.com:23000          
     STATESTORE          state.store.port                        brooklyn.onefoursix.com:24000           
     STATESTORE          statestore.webserver.port               brooklyn.onefoursix.com:25010           

    
     
