
# ...


#breakpoint()
# type(df["value"][0]) #> str

# new column as float version of original strings column
df["unemployment_rate"] = df["value"].astype(float)

# remove original column to clean up
df.drop(columns=["value"], inplace=True)
