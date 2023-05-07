context ={
    "the biggest mountain":"everest",
    "the biggest local lake":"van lake",
    "the biggest city":"tokio",
    "the biggest waterfall":"niagara",
    "the biggest plane":"Antonov An-225 Mriya",

}
score=0
for key,value in context.items():
    print(key,"?")
    answer=str(input("your answer: "))
    if value.lower() == answer.lower():
        print("answer is true ")
        score=score+1
        print("your score: ",score)
    else:
        print("right answer is :",value)
        print("your score:",score)

print("your final score: ", score)
