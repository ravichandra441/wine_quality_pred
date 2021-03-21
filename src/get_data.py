## read params
##process
##return data frame

import os
import yaml
import pandas as pd
import argparse

def get_data(config_path):
    pass

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()