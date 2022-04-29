import pandas as pd
import numpy as np


def make_dict():
    stock_stats = pd.read_csv("../japanstock/japan stock/jpx-tokyo-stock-exchange-prediction/train_files/stock_prices.csv")
    stock_stats2 = pd.read_csv("../japanstock/japan stock/jpx-tokyo-stock-exchange-prediction/train_files/secondary_stock_prices.csv")
    stock_names = pd.read_csv("../japanstock/japan stock/stock_list.csv")

    stock_data = {}

    for i in stock_names["SecuritiesCode"]:
        stock_data[i] = []

    for i in range(len(stock_stats)):
        new_data = [stock_stats['Open'][i], stock_stats['High'][i], stock_stats['Low'][i], stock_stats['AdjustmentFactor'][i], stock_stats['Target'][i]]
        stock_data[stock_stats['SecuritiesCode'][i]].append(new_data)

    for i in range(len(stock_stats2)):
        new_data = [stock_stats2['Open'][i], stock_stats2['High'][i], stock_stats2['Low'][i], stock_stats2['AdjustmentFactor'][i], stock_stats2['Target'][i]]
        stock_data[stock_stats2['SecuritiesCode'][i]].append(new_data)

    return stock_data