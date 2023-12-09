#   LIGHT
import random


def home_work(file_name):
    with open(file_name, 'r', encoding='1251') as file:
        all_chois = ["1", "0"]
        with open("result_lite.txt", "a", encoding='utf-8') as string:
            string.write(f"{file.name:>50} - encoding {file.encoding}\n")
        for line in file:
            lst_line = line.split(",")
            lst_line = [item.replace('\xa0', '') for item in lst_line]
            lst_line = [item.replace('\n', '') for item in lst_line]
            lst_line = [item.replace(item, item) for item in lst_line if len(item) >= 1]
            if len(lst_line) < 3:
                [lst_line.append(random.choice(all_chois)) for _ in range(3)]
            lst_line = [item.replace('1', "+") for item in lst_line]
            lst_line = [item.replace('0', '-') for item in lst_line]
            # print(lst_line)
            answer_str = ""
            for numb, item in enumerate(lst_line):
                if numb == 0:
                    answer_str += f"{item:^35}"
                elif numb == 1:
                    answer_str += f"{item:^25}"
                else:
                    answer_str += f"{item:^15}"
            with open("result_lite.txt", "a", encoding='utf-8') as string:
                string.write(f"{answer_str}\n")
home_work("data.csv")