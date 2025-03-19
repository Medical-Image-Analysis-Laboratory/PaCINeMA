import pandas as pd


df = pd.read_csv("/home/vzalevskyi/Desktop/Fetal_MRI_CHUV (2).csv")

subs = [
    "chuv003",
    "chuv005",
    "chuv007",
    "chuv009",
    "chuv010",
    "chuv011",
    "chuv012",
    "chuv012",
    "chuv014",
    "chuv016",
    "chuv020",
    "chuv026",
    "chuv027",
    "chuv028",
    "chuv030",
    "chuv031",
    "chuv034",
    "chuv035",
    "chuv036",
    "chuv037",
    "chuv038",
    "chuv041",
    "chuv042",
    "chuv043",
    "chuv045",
    "chuv048",
    "chuv050",
    "chuv051",
    "chuv052",
    "chuv053",
    "chuv054",
    "chuv056",
    "chuv059",
    "chuv060",
    "chuv061",
    "chuv063",
    "chuv067",
    "chuv069",
    "chuv071",
    "chuv072",
]


print(df[df["chuv_id"].isin(subs)]["Results"].values)
