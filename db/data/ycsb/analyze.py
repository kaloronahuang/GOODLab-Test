# analyze_mysql.py
import os
import pandas as pd

def read_datapoint_mysql(path : str, thread_num : int):
    with open(path, 'r') as dpfile:
        x = 2 * thread_num + 1
        ln = dpfile.readlines()[x]
        traits = ln.split(',')
        data = traits[2][1:-1]
        return float(data)

def read_datapoint_rocksdb(path : str):
    with open(path, 'r') as dpfile:
        ln = dpfile.readlines()[1]
        traits = ln.split(',')
        data = traits[2][1:-1]
        return float(data)

def read_workload_mysql(task_type : str):
    path_dir = os.path.join('/home/kalorona/Develop/GOODLab-Test/db/data/ycsb/raw-data', 'mysql')
    data = []
    for thread_num in [1, 2, 4, 6, 8]:
        acc = 0.0
        for i in range(1, 4):
            filename = os.path.join(path_dir, f'thread{str(thread_num)}-{str(i)}', 'workload' + task_type + '.txt')
            acc += read_datapoint_mysql(filename, thread_num)
        avg = acc / 3
        data.append(avg)
    return data

def read_workload_rocksdb(task_type : str):
    path_dir = os.path.join('/home/kalorona/Develop/GOODLab-Test/db/data/ycsb/raw-data', 'rocksdb')
    data = []
    for thread_num in [1, 2, 4, 6, 8]:
        acc = 0.0
        for i in range(1, 4):
            filename = os.path.join(path_dir, f'thread{str(thread_num)}-{str(i)}', 'workload' + task_type + '.txt')
            acc += read_datapoint_rocksdb(filename)
        avg = acc / 3
        data.append(avg)
    return data

def main():
    for c in range(ord('a'), ord('g')):
        x = chr(c)
        data_mysql = read_workload_mysql(x)
        data_rockdb = read_workload_rocksdb(x)
        workload_frame = {'Threads' : [1, 2, 4, 6, 8], 'MySQL' : data_mysql, 'RocksDB' : data_rockdb}
        df = pd.DataFrame(workload_frame)
        df.to_csv('workload-' + x + '-report.csv')

if __name__ == '__main__':
    main()