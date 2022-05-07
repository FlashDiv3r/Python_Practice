# Written by: Catlin Rehders for submission on 07/16/2021 
# Adapted from template provided in UTK-COSC111 by: Stephen Marz
# Program calculates how many days free food is served by at least one event
# during the dates provided by the user.

def get_input():
    num_events = int(input())
    events = []
    # Iterates through the total number of events to determine what 
    # days each individual event is scheduled by getting the start and end day
    # for each event from the user.
    for i in range(num_events):
        # Takes start and end day input on the same line and splits it into 
        # two seperate values by splitting at the space.
        si, ti = input().split()
        # Adds the start and end days, as well as all days within that range 
        # of dates to the events list.
        events.extend(range(int(si), int(ti) + 1))
    # Returns the updated list of events with full range of start and end days 
    # to include the days inbetween.
    return events

def calculate(events):
    # Converts the list of events into a set to remove the duplicate days and 
    # counts the number of days within that set to determine how many days 
    # free food is served by at least one event.
    unique_days = len(set(events))
    # Returns the number of unique days to allow this value to be used for
    # the main function when printing the free food total
    return unique_days

if __name__ == "__main__":
    events = get_input()
    free_food = calculate(events)
    print(free_food)