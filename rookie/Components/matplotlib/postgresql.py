import psycopg2
import psycopg2.extras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from contextlib import closing
from datetime import datetime, timedelta
from sqlalchemy import create_engine

class HotToneVisualizer:
    def __init__(self, db_url='postgresql://ess:cjfzdmm#312@10.201.17.11:15400/ess'):
        self.engine = create_engine(db_url)
        self.rack_query = """
             select
                 time,
                 rackcode,
                 syscurr_a__
             from station_bank_hottone_source_rack sbhsr
             where projectid = %(projectid)s and bankcode = %(bankcode)s
             order by time
         """
    
    def generate_plot(self, params, figsize=(10, 6)):
        """
        生成不同 rackcode 的 syscurr_a__ 随时间变化折线图
        
        参数:
        params: dict - 包含 projectid 和 bankcode 的字典
        figsize: tuple - 图表尺寸，默认为 (10, 6)
        
        返回:
        matplotlib.pyplot.Figure - 生成的图表对象
        """
        # 执行查询获取数据
        df = pd.read_sql_query(self.rack_query, self.engine, params=params)
        print(df.shape)

        # 将 time 列转换为 datetime 类型
        df['time'] = pd.to_datetime(df['time'])
        
        # 按 rackcode 分组，绘制折线图
        plt.figure(figsize=figsize)
        for rackcode, group in df.groupby('rackcode'):
            plt.plot(group['time'], group['syscurr_a__'], label=rackcode)
        
        plt.xlabel('时间')
        plt.ylabel('syscurr_a__')
        plt.title(f'不同 rackcode 的 syscurr_a__ 随时间变化折线图 (projectid: {params["projectid"]}, bankcode: {params["bankcode"]})')
        plt.legend(title='rackcode')
        plt.grid(True)
        plt.tight_layout()
        
        return plt

# 示例用法
if __name__ == "__main__":
    # 创建可视化器实例
    visualizer = HotToneVisualizer()
    
    # 定义参数
    params = {'projectid': 2005537568530546690, 'bankcode': 'N10'}
    
    # 生成并显示图表
    plt = visualizer.generate_plot(params)
    plt.show()
