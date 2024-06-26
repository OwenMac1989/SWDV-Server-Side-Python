from dice import Dice, Die

def main():
      print("The Dice Roller program")
      for i in range(1,7):
            die = Die()
            die.value = i
            print(die.image)
      print()
        

    # get number of dice from user
      count = int(input("Enter the number of dice to roll: "))

      # create Die objects and add to Dice object
      dice = Dice()
      for i in range(count):
            die = Die()
            dice.addDie(die)

      choice = "y"
      while choice.lower() == "y":        
            # roll the dice
            dice.rollAll()

            #display to user
            print("YOUR ROLL:  ", end="\n")
            total = 0 
            for die in dice.list:
            print(die.image, end="  ")
            print(die.value, end="\n")
            total += die.value

            print("\n")
            print(f"Total Roll : {total}")

            choice = input("Roll again? (y/n): ")
            
      print("Bye!")

if __name__ == "__main__":
    main()
