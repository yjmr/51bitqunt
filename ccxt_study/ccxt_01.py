import ccxt
import time
import pandas as pd
print(ccxt.exchanges)

huobipro = ccxt.huobipro({'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/27766569-15aa7b9a-5edd-11e7-9e7f-44791f4ee49c.jpg',
                'api': {
                    'market': 'https://api.huobi.br.com',
                    'public': 'https://api.huobi.br.com',
                    'private': 'https://api.huobi.br.com',
                    'zendesk': 'https://huobiglobal.zendesk.com/hc/en-us/articles',
                },
                'www': 'https://www.huobi.pro',
                'referral': 'https://www.huobi.br.com/en-us/topic/invited/?invite_code=rwrd3',
                'doc': 'https://github.com/huobiapi/API_Docs/wiki/REST_api_reference',
                'fees': 'https://www.huobi.pro/about/fee/',
            }})


## 方法一: 设置apiKey和secret
# binance = ccxt.binance({
#     'apiKey': 'XXXX',
#     'secret': 'XXXXX'
# })

## 方法二:设置apiKey和secret
# binance.secret = 'xxxx'
# binance.apiKey = 'xxxxxx'




# huobipro.loadMarkets()
# huobipro.load_markets()
#
# print(huobipro.symbols)

# binance.load_markets()  # EOS/BTC
# print(binance.symbols)

# huobipro.fetchOHLCV()


# ticker

symbol = 'BTC/USDT'
# huobi_btc_ticker = huobipro.fetch_ticker(symbol)
# binance_btc_ticker = binance.fetch_ticker(symbol)
# print(huobi_btc_ticker)
# print(binance_btc_ticker)
#


# 获取开盘价、最高价、最低价、收盘价、成交量 OHLCV


# ohlcv = binance.fetch_ohlcv(symbol, timeframe='15m')
# # print(ohlcv)
# df = pd.DataFrame(ohlcv)  # open_time , open , high, low , close
# print(df)
#
# balance = binance.fetch_balance()
# print(balance)


# exchange = ccxt.okex({'urls': {
#                 'logo': 'https://user-images.githubusercontent.com/1294454/32552768-0d6dd3c6-c4a6-11e7-90f8-c043b64756a7.jpg',
#                 'api': {
#                     'web': 'https://www.okex.me/v2',
#                     'public': 'https://www.okex.me/api',
#                     'private': 'https://www.okex.me/api',
#                 },
#                 'www': 'https://www.okex.com',
#                 'doc': [
#                     'https://github.com/okcoin-okex/API-docs-OKEx.com',
#                     'https://www.okex.com/docs/en/',
#                 ],
#                 'fees': 'https://www.okex.com/pages/products/fees.html',
#                 'referral': 'https://www.okex.com',
#             }})
# exchange.load_markets()
#
#
# for symbol in exchange.markets:
#     market = exchange.markets[symbol]
#     if market['future']:
#         print('----------------------------------------------------')
#         print(symbol, exchange.fetch_ticker(symbol))
#         time.sleep(exchange.rateLimit / 1000)