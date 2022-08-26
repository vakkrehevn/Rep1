class House:
    def __init__(self, x, y, width, height, number_of_floors, coefficient):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.area = width * height
        self.number_of_floors = number_of_floors
        self.coefficient = coefficient
        self.number_of_people = width * height * number_of_floors // coefficient
    def calculate_work_load_of_metro(self):
        # надо будет умножить на процент людей, ездящих на метро,
        # от всех пользующихся общественным транспортом
        return self.number_of_people * 0.6 * 0.35
    def calculate_work_load_of_road(self):
        return self.number_of_people * 0.4 / 1.2 * 0.35
    def calculate_work_load_of_schools(self):
        return self.number_of_people * 0.15
