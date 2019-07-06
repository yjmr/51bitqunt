
"""
  微信：bitquant51
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

"""
import ccxt
# 获取私有api
apiKey = '换成你的apiKey'
secret = '请换成你的secret'
binance = ccxt.binance({"apiKey": apiKey, 'secret': secret})

# 如何设置代理.
# binance.proxies = {
#   'http': 'http://10.10.1.10:3128', # these proxies won't work for you, they are here for example
#   'https': 'https://10.10.1.10:1080',
# }

# balance = binance.fetch_balance()  # 账户的资金情况
# print(balance)
# print(balance['BNB'])
# print(balance['ETH'])
# exit()
balance = """{'info': 
{'makerCommission': 10, 
'takerCommission': 10, 
'buyerCommission': 0, 
'sellerCommission': 0, 
'canTrade': True, 
'canWithdraw': True,
 'canDeposit': True, 
 'updateTime': 1562418686043, 
 'accountType': 'MARGIN', 
 'balances': [{'asset': 'BTC', 'free': '0.00000000', 'locked': '0.00000000'}, 
 {'asset': 'LTC', 'free': '0.00000000', 'locked': '0.00000000'},
  {'asset': 'ETH', 'free': '0.00000000', 'locked': '0.00000000'}, 
  {'asset': 'NEO', 'free': '0.00000000', 'locked': '0.00000000'}, 
  {'asset': 'BNB', 'free': '4.56050497', 'locked': '0.00000000'}, 
  {'asset': 'QTUM', 'free': '0.00000000', 'locked': '0.00000000'},
   {'asset': 'EOS', 'free': '0.00000000', 'locked': '0.00000000'}, 
   {'asset': 'SNT', 'free': '0.00000000', 'locked': '0.00000000'}, 
   {'asset': 'BNT', 'free': '0.00000000', 'locked': '0.00000000'}, 
   {'asset': 'GAS', 'free': '0.00000000', 'locked': '0.00000000'}, 
   {'asset': 'BCC', 'free': '0.00000000', 'locked': '0.00000000'}, 
   {'asset': 'USDT', 'free': '0.00000000', 'locked': '0.00000000'}, 
   {'asset': 'HSR', 'free': '0.00000000', 'locked': '0.00000000'}, 
   {'asset': 'OAX', 'free': '0.00000000', 'locked': '0.00000000'}, 
   {'asset': 'DNT', 'free': '0.00000000', 'locked': '0.00000000'}, 
   {'asset': 'MCO', 'free': '0.00000000', 'locked': '0.00000000'}, 
   {'asset': 'ICN', 'free': '0.00000000', 'locked': '0.00000000'}, 
   {'asset': 'ZRX', 'free': '0.00000000', 'locked': '0.00000000'}, 
   {'asset': 'OMG', 'free': '0.00000000', 'locked': '0.00000000'},
    {'asset': 'WTC', 'free': '0.00000000', 'locked': '0.00000000'}, 
    {'asset': 'YOYO', 'free': '0.00000000', 'locked': '0.00000000'}, 
    {'asset': 'LRC', 'free': '0.00000000', 'locked': '0.00000000'}, 
    {'asset': 'TRX', 'free': '0.00000000', 'locked': '0.00000000'}, 
    {'asset': 'SNGLS', 'free': '0.00000000', 'locked': '0.00000000'}, 
    {'asset': 'STRAT', 'free': '0.00000000', 'locked': '0.00000000'}, 
    {'asset': 'BQX', 'free': '0.00000000', 'locked': '0.00000000'}, 
    {'asset': 'FUN', 'free': '0.00000000', 'locked': '0.00000000'}, 
    {'asset': 'KNC', 'free': '0.00000000', 'locked': '0.00000000'}, 
    {'asset': 'CDT', 'free': '0.00000000', 'locked': '0.00000000'}, 
    {'asset': 'XVG', 'free': '0.00000000', 'locked': '0.00000000'}, 
    {'asset': 'IOTA', 'free': '0.00000000', 'locked': '0.00000000'},
     {'asset': 'SNM', 'free': '0.00000000', 'locked': '0.00000000'},
      {'asset': 'LINK', 'free': '0.00000000', 'locked': '0.00000000'}, 
      {'asset': 'CVC', 'free': '0.00000000', 'locked': '0.00000000'}, 
      {'asset': 'TNT', 'free': '0.00000000', 'locked': '0.00000000'}, 
      {'asset': 'REP', 'free': '0.00000000', 'locked': '0.00000000'}, 
      {'asset': 'MDA', 'free': '0.00000000', 'locked': '0.00000000'},
      {'asset': 'DOGE', 'free': '0.00000000', 'locked': '0.00000000'}]}, 
      'BTC': {'free': 0.0, 'used': 0.0, 'total': 0.0},
       'LTC': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 
       'ETH': {'free': 0.0, 'used': 0.0, 'total': 0.0},
        'NEO': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 
        'BNB': {'free': 4.56050497, 'used': 0.0, 'total': 4.56050497}, 
        'QTUM': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 
        'EOS': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 
        'SNT': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 
        'BNT': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 
        'GAS': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 
        'BCC': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 
        'USDT': {'free': 0.0, 'used': 0.0, 'total': 0.0},  
        'MTH': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 
        'ADX': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 
        'ETC': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ENG': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ZEC': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'AST': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'GNT': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'DGD': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'BAT': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'DASH': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'POWR': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'BTG': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'REQ': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'XMR': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'EVX': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'VIB': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ENJ': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'VEN': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ARK': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'XRP': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'MOD': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'STORJ': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'KMD': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'RCN': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'EDO': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'DATA': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'DLT': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'MANA': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'PPT': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'RDN': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'GXS': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'AMB': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ARN': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'BCPT': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'CND': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'GVT': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'POE': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'BTS': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'FUEL': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'XZC': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'QSP': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'LSK': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'BCD': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'TNB': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ADA': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'LEND': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'XLM': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'CMT': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'WAVES': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'WABI': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'GTO': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ICX': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'OST': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ELF': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'AION': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'WINGS': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'BRD': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'NEBL': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'NAV': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'VIBE': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'LUN': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'TRIG': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'APPC': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'CHAT': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'RLC': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'INS': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'PIVX': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'IOST': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'STEEM': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'NANO': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'AE': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'VIA': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'BLZ': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'SYS': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'RPX': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'NCASH': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'POA': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ONT': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ZIL': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'STORM': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'XEM': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'WAN': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'WPR': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'QLC': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'GRS': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'CLOAK': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'LOOM': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'BCN': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'TUSD': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ZEN': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'SKY': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'THETA': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'IOTX': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'QKC': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'AGI': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'NXS': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'SC': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'NPXS': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'KEY': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'NAS': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'MFT': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'DENT': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ARDR': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'HOT': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'VET': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'DOCK': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'POLY': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'VTHO': {'free': 2063.904624, 'used': 0.0, 'total': 2063.904624}, 'ONG': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'PHX': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'HC': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'GO': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'PAX': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'RVN': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'DCR': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'USDC': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'MITH': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'BCH': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'BSV': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'REN': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'BTT': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'USDS': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'FET': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'TFUEL': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'CELR': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'MATIC': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ATOM': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'PHB': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ONE': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'FTM': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'BTCB': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'USDSB': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ALGO': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'ERD': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'DOGE': {'free': 0.0, 'used': 0.0, 'total': 0.0}, 'free': {'BTC': 0.0, 'LTC': 0.0, 'ETH': 0.0, 'NEO': 0.0, 'BNB': 4.56050497, 'QTUM': 0.0, 'EOS': 0.0, 'SNT': 0.0, 'BNT': 0.0, 'GAS': 0.0, 'BCC': 0.0, 'USDT': 0.0, 'HSR': 0.0, 'OAX': 0.0, 'DNT': 0.0, 'MCO': 0.0, 'ICN': 0.0, 'ZRX': 0.0, 'OMG': 0.0, 'WTC': 0.0, 'YOYOW': 0.0, 'LRC': 0.0, 'TRX': 0.0, 'SNGLS': 0.0, 'STRAT': 0.0, 'BQX': 0.0, 'FUN': 0.0, 'KNC': 0.0, 'CDT': 0.0, 'XVG': 0.0, 'IOTA': 0.0, 'SNM': 0.0, 'LINK': 0.0, 'CVC': 0.0, 'TNT': 0.0, 'REP': 0.0, 'MDA': 0.0, 'MTL': 0.0, 'SALT': 0.0, 'NULS': 0.0, 'SUB': 0.0, 'MTH': 0.0, 'ADX': 0.0, 'ETC': 0.0, 'ENG': 0.0, 'ZEC': 0.0, 'AST': 0.0, 'GNT': 0.0, 'DGD': 0.0, 'BAT': 0.0, 'DASH': 0.0, 'POWR': 0.0, 'BTG': 0.0, 'REQ': 0.0, 'XMR': 0.0, 'EVX': 0.0, 'VIB': 0.0, 'ENJ': 0.0, 'VEN': 0.0, 'ARK': 0.0, 'XRP': 0.0, 'MOD': 0.0, 'STORJ': 0.0, 'KMD': 0.0, 'RCN': 0.0, 'EDO': 0.0, 'DATA': 0.0, 'DLT': 0.0, 'MANA': 0.0, 'PPT': 0.0, 'RDN': 0.0, 'GXS': 0.0, 'AMB': 0.0, 'ARN': 0.0, 'BCPT': 0.0, 'CND': 0.0, 'GVT': 0.0, 'POE': 0.0, 'BTS': 0.0, 'FUEL': 0.0, 'XZC': 0.0, 'QSP': 0.0, 'LSK': 0.0, 'BCD': 0.0, 'TNB': 0.0, 'ADA': 0.0, 'LEND': 0.0, 'XLM': 0.0, 'CMT': 0.0, 'WAVES': 0.0, 'WABI': 0.0, 'GTO': 0.0, 'ICX': 0.0, 'OST': 0.0, 'ELF': 0.0, 'AION': 0.0, 'WINGS': 0.0, 'BRD': 0.0, 'NEBL': 0.0, 'NAV': 0.0, 'VIBE': 0.0, 'LUN': 0.0, 'TRIG': 0.0, 'APPC': 0.0, 'CHAT': 0.0, 'RLC': 0.0, 'INS': 0.0, 'PIVX': 0.0, 'IOST': 0.0, 'STEEM': 0.0, 'NANO': 0.0, 'AE': 0.0, 'VIA': 0.0, 'BLZ': 0.0, 'SYS': 0.0, 'RPX': 0.0, 'NCASH': 0.0, 'POA': 0.0, 'ONT': 0.0, 'ZIL': 0.0, 'STORM': 0.0, 'XEM': 0.0, 'WAN': 0.0, 'WPR': 0.0, 'QLC': 0.0, 'GRS': 0.0, 'CLOAK': 0.0, 'LOOM': 0.0, 'BCN': 0.0, 'TUSD': 0.0, 'ZEN': 0.0, 'SKY': 0.0, 'THETA': 0.0, 'IOTX': 0.0, 'QKC': 0.0, 'AGI': 0.0, 'NXS': 0.0, 'SC': 0.0, 'NPXS': 0.0, 'KEY': 0.0, 'NAS': 0.0, 'MFT': 0.0, 'DENT': 0.0, 'ARDR': 0.0, 'HOT': 0.0, 'VET': 0.0, 'DOCK': 0.0, 'POLY': 0.0, 'VTHO': 2063.904624, 'ONG': 0.0, 'PHX': 0.0, 'HC': 0.0, 'GO': 0.0, 'PAX': 0.0, 'RVN': 0.0, 'DCR': 0.0, 'USDC': 0.0, 'MITH': 0.0, 'BCH': 0.0, 'BSV': 0.0, 'REN': 0.0, 'BTT': 0.0, 'USDS': 0.0, 'FET': 0.0, 'TFUEL': 0.0, 'CELR': 0.0, 'MATIC': 0.0, 'ATOM': 0.0, 'PHB': 0.0, 'ONE': 0.0, 'FTM': 0.0, 'BTCB': 0.0, 'USDSB': 0.0, 'ALGO': 0.0, 'ERD': 0.0, 'DOGE': 0.0}, 'used': {'BTC': 0.0, 'LTC': 0.0, 'ETH': 0.0, 'NEO': 0.0, 'BNB': 0.0, 'QTUM': 0.0, 'EOS': 0.0, 'SNT': 0.0, 'BNT': 0.0, 'GAS': 0.0, 'BCC': 0.0, 'USDT': 0.0, 'HSR': 0.0, 'OAX': 0.0, 'DNT': 0.0, 'MCO': 0.0, 'ICN': 0.0, 'ZRX': 0.0, 'OMG': 0.0, 'WTC': 0.0, 'YOYOW': 0.0, 'LRC': 0.0, 'TRX': 0.0, 'SNGLS': 0.0, 'STRAT': 0.0, 'BQX': 0.0, 'FUN': 0.0, 'KNC': 0.0, 'CDT': 0.0, 'XVG': 0.0, 'IOTA': 0.0, 'SNM': 0.0, 'LINK': 0.0, 'CVC': 0.0, 'TNT': 0.0, 'REP': 0.0, 'MDA': 0.0, 'MTL': 0.0, 'SALT': 0.0, 'NULS': 0.0, 'SUB': 0.0, 'MTH': 0.0, 'ADX': 0.0, 'ETC': 0.0, 'ENG': 0.0, 'ZEC': 0.0, 'AST': 0.0, 'GNT': 0.0, 'DGD': 0.0, 'BAT': 0.0, 'DASH': 0.0, 'POWR': 0.0, 'BTG': 0.0, 'REQ': 0.0, 'XMR': 0.0, 'EVX': 0.0, 'VIB': 0.0, 'ENJ': 0.0, 'VEN': 0.0, 'ARK': 0.0, 'XRP': 0.0, 'MOD': 0.0, 'STORJ': 0.0, 'KMD': 0.0, 'RCN': 0.0, 'EDO': 0.0, 'DATA': 0.0, 'DLT': 0.0, 'MANA': 0.0, 'PPT': 0.0, 'RDN': 0.0, 'GXS': 0.0, 'AMB': 0.0, 'ARN': 0.0, 'BCPT': 0.0, 'CND': 0.0, 'GVT': 0.0, 'POE': 0.0, 'BTS': 0.0, 'FUEL': 0.0, 'XZC': 0.0, 'QSP': 0.0, 'LSK': 0.0, 'BCD': 0.0, 'TNB': 0.0, 'ADA': 0.0, 'LEND': 0.0, 'XLM': 0.0, 'CMT': 0.0, 'WAVES': 0.0, 'WABI': 0.0, 'GTO': 0.0, 'ICX': 0.0, 'OST': 0.0, 'ELF': 0.0, 'AION': 0.0, 'WINGS': 0.0, 'BRD': 0.0, 'NEBL': 0.0, 'NAV': 0.0, 'VIBE': 0.0, 'LUN': 0.0, 'TRIG': 0.0, 'APPC': 0.0, 'CHAT': 0.0, 'RLC': 0.0, 'INS': 0.0, 'PIVX': 0.0, 'IOST': 0.0, 'STEEM': 0.0, 'NANO': 0.0, 'AE': 0.0, 'VIA': 0.0, 'BLZ': 0.0, 'SYS': 0.0, 'RPX': 0.0, 'NCASH': 0.0, 'POA': 0.0, 'ONT': 0.0, 'ZIL': 0.0, 'STORM': 0.0, 'XEM': 0.0, 'WAN': 0.0, 'WPR': 0.0, 'QLC': 0.0, 'GRS': 0.0, 'CLOAK': 0.0, 'LOOM': 0.0, 'BCN': 0.0, 'TUSD': 0.0, 'ZEN': 0.0, 'SKY': 0.0, 'THETA': 0.0, 'IOTX': 0.0, 'QKC': 0.0, 'AGI': 0.0, 'NXS': 0.0, 'SC': 0.0, 'NPXS': 0.0, 'KEY': 0.0, 'NAS': 0.0, 'MFT': 0.0, 'DENT': 0.0, 'ARDR': 0.0, 'HOT': 0.0, 'VET': 0.0, 'DOCK': 0.0, 'POLY': 0.0, 'VTHO': 0.0, 'ONG': 0.0, 'PHX': 0.0, 'HC': 0.0, 'GO': 0.0, 'PAX': 0.0, 'RVN': 0.0, 'DCR': 0.0, 'USDC': 0.0, 'MITH': 0.0, 'BCH': 0.0, 'BSV': 0.0, 'REN': 0.0, 'BTT': 0.0, 'USDS': 0.0, 'FET': 0.0, 'TFUEL': 0.0, 'CELR': 0.0, 'MATIC': 0.0, 'ATOM': 0.0, 'PHB': 0.0, 'ONE': 0.0, 'FTM': 0.0, 'BTCB': 0.0, 'USDSB': 0.0, 'ALGO': 0.0, 'ERD': 0.0, 'DOGE': 0.0}, 'total': {'BTC': 0.0, 'LTC': 0.0, 'ETH': 0.0, 'NEO': 0.0, 'BNB': 4.56050497, 'QTUM': 0.0, 'EOS': 0.0, 'SNT': 0.0, 'BNT': 0.0, 'GAS': 0.0, 'BCC': 0.0, 'USDT': 0.0, 'HSR': 0.0, 'OAX': 0.0, 'DNT': 0.0, 'MCO': 0.0, 'ICN': 0.0, 'ZRX': 0.0, 'OMG': 0.0, 'WTC': 0.0, 'YOYOW': 0.0, 'LRC': 0.0, 'TRX': 0.0, 'SNGLS': 0.0, 'STRAT': 0.0, 'BQX': 0.0, 'FUN': 0.0, 'KNC': 0.0, 'CDT': 0.0, 'XVG': 0.0, 'IOTA': 0.0, 'SNM': 0.0, 'LINK': 0.0, 'CVC': 0.0, 'TNT': 0.0, 'REP': 0.0, 'MDA': 0.0, 'MTL': 0.0, 'SALT': 0.0, 'NULS': 0.0, 'SUB': 0.0, 'MTH': 0.0, 'ADX': 0.0, 'ETC': 0.0, 'ENG': 0.0, 'ZEC': 0.0, 'AST': 0.0, 'GNT': 0.0, 'DGD': 0.0, 'BAT': 0.0, 'DASH': 0.0, 'POWR': 0.0, 'BTG': 0.0, 'REQ': 0.0, 'XMR': 0.0, 'EVX': 0.0, 'VIB': 0.0, 'ENJ': 0.0, 'VEN': 0.0, 'ARK': 0.0, 'XRP': 0.0, 'MOD': 0.0, 'STORJ': 0.0, 'KMD': 0.0, 'RCN': 0.0, 'EDO': 0.0, 'DATA': 0.0, 'DLT': 0.0, 'MANA': 0.0, 'PPT': 0.0, 'RDN': 0.0, 'GXS': 0.0, 'AMB': 0.0, 'ARN': 0.0, 'BCPT': 0.0, 'CND': 0.0, 'GVT': 0.0, 'POE': 0.0, 'BTS': 0.0, 'FUEL': 0.0, 'XZC': 0.0, 'QSP': 0.0, 'LSK': 0.0, 'BCD': 0.0, 'TNB': 0.0, 'ADA': 0.0, 'LEND': 0.0, 'XLM': 0.0, 'CMT': 0.0, 'WAVES': 0.0, 'WABI': 0.0, 'GTO': 0.0, 'ICX': 0.0, 'OST': 0.0, 'ELF': 0.0, 'AION': 0.0, 'WINGS': 0.0, 'BRD': 0.0, 'NEBL': 0.0, 'NAV': 0.0, 'VIBE': 0.0, 'LUN': 0.0, 'TRIG': 0.0, 'APPC': 0.0, 'CHAT': 0.0, 'RLC': 0.0, 'INS': 0.0, 'PIVX': 0.0, 'IOST': 0.0, 'STEEM': 0.0, 'NANO': 0.0, 'AE': 0.0, 'VIA': 0.0, 'BLZ': 0.0, 'SYS': 0.0, 'RPX': 0.0, 'NCASH': 0.0, 'POA': 0.0, 'ONT': 0.0, 'ZIL': 0.0, 'STORM': 0.0, 'XEM': 0.0, 'WAN': 0.0, 'WPR': 0.0, 'QLC': 0.0, 'GRS': 0.0, 'CLOAK': 0.0, 'LOOM': 0.0, 'BCN': 0.0, 'TUSD': 0.0, 'ZEN': 0.0, 'SKY': 0.0, 'THETA': 0.0, 'IOTX': 0.0, 'QKC': 0.0, 'AGI': 0.0, 'NXS': 0.0, 'SC': 0.0, 'NPXS': 0.0, 'KEY': 0.0, 'NAS': 0.0, 'MFT': 0.0, 'DENT': 0.0, 'ARDR': 0.0, 'HOT': 0.0, 'VET': 0.0, 'DOCK': 0.0, 'POLY': 0.0, 'VTHO': 2063.904624, 'ONG': 0.0, 'PHX': 0.0, 'HC': 0.0, 'GO': 0.0, 'PAX': 0.0, 'RVN': 0.0, 'DCR': 0.0, 'USDC': 0.0, 'MITH': 0.0, 'BCH': 0.0, 'BSV': 0.0, 'REN': 0.0, 'BTT': 0.0, 'USDS': 0.0, 'FET': 0.0, 'TFUEL': 0.0, 'CELR': 0.0, 'MATIC': 0.0, 'ATOM': 0.0, 'PHB': 0.0, 'ONE': 0.0, 'FTM': 0.0, 'BTCB': 0.0, 'USDSB': 0.0, 'ALGO': 0.0, 'ERD': 0.0, 'DOGE': 0.0}}"""

