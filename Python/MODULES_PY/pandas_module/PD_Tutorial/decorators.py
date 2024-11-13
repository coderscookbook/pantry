# TODO: add https://python.plainenglish.io/five-python-wrappers-that-can-reduce-your-code-by-half-af775feb1d5

import time as t
import pandas as pd # type: ignore

# Prints a visual separator
def Sep() -> None:
    return print('----------------------------------------------------------------------------------------------------------------')

# Timing decorator
def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = t.time()
        result = func(*args, **kwargs)
        end_time = t.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds...")
        return result
    return wrapper

# Times and Loads csv data to a DF
@time_it
def CsvToDF(filepath: str) -> pd.DataFrame:
  data = pd.read_csv(filepath)
  print(f"Data imported successfully from '{filepath}'")
  return data

# Returns original DF head/tail, shape + head/tail of new DF, Dtypes + head/tail of new DF
def VerifyData(dataframe: pd.DataFrame, df_name: str="DataFrame", rows_to_display: int=5) -> None:
    """Prints n-rows of DF head and tail, DF dtypes, DF shape, and DF summary statistics
    Args:
        dataframe (pd.DataFrame): 
        df_name (str): 
        rows_to_display (int): 
    """
    Sep()
    print(f"<<<<<<<<<<<<<<<<\t{df_name}: Head\t\t>>>>>>>>>>>>>>>>\n", dataframe.head(rows_to_display).to_string(), "\n")
    print(f"<<<<<<<<<<<<<<<<\t{df_name}: Tail\t\t>>>>>>>>>>>>>>>>\n", dataframe.tail(rows_to_display).to_string(), "\n")
    print(f"<<<<<<<<<<<<<<<<\t{df_name}: DTypes\t>>>>>>>>>>>>>>>>\n",dataframe.dtypes, "\n")    # !!!: 'object' refers to strings
    print(f"<<<<<<<<<<<<<<<<\t{df_name}: Shape\t>>>>>>>>>>>>>>>>\n",dataframe.shape, "\n")
    print(f"<<<<<<<<<<<<<<<<\t{df_name}: Statistics\t>>>>>>>>>>>>>>>>\n",dataframe.describe().to_string(), "\n")
    print("<<<<<<<<<<<<<<<< End of VerifyData! >>>>>>>>>>>>>>>>")
    Sep()

def main():
    print("Decorators module active...") 

if __name__ == "__main__":
    main()