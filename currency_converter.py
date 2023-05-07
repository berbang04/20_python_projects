def currency():
    print("welcome to currency converter: ")
    dollars=eval(input("enter your usd amount to convert: "))
    tl=convert_to_tl(dollars)
    print("that is ",tl,"tl.")
convert_to_tl=lambda dollars:dollars*19.82
currency()    