"""
Task 7_2
Create classes Employee, SalesPerson, Manager and Company with predefined functionality.

Create basic class Employee and declare following content:
• Attributes – `name` (str), `salary` and `bonus` (int), set with property decorator
• Constructor - parameters `name` and `salary`
• Method `bonus` - sets bonuses to salary, amount of which is delegated as `bonus`
• Method `to_pay` - returns the value of summarized salary and bonus.

Create class SalesPerson as class Employee inheritor and declare within it: • Constructor with parameters: `name`,
`salary`, `percent` – percent of plan performance (int, without the % symbol), first two of which are passed from
basic class constructor • Redefine method of parent class `bonus` in the following way: if the sales person completed
the plan more than 100%, their bonus is doubled (is multiplied by 2), and if more than 200% - bonus is tripled (is
multiplied by 3)

Create class Manager as Employee class inheritor, and declare within it: • Constructor with parameters: `name`,
`salary` and `client_number` (int, number of served clients), first two of which are passed to basic class
constructor. • Redefine method of parent class `bonus` in the following way: if the manager served over 100 clients,
their bonus is increased by 500, and if more than 150 clients – by 1000.

Create class Company and declare within it: • Constructor with parameters: `employees` – list of company`s employees
(made up of Employee/SalesPerson/Manager classes instances) with arbitrary length `n` • Method `give_everybody_bonus`
with parameter company_bonus (int) that sets the amount of basic bonus for each employee. • Method `total_to_pay`
that returns total amount of salary of all employees including awarded bonus • Method `name_max_salary` that returns
name of the employee, who received maximum salary including bonus.

Note:
Class attributes and methods should bear exactly the same names as those given in task description
Methods should return only target values, without detailed explanation within `return`
"""
from typing import List


class Employee:
    def __init__(self, name: str, salary: int):
        self._name = name
        self._salary = salary
        self._bonus = 0

    @property
    def name(self):
        """
        Get name of the employee.
        :return: name of the employee
        :rtype: str
        """
        return self._name

    @property
    def salary(self):
        """
        Get salary of the employee.
        :return: salary of the employee
        :rtype: int
        """
        return self._salary

    @property
    def bonus(self) -> int:
        """
        Get or set the bonus for the employee.
        :return: bonus of the employee
        :rtype: int
        """
        return self._bonus

    @bonus.setter
    def bonus(self, bonus) -> None:
        self._bonus = bonus

    def to_pay(self) -> int:
        """
        Calculate and return total payments of employee based on salary and bonus.
        :return: total payments of the employee
        :rtype: int
        """
        return self._salary + self._bonus


class SalesPerson(Employee):
    def __init__(self, name: str, salary: int, percent: int):
        super(SalesPerson, self).__init__(name, salary)
        self._percent = percent

    @property
    def bonus(self) -> int:
        """
        Get or set bonus of sales person.
        :return: bonus of sales person.
        :rtype: int
        """
        return self._bonus

    @bonus.setter
    def bonus(self, bonus: int) -> None:
        if self._percent > 200:
            self._bonus = bonus * 3
        elif self._percent > 100:
            self._bonus = bonus * 2
        else:
            self._bonus = bonus


class Manager(Employee):
    def __init__(self, name: str, salary: int, client_number: int):
        super(Manager, self).__init__(name, salary)
        self._client_number = client_number

    @property
    def bonus(self) -> int:
        """
        Get or set bonus of manager.
        :return: bonus of manager
        :rtype: int
        """
        return self._bonus

    @bonus.setter
    def bonus(self, bonus: int) -> None:
        if self._client_number > 150:
            self._bonus = bonus + 1000
        elif self._client_number > 100:
            self._bonus = bonus + 500
        else:
            self._bonus = bonus


class Company:
    def __init__(self, employees: List[Employee]):
        self.employees = employees

    def give_everybody_bonus(self, company_bonus: int) -> None:
        """
        Set bonus for every worker of company
        :param company_bonus: bonus to set
        :type company_bonus: int
        """
        for worker in self.employees:
            worker.bonus = company_bonus

    def total_to_pay(self) -> int:
        """
        Calculate total salary of all company workers.
        :return: total salary
        :rtype: int
        """
        total_salary = 0
        for worker in self.employees:
            total_salary += worker.to_pay()
        return total_salary

    def name_max_salary(self) -> str:
        """
        Find the name of worker with highest total salary and bonus
        :return: name of worker with highest total salary and bonus
        :rtype: str
        """
        max_salary, max_salary_worker = 0, None
        for worker in self.employees:
            if worker.to_pay() > max_salary:
                max_salary = worker.to_pay()
                max_salary_worker = worker
        return max_salary_worker.name


# employee = Employee('John', 1000)
# sales_person = SalesPerson('Jane', 1500, 201)
# manager = Manager('Jen', 2500, 151)
# company_workers = Company([employee, sales_person, manager])
# company_workers.give_everybody_bonus(200)
# print(company_workers.total_to_pay())
# print(company_workers.name_max_salary())
#
# print('\n')
# print(employee.salary)
# print(employee.name)
# print(employee.bonus)
# print(employee.to_pay())
#
# print('\n')
# print(sales_person.salary)
# print(sales_person.name)
# print(sales_person.bonus)
# print(sales_person.to_pay())
#
# print('\n')
# print(manager.salary)
# print(manager.name)
# print(manager.bonus)
# print(manager.to_pay())
