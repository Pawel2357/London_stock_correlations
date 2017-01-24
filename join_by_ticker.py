import argparse
import pickle


def preproces_data(filename, col_names):
    data = pd.read_csv(filename, sep=" ", header = None)
    data.columns = col_names
    return data

def compute_join_by_ticker(df_1, df_2, col_name):
    dataframe = pd.concat([df_1, df_2], axis=1, join_axes=[df_1[col_name]])
    return dataframe

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename_1",
        help = "txt filename")
    parser.add_argument("column_names_1",
        help = "txt filename")
    parser.add_argument("filename_2",
        help = "list of column names in pickle")
    parser.add_argument("column_names_2",
        help = "list of column names in pickle")