# orders = binance.fetch_orders('BNB/BTC')
# print(len(orders))
# print(orders)
# print('order_id: ' + str(orders[0]['id']))
# print('order_price: ' + str(orders[0]['price']))
# print('order_amount: ' + str(orders[0]['amount']))
#
# print('orderId: ' + str(orders[0]['info']['orderId']))
# exit()


# 创建订单. create_order(self, symbol, type, side, amount, price=None, params={})  buy
# new_order = binance.create_order(symbol='BNB/BTC', type='limit', side='sell', amount=0.85, price=0.0030952)
# print(new_order['info']['orderId'])  # 216136323
# exit()

# 取消订单
"""
{'info': {'symbol': 'BNBBTC', 'orderId': 216112047, 'clientOrderId': 'mSKVC90FodJu3VLnBEjgHF', 'transactTime': 1562421786483, 'price': '0.00309520', 'origQty': '0.85000000', 'executedQty': '0.00000000', 'cummulativeQuoteQty': '0.00000000', 'status': 'NEW', 'timeInForce': 'GTC', 'type': 'LIMIT', 'side': 'SELL'}, 'id': '216112047', 'timestamp': 1562421786483, 'datetime': '2019-07-06T14:03:06.483Z', 'lastTradeTimestamp': None, 'symbol': 'BNB/BTC', 'type': 'limit', 'side': 'sell', 'price': 0.0030952, 'amount': 0.85, 'cost': 0.0, 'average': None, 'filled': 0.0, 'remaining': 0.85, 'status': 'open', 'fee': None, 'trades': None}
"""
# delete_order = binance.cancel_order(id='216136323', symbol='BNB/BTC')
# print(delete_order)

