
        #012345678901234
dragon= "fire breathing"
print(dragon)
print(dragon[4])
print(dragon[5])


        #012345678901234
        #43210987654321
dragon= "fire breathing"
print(dragon)
print(dragon[-10])
print(dragon[-9])


        #012345678901234
dragon= "fire breathing"
print(dragon[5:11]) #breath
print(dragon[0:3])  #fir
print(dragon[:3])   #fir (start of string up to but not including 3)
print(dragon[3:])   #e breathing (3 to the end of string)
print(dragon[:])    #fire breathing (start to end of string)


        #012345678901234
        #43210987654321
dragon= "fire breathing"
print(dragon)
print(dragon[-14:-10])    #fire
print(dragon[4:-14])      #Does not print anything. Cannot print backwards from starting.
print(dragon[-14:4])      #fire (can combine +ve/-ve numbers, but only count forwards from start)



        #012345678901234
dragon= "fire breathing"
weight= "9$8*k%g|&#*!@|"
print(dragon[3:12:4]) #eei (print char in range 3-11, in steps of 4 counting from start)
print(dragon[1::3])   #i ehg (print char from 1 to end of string, in steps of 3)
print(weight[:7:2])   #98kg (print char from start to 6th char, in steps of 2)

        #654321
        #012345
letters="abcdef"
print(letters[5:0:-1])  #fedcb (char from 5 backwards in steps of 1 to charc 0 excluding it)
print(letters[5::-2])   #fdb (char from 5 backwards in steps of 2 until the start of string)
print(letters[5:-1:-1]) #Does not print (5th char backwards in steps of 1 to -1 char excluding it
                        #5th char= -1th char= f, which is excluded, hence nothing printed)

print(letters[::-1])   #fedcba

name="tim"
age=24
print(name + " is " + str(age)+ " years.")
print(f"{name} is {age} years.")

print(f"pi is approximately {22/7:10.20f}")
pi=22/7
print(f"pi is approximately {pi:10.20f}")


a=2
b=6
print(b/a)   #3.0  (float)
print(b//a)   #3   (int)


c=2.0
d=5
e=2
print(c*d)   #10.0 (gives float value because one of the values is float )
print(d*e)   #10  (gives int because both values are int)




