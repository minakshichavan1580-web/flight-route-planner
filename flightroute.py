class FlightRoutePlanner:
    def __init__(self):
        # Using an adjacency list to represent the graph
        self.graph = {}

    def add_airport(self, airport_code):
        """Adds a new airport (node) to the network."""
        if airport_code not in self.graph:
            self.graph[airport_code] = {}
            print(f"✈️ Airport {airport_code} added successfully.")
        else:
            print(f"⚠️ Airport {airport_code} already exists.")

    def add_flight_path(self, source, destination, distance):
        """Adds a directed flight path (edge) with a distance weight."""
        if source not in self.graph:
            print(f"⚠️ Source airport {source} does not exist. Create it first.")
            return
        if destination not in self.graph:
            print(f"⚠️ Destination airport {destination} does not exist. Create it first.")
            return
        
        # Add the route with its distance
        self.graph[source][destination] = distance
        print(f"🔗 Flight path created: {source} ➔ {destination} ({distance} km)")

    def display_network(self):
        """Prints the entire graph/flight network."""
        print("\n--- Current Flight Network ---")
        if not self.graph:
            print("The network is empty.")
            return
        for airport, connections in self.graph.items():
            if connections:
                routes = ", ".join([f"{dest} ({dist} km)" for dest, dist in connections.items()])
                print(f"  {airport} ➔ {routes}")
            else:
                print(f"  {airport} ➔ No direct flights")
        print("-----------------------------\n")

    def find_all_paths(self, start, end, path=[]):
        """Finds all possible routes between two airports using DFS."""
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        
        paths = []
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.find_all_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def show_routes(self, start, end):
        """Displays available routes and calculates total distances."""
        print(f"\n🔍 Searching flights from {start} to {end}...")
        all_routes = self.find_all_paths(start, end)
        
        if not all_routes:
            print(f"❌ No available flight routes found between {start} and {end}.")
            return
            
        print(f"✅ Found {len(all_routes)} available route(s):")
        for i, route in enumerate(all_routes, 1):
            # Calculate total route distance
            total_distance = 0
            for j in range(len(route) - 1):
                total_distance += self.graph[route[j]][route[j+1]]
            
            route_str = " ➔ ".join(route)
            print(f"  Route {i}: {route_str} | Total Distance: {total_distance} km")


# --- Demonstration of the Project ---
if __name__ == "__main__":
    planner = FlightRoutePlanner()

    print("=== Step 1: Adding Airports ===")
    planner.add_airport("BOM")  # Mumbai
    planner.add_airport("DEL")  # Delhi
    planner.add_airport("BLR")  # Bangalore
    planner.add_airport("PNQ")  # Pune
    planner.add_airport("CCU")  # Kolkata

    print("\n=== Step 2: Adding Flight Paths ===")
    planner.add_flight_path("BOM", "DEL", 1150)
    planner.add_flight_path("BOM", "BLR", 840)
    planner.add_flight_path("DEL", "CCU", 1300)
    planner.add_flight_path("BLR", "CCU", 1550)
    planner.add_flight_path("PNQ", "BOM", 120)
    planner.add_flight_path("PNQ", "BLR", 730)

    # Display the network topology
    planner.display_network()

    print("=== Step 3: Route Planning Queries ===")
    # Query 1: Direct and multi-hop paths
    planner.show_routes("BOM", "CCU")
    
    # Query 2: Multi-hop path from a smaller airport
    planner.show_routes("PNQ", "CCU")
