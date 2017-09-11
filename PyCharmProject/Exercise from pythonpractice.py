import math
import random

class Mathematic:
    def less_than_ten(self, start=1, stop=2, step=1):
        print(str([x for x in range(start, stop, step) if x < 5]))

    def divisors(self, numb):
        my_number = [x for x in range(1,numb + 1) if numb % x == 0]
        print(str([x for x in range(1,numb + 1) if numb % x == 0]))
        return my_number

    def two_list_overlap_first(self, list_one, list_two):
        if isinstance(list_one, list) and isinstance(list_two, list):
            overlaps =list(set(list_one) & set(list_two))
        else:
            print("You don't give me a list!")
        print(overlaps)

    def palindrom_string(self, my_str):
        # elegant solution  str(mystr) == str(mystr)[::-1] from stackoverflow
        if my_str == "":
            print("You give me blank string!")
        if isinstance(my_str, str):
            revert = my_str[::-1]
            if revert == my_str:
                print("This is palindorm!")
            else:
                print("it's not palindrom!")

    def even_element_of_list(self,my_list):
        print(str([x for x in my_list if x%2 == 0]))

    def game_rock_paper_scissiors(self,):
        # from pythonpractice
        print('''Please pick one:
                    rock
                    scissors
                    paper''')

        while True:
            game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
            player_a = str(input("Player a: "))
            player_b = str(input("Player b: "))
            a = game_dict.get(player_a)
            b = game_dict.get(player_b)
            dif = a - b

            if dif in [-1, 2]:
                print('player a wins.')
                if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                    continue
                else:
                    print('game over.')
                    break
            elif dif in [-2, 1]:
                print('player b wins.')
                if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                    continue
                else:
                    print('game over.')
                    break
            else:
                print('Draw.Please continue.')
                print('')

    def guessing_game_one(self):
        print("I generate a random number between 1 and 10, guess it!")
        rand_number = round(random.random()*10)
        user_input = int(input("? : "))
        if rand_number == user_input:
            print("Good you geues it! O_o")
        elif (user_input >= rand_number + 5) or (user_input <= rand_number - 5):
            print("Soo far T_T")
        elif (user_input >= rand_number + 3) or (user_input <= rand_number - 3):
            print("Not bad ^_^")
        elif (user_input >= rand_number + 1) or (user_input <= rand_number - 1):
            print("So near *_*")
        print(str(rand_number))

    def two_list_overlap_second(self, my_first_list, my_second_list):
        # elegant user solution result = [i for i in a if i in b]
        if isinstance(my_first_list, list) and isinstance(my_first_list, list):
            output_list = []
            for x in range(my_first_list.__len__()):
                for y in range(my_second_list.__len__()):
                    if my_first_list[x] == my_second_list[y]:
                        output_list.append(my_first_list[x])
            output_list = set(output_list)
        else:
            print("You don't give me a two correct list!")
        print(output_list)

    def primer_function(self):
        user_input = int(input("Type some number and I you tell is it a prime number: "))
        local_numb = self.divisors(user_input)
        if local_numb.__len__() > 2:
            print("This is not prime number")
        else:
            print("This is a prime number!")
        return local_numb

    def list_ends(self, my_list):
        if isinstance(my_list, list):
            new_list = [my_list[0], (my_list[my_list.__len__() - 1])]
            print(new_list)
        else:
            print("You don't give me a list!")
        return new_list

    def fibonacci_count(self):
        numb = int(input("Tell me how many Fibonacci numbers generate?: "))
        preindex = 0
        index = 1
        fibonacci_number = []
        for i in range(numb):
            preindex, index = index, preindex + index
            fibonacci_number.append(preindex)
        print(fibonacci_number)

    def my_own_set_function(self, input_list):
        if isinstance(input_list, list):
            new_list = []
            for y in input_list:
               if y in input_list and y not in new_list:
                   new_list.append(y)
        else:
            print("You dont give me a list!")
        return new_list

    def reverse_words(self):
        # from pythonpractice   return ' '.join(input_words.split()[::-1])
        input_words = input("Tel me somthing: ")
        input_words = input_words.split(" ")
        output_words = " ".join(input_words[::-1])
        return output_words



a = [1, 1, 2, 3, 5, 8, 13, 3, 21, 1, 34, 55, 89]
b = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13]
myclass = Mathematic()
# myclass.twolistoverlap(a,b)

c = myclass.reverse_words()
print(c)