# 获取open_orders
# open_orders = binance.fetch_open_orders('BNB/BTC')
# print(open_orders)

"""
[{'info': {'symbol': 'BNBBTC', 'orderId': 133982998, 'clientOrderId': 'and_e59df70e20f4479fb8284724e6808a82', 
'price': '0.00422410', 'origQty': '78.77000000', 'executedQty': '78.77000000', 'cummulativeQuoteQty': '0.33273235', 
'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'LIMIT', 'side': 'BUY', 'stopPrice': '0.00000000', 'icebergQty': '0.00000000',
 'time': 1554104060825, 'updateTime': 1554104085528, 'isWorking': True}, 
 'id': '133982998', 'timestamp': 1554104060825, 'datetime': '2019-04-01T07:34:20.825Z', 'lastTradeTimestamp': None, 'symbol': 'BNB/BTC', 'type': 'limit', 
 'side': 'buy', 'price': 0.0042241, 'amount': 78.77, 'cost': 0.33273235, 'average': 0.004224099911133681, 
 'filled': 78.77, 'remaining': 0.0, 'status': 'closed', 'fee': None, 'trades': None}, 
 {'info': {'symbol': 'BNBBTC', 'orderId': 216106130, 'clientOrderId': 'web_506bb43a60ea4ea89701d3a3a0f4b2b8', 'price': '0.00309520', 'origQty': '1.14000000', 'executedQty': '0.00000000', 'cummulativeQuoteQty': '0.00000000', 'status': 'NEW', 'timeInForce': 'GTC', 'type': 'LIMIT', 'side': 'SELL', 'stopPrice': '0.00000000', 'icebergQty': '0.00000000', 'time': 1562420837356, 'updateTime': 1562420837356, 'isWorking': True}, 
 'id': '216106130', 'timestamp': 1562420837356, 'datetime': '2019-07-06T13:47:17.356Z', 'lastTradeTimestamp': None, 'symbol': 'BNB/BTC', 'type': 'limit', 'side': 'sell', 'price': 0.0030952, 'amount': 1.14, 'cost': 0.0, 'average': None, 'filled': 0.0, 'remaining': 1.14, 'status': 'open', 'fee': None, 'trades': None}
 ]
 
"""

# 获取close_orders
closed_orders = binance.fetch_closed_orders('BTC/USDT')
print(closed_orders)


# binance.post_order_id_cancel({
# })



