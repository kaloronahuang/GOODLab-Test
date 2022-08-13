# System Specification

## Hardware Spec

```plain
CPU     Intel Core i7 6700k
Memory  DDR4 24G
SSD     Intel 600p 512G
GPU     nVidia Geforce GTX 1080
```

## Linux System

```plain
>uname -a
Linux kalorona-hpc 5.15.0-41-generic #44-Ubuntu SMP Wed Jun 22 14:20:53 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
```

## MySQL Version

```plain
mysql> \s
--------------
mysql  Ver 8.0.30-0ubuntu0.22.04.1 for Linux on x86_64 ((Ubuntu))

Connection id:          9
Current database:
Current user:           root@localhost
SSL:                    Not in use
Current pager:          stdout
Using outfile:          ''
Using delimiter:        ;
Server version:         8.0.30-0ubuntu0.22.04.1 (Ubuntu)
Protocol version:       10
Connection:             Localhost via UNIX socket
Server characterset:    utf8mb4
Db     characterset:    utf8mb4
Client characterset:    utf8mb4
Conn.  characterset:    utf8mb4
UNIX socket:            /var/run/mysqld/mysqld.sock
Binary data as:         Hexadecimal
Uptime:                 1 min 15 sec

Threads: 2  Questions: 6  Slow queries: 0  Opens: 119  Flush tables: 3  Open tables: 38  Queries per second avg: 0.080
--------------
```
## RocksDB Version

`rocksdb-7.4.4`

## YCSB Version

`ycsb-0.17.0`