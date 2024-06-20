import sys
import glob
import os
import json
import re
import pandas as pd

def get_column_names(schemas, ds_name, sorting_key='column_position'):
    column_details = schemas[ds_name]
    columns = sorted(column_details, key=lambda col: col[sorting_key])
    return [col['column_name'] for col in columns]

def read_csv(file, schemas):
    file_path_list = file.split('/')
    ds_name = file_path_list[-2]
    columns = get_column_names(schemas, ds_name)
    df = pd.read_csv(file, names=columns)
    return df

def to_json(df, tgt_base_dir, ds_name, file_name):
    json_file_path = f'{tgt_base_dir}/{ds_name}/{file_name}'
    os.makedirs(f'{tgt_base_dir}/{ds_name}', exist_ok=True)
    df.to_json(
        json_file_path,
        orient='records',
        lines=True
    )
    
def file_converter(src_base_dir, tgt_base_dir, ds_name):
    schemas = json.load(open(f'{src_base_dir}/schemas.json'))
    files = glob.glob(f'{src_base_dir}/{ds_name}/part-*')
    #print(files)
    for file in files:
        df = read_csv(file, schemas)
        file_name = re.split('[/\\\]', file)[-1]
        to_json(df, tgt_base_dir, ds_name, file_name)

def process_files(ds_names=None):
    src_base_dir = os.environ.get('SRC_BASE_DIR') 
    tgt_base_dir = os.environ.get('TGT_BASE_DIR')
    schemas = json.load(open(f'{src_base_dir}/schemas.json'))
    #print(schemas)
    #a=schemas.keys()
    #print(a)
    if not ds_names:
        ds_names = schemas.keys()
    for ds_name in ds_names:
        if ds_name not in schemas:
            print(f'{ds_name} is not there in the schemas')
        else:
            print(f'Processing {ds_name}')
            file_converter(src_base_dir, tgt_base_dir, ds_name)
                
        
if __name__=="__main__" :
    if len(sys.argv) == 2:
        ds_names=json.loads(sys.argv[1])
        process_files(ds_names)
    else:
        process_files()