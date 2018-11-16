
def common_tickers(stock_exchange_1, stock_exchange_2):
    return stock_exchange_1.intersection(stock_exchange_2)


def uncommon_tickers(stock_exchange_1, stock_exchange_2):
    return stock_exchange_1.difference(stock_exchange_2)