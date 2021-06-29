#!/usr/bin/python3

def main():
    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

    
    # challenge 1:
 
    # My eyes! The goggles do nothing!

    print ("\nChallenge 1:\n")
    print ('My ' + challenge[2][1] + '! The ' + challenge[2][0] + ' do ' + challenge[3] + '!')

    print ("\n-----------------------------------------------------------------------------------")

    # challenge 2:
    
    print ("\nChallenge 2:\n")
    print ('My ' + trial[2]["goggles"] + '! The ' + trial[2]["eyes"] + ' do ' + trial[3] + '!')


    print ("\n-----------------------------------------------------------------------------------")

    # challenge 3:

    print ("\nChallenge 3:\n")
    print ('My ' + nightmare[0]["goggles"] + '! The ' + trial[2]["eyes"] + ' do ' + trial[3] + '!')

    
    print ("\n-----------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()        
