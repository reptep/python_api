#!/usr/bin/python3

def main():
    fruitcompanies= [{"name":"Zesty","employees":["Ambu","Brent", "Bryan","Carlee","Chad"]},
                 {"name":"Ripe.ly","employees":["Darlene","Eric","Fernando","Peter",]},
                 {"name":"FruitBee","employees":["Jennae","Joel","Jonas","Josh",]},
                 {"name":"JuiceGrove","employees":["Kurt","Nate","Patrick","Rachel",]}]

    # challenge 1:
  
    print ("\nChallenge 1:\n")
    for i in fruitcompanies[1]["employees"]:
        print (i) 

    print ("\n-----------------------------------------------------------------------------------")

    # challenge 2:

    print ("\nChallenge 2:\n")

    companyName = ""

    for i in fruitcompanies:
        companyName = companyName + " | " + (i["name"])

    companyName=companyName.lstrip(" | ")

    myPrompt="Enter company name (" + companyName + "): "

    myCompanyName=input (myPrompt)
    # print (myCompanyName)

    print("\nEmployees of " + myCompanyName + ":" )

    for i in fruitcompanies:
        if i["name"] == myCompanyName:
            for j in i["employees"]:
                print ("\t" + j)

    print ("\n-----------------------------------------------------------------------------------")

    # challenge 3:

    print ("\nChallenge 3:\n")

    companyName = ""

    for i in fruitcompanies:
        companyName = companyName + " | " + (i["name"])

    companyName=companyName.lstrip(" | ")

    myPrompt="Enter company name (" + companyName + "): "

    myCompanyName=input (myPrompt)
    # print (myCompanyName)

    print("\nEmployees of " + myCompanyName + ":" )

    for i in fruitcompanies:
        if i["name"] == myCompanyName:
            for j in i["employees"]:
                if j != "Chad":
                    print ("\t" + j)
    
    print ("\n-----------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()        
