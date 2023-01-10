import os
import pandas as pd


def get_tasks(files_path: str):
    tasks = set()

    for file in os.listdir(files_path):
        if "sensor" not in file:
            continue

        df = pd.read_csv(f"{files_path}/{file}")
        tasks = tasks | set(df["task"].unique().flatten())

    tasks = tasks - {"quest", "post"}

    print(2)
    return 2
