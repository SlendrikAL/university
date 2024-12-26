class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def get_info(self):
        return 'Имя', self.name, 'Идентификационный номер', self.id

class Manager(Employee):
    def __init__(self, department,name,id):
        self.department = department
        Employee.__init__(self,name,id)
    def manage_project(self):
        return self.name, 'выполняет проект'

class Technician(Employee):
    def __init__(self,specialization,name,id):
        self.specialization = specialization
        Employee.__init__(self,name,id)
    def perform_maintenance(self):
        return self.name, 'Начал выполнение технического обслуживания'
class TechManager(Manager, Technician):
    def __init__(self,name,id,department,specialization):
        Manager.__init__(self,name,id,department)
        Technician.__init__(self,specialization,name,id)
        self.team = []
    def add_employee(self,employee):
        self.team.append(employee)
    def get_team_info(self):
        return [employee.get_info() for employee in self.team]

employee = Employee('Иванов Сергей Давидович', 5848)
print(employee.get_info())

manager = Manager('Дизайн','Покрышкин Николай Альбертович',3344)
print(manager.manage_project())

technician = Technician('Разработчик', 'Клавишкин Александр Артёмович', 5665)
print(technician.perform_maintenance())

techmanager = TechManager('Ломов Кирилл Богданович', 2331, 'Тестировка', 'Тестер')
techmanager.add_employee(employee)
techmanager.add_employee(manager)
techmanager.add_employee(technician)
print(techmanager.get_team_info())
