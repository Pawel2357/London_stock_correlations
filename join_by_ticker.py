import argparse
import pickle
import pandas as pd


def remove_end(filename, col_names):
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

    constituents_100 = pd.read_csv(args.filename_1, sep=" ", names=columns_1)
    constituents_100['ticker'] = constituents_100['ticker'].apply(lambda x: x[:-2])
    stock_codes = pd.read_csv(args.filename_2, sep=" ", names=columns_2)
    data_industries = pd.read_csv(args.filename_3, names=["name", "ticker", "industry", "a", "b"])

    stock_codes_industry = pd.merge(stock_codes, data_industries, on='ticker', how='inner')

    ftse_100_industries = pd.merge(constituents_100, data_industries, on='ticker', how='inner')
    ftse_100_stock_codes_intersection = pd.merge(constituents_100, stock_codes, on='ticker', how='inner')

    ftse_100_stock_codes_intersection.to_csv("./ftse_100_stock_codes_intersection.csv")


