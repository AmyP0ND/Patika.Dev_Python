def reverse(liste):

    for i in liste:
        if isinstance(i, list):
            reverse(i)
            i=i.reverse()
        else:
            Liste.reverse()

Liste = [[1, 2], [3, 4], [5, 6, 7]]

reverse(Liste)
print("Ters Liste: ", Liste)