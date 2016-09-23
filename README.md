# Dataset_for_Test

Dataset_test.csv -- Modified Tweets Data

schema.xml -- For Solr

log4j.properties, morphlines.conf, morphline-hbase-mapper.xml -- For LilyIndexer

#Indexing Data (Important Steps)

1 -- Import Data into HDFS and HBase

[cloudera@quickstart ~]$ hadoop fs -put Dataset_test.csv

[cloudera@quickstart ~]$ hbase shell

hbase(main):001:0> create 'test', 'raw_cf'

[cloudera@quickstart ~]$ hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator=,  -Dimporttsv.columns="HBASE_ROW_KEY,raw_cf:c1,raw_cf:c2,raw_cf:c3,raw_cf:c4,raw_cf:c5,raw_cf:c6,raw_cf:c7,raw_cf:c8,raw_cf:c9,raw_cf:c10,raw_cf:c11,raw_cf:c21" test Dataset_test.csv

2 -- Create Solr Collection

[cloudera@quickstart ~]$ solrctl instancedir --generate $HOME/datatest_collection

Replace the default schema.xml with this one

[cloudera@quickstart ~]$ solrctl instancedir --create datatest_collection $HOME/datatest_collection

[cloudera@quickstart ~]$ solrctl collection --create datatest_collection

3 -- Morphline

Copy log4j.properties, morphlines.conf and morphline-hbase-mapper.xml to your local directory.

4 -- LilyIndexer

For Virtual Cloudera

[cloudera@quickstart ~]$ hadoop --config /etc/hadoop/conf jar /usr/lib/hbase-solr/tools/hbase-indexer-mr-*-job.jar --conf /etc/hbase/conf/hbase-site.xml -D 'mapred.child.java.opts=-Xmx500m' --hbase-indexer-file [LOCAL_DIR]/morphline-hbase-mapper.xml --zk-host 127.0.0.1/solr --collection [COLLECTION_NAME] --go-live --log4j [LOCAL_DIR]/log4j.properties

For Hadoop Cluster

[cs5604f16_solr@node1 ~]$ hadoop --config /etc/hadoop/conf jar /opt/cloudera/parcels/CDH/lib/hbase-solr/tools/hbase-indexer-mr-1.5-cdh5.6.0-job.jar --conf /etc/hbase/conf/hbase-site.xml -D 'mapred.child.java.opts=-Xmx1024m' --hbase-indexer-file [LOCAL_DIR]/morphline-hbase-mapper.xml --zk-host node1.dlrl:2181,node2.dlrl:2181,node3.dlrl:2181,node4.dlrl:2181,solr2.dlrl:2181/solr --collection [COLLECTION_NAME] --go-live --log4j [LOCAL_DIR]/log4j.properties

