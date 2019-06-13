"""
  微信：Griezmann_JR
  火币交易所推荐码：asd43
  币安推荐码: 22795115
  币安推荐链接：https://www.binance.co/?ref=22795115
  Gateio交易所荐码：1100714
  Bitmex交易所推荐码：SzZBil 或者 https://www.bitmex.com/register/SzZBil

  代码地址： https://github.com/ramoslin02/51bitqunt
  视频更新：首先在Youtube上更新，搜索51bitquant 关注我

  1. bilibili.com
  2. 优酷  youku.com
  3. 百家号 baijiahao
  4. 头条号 toutiao
  5. 简书博客：https://www.jianshu.com/u/9afa76d7d7f0

"""

import requests
import time
import pandas as pd
pd.set_option('expand_frame_repr', False)

# BASE_URL = 'https://api.binance.com'
# #
# # kline = '/api/v1/klines'
# # #
# # kline_url = BASE_URL + kline + '?' + 'symbol=BTCUSDT&interval=1h&limit=1000'
# # print(kline_url)
# # resp = requests.get(kline_url)
# # print(resp.json())
# # df = pd.DataFrame(resp.json())
# # print(df)
# # exit()

# 如何获取binance过去一年的数据.  For While.


BASE_URL = 'https://api.binance.com'
limit = 1000
end_time = int(time.time() // 60 * 60 * 1000)
print(end_time)
start_time = int(end_time - limit*60*1000)
print(start_time)

while True:

    url = BASE_URL + '/api/v1/klines' + '?symbol=BTCUSDT&interval=1m&limit=' + str(limit) + '&startTime=' + str(
        start_time) + '&endTime=' + str(end_time)
    print(url)
    resp = requests.get(url)
    data = resp.json()
    df = pd.DataFrame(data, columns={'open_time': 0, 'open': 1, 'high': 2, 'low': 3, 'close': 4, 'volume': 5,
                                     'close_time': 6, 'quote_volume': 7, 'trades': 8, 'taker_base_volue': 9,
                                     'taker_quote_volume': 10, 'ignore': 11})

    df.set_index('open_time', inplace=True)
    df.to_csv(str(end_time) + '.csv')
    print(df)

    if len(df) < 1000:
        break

    end_time = start_time
    start_time = int(end_time - limit * 60 * 1000)
