
def common_tickers(stock_exchange_1, stock_exchange_2):
    return stock_exchange_1.intersection(stock_exchange_2)


def uncommon_tickers(stock_exchange_1, stock_exchange_2):
    return stock_exchange_1.difference(stock_exchange_2)


def all_tickers(stock_exchange_1, stock_exchange_2):
    return stock_exchange_1.union(stock_exchange_2)


def has_common_tickers(stock_exchange_1, stock_exchange_2):
    if common_tickers(stock_exchange_1, stock_exchange_2):
        return True
    else:
        return False
