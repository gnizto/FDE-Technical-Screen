import pandas as pd

def run(path_csv: str):
    df = pd.read_csv(path_csv, usecols=[0,1,2,3], dtype=str)
    for col in df:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype(float)
    df = df[~df.isna().any(axis=1)]
    df = df[~((df["Width"] <= 0) | (df["Height"] <= 0) | (df["Length"] <= 0) | (df["Mass"] <= 0))]
    
    df["Volume"] = df.apply(lambda row: volume(row["Width"], row["Height"], row["Length"]), axis=1)
    df["Sort"] = df.apply(lambda row: sort(row["Width"], row["Height"], row["Length"], row["Mass"]), axis=1)
    
    total = len(df)
    counting = df.groupby(by="Sort")["Sort"].agg(["count"])
    counting["Percent"] = (counting.values / total) * 100

    summary_mass = df.groupby(by="Sort")["Mass"].agg(["mean","min","max"])
    summary_volume = df.groupby(by="Sort")["Volume"].agg(["mean","min","max"])


    print("--- COUNT SUMMARY ---")
    print(counting.to_markdown())
    print("--- MASS SUMMARY ---")
    print(summary_mass.to_markdown())
    print("--- VOLUME SUMMARY ---")
    print(summary_volume.to_markdown())


def sort(width: float, height: float, length: float, mass: float) -> str:
    is_bulky = _is_bulky(width, height, length)
    is_heavy = _is_heavy(mass)

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

def _is_bulky(width: float, height: float, length: float) -> bool:
    BULKY_VOLUME_REF = 1_000_000
    BULKY_SIDE_REF = 150

    is_area_bulky = volume(width, height, length) >= BULKY_VOLUME_REF
    is_side_bulky = max(width, height, length) >= BULKY_SIDE_REF
    return is_area_bulky or is_side_bulky 

def volume(width: float, height: float, length: float) -> float:
    return width * height * length

def _is_heavy(mass: float) -> bool:
    HEAVY_REF = 20
    return mass >= HEAVY_REF

if __name__ == "__main__":
    run("./files/packages.csv")
