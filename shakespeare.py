a = 1
while a == 1:
    darling_said = input("You say that you love.....(from the clouds?): ")
    if darling_said == "rain":
        print("But you open your umbrella when it rains.")
        a = 0

a = 1
while a == 1:
    darling_said = input("You say that you love the.....(shines in the sky?): ")
    if darling_said == "sun":
        print("But you find a shadow spot when the sun shines.")
        a = 0

a = 1
while a == 1:        
    darling_said = input("You say that you love the.....(breeze?): ")
    if darling_said == "wind":
        print("But you close your windows when",darling_said, "blows.")
        print(" ")
        print("""
You say that you love rain,\nBut you open your umbrella when it rains.\n
You say that you love the sun.\nBut you find a shadow spot when the sun shines.\n
You say that you love the wind,\nBut you close your windows when wind blows.\n
This is why I am afraid,\nYou say that you love me too!
""")
        a = 0

question = input("Do you know the author of this poem? : ")
if question == "shakespeare":
    print("")
        
    print("congratulations!".center(64))
    
        

