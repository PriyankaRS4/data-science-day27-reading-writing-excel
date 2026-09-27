import pandas as pd

df = pd.read_excel("superstore_input.xlsx", sheet_name="Superstore")
df.columns = [str(c).strip() for c in df.columns]
df = df.dropna(how="all").drop_duplicates().copy()

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

for col in ["Sales", "Profit", "Quantity", "Discount"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

df.to_excel("superstore_processed.xlsx", sheet_name="Processed_Data", index=False)
print("Processed Excel output created successfully.")
print(df.head())
