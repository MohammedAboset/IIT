movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = []

# Part A - Input loop
while True:
    title = input("Enter movie title or 'done': ")

    if title == "done":
        break

    if title not in movies:
        print("Available movies are:")
        for movie in movies:
            print(movie)
        continue

    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a number.")
        continue

    purchases.append((title, qty, movies[title]))


# Part B - Receipt
print("\nReceipt")

grand_total = 0

for title, qty, price_each in purchases:
    line_total = qty * price_each

    if qty >= 4:
        line_total = line_total * 0.90

    print(title, "-", qty, "tickets - $", round(line_total, 2))
    grand_total += line_total


# Member discount
member = input("Do you have a member code? yes/no: ")

if member.lower() == "yes":
    grand_total = grand_total * 0.95

print("Total: $", round(grand_total, 2))


# Part C - Sales summary
tickets_by_movie = {}
revenue_by_movie = {}

for title, qty, price_each in purchases:

    line_total = qty * price_each

    if qty >= 4:
        line_total = line_total * 0.90

    if title in tickets_by_movie:
        tickets_by_movie[title] += qty
        revenue_by_movie[title] += line_total

    else:
        tickets_by_movie[title] = qty
        revenue_by_movie[title] = line_total


print("\nSales Summary")

for title in tickets_by_movie:
    print(
        title,
        "- Tickets:",
        tickets_by_movie[title],
        "- Revenue: $",
        round(revenue_by_movie[title], 2)
    )


# Part E - Top selling movie
top_title = None
top_qty = -1

for title, qty in tickets_by_movie.items():
    if qty > top_qty:
        top_title = title
        top_qty = qty

print("\nTop seller:", top_title, "-", top_qty, "tickets")


# Sort movies by revenue
sorted_by_rev = sorted(
    revenue_by_movie.items(),
    key=lambda item: item[1],
    reverse=True
)

print("Movies sorted by revenue:")

for title, revenue in sorted_by_rev:
    print(title, "- $", round(revenue, 2))


# Average tickets per purchase
if len(purchases) > 0:
    total_tickets = 0

    for title, qty, price_each in purchases:
        total_tickets += qty

    average = total_tickets / len(purchases)

    print("Average tickets per purchase:", round(average, 2))
else:
    print("Average tickets per purchase: 0")
