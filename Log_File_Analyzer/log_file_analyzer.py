import pandas as pd

df = pd.read_csv(
        "Application.log",
        sep=" - ",
        names=["Level", "Message"],
        engine="python"
        )
print(df.head())
#Count total log entries.
print(f" total log entries : {len(df)}")
#Count ERROR occurrences.
print(f"ERROR DATA FRAME {df[df["Level"]=="ERROR"]}")
print(f"ERROR occurrence: {df[df["Level"]=="ERROR"].count()}")
#Count WARNING occurrences.
print(f"WARNING occurrence: {df[df["Level"]=="WARNING"].count()}")
#Count INFO occurrences.
print(f"INFO occurrence: {df[df["Level"]=="INFO"].count()}")
#Create
#errors.txt
#warnings.txt
#Store appropriate log entries inside those files.
df_error= df[df["Level"]=="ERROR"]
df_warning= df[df["Level"]=="WARNING"]
df_error.to_csv("errors.txt", sep="\t", index=False)
df_warning.to_csv("warnings.txt", sep="\t", index=False)

## meta data infor ##
print(df.info())
print("## describe ##")
print(df.describe())
print(df.head())
print(df.tail())
print(df.count())

## frequency analysis ##

print(df.groupby("Level").count())