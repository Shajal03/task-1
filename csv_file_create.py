import pandas as pd

# Example dataset with more data
data = {
    'plot': [
        "In a dystopian future, a group of rebels fight against a totalitarian regime.",
        "A young girl befriends an alien stranded on Earth and helps him return home.",
        "A detective investigates a series of murders in a small town.",
        "A woman discovers she has the ability to time travel and tries to change her past.",
        "A group of astronauts embark on a mission to find a new habitable planet.",
        "A retired hitman is forced back into the criminal underworld to repay a debt.",
        "A young couple navigates the challenges of a long-distance relationship.",
        "A team of superheroes unite to save the world from an alien invasion.",
        "A woman returns to her hometown to uncover the truth about her parents' death.",
        "A cat and a dog team up to find their way back home after getting lost.",
        "An undercover cop infiltrates a criminal gang to bring them down.",
        "A scientist invents a device that can read people's minds.",
        "A soldier struggles with life after returning home from war.",
        "A princess defies tradition to follow her dreams and find true love.",
        "A journalist uncovers a government conspiracy while investigating a murder.",
        "A young wizard embarks on a quest to find magical artifacts.",
        "A group of teenagers discover they have superpowers and must save the world.",
        "A detective partners with a psychic to solve a series of kidnappings.",
        "A chef travels the world to find the rarest ingredients for a special dish.",
        "A haunted house terrorizes its new inhabitants with supernatural occurrences."
    ],
    'genre': [
        "Science Fiction",
        "Family",
        "Thriller",
        "Science Fiction",
        "Adventure",
        "Action",
        "Romance",
        "Action",
        "Mystery",
        "Family",
        "Crime",
        "Science Fiction",
        "Drama",
        "Fantasy",
        "Thriller",
        "Fantasy",
        "Adventure",
        "Thriller",
        "Adventure",
        "Horror"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
csv_path = 'movies.csv'
df.to_csv(csv_path, index=False)

print(f"CSV file saved to {csv_path}")
