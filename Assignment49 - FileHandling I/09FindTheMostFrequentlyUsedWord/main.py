from pathlib import Path as path
import string


base_dir = path(__file__).parent
file_path = base_dir / "article.txt"

n = input("Enter Your Para: ")

with open(file_path, "w+") as f:

    f.write(n)

    f.seek(0)

    line = f.read()

    most_frequent_word=''
    most_frequent=0

    

    for word in line.split():

        word = word.strip(string.punctuation).lower()
        count=0

        for i in line.split():
            i=i.strip(string.punctuation).lower()
            if i==word:
                count+=1
        
        if count > most_frequent:
            most_frequent=count
            most_frequent_word=word


    print(f"Most Frequent Word : {most_frequent_word}")
    print(f"Frequency Of Word  : {most_frequent}")
            

