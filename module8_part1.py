class Vehicle:
    def __init__(self, name, mileage):
        self.__name = name
        self.__mileage = mileage

    def get_vehicle_type(self, wheels):
        if wheels == 2:
            return f"Это мотоцикл марки {self.__name}"
        elif wheels == 3:
            return f"Это трицикл марки {self.__name}"
        elif wheels == 4:
            return f"Это автомобиль марки {self.__name}"
        else:
            return "Я не знаю таких ТС"

    def get_vehicle_advice(self):
        if self.__mileage < 50000:
            return f"Неплохо! {self.__name} можно брать!"
        elif self.__mileage < 100000:
            return f"{self.__name} надо внимательно проверить!"
        elif self.__mileage < 150000:
            return f"{self.__name} надо провести полную диагностику!"
        else:
            return f"{self.__name} лучше не покупать!"


class Soldier:
    def __init__(self, name, lastname, age, rank, city):
        self.__name = name
        self.__lastname = lastname
        self.__age = age
        self.__rank = rank
        self.__city = city

    def get_salary_supplement(self, length_of_service):
        if length_of_service > 5:
            return f"{self.__name} {self.__lastname} за {length_of_service} лет надбавка к зарплате составляет 2500р."
        if length_of_service > 10:
            return f"{self.__name} {self.__lastname} за {length_of_service} лет надбавка к зарплате составляет 5000р."
        if length_of_service > 15:
            return f"{self.__name} {self.__lastname} за {length_of_service} лет надбавка к зарплате составляет 7500р."
        if length_of_service > 20:
            return f"{self.__name} {self.__lastname} за {length_of_service} лет надбавка к зарплате составляет 10000р."
        else:
            return f"{self.__name} {self.__lastname} за {length_of_service} лет надбавки к зарплате не предусмотрено."

    def get_information(self):
        return f"{self.__rank} {self.__name} {self.__lastname}, {self.__age} лет. Работает в городе {self.__city}"

    def transfer(self, another_city):
        self.__city = another_city

    def up_rank(self, new_rank):
        self.__rank = new_rank


bmw_auto = Vehicle("BMW", 135000)
print(bmw_auto.get_vehicle_advice())
ducati_moto = Vehicle("Ducati", 25000)
print(ducati_moto.get_vehicle_type(2))
triscooter = Vehicle("TRISCOOTER", 165000)
print(triscooter.get_vehicle_advice())
honda_auto = Vehicle("Honda", 15000)
print(honda_auto.get_vehicle_type(4))

semen_vatnikov = Soldier("Семен", "Ватников", "25", "Капитан", "Уфа")
print(semen_vatnikov.get_information())
alena_trubkina = Soldier("Алена", "Трубкина", "45", "Майор", "Лабытнанги")
print(alena_trubkina.get_information())
print(alena_trubkina.get_salary_supplement(20))
egor_agafonov = Soldier("Егор", "Агафонов", "30", "Мичман", "Владивосток")
print(egor_agafonov.get_information())
egor_agafonov.transfer("Калининград")
egor_agafonov.up_rank("Старший Мичман")
print(egor_agafonov.get_information())
