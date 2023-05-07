def main():
    word_dictipnary={
        "man":"has a d*ck",
        "woman":"has a p*ssy",
        "animal":"has no thinking",
        "plant":"does photosynthesis",
        
    }
    while True:
        word=str(input("enter ur word please: "))
        if word =="":
            break
        if word in word_dictipnary:
            print(word,":",word_dictipnary[word])
        else:
            print("not in the dictionary")

main()