# The event class keeps record of users logging in/out of a specific machine
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

# Returns the date of each event and is used in current_users() function
def get_event_date(event):
    return event.date

# Sorts each Event in the events List by the event date using get_event_date()
# Returns a Dictionary of machines that have recorded an event where a user has logged in
def current_users(events):
    events.sort(key=get_event_date)
    machines = {} # Empty Dictionary
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user) # Add the user to Dictionary if 'login'
        elif event.type == "logout":
            machines[event.machine].remove(event.user) # Remove the user from Dictionary if 'logout'
    return machines

# Generates a report of users logged into a machine and returns the results to the terminal
def generate_report(machines):
    print("Below is a list of users that are logged into a machine:")
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

# Holds a list of Events
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 12:35:23', 'login', 'myworkstation.local', 'chris'),
    Event('2020-01-23 13:09:56', 'login', 'cloud-vm-dc01', 'ben'),
    Event('2020-01-23 14:24:49', 'login', 'cloud-vm-ps01', 'chris'),
]

# Create a Dictionary of users that are logged in using the current_users() function
users = current_users(events)

# Pass the Dictionary as a parameter and generate a report of users that are logged in
generate_report(users)
