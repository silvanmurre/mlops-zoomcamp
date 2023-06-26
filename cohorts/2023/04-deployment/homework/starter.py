import pandas as pd
import pickle
import sys

from datetime import datetime
from pathlib import Path


def read_data(filename, categorical):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


def apply_model(input_file, output_file, run_date):
    categorical = ['PULocationID', 'DOLocationID']
    df = read_data(input_file, categorical)
    
    with open('model.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)

    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)

    print(f"The mean predicited duration for {run_date.year:04d}-{run_date.month:02d} is: {round(y_pred.mean(), 2)}")


def get_paths(run_date, taxi_type):
    year = run_date.year
    month = run_date.month 
    
    input_full = f'https://d37ci6vzurychx.cloudfront.net/trip-data/{taxi_type}_tripdata_{year:04d}-{month:02d}.parquet'
    
    output_folder = Path(f'output/{taxi_type}')
    output_folder.mkdir(parents=True, exist_ok=True)
    output_file = Path(f'{year:04d}-{month:02d}.parquet')
    output_full = output_folder / output_file
    return input_full, output_full


def ride_duration_prediction(
        taxi_type: str,
        run_date: datetime = None):
    
    input_file, output_file = get_paths(run_date, taxi_type)

    apply_model(input_file=input_file,
                output_file=output_file,
                run_date=run_date)


def run():
    taxi_type = sys.argv[1] # 'green'
    year = int(sys.argv[2]) # 2021
    month = int(sys.argv[3]) # 3

    ride_duration_prediction(taxi_type=taxi_type,
                             run_date=datetime(year=year, month=month, day=1))


if __name__ == '__main__':
    run()
