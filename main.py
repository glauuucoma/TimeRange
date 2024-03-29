from timerange import TimeRange
from friend import Friend
from custom_list import CustomList
import helpers as h
import intro as i

def main():
    i.welcomeMessage();
    i.handleInput();
    available_minutes = CustomList(range(480, 1200))
    f1 = Friend("Jim")
    f1.add_busy_range(TimeRange(start_time="8:00", end_time="10:00"))
    f2 = Friend("Chris")
    f2.add_busy_range(TimeRange(start_time="8:00", end_time="10:00"))
    # Program doesn't check whether the start time is earlier than end time
    for m in available_minutes[:]:
        for r in Friend.all_busy_minutes_range:
            if m in r:
                available_minutes.remove_if_exist(m)

    for tr in h.prettify_available_minutes(available_minutes):
        print(f"You can meet in {tr}")
    


if __name__ == "__main__":
    main()