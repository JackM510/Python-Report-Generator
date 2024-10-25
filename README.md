# Python-logged-in-users
A simple Python script which generates a report of users that are logged into a machine.

The script contains an 'Event' class and a List element named 'events'. 
An Event occurs when a user logs in/out of a machine.
The 'events' list holds several 'Event' objects which contain information about a specific event.

This script uses a function called current_users() which creates a Dictionary element called 'machines'.
The function adds each machine specified in the 'events' List to the 'machines' Dictionary as a key. 
If an 'Event' records that a user has logged into a machine, the name of the user is added to the 'machines' Dictionary as a value under the machine key. 
If an 'Event' records that a user has logged out of a machine, the name of the user is removed from the 'machines' Dictionary using the machine key.
This function organises the 'events' List and returns the 'machines' Dictionary which contains only a list of users that are logged into a machine.

The function generate_report() iterates over the Dicitonary returned from current_users() and prints a list of users logged into each machine to the console.
