import json
import requests
import time
import datetime
import argparse


def get_data_url(arguments):
    time.sleep(0.5)
    return requests.get("https://api.exchangerate.host/convert",
                        params={"from": arguments.currency_from,
                                "to": arguments.currency_to,
                                "amount": arguments.amount,
                                "date": arguments.start_date}).json()


def arg_parser():
    parser = argparse.ArgumentParser(description="Online exchange rates")
    parser.add_argument("currency_from")
    parser.add_argument("currency_to")
    parser.add_argument("amount")
    parser.add_argument("-sd", "--start_date", default=datetime.datetime.now())
    return parser.parse_args()


def list_creation():
    new_list = [['date', 'from', 'to', 'amount', 'rate', 'result']]
    list_add = []
    count = 0
    try:
        args.start_date = datetime.datetime.strptime(args.start_date, "%Y-%m-%d")
    except ValueError:
        args.start_date = datetime.datetime.now()
    while count <= 15 and args.start_date <= datetime.datetime.now():
        # print(count)
        list_data = get_data_url(args)
        for line in list_data:
            list_add = [list_data["date"],
                        list_data["query"]["from"],
                        list_data["query"]["to"],
                        list_data["query"]["amount"],
                        list_data["info"]["rate"],
                        list_data["result"]]
        new_list.append(list_add)
        count += 1
        args.start_date = args.start_date + datetime.timedelta(days=1)
    return new_list


def check_input():
    with open("symbols.json", 'r') as file:
        check_symbols = json.load(file)
        correct_list = check_symbols["symbols"]
        if args.currency_from not in correct_list:
            print("incorrect input argument \"currency_from\"")
            exit()
        if args.currency_to not in correct_list:
            print("incorrect input argument \"currency_to\"")
            exit()


args = arg_parser()
check_input()
result_list = list_creation()
print(result_list)
