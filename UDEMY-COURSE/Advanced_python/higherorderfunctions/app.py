movies=[
    {'name':'Avatar11','director':'James Cameroon1'},
    {'name':'Avatar12','director':'James Cameroon12'},
    {'name':'Avatar13','director':'James Cameroon13'},
    {'name':'Avatar14','director':'James Cameroon14'},
    {'name':'Avatar15','director':'James Cameroon15'},
    {'name':'Avatar16','director':'James Cameroon16'}
]

def list_movie(expected,finder):
    for movie in movies:
        if finder(movie) == expected:
            return movie


find_by=input('How do you  want to find the movie by:')
looking_for=input('What are you looking for:')
#print(list_movie('Avatar11',lambda movie:movie['name']))
movie=list_movie(looking_for,lambda movie:movie[find_by])

print(movie or 'No movie found')