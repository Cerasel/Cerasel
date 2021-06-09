class DuplicateDataException(ValueError):
    pass
from datetime import date
class ShoIter:
    def __init__(self, data: list):
        self.data = data
    def __iter__(self):
        return self
    def __next__(self):
        if not self.data:
            raise StopIteration
        return self.data.pop(0)
class Factory:
    def __init__(self, date):
        self.date = date
        self.work = {}
        self.cheating_dict = {}
    def add_work(self, name: str, series: list):
        for worker_name, worker_data in self.work.items():
            for j in worker_data:
                if j in series:
                    if worker_name == name:
                        raise DuplicateDataException('Duplicate values!')
                    else:
                        series.remove(j)
                        self.work[name] = series
                        list_to_modify = self.work[worker_name]
                        list_to_modify.remove(j)
                        self.cheating_dict[j] = (worker_name, name)
                        raise ValueError(f"Conflict series: {j}, Workers: {worker_name}, {name}")
        self.work[name] = series
    def __iter__(self):
        result = []
        for v in self.work.values():
            result.extend(v)
        return ShoIter(result)
shoe = Factory(date.fromisoformat('2021-06-09'))
shoe.add_work('Adi', [101, 102])
try:
    shoe.add_work('Dan', [100, 101])
except ValueError:
    pass
print(shoe.work)
print(shoe.cheating_dict)
with open('test', 'w' ) as file :
    for x in shoe:
         file.write(str(x) +  '\n')