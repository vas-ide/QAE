import random


class Personel:

    def __init__(self, file):
        self.extract_file = file
        self.surname = []
        self.name = []
        self.lastname = []
        self.surname_man = []
        self.name_man = []
        self.lastname_man = []
        self.city = []
        self.employees = []
        self.all_position = ["+", "-"]
        self.final_lst = []

    def extract_info(self):
        with open(self.extract_file, 'r', encoding='1251') as file:
            print(f"{file.name:>50} - encoding {file.encoding}")
            for line in file:
                lst_line = line.split(",")
                lst_line = [item.replace('\xa0', '') for item in lst_line]
                lst_line = [item.replace('\n', '') for item in lst_line]
                lst_line = [item.replace(item, item) for item in lst_line if len(item) > 1]
                if lst_line[0] == 'ФИО':
                    self.final_lst.append(lst_line)
                if lst_line[1] != "Город":
                    self.city.append(lst_line[1])
                lst_line = lst_line[0].split(" ")

                if lst_line[0] == 'ФИО':
                    pass
                elif lst_line[2][-1] == "а":
                    self.surname.append(lst_line[0])
                    self.name.append(lst_line[1])
                    self.lastname.append(lst_line[2])
                else:
                    self.surname_man.append(lst_line[0])
                    self.name_man.append(lst_line[1])
                    self.lastname_man.append(lst_line[2])
        # print(self.surname, "\n", self.name, "\n", self.lastname,"\n", self.surname_man, "\n", self.name_man, "\n",
        #       self.lastname_man)
        # print(self.final_lst)
        # print(self.city)

    def generate_people(self):
        for surname in self.surname:
            for name in self.name:
                for lastname in self.lastname:
                    new_data = [f"{surname} {name} {lastname}", random.choice(self.city)]
                    for _ in range(3):
                        new_data.append(random.choice(self.all_position))
                    self.final_lst.append(new_data)
        for surname in self.surname_man:
            for name in self.name_man:
                for lastname in self.lastname_man:
                    new_data = [f"{surname} {name} {lastname}", random.choice(self.city)]
                    for _ in range(3):
                        new_data.append(random.choice(self.all_position))
                    self.final_lst.append(new_data)

        print(len(self.final_lst), self.final_lst)

    def write_file(self):
        pass

    def run(self):
        self.extract_info()
        self.generate_people()
        self.write_file()


job = Personel('data.csv')
job.run()
