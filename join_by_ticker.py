import argparse
import pickle
import pandas as pd


def preproces_data(filename, col_names):
    data = pd.read_csv(filename, sep=" ", names=col_names)
    return data

def compute_join_by_ticker(df_1, df_2, col_name):
    dataframe = pd.concat([df_1, df_2], axis=1, join_axes=[df_1[col_name]])
    return dataframe

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename_1",
        help = "txt file")
    parser.add_argument("column_names_1",
        help = "list of column names in pickle")
    parser.add_argument("filename_2",
        help = "txt file")
    parser.add_argument("column_names_2",
        help = "list of column names in pickle")
    parser.add_argument("filename_3",
        help = "txt file")

    args = parser.parse_args()

    columns_1 = pickle.load(open(args.column_names_1, 'rb'))
    columns_2 = pickle.load(open(args.column_names_2, 'rb'))

    constituents_100 = preproces_data(args.filename_1, columns_1)

    stock_codes = preproces_data(args.filename_2, columns_2)

    data = pd.read_csv(args.filename_3)

    print constituents_100
    print stock_codes
    print data


