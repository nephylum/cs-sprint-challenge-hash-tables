#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    hash = {}
    #add each ticket into hash
    for ticket in tickets:
        hash[ticket.source] = ticket.destination
    #start with None
    x = hash["NONE"]
    trip = []
    trip.append(x)
    #end with None
    while x != 'NONE':
        x = hash[x]
        trip.append(x)

    return trip
