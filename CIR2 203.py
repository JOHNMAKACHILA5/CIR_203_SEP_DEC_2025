# Task 1: Create a list of 10 delivery routes
routes = [
"Nairobi-CBD",
"Mombasa-Port",
 "Kisumu-Lakeside",
"Eldoret-Express",
"Nakuru-Hub",
"Thika-Industrial",
"Nyeri-Highlands",
"Kitale-Farmway",
"Garissa-Desert",
"Meru-Market"
]

# Task 2: Append a new route and remove a discontinued one
routes.append("Busia-Border")
routes.remove("Garissa-Desert")  # Assuming this route is discontinued

# Task 3: Sort the list alphabetically and reverse it
routes.sort()
routes.reverse()

# Task 4: Count how many routes start with the letter “N”
n_routes_count = sum(route.startswith("N") for route in routes)

# Task 5: List comprehension for routes longer than 10 characters
long_routes = [route for route in routes if len(route) > 10]

# Output results
print("Updated Routes List:", routes)
print("Number of routes starting with 'N':", n_routes_count)
print("Routes longer than 10 characters:", long_routes)
