import psycopg2
import psycopg2.extras
import numpy as np
import pandas as pd
from contextlib import closing
from datetime import datetime, timedelta
from sqlalchemy import create_engine

# def read1():
#     conn = psycopg2.connect(
#         host="10.201.17.11",
#         port=15400,
#         database="ess",
#         user="ess",
#         password="cjfzdmm#312"
#     )
#
#     # 方法3.1：读取为 DataFrame 再转换
#     query = "select * from station_bank_hottone_source_bau sbhsb where projectid = 2005537568530546690 and bankcode = 'N11' limit 10;"
#     df = pd.read_sql_query(query, conn)
#     array_data = df.to_numpy()
#
#     print(f"数组形状: {array_data.shape}")
#     print(f"列名: {df.columns.tolist()}")
#     conn.close()

# array_data, columns = read_large_table_to_array('your_table', chunk_size=5000)
# def read_large_table_to_array(table_name, chunk_size=10000):
#     """
#     分批读取大型数据表
#     """
#     conn = psycopg2.connect(
#         host="localhost",
#         database="your_database",
#         user="your_username",
#         password="your_password"
#     )
#
#     with closing(conn.cursor(name='fetch_cursor')) as cursor:
#         # 使用服务端游标避免内存溢出
#         cursor.itersize = chunk_size
#
#         # 获取总行数
#         cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
#         total_rows = cursor.fetchone()[0]
#
#         # 获取列信息
#         cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
#         column_names = [desc[0] for desc in cursor.description]
#
#         # 执行查询
#         cursor.execute(f"SELECT * FROM {table_name}")
#
#         # 分批读取
#         all_data = []
#         rows_fetched = 0
#
#         while True:
#             chunk = cursor.fetchmany(chunk_size)
#             if not chunk:
#                 break
#
#             chunk_array = np.array(chunk)
#             all_data.append(chunk_array)
#             rows_fetched += len(chunk)
#
#             print(f"已读取 {rows_fetched}/{total_rows} 行")
#
#         # 合并所有块
#         if all_data:
#             final_array = np.vstack(all_data)
#             return final_array, column_names
#         else:
#             return np.array([]), column_names

class HotToneAnalyzer:
    def __init__(self, host, port, dbname, user, password):
        self.conn_params = {
            'host': host,
            'port': port,
            'database': dbname,
            'user': user,
            'password': password
        }

    # def analyze_sales(self, sales_array):
    #     """分析销售数据"""
    #     print("=== 销售分析报告 ===")
    #     print(f"总销售记录数: {len(sales_array)}")
    #     print(f"总销售额: {np.sum(sales_array['quantity'] * sales_array['unit_price']):.2f}")
    #     print(f"平均单价: {np.mean(sales_array['unit_price']):.2f}")
    #     print(f"最大销量: {np.max(sales_array['quantity'])}")
    #     print(f"最畅销产品ID: {np.argmax(np.bincount(sales_array['product_id']))}")
    #
    #     # 按日期分组统计
    #     unique_dates = np.unique(sales_array['sale_date'])
    #     print(f"\n销售天数: {len(unique_dates)}")
    #
    #     # 转为pandas DataFrame进行更复杂的分析
    #     df = pd.DataFrame({
    #         'product_id': sales_array['product_id'],
    #         'sale_date': sales_array['sale_date'],
    #         'quantity': sales_array['quantity'],
    #         'revenue': sales_array['quantity'] * sales_array['unit_price']
    #     })
    #
    #     daily_sales = df.groupby('sale_date')['revenue'].sum()
    #     print(f"\n日均销售额: {daily_sales.mean():.2f}")
    #
    #     return df

    # def get_racks(self, projectid, bankcode):
    #     query = """
    #          select
    #              to_char(time, 'YYYY-MM-DD HH24:MI:SS'),
    #              rackcode,
    #              syscurr_a__
    #          from station_bank_hottone_source_rack sbhsr
    #          where projectid = %s and bankcode = %s
    #          order by time
    #          limit 10
    #      """
    #
    #     with psycopg2.connect(**self.conn_params) as conn:
    #         with conn.cursor() as cur:
    #             cur.execute(query, (projectid, bankcode))
    #             data = cur.fetchall()
    #
    #             df = pd.DataFrame(data)
    #
    #             # 转为结构化numpy数组
    #             dtype = np.dtype([
    #                 ('time', 'U20'),
    #                 ('rackcode', 'U10'),
    #                 ('syscurr_a__', np.float64),
    #             ])
    #
    #             rank_array = np.array([
    #                 (np.datetime64(r[0]), r[1], float(r[2]))
    #                 for r in data
    #             ], dtype=dtype)
    #
    #             return rank_array

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



if __name__ == "__main__":
    analyzer = HotToneAnalyzer(
        host="10.201.17.11",
        port=15400,
        dbname="ess",
        user="ess",
        password="cjfzdmm#312"
    )

    array_data = analyzer.get_racks(2005537568530546690, 'N11')
    # df = pd.DataFrame({
    #     'time': array_data['time'],
    #     'rackcode': array_data['rackcode'],
    #     'curr': array_data['syscurr_a__'],
    # })
    # df['curr'] = df['curr'].astype(float)
    #
    # print("原始数据:")
    # print(df)
    # print("\n" + "=" * 60)
    # print("\n方法1: 使用 groupby 遍历:")
    # grouped = df.groupby(['time', 'rackcode'])
    # for (time, rackcode), group_df in grouped:
    #     print(f"\n{time}年 {rackcode} 季度数据:")
    #     print(group_df)
    #
    #
    #
    # daily_sales = df.groupby('sale_date')['revenue'].sum()





