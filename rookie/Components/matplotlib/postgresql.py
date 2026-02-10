import psycopg2
import psycopg2.extras
import numpy as np
import pandas as pd
from contextlib import closing
from datetime import datetime, timedelta
from sqlalchemy import create_engine

class HotToneAnalyzer:
    def __init__(self, host, port, dbname, user, password):
        self.conn_params = {
            'host': host,
            'port': port,
            'database': dbname,
            'user': user,
            'password': password
        }

    def get_racks(self, projectid, bankcode):
        query = f"""
             select
                time
                 rackcode,
                 syscurr_a__
             from station_bank_hottone_source_rack sbhsr
             where projectid = {projectid} and bankcode = '{bankcode}'
             order by time
             limit 10
         """

        conn = psycopg2.connect(**self.conn_params)
        df = pd.read_sql_query(query, conn)

        with psycopg2.connect(**self.conn_params) as conn:
            df = pd.read_sql_query(query, conn)
            array_data = df.to_numpy()

            print(f"数组形状: {array_data.shape}")
            print(f"列名: {df.columns.tolist()}")

# 创建连接引擎
engine = create_engine('postgresql://ess:cjfzdmm#312@10.201.17.11:15400/ess')

query = f"""
     select
         time,
         rackcode,
         syscurr_a__
     from station_bank_hottone_source_rack sbhsr
     where projectid = %s and bankcode = %s
     order by time
     limit 10
 """

# 读取数据到 DataFrame
# df = pd.read_sql_table('your_table', engine)
# 或执行自定义查询
df = pd.read_sql_query('SELECT * FROM your_table LIMIT 1000', engine)

# 转换为 numpy array
array_data = df.to_numpy()

# 如果需要指定数据类型
numeric_cols = ['price', 'quantity', 'discount']
numeric_data = df[numeric_cols].to_numpy(dtype=np.float64)

print(f"完整数组形状: {array_data.shape}")
print(f"数值数组形状: {numeric_data.shape}")