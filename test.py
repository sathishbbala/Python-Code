import pandas as pd
import hashlib

def dataframe_hash(df: pd.DataFrame) -> str:
    # Step 1: normalize column order
    df = df.sort_index(axis=1)

    # Step 2: normalize NULLs and types
    df = df.fillna("").astype(str)

    # Step 3: sort rows deterministically
    df = df.sort_values(by=list(df.columns)).reset_index(drop=True)

    # Step 4: hash each row
    row_hashes = df.apply(
        lambda row: hashlib.sha256(
            "|".join(row.values).encode("utf-8")
        ).hexdigest(),
        axis=1
    )

    # Step 5: aggregate row hashes into a final hash
    final_hash = hashlib.sha256(
        "".join(row_hashes).encode("utf-8")
    ).hexdigest()

    return final_hash

df1 = pd.read_excel("data/advertising.xlsx")
df2 = pd.read_excel("data/advertising1.xlsx")

# Normalize
# df1 = df1.sort_index(axis=1).sort_values(by=list(df1.columns)).reset_index(drop=True)
# df2 = df2.sort_index(axis=1).sort_values(by=list(df2.columns)).reset_index(drop=True)

# print(df1.equals(df2))  # True if dataframes are equal, False otherwise 
hash1 = dataframe_hash(df1)
hash2 = dataframe_hash(df2)

print("Hash 1:", hash1)
print("Hash 2:", hash2)

if hash1 == hash2:
    print("✅ Data is identical")
else:
    print("❌ Data differs")