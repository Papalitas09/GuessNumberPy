import random
import webbrowser


url = 'https://youtube.com/shorts/fCKB_eKUOYU?feature=share'
user_input1 = int(input("Input Number 1 : "))
user_input2 = int(input("Input Number 2 : "))

if user_input1 > user_input2:
    while True:
        try:
            print("Your second number too low then first number!!")
            user_input1 = int(input("Input Number 1 : "))
            user_input2 = int(input("Input Number 2 : "))
            if user_input1 < user_input2:
                break            
        except:
            print("apalah")


backend_Random = random.randint(user_input1, user_input2)

print(backend_Random)


if user_input1 and user_input2 != "":
    while True:
        try:
            guess_Input = int(input(f"What your guess? between {user_input1} and {user_input2} ?  "))
            
            if guess_Input > backend_Random:
                high = backend_Random + 1
               
                if guess_Input == high:
                    print("Little bit High")
                else:
                    print("Too High")
            elif guess_Input < backend_Random:
                low = backend_Random - 1 
                if guess_Input == low:
                    print("Little bit low")
                else:
                    print("Too Low")
            else:
                 print("Congratulations You guessed it right!!")
                 webbrowser.open_new(url)
                 break
        except:
            print("ERROR")

       
    
    