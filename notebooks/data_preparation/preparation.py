import os
from IPython.display import display

import pandas as pd


# Get All CSV Files Path From A Folder
def get_files_path(folder):
    all_files = os.listdir(folder)
    file_names = [file.replace(".csv", "") for file in all_files if file.endswith(".csv")]
    file_paths = [folder + file for file in all_files if file.endswith(".csv")]

    file_details = {}
    for name, path in zip(file_names, file_paths):
        file_details[name] = path

    return file_details


# Get and Load Raw Data Into a List
def get_processed_df(path, cols, category):
    df = pd.read_csv(path)
    df = df.loc[:, cols]
    if len(cols) == 4:
        df.rename(columns={
            cols[0]: "title",
            cols[1]: "description",
            cols[2]: "genres",
            cols[3]: "rating"},
            inplace=True,
            errors='raise'
        )
    elif len(cols) == 3:
        df.rename(columns={
            cols[0]: "title",
            cols[1]: "description",
            cols[2]: "genres"},
            inplace=True,
            errors='raise'
        )
    df = df.dropna(axis=0, how="any")
    df = df.drop_duplicates(subset="title", keep='first')
    df = df.drop_duplicates(subset="description", keep='first')

    df["primary_genre"] = get_primary_gen(df)
    df["category"] = category
    return df


# Get All DataFrames
def get_all_df(path, cols, category):
    csv_file_paths = get_files_path(path)

    df_list = {}
    for name, path in csv_file_paths.items():
        df_list[name] = get_processed_df(path, cols, category)

    return df_list


# Get Combined Dataframes
def get_combined_df(df_dict):
    df_list = list(df_dict.values())
    combined_df = pd.concat(df_list, axis=0)
    return combined_df


# Clean Dataframe
def drop_duplicate(df):
    df = df.drop_duplicates(subset="title", keep="first")
    df = df.drop_duplicates(subset="description", keep="first")
    return df


# Get Primary Genre
def get_primary_gen(df):
    primary_genre = []

    for i in range(df.shape[0]):
        primary_genre.append(df["genres"].iloc[i].split(",")[0])

    return primary_genre


# Get DataFrame Information
def get_df_info(df):
    print("Shape of the dataframe: ", df.shape)
    print("The DataFrame: ")
    display(df.head())
    print("All Data Types: ")
    display(df.dtypes)
    print("Null Values:")
    display(df.isna().sum())
    try:
        print("Duplicate Movie Name Count: ", df["title"].duplicated().sum())
    except Exception:
        pass
    print("Duplicate Description Count: ", df["description"].duplicated().sum())
    print("DataFrame Details:")
    display(df.describe(include="all"))


# Convert DataFrame to CSV and Save
def write_dataframe_to_csv(path, dataframe):
    if os.path.exists(path):
        print(f"The file already exists ...! [Find the file in the location '{path}']")
    else:
        dataframe.to_csv(path, index=False)
        print("Dataframe saved successfully: ", path)


if __name__ == "__main__":
    pass
