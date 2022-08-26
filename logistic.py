
class Road:
    id = None
    a = None
    b = None
    base_people = None
    people = None
    max_people = None
    houses = []
    output = []
    tables = []
    previos = []
    new = []
    def __init__(self, id, a, b, base_people, max_people, output, tables):
        self.id = id
        self.a = a
        self.b = b
        self.base_people = base_people
        self.people = base_people
        self.max_people = max_people
        self.output = output
        self.tables = tables
        self.previos = base_people
