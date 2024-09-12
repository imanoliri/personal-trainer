from config import PERSONAL_DATA_INPUT_FILE, PERSONAL_DATA_FILE
import pandas as pd
import bioparameters


def add_bioparameters_to_personal_data():
    df_personal = pd.read_csv(PERSONAL_DATA_INPUT_FILE)
    add_bioparameters(df_personal).to_csv(PERSONAL_DATA_FILE)


def add_bioparameters(df: pd.DataFrame) -> pd.DataFrame:
    return df.apply(lambda x: pd.Series(calculate_bioparameters(x.to_dict())), axis=1)


def calculate_bioparameters(data: dict) -> dict:
    """
    - BMR (Basal Metabolic Rate)
    - BMI (Body Mass Index)
    - ...
    """
    data["BMR"] = int(bioparameters.BMR(**data))
    data["BMI"] = round(bioparameters.BMI(**data), 1)
    data["BMI_prime"] = round(bioparameters.BMI_prime(**data), 2)
    data["BMI_new"] = round(bioparameters.BMI_new(**data), 1)
    data["BMI_corpulence"] = round(bioparameters.BMI_corpulence(**data), 1)

    return data
