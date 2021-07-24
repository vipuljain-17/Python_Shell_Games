movies_list = ["Bazigaar","Chak De India","Gundey","Khalnayak","Don","Deewar","Ishq","Beta","Dabaang","Jab we met","Kaho na pyarr hai","Bajirao Mastani",
                "Coolie No. 1 ","Amar Akbar Anthony","Andaz Apna Apna","Humpty Sharma ki Dulhania","Khoobsurat","Kick","Hum","Delhi belly","ROckstar","Ragni MSS 2",
                "Run","Mr. India","3 idiots","Daamini","Welcome","Dangal","Mohra","PK","Piku","DDLJ","Bahubali","Golmaal","Dhoom3","Raja Babu","Ram lakhan",
                "hera pheri","Kabhi Khushi Kabhi gaham","Tezaab","Mugal-e-azam","Fukrey","Roy","Shehenshah","Wanted","Chup Chup ke","Sholey","Saudagar","Ready","YJHD",
                "Singham","Vishwatam","DevDas","Aashiqui2","April Fool"]

movies_remaining = movies_list
movies_done = list()

import random
print("The BollyWood Movies Tambola")
print("1 for random movie\n2 for movies done\n3 for remaining\nexit for quiting the game")

while len(movies_remaining) != 0:
    s = input("Enter number: ")
    if s == "exit":
        print(movies_done)
        exit()
    elif int(s) == 1:
        random.shuffle(movies_remaining)
        if len(movies_remaining) > 0:
            current_movie = movies_remaining.pop()
            movies_done.append(current_movie)
            print(f"Current Movie: {current_movie}")
        #print(f"Previous Movie: {movies_done[-2]}")

    elif int(s) == 2:
        print(f"Number of movies done: {len(movies_done)}")
        print(sorted(movies_done))
    elif int(s) == 3:
        print(f"Number of movies reminaing: {len(movies_remaining)}")
        print(sorted(movies_remaining))
    else:
        print("Try any 1,2,3 or exit number!")
