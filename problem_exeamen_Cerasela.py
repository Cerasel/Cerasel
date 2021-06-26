from datetime import datetime

class WorkStartError(ValueError):
    pass

class WorkEndError(ValueError):
    pass

class TimeIter:
    def __init__(self, working_time: list):
        self.working_time = working_time

    def __iter__(self):
        return self

    def __next__(self):
        if not self.working_time:
            raise StopIteration
        else:
            return self.working_time.pop(0)

class TimeKeeper:

     ledger = {}

     def __init__(self, date: list):
         self.date = date

     def __iter__(self):
         result = []
         for name, start_end in self.ledger.items():
             result.append((name, start_end[1] - start_end[0]))
         return TimeIter(result)

     def start_work(self, name:str, start_time:list):
         """add start time"""
         if self.ledger.get(name, None):
             raise WorkStartError(f'{name} already started work')
         self.ledger[name] = [datetime(*self.date, *start_time)]

     def end_work(self, name:str, end_time:list):
         """add end time"""
         try:
             self.ledger[name][1]
         except IndexError:
             self.ledger[name].append(datetime(*self.date, *end_time))
         else:
              raise  WorkEndError(f'{name} already started work')

timer = TimeKeeper([2021, 3, 4] )

#start time

timer.start_work('Joe', [9, 1, 20])
timer.start_work('Ana', [9, 3, 15])
timer.start_work('Tim', [9, 4, 25])
try:
    timer.start_work('Tim', [9, 4, 30])
except WorkStartError:
    print('got passed WorkStartError')

#end time

timer.end_work('Joe', [16, 1, 20])
timer.end_work('Ana', [18, 4, 15])
timer.end_work('Tim', [18, 5, 25])
try:
    timer.end_work('Tim', [18, 5, 30])
except WorkEndError:
    print('got passed WorkEndError')



with open('timer.log', 'w') as file :
    for data in timer:
        file.write(f'{data[0]}: {data[1]}\n')









