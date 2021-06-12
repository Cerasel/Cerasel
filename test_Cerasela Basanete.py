class WorkStartError(ValueError):
    pass
# class for WorkStartError
from datetime import date

class WorkEndError(ValueError):
    pass
# class for WorkEndError
from datetime import date

class ShoIter:
#Class that receives the date

    def __init__(self, data: list):
        self.data = data
    def __iter__(self):
        return self
    def __next__(self):
        if not self.data:
            raise StopIteration
        return self.data.pop(0)


class Worker:
#class for all workers
    def __init__(self, date):
        self.date = date
        self.startwork = {}
        self.endwork = {}
#method for adding workers and times
    def add_work(self, name: str, series:list):
#method for start,end worktime
         for worker_name, worker_data in self.work.items():
             for j in worker_data:
                 if j in series:
                     if worker_name == name:
                         raise WorkStartError()
                     else:
                           series.remove(j)
                           self.stratwork[name] = series
                           list_to_modify = self.work[worker_name]
                           list_to_modify.remove(j)
                           self.endwork[name] = series
                           raise ValueError(f"Conflict series: {j}, Workers: {worker_name}, {name}")
         self.work[name]=series




factory_work_start=Worker(date.fromisoformat('2021-06-12'))
factory.__addwork__('Joe', [9:01:20 ])
factory.__addwork__('Ana', [9:03:15 ])
factory.__addwork__('Tim', [9:04:25 ])
try:
factory.__addwork__('Tim', [9:04:30])

except VallueError:
 pass
 print(worker)

factory_work_end=Worker(date.fromisoformat(:'2021-06-12'))
factory.__addwork__('Joe', [16:01:20 ])
factory.__addwork__('Ana', [18:04:15 ])
factory.__addwork__('Tim', [18:05:25 ])
try:
factory.__addwork__('Tim', [18:05:30])

except VallueError:
 pass
 print(worker)

 with open('test', 'w') as file:
     for x in worker:
         file.write(str(x) + '\n')