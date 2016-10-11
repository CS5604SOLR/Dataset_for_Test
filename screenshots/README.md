

# README for Screenshots
if you see some similar screeshots, you succeed!

## Test importing a table into a hbase (after org.apache.hadoop.hbase.mapreduce.ImportTsv command)
open a shell:
```bash
hbase shell
```

get a list of tables
```bash
list
```

scan the table named test
```bash
scan "test"
```
![myimage-alt-tag](https://github.com/CS5604SOLR/Dataset_for_Test/blob/master/screenshots/scan-finish.png)


## Test the solrctl instancedir and create command (after you generate and create a datatest_collection)
```bash
solrctl instancedir --list
solrctl collection --list
```
![myimage-alt-tag](https://github.com/CS5604SOLR/Dataset_for_Test/blob/master/screenshots/collection-list.png)


## Webpage for HBase layout with raw data
![myimage-alt-tag](https://github.com/CS5604SOLR/Dataset_for_Test/blob/master/screenshots/hbaselayout.png)

## Webpage for indexing in Solr
![myimage-alt-tag](https://github.com/CS5604SOLR/Dataset_for_Test/blob/master/screenshots/query.png)

## Facet Search

Here are some useful links on facet search:

The query - set facet true 

![myimage-alt-tag](https://github.com/CS5604SOLR/Dataset_for_Test/blob/master/screenshots/1.png)

The result:

![myimage-alt-tag](https://github.com/CS5604SOLR/Dataset_for_Test/blob/master/screenshots/2.png)
