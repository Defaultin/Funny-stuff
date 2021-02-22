from random import uniform
from matplotlib import pyplot as plt


BASE_CAPITAL = 10_000
TRADE_VOLUME = 50
TIME = 200
COMMISSION = 0.01


class Value:
    def __init__(self, value):
        self.value = value

    def __get__(self, obj, obj_type):
        return self.value
        
    def __set__(self, obj, value):
        self.value = value - value * obj.commission
        
    def __delete__(self, obj):
        pass
    

class Account:
    BTC = Value(0)
    USD = Value(BASE_CAPITAL)
    def __init__(self, commission):
        self.commission = commission

    def sell(self, bct, rate):
        self.BTC -= bct
        self.USD += bct * rate

    def buy(self, usd, rate):
        self.USD -= usd
        self.BTC += usd / rate
    

def get_rate(N, start=50000):
    rate = [start]
    for _ in range(N):
        current = rate[-1]
        rate.append(current + uniform(-100, 100))
    return rate


def trade(N, volume, commission):
    rate = get_rate(N)
    account = Account(commission)
    purchases, sales = [], []
    history = {
        "last_buy": 0, 
        "last_sell": 0, 
        "last_rate": 0, 
        "penult_rate": 0
    }

    account.buy(volume, rate[0])
    history["last_buy"] = rate[0]
    history["last_rate"] = rate[0]
    history["penult_rate"] = rate[0]

    for i, current_rate in enumerate(rate):
        # sharp increasing
        if history["penult_rate"] > history["last_rate"] < current_rate and history["last_sell"] >= current_rate:
            history["last_rate"], history["penult_rate"] = current_rate, history["last_rate"]
            history["last_buy"] = current_rate
            account.buy(volume, current_rate)
            purchases.append((i, current_rate))
        # sharp descending
        elif history["penult_rate"] < history["last_rate"] > current_rate and history["last_buy"] <= current_rate:
            history["last_rate"], history["penult_rate"] = current_rate, history["last_rate"]
            history["last_sell"] = current_rate
            account.sell(account.BTC, current_rate)
            sales.append((i, current_rate))
        # continuous increasing / descending
        else:
            history["last_rate"], history["penult_rate"] = current_rate, history["last_rate"]

    account.sell(account.BTC, current_rate)
    print(f'USD: {account.USD}')
    plt.plot(range(N+1), rate)
    plt.scatter([i[0] for i in purchases], [i[1] for i in purchases], c='green')
    plt.scatter([i[0] for i in sales], [i[1] for i in sales], c='red')
    plt.title("BTC - USD");
    plt.legend(["Rate", "Purchases", "Sales"])


if __name__ == "__main__":
    trade(TIME, TRADE_VOLUME, COMMISSION)