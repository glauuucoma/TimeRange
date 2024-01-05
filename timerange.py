import helpers as h
from dataclasses import dataclass, field

@dataclass
class TimeRange:
    start_time : str # 10:10
    end_time : str # 9:10

    start_minutes : int = field(init=False, repr=False) # 30
    end_minutes : int = field(init=False, repr=False) # 50

    minutes_range : range = field(init=False, repr=False)

    def __post_init__(self):
        self.start_minutes = h.timerange_to_minutes(self.start_time)
        self.end_minutes = h.timerange_to_minutes(self.end_time)
        self.minutes_range = range(self.start_minutes, self.end_minutes, 1)

