
def common_tickers(stock_exchange_1, stock_exchange_2):
    return stock_exchange_1.intersection(stock_exchange_2)


def uncommon_tickers(stock_exchange_1, stock_exchange_2):
    return stock_exchange_1.difference(stock_exchange_2)


def all_tickers(stock_exchange_1, stock_exchange_2):
    return stock_exchange_1.union(stock_exchange_2)


def has_common_tickers(stock_exchange_1, stock_exchange_2):
    result = True
    for se1 in stock_exchange_1:
        for se2 in stock_exchange_2:
            if se1 == se2:
                result = True
                return result
        result = False
        return result
    return result
