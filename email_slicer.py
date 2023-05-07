def main():
    print("welcome man to email slicer \n")
    email_input=input("input ur email please: ")
    (username,domain)=email_input.split("@")
    (domain,extension)=domain.split(".")
    print("username: ",username)
    print("domain: ",domain)
    print("extension: ",extension)
main()    

# we made simple slicer , divided the input base on some characters we wrote in split()