import pandas as pd


def load():
    return pd.read_csv("students_messy.csv")


def clean(df):
    df = df.copy()
    df["name"] = df["name"].str.strip().replace("", pd.NA)
    df["city"] = df["city"].str.strip().str.title().replace("", pd.NA)
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["score"] = pd.to_numeric(df["score"], errors="coerce")

    df = df.dropna(subset=["name", "city", "age", "score"])
    return df.drop_duplicates().reset_index(drop=True)


def add_features(df):
    df = df.copy()
    df["passed"] = df["score"] >= 50
    df["score_rank"] = df["score"].rank(ascending=False, method="min").astype(int)
    return df


if __name__ == "__main__":
    df = load()
    df = clean(df)
    df = add_features(df)
    df.to_csv("students_clean.csv", index=False)