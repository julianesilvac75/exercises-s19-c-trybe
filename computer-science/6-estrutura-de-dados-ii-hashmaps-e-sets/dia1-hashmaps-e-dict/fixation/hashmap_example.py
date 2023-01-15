class Employee:
    def __init__(self, id_num, name):
        self.id_num = id_num
        self.name = name


class HashMap:
    def __init__(self):
        self._buckets = [[] for i in range(10)]

    def get_address(self, id_num):
        return id_num % 10

    def insert(self, employee):
        address = self.get_address(employee.id_num)
        self._buckets[address].append(employee)

    def get_value(self, id_num):
        address = self.get_address(id_num)
        for item in self._buckets[address]:
            if item.id_num == id_num:
                return item.name
        return None

    def has(self, id_num):
        address = self.get_address(id_num)
        if len(self._buckets[address]) != 0:
            for item in self._buckets[address]:
                if item.id_num == id_num:
                    return True
        
        return False

    def update_value(self, id_num, new_name):
        address = self.get_address(id_num)
        for item in self._buckets[address]:
            if item.id_num == id_num:
                print("Old name:", item.name)
                item.name = new_name
                print("New name:", item.name)


if __name__ == "__main__":
    employees = [(14, "name1"), (23, "name2"), (10, "name3"), (9, "name4")]
    hashmap = HashMap()

    for id_num, name in employees:
        employee = Employee(id_num, name)

        hashmap.insert(employee)

    if hashmap.has(23):
        print(hashmap.get_value(23))

    print("----------")

    if hashmap.has(10):
        hashmap.update_value(10, "name30")