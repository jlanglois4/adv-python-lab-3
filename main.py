import csv
import json
from pathlib import Path

chr_types = {}
output_list = []


def main():
    file_path = Path.cwd() / "data.json"
    with file_path.open() as my_file:
        lines = my_file.read().replace('\n', '')
        json_data = json.loads(lines)
        character_list = json_data["charcters"]
        for a_line in character_list:
            type_of_character = a_line["Type"]
            if type_of_character in chr_types:
                chr_types[type_of_character] += int(a_line["Health"])
            else:
                chr_types[type_of_character] = int(a_line["Health"])
    for key in chr_types:
        print(f"{key} {chr_types[key]}")


def output():
    with open('./output.csv', 'wt') as f:
        csv_writer = csv.writer(f, delimiter='|')
        csv_writer.writerows(output_list)


if __name__ == "__main__":
    main()
    output()
