# Dataset_for_Test

dataset_test.csv -- Modified Tweets Data

schema.xml -- For Solr

log4j.properties, morphlines.conf, morphline-hbase-mapper.xml -- For LilyIndexer

# Indexing Data on Virtual Cloudera

## 1 -- Import Data into HDFS and HBase

[cloudera@quickstart ~]$ hadoop fs -put dataset_test.csv

[cloudera@quickstart ~]$ hbase shell

hbase(main):001:0> create 'test', 'raw_cf'

[cloudera@quickstart ~]$ hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator=,  -Dimporttsv.columns="HBASE_ROW_KEY,raw_cf:c1,raw_cf:c2,raw_cf:c3,raw_cf:c4,raw_cf:c5,raw_cf:c6,raw_cf:c7,raw_cf:c8,raw_cf:c9,raw_cf:c10,raw_cf:c11,raw_cf:c12" test dataset_test.csv

## 2 -- Create Solr Collection

[cloudera@quickstart ~]$ solrctl instancedir --generate $HOME/datatest_collection

Replace the default schema.xml with the one here

[cloudera@quickstart ~]$ solrctl instancedir --create datatest_collection $HOME/datatest_collection

[cloudera@quickstart ~]$ solrctl collection --create datatest_collection

## 3 -- LilyIndexer

Copy log4j.properties, morphlines.conf and morphline-hbase-mapper.xml to your local directory.

For Virtual Cloudera 5.8, the morphlines.conf must be put under the path: /etc/hbase-solr/conf/

### 3.1 -- Indexing Data with live mode (online, easy, small dataset)

[cloudera@quickstart ~]$ hadoop --config /etc/hadoop/conf jar /usr/lib/hbase-solr/tools/hbase-indexer-mr-*-job.jar --conf /etc/hbase/conf/hbase-site.xml -D 'mapred.child.java.opts=-Xmx500m' --hbase-indexer-file [LOCAL_DIR]/morphline-hbase-mapper.xml --zk-host 127.0.0.1/solr --collection [COLLECTION_NAME] --go-live --log4j [LOCAL_DIR]/log4j.properties

### 3.2 -- Indexing Data with batch mode (offline, complex, big dataset)

#### Generate and output the index files

[cloudera@quickstart ~]$ hadoop --config /etc/hadoop/conf jar /usr/lib/hbase-solr/tools/hbase-indexer-mr-*-job.jar --conf /etc/hbase/conf/hbase-site.xml -D 'mapred.child.java.opts=-Xmx500m' --hbase-indexer-file [LOCAL_DIR]/morphline-hbase-mapper.xml --zk-host 127.0.0.1/solr --log4j [LOCAL_DIR]/log4j.properties --collection [COLLECTION_NAME] --verbose --output-dir hdfs://quickstart.cloudera/user/cloudera/small-index --overwrite-output-dir --shards 1

If a Java Heap Space error kills the indexing job , change the values of mapreduce.map.java.opts and mapreduce.reduce.java.opts in mapred-site.xml (/etc/hadoop/conf/) 

#### Copy the index files into local directory

[cloudera@quickstart ~]$ hadoop fs -get small-index/results/part-00000/data/index index

#### Clear the existing solr collection on HDFS

[cloudera@quickstart ~]$ sudo -u hdfs hadoop fs -rm -r -skipTrash /solr/[COLLECTION_NAME]/core_node1/data/index

[cloudera@quickstart ~]$ sudo -u hdfs hadoop fs -rm -r -skipTrash /solr/[COLLECTION_NAME]/core_node1/data/tlog

(Optional)

[cloudera@quickstart ~]$ solrctl collection --deletedocs [COLLECTION_NAME]

#### Put the offline index files into the solr collection

[cloudera@quickstart ~]$ sudo -u solr hadoop fs -put index /solr/[COLLECTION_NAME]/core_node1/data/

#### Restart the solr service

[cloudera@quickstart ~]$ sudo service solr-server restart


## Tips:

Delete table in HBase: [disable 'TABLE_NAME'] [drop 'TABLE_NAME']

Update/Delete Solr collection: [solrctl --help]


## Useful links:

[SolrQuerySyntax](https://wiki.apache.org/solr/SolrQuerySyntax)

[Lily HBase Index (For Virtual Cloudera 5.3)](http://www.cloudera.com/documentation/enterprise/5-3-x/topics/search_hbase_batch_indexer.html)

[Lily HBase Index (For Virtual Cloudera 5.8)](http://www.cloudera.com/documentation/enterprise/latest/topics/search_hbase_batch_indexer.html)

