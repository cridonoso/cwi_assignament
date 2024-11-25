import pandas as pd


def format_table(row):
    table = []
    for x in row:
        table.append(list(x))
    t = pd.DataFrame(table[1:], columns=table[0])
    return t