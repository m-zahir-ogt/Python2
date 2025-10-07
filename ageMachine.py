"""
this function take integer age as Argumentand and
print if he/she/they/them is old or will be old 
"""
def ageMachine(age):
        if age > 50:
            print("Su bist alt geworden")
        else:
            print("Aha eines Tages du wirst Alt auch")

"""
this function accept tow integer as Argument and add them
return result of summation
"""
def addTwoNummer(first_number: int, second_nummer: int) -> int:
    return first_number + second_nummer

result = addTwoNummer(5,6)
print("it is result:{result}")

ageMachine(50)
