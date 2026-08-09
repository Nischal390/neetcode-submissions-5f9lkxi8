class Person:
    def __init__(self, lastName: str, age: int, married: bool):
        self.lastName = lastName
        self.age = age
        self.married = married

    def getLastName(self) -> str:
        return self.lastName

    def getAge(self) -> int:
        return self.age

    def isMarried(self) -> bool:
        return self.married

class PersonFilter(Protocol):
    def apply(self, person: Person) -> bool:
        ...

class AdultFilter(PersonFilter):
    # Implement Adult filter
    def apply(self, person):
        if person.getAge()>=18:
            return True
        return False

class SeniorFilter(PersonFilter):
    # Implement Senior filter
    def apply(self, person):
        if person.getAge()>=65:
            return True
        return False

class MarriedFilter(PersonFilter):
    # Implement Married filter
    def apply(self, person):
        if person.isMarried():
            return True
        return False

class PeopleCounter:
    def __init__(self):
        self.filter: PersonFilter = None

    def setFilter(self, filter: PersonFilter) -> None:
        self.filter = filter

    def count(self, people: List[Person]) -> int:
        # Implement method here
        self.val = 0
        for peep in people:
            if self.filter.apply(peep):
                self.val+=1
        return self.val