# File Format Converter

## Overview
The File Format Converter is a Python script that converts CSV files to JSON. This script reads CSV files based on a predefined schema and outputs JSON files in a specified directory.

## Features
- Convert CSV files to JSON format.
- Handle multiple datasets defined in a schema.
- Create output directories if they do not exist.

## Requirements
- Python 3.6+
- Pandas library

### Clone the Repository
Clone the repository to your local machine using the following command:

1. git clone https://github.com/MADDURISANKETH/File_Format_Converter.git
cd File_Format_Converter

2. Install Dependencies
    Install the necessary Python libraries using pip:
    pip install pandas
Prepare Environment Variables
Set the environment variables SRC_BASE_DIR and TGT_BASE_DIR to specify the source and target directories, respectively. You can set them in your terminal session:
export SRC_BASE_DIR=/path/to/source_directory
export TGT_BASE_DIR=/path/to/target_directory
Usage
Running the Script
To run the script, navigate to the project directory and execute the following command:
python file_converter.py '["dataset1", "dataset2"]'
Schema File
Ensure that your schemas.json file is located in the SRC_BASE_DIR. This file should contain the schema definitions for the datasets, specifying column names and positions.
Code Description
Functions
get_column_names(schemas, ds_name, sorting_key='column_position'): Retrieves column names for a given dataset based on the schema.
read_csv(file, schemas): Reads a CSV file into a pandas DataFrame using the schema.
to_json(df, tgt_base_dir, ds_name, file_name): Converts a DataFrame to a JSON file and saves it to the target directory.
file_converter(src_base_dir, tgt_base_dir, ds_name): Converts all CSV files for a given dataset to JSON format.
process_files(ds_names=None): Processes files for specified datasets or all datasets if none are specified.
Main Execution
The script can be executed with or without arguments. If no arguments are provided, it processes all datasets defined in the schema. If a JSON-formatted string of dataset names is provided, it processes only those datasets.
