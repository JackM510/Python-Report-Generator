#the event class keeps record of users logging in/out of a specific machine.
#an event is comprised of an event date, the type of event (log in OR log out),
#the machine the event occured on, and the user which triggered the event.
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

#this function returns the date of each event and is used in current_users function.
def get_event_date(event):
    return event.date

#this function sorts each Event in the events List by the event date using get_event_date().
#an empty Dictionary is instantiated and uses conditional statements to add key-value pairs:
#each machine is added to the machines Dictionary as a key.
#each user that is logged into a machine is stored as a value in an empty set() element.
#each user that logs out of a machine is removed from the key-value pair for that particular machine.
def current_users(events):
    events.sort(key=get_event_date) #sort each Event in the events List by date.
    machines = {} #intialise an empty Dictionary.
    for event in events:
        if event.machine not in machines: #if a machine in the events List is not in the machines Dictionary:
            machines[event.machine] = set() #add the machine to the machines Dictionary and create an empty set() which will store a set of users logged into that machine.
        if event.type == "login": #if an event type specifies a login:
            machines[event.machine].add(event.user) #add the user to the machines Dictionary under the machine they are logged into.
        elif event.type == "logout": #if an event type specifies a logout:
            machines[event.machine].remove(event.user) #remove the user from the machines Dictionary under the machine they are logging out of.
    return machines

#this function generates a report of users logged into a machine.
#this function will automatically print out the report results to the console.
def generate_report(machines):
    print("Below is a list of users that are logged into a machine:")
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

#the events variable below is a List which contains several Event objects.
#each event holds event data for a user logging in/out of a machine.
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

#create a Dictionary of users based on each Event listed in the events List.
users = current_users(events)

#use the generate_report function and pass the list of users to return only
#a list of users that are logged into a machine.
generate_report(users)
