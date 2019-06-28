"""
  微信：Griezmann_JR
  火币交易所推荐码：asd43
  币安推荐码: 22795115
  币安推荐链接：https://www.binance.co/?ref=22795115
  Gateio交易所荐码：1100714
  Bitmex交易所推荐码：SzZBil 或者 https://www.bitmex.com/register/SzZBil

  github代码地址： https://github.com/ramoslin02/51bitqunt
  视频更新：首先在Youtube上更新，搜索51bitquant 关注我

  0. Youtube: https://www.youtube.com/channel/UCjCMoRi4dZ6LRV2KL_RP8KQ/videos
  1. bilibili.com 51bitquant
  2. 爱奇艺：https://www.iqiyi.com/u/1752521752
  3. 优酷  youku.com
  4. 百家号 baijiahao
  5. 头条号 toutiao
  6. 简书博客：https://www.jianshu.com/u/9afa76d7d7f0

#####################################################
Pandas 如何批量导入数据

官方文档： http://pandas.pydata.org/pandas-docs/stable/api.html

#####################################################
"""

import pandas as pd
import os

pd.set_option('expand_frame_repr', False)

project_dir = os.path.dirname(os.path.dirname(__file__))
# print(project_dir)

csv_dir = project_dir + '/binance_api'
# print(csv_dir)

# for root, dirs, files in os.walk(csv_dir):
#     print('root:', root)  # 当前的目录
#     print('dirs:', dirs)  # 文件件加目录
#     print('files:', files)  # 文件
#     print("**"*20)
#
# print("****"*10)
# 批量读取文件名称
csv_file_paths = []

for root, dirs, files in os.walk(csv_dir):
    # 当files不为空的时候
    if files:
        for f in files:
            if f.endswith('.csv'):
                file_path = os.path.join(root, f)
                # print(file_path)
                csv_file_paths.append(file_path)


# 遍历文件名，批量导入数据
all_df = pd.DataFrame()

print(csv_file_paths)

for file in sorted(csv_file_paths):
    print(file)
    # 导入数据
    df = pd.read_csv(file)
    #  合并数据
    all_df = all_df.append(df, ignore_index=True)

# print(all_df)


# 删除重复的数据.
all_df.drop_duplicates(subset=['open_time'], inplace=True, keep='first')
# print(all_df)


all_df.sort_values(by=['open_time'], ascending=1, inplace=True)

all_df['open_time'] = pd.to_datetime(all_df['open_time'], unit='ms')
all_df = all_df[['open_time', 'open', 'high', 'low', 'close', 'volume']]


# df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
all_df.set_index('open_time', inplace=True)

all_df.to_csv('binance_btc_1min.csv')
print(all_df)
exit()