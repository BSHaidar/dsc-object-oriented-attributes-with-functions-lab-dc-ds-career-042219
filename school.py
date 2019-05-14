class School():

    def __init__(self, name):
        self.name = name
        self.roster = {}

    def add_student(self, fullname, grade):
        self.fullname = fullname
        self.grade = grade
        if grade in self.roster:
            self.roster[grade].append(fullname)
        else:
            self.roster[grade] = [fullname]

    def grade_1(self, grade):
        return self.roster[grade]

    def sort_roster(self):
        sort_dict = self.roster
        for key in sort_dict:
            sort_dict[key].sort()
        return sort_dict
