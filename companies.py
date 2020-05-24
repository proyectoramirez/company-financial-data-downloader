from pandas import read_csv
from parsed_args import args


def getCompanies():
    return read_csv(args.company_file).iloc[0]
