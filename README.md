# Dataset_for_Test

Dataset_test.csv -- Modified Tweets Data

schema.xml -- For Solr

log4j.properties, morphlines.conf, morphline-hbase-mapper.xml -- For LilyIndexer

#Indexing Data on Virtual Cloudera (Important Steps)

1 -- Import into HDFS

[cloudera@quickstart ~]$ hadoop fs -put Dataset_test.csv

2 -- Create HBase Table

[cloudera@quickstart ~]$ hbase shell

hbase(main):001:0> create 'test', 'raw_cf'

3 -- Import into HBase

[cloudera@quickstart ~]$ hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator=,  -Dimporttsv.columns="HBASE_ROW_KEY,raw_cf:c1,raw_cf:c2,raw_cf:c3,raw_cf:c4,raw_cf:c5,raw_cf:c6,raw_cf:c7,raw_cf:c8,raw_cf:c9,raw_cf:c10,raw_cf:c11,raw_cf:c21" test Dataset_test.csv

