import pandas as pd
from pipeline import clean


def test_clean():
    df = pd.DataFrame(
        [["Ali", " karachi ", 21, 80], ["Ali", "KARACHI", 21, 80]],
        columns=["name", "city", "age", "score"],
    )

    assert clean(df)["city"].tolist() == ["Karachi"]