from dataclasses import dataclass, field

@dataclass
class TimeRange:
    start_time : str # 10:10
    end_time : str # 9:10

    start_minutes : int = field(init=False) # 30
    end_minutes : int = field(init=False) # 50

