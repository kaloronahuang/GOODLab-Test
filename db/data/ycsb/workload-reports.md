# ycsb-workload-reports

## MySQL

### workloada

```plain
(py27) kalorona@kalorona-hpc:~/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0$ bin/ycsb load jdbc -P workloads/workloada -P db.properties
java -cp /home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/conf:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/conf:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/lib/HdrHistogram-2.1.4.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/lib/core-0.17.0.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/lib/jackson-core-asl-1.9.4.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/lib/htrace-core4-4.1.0-incubating.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/lib/jackson-mapper-asl-1.9.4.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/geronimo-jta_1.1_spec-1.1.1.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/openjpa-jdbc-2.1.1.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/openjpa-kernel-2.1.1.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/commons-collections-3.2.1.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/geronimo-jms_1.1_spec-1.1.1.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/mysql-connector-java-8.0.30.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/serp-1.13.1.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/openjpa-lib-2.1.1.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/jdbc-binding-0.17.0.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/commons-lang-2.4.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/commons-pool-1.5.4.jar site.ycsb.Client -db site.ycsb.db.JdbcDBClient -P workloads/workloada -P db.properties -load
Command line: -db site.ycsb.db.JdbcDBClient -P workloads/workloada -P db.properties -load
YCSB Client 0.17.0

Loading workload...
Starting test.
Loading class `com.mysql.jdbc.Driver'. This is deprecated. The new driver class is `com.mysql.cj.jdbc.Driver'. The driver is automatically registered via the SPI and manual loading of the driver class is generally unnecessary.
Adding shard node URL: jdbc:mysql://127.0.0.1:3306/test_db
Using shards: 1, batchSize:-1, fetchSize: -1
DBWrapper: report latency for each error is false and specific error codes to track for latency are: []
[OVERALL], RunTime(ms), 5177
[OVERALL], Throughput(ops/sec), 193.16206297083252
[TOTAL_GCS_PS_Scavenge], Count, 0
[TOTAL_GC_TIME_PS_Scavenge], Time(ms), 0
[TOTAL_GC_TIME_%_PS_Scavenge], Time(%), 0.0
[TOTAL_GCS_PS_MarkSweep], Count, 0
[TOTAL_GC_TIME_PS_MarkSweep], Time(ms), 0
[TOTAL_GC_TIME_%_PS_MarkSweep], Time(%), 0.0
[TOTAL_GCs], Count, 0
[TOTAL_GC_TIME], Time(ms), 0
[TOTAL_GC_TIME_%], Time(%), 0.0
[CLEANUP], Operations, 1
[CLEANUP], AverageLatency(us), 2653.0
[CLEANUP], MinLatency(us), 2652
[CLEANUP], MaxLatency(us), 2653
[CLEANUP], 95thPercentileLatency(us), 2653
[CLEANUP], 99thPercentileLatency(us), 2653
[INSERT], Operations, 1000
[INSERT], AverageLatency(us), 4812.849
[INSERT], MinLatency(us), 2396
[INSERT], MaxLatency(us), 45759
[INSERT], 95thPercentileLatency(us), 6535
[INSERT], 99thPercentileLatency(us), 9551
[INSERT], Return=OK, 1000
```

```plain
(py27) kalorona@kalorona-hpc:~/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0$ bin/ycsb run jdbc -P workloads/workloada -P db.properties
java -cp /home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/conf:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/conf:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/lib/HdrHistogram-2.1.4.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/lib/core-0.17.0.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/lib/jackson-core-asl-1.9.4.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/lib/htrace-core4-4.1.0-incubating.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/lib/jackson-mapper-asl-1.9.4.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/geronimo-jta_1.1_spec-1.1.1.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/openjpa-jdbc-2.1.1.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/openjpa-kernel-2.1.1.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/commons-collections-3.2.1.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/geronimo-jms_1.1_spec-1.1.1.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/mysql-connector-java-8.0.30.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/serp-1.13.1.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/openjpa-lib-2.1.1.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/jdbc-binding-0.17.0.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/commons-lang-2.4.jar:/home/kalorona/Develop/GOODLab-Test/db/launchpad/ycsb-0.17.0/jdbc-binding/lib/commons-pool-1.5.4.jar site.ycsb.Client -db site.ycsb.db.JdbcDBClient -P workloads/workloada -P db.properties -t
Command line: -db site.ycsb.db.JdbcDBClient -P workloads/workloada -P db.properties -t
YCSB Client 0.17.0

Loading workload...
Starting test.
Loading class `com.mysql.jdbc.Driver'. This is deprecated. The new driver class is `com.mysql.cj.jdbc.Driver'. The driver is automatically registered via the SPI and manual loading of the driver class is generally unnecessary.
Adding shard node URL: jdbc:mysql://127.0.0.1:3306/test_db
Using shards: 1, batchSize:-1, fetchSize: -1
DBWrapper: report latency for each error is false and specific error codes to track for latency are: []
[OVERALL], RunTime(ms), 2961
[OVERALL], Throughput(ops/sec), 337.7237419790611
[TOTAL_GCS_PS_Scavenge], Count, 0
[TOTAL_GC_TIME_PS_Scavenge], Time(ms), 0
[TOTAL_GC_TIME_%_PS_Scavenge], Time(%), 0.0
[TOTAL_GCS_PS_MarkSweep], Count, 0
[TOTAL_GC_TIME_PS_MarkSweep], Time(ms), 0
[TOTAL_GC_TIME_%_PS_MarkSweep], Time(%), 0.0
[TOTAL_GCs], Count, 0
[TOTAL_GC_TIME], Time(ms), 0
[TOTAL_GC_TIME_%], Time(%), 0.0
[READ], Operations, 511
[READ], AverageLatency(us), 995.1311154598826
[READ], MinLatency(us), 196
[READ], MaxLatency(us), 19471
[READ], 95thPercentileLatency(us), 1665
[READ], 99thPercentileLatency(us), 1796
[READ], Return=OK, 511
[CLEANUP], Operations, 1
[CLEANUP], AverageLatency(us), 3739.0
[CLEANUP], MinLatency(us), 3738
[CLEANUP], MaxLatency(us), 3739
[CLEANUP], 95thPercentileLatency(us), 3739
[CLEANUP], 99thPercentileLatency(us), 3739
[UPDATE], Operations, 489
[UPDATE], AverageLatency(us), 4261.576687116564
[UPDATE], MinLatency(us), 2242
[UPDATE], MaxLatency(us), 14351
[UPDATE], 95thPercentileLatency(us), 6031
[UPDATE], 99thPercentileLatency(us), 7583
[UPDATE], Return=OK, 489
```