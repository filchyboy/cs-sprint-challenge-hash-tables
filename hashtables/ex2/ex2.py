#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = []
    flight_hash = {}
    for i in range(length):
        flight_hash[tickets[i].source] = tickets[i].destination

    key = "NONE"
    for j in flight_hash.items():
        route.append(flight_hash[key])
        key = flight_hash[key]
        
    return route