import csv
import argparse


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('o')
    parser.add_argument('-b', '--brand')
    parser.add_argument('-c', '--color')
    parser.add_argument('-y', '--year')
    parser.add_argument('-f', '--fuel')
    parser.add_argument('-r', '--reg_num')
    arguments = parser.parse_args()
    if arguments.brand is None \
            and arguments.color is None \
            and arguments.year is None \
            and arguments.fuel is None:
        print("Incorrect arguments for search")
        exit()
    return arguments


def get_data_csv(arguments):
    with open(arguments.o, mode='r', encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=';')
        polished_data = []
        for row in file_reader:
            if row['BRAND'] == arguments.brand \
                    and row['COLOR'] == arguments.color \
                    and row['MAKE_YEAR'] == arguments.year \
                    and row['FUEL'] == arguments.fuel:
                polished_data.append({'D_REG': row['D_REG'],
                                      'BRAND': row['BRAND'],
                                      'MODEL': row['MODEL'],
                                      'COLOR': row['COLOR'],
                                      'MAKE_YEAR': row['MAKE_YEAR'],
                                      'FUEL': row['FUEL'],
                                      'N_REG_NEW': row['N_REG_NEW']})
    return polished_data


def get_filename(arguments) -> str:
    return f'brand-{arguments.brand}-year-{arguments.year}.csv'


def write_to_csv(data, arguments):

    with open(get_filename(arguments), mode='w', encoding='utf-8') as w_file:
        names = ['D_REG', 'BRAND', 'MODEL', 'COLOR', 'MAKE_YEAR', 'FUEL', 'N_REG_NEW']
        file_writer = csv.DictWriter(w_file, delimiter=';', lineterminator='\r', fieldnames=names)
        file_writer.writeheader()
        file_writer.writerows(data)


if __name__ == "__main__":
    args = arg_parser()
    csv_data = get_data_csv(args)
    write_to_csv(csv_data, args)