from pandas import read_csv
from parsed_args import args


def getCompanies():
    csv = read_csv(args.company_file, header=None, squeeze=True)
    return csv
