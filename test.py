genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
# for i in range(len(genre)):
#    print("I like", genre[i])

# for oneGenre in genre:
#    print(oneGenre)

# allGenres = []
# genres = [oneGenre for oneGenre in genre]
# allGenres.append(genres)
# print(allGenres)

allGenres = []
for oneGenre in genre:
    allGenres.append(oneGenre)
print(allGenres)
