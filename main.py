import csv
from pathlib import Path

chr_types = {}
output_list = []


def main():
    file_path = Path.cwd() / "data.csv"
    if file_path.exists():
        with file_path.open() as my_file:
            csv_reader = csv.reader(my_file)  # , delimiter='|'
            # skip headings // next(csv_reader)
            for line in csv_reader:
                type_of_character = line[0].split(',')[1].strip()
                output_list.append([type_of_character, line[1], line[2]])
                if type_of_character in chr_types:
                    chr_types[type_of_character] += int(line[2])
                else:
                    chr_types.update({type_of_character: int(line[2])})

        for key in chr_types:
            print(f"{key} {chr_types[key]}")


def output():
    with open('./output.csv', 'wt') as f:
        csv_writer = csv.writer(f, delimiter='|')
        csv_writer.writerows(output_list)


if __name__ == "__main__":
    main()
    output()