from binance.enums import *
from binance.client import Client
import config


client = Client(config.API_KEY, config.API_SECRET)


def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print("Sending order.")
        order = client.create_order(
            symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print(e)
        return False
    return True


if(__name__ == "__main__"):
    order_succedded = order(SIDE_BUY, 38, "CHZUSDT")
    if(order_succedded):
        print("Order succeded")
    else:
        print("Order fail")
