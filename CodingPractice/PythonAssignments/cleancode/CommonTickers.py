
def common_tickers(NYSE, LON):
    common_ticker = set()
    for t in NYSE:
        for e in LON:
            if t == e:
                return common_ticker.add(e)
