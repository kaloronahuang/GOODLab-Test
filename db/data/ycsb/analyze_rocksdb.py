# analyze_rocksdb.py
import os
import pandas as pd

def read_datapoint(path : str):
    data_point = dict()
    with open(path, 'r') as dpfile:
        lns = dpfile.readlines()
        for ln in lns:
            traits = ln.split(',')
            trait_name = traits[0][1:-1]
            metric = traits[1][1:]
            data = traits[2][1:-1]
            data_point[trait_name + ' - ' + metric] = data
    return data_point

def read_workload(task_type : str):
    data = []
    path_dir = os.path.join('/home/kalorona/Develop/GOODLab-Test/db/data/ycsb/raw-data', 'rocksdb', 'workload' + task_type)
    for filename in os.listdir(path_dir):
        dp = read_datapoint(os.path.join(path_dir, filename))
        data.append(dp)
    df = pd.DataFrame(data)
    return df

def main():
    for c in range(ord('a'), ord('g')):
        df = read_workload(chr(c))
        df.to_csv('rocksdb-ycsb-workload' + chr(c) + '.csv')

if __name__ == '__main__':
    main()