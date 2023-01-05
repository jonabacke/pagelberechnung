#!/usr/bin/env python
import pandas as pd
# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

input_signal = 20
node_loss = 3
distance_loss = 1
df_table = pd.DataFrame()


class calc_signal:
    def __init__(self):
        pass

    def load_table(self):
        self.df_table = pd.read_csv('table.csv')
        self.df_table = self.df_table.set_index('label')
        self.df_table = self.df_table.fillna(0)
        print(df_table)

    def calc_signal(self, column, signal_strength, last_node):
        if signal_strength <= 0:
            return
        self.df_table['node_signal'].loc[column] += signal_strength

        for row in self.df_table[column].index:
            if self.df_table[column][row] != 0 and row != last_node:
                self.calc_signal(column=row, signal_strength=signal_strength - self.df_table[column][row] * distance_loss - 1, last_node=column)

    def print_in_table(self):
        self.df_table.to_csv('table.csv')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calc_table = calc_signal()
    calc_table.load_table()
    calc_table.df_table['node_signal'] = 0
    calc_table.calc_signal(column=calc_table.df_table.columns[0], signal_strength=input_signal, last_node=None)
    calc_table.print_in_table()
    print(calc_table.df_table)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
