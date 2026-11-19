import os
import pandas as pd

def test_datas():
    """This file tests the dataset to make
    sure the necessary coumns are included
    """
    df = pd.read_csv("data/compas-scores-two-years.csv")
    assert len(df) == 7214
    assert "two_year_recid" in df.columns
    assert "race" in df.columns



if __name__ == "__main__":
    test_datas()
    print("Passing all tests")
