from datetime import datetime,timedelta

def add(moment):
    gigasecond = 1000 * 1_000_000

    hrs_gigasecond = gigasecond/(60*60)

    return moment+timedelta(hours=hrs_gigasecond)