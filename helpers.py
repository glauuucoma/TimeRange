def timerange_to_minutes(t_str):
    """
    Return amount of minutes for time ranges in format HH:MM
    :param t_str:
    :return:
    """
    # 10:00

    hour = int(t_str.split(":")[0])
    minutes = int(t_str.split(":")[1])
    hour_to_minutes = hour * 60

    return hour_to_minutes+ minutes

def prettify_available_minutes():
    l = [0,1,2,3,4,5,70,71,72,73,74]
    # Group the list so that: [[0,1,2], [60,61,62]]