# Dataset_for_Test

Dataset_test.csv -- Modified Tweets Data

schema.xml -- For Solr

log4j.properties, morphlines.conf, morphline-hbase-mapper.xml -- For LilyIndexer

#Indexing Data on Virtual Cloudera (Important Steps)

1 -- Import into HDFS

[cloudera@quickstart ~]$ hadoop fs -put Dataset_test.csv

2 -- Create HBase Table

[cloudera@quickstart ~]$ hbase shell

hbase(main):001:0> create 'tweets', 'raw'

