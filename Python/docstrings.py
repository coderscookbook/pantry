def VerifyData(dataframe: .DataFrame, df_name: str="DataFrame", rows_to_display: int=5) -> None:
    """Prints n-rows of DF head and tail, DF dtypes, DF shape, and DF summary statistics
    Args:
        dataframe (.DataFrame): 
        df_name (str): 
        rows_to_display (int): 
    """
    print(f"<<<<<<<<<<<<<<<<\t{df_name}: Head\t\t>>>>>>>>>>>>>>>>\n", dataframe.head(rows_to_display).to_string(), "\n")
    print(f"<<<<<<<<<<<<<<<<\t{df_name}: Tail\t\t>>>>>>>>>>>>>>>>\n", dataframe.tail(rows_to_display).to_string(), "\n")
    print(f"<<<<<<<<<<<<<<<<\t{df_name}: DTypes\t>>>>>>>>>>>>>>>>\n",dataframe.dtypes, "\n")    # !!!: 'object' refers to strings
    print(f"<<<<<<<<<<<<<<<<\t{df_name}: Shape\t>>>>>>>>>>>>>>>>\n",dataframe.shape, "\n")
    print(f"<<<<<<<<<<<<<<<<\t{df_name}: Statistics\t>>>>>>>>>>>>>>>>\n",dataframe.describe().to_string(), "\n")
    print("<<<<<<<<<<<<<<<< End of VerifyData! >>>>>>>>>>>>>>>>")


VerifyData()
