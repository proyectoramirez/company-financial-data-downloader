import argparse

DEFAULT_COMPANY_LIST_FILE = "./companies.csv"

__parser__ = argparse.ArgumentParser()

__parser__.add_argument("-c", "--companies", dest="company_file",
                        default=DEFAULT_COMPANY_LIST_FILE)

args = __parser__.parse_args()
