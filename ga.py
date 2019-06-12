import random
from random import shuffle

def function(x):
    return 9*x**5-194.7*x**4+1680.1*x**3-7227.94*x**2+15501.2*x-13257.2
def fitness_function(x):
    return abs(function(x))

def compute_val(s):
    c=0
    z=2**9
    for i in range(0,10):
        if(s[i]=='1'):
            c=c+z
        z/=2
    for i in range(11,20):
        if(s[i]=='1'):
            c=c+z
        z/=2
    return c

def best_fitness(society):
    min=1000000000000000000000000
    j=-1
    for  i in range(len(society)):
        if(min>fitness_function(compute_val(society[i]))):
            min=fitness_function(compute_val(society[i]))
            j=i
    return((j,min))

def create_random_population(n):
    society=[]
    for i in range(n):
        particle=""
        for i in range(10):
            particle+=random.choice(['1','0'])
        particle+="."
        for i in range(10):
            particle+=random.choice(['1','0'])
        society.append(particle[:])
    return society

def crossover(society):
    shuffle(society)
    new_society=[]
    for i in range(0,len(society),2):
        crossover_point=random.randint(0,19)
        if(crossover_point>9):
            crossover_point+=1
        s1=society[i]
        s2=society[i+1]
        s3=s1[:crossover_point]+s2[crossover_point:]
        s4=s2[:crossover_point]+s1[crossover_point:]
        new_society.append(s3)
        new_society.append(s4)
    society=new_society
    return society

def mutation(society,mutation_rate):
    for i in range(len(society)):
        rand=random.randint(0,100)
        if(rand<mutation_rate):
            rand2=random.randint(0,19)
            if(rand2>9):
                rand2+=1
            new = list(society[i])
            
            if(new[rand2]=='1'):
                new[rand2]='0'
            else:
                new[rand2]='1'

            society[i]=''.join(new)
    return society  

def natural_choose(society,old_society):
    new_society=[]
    for i in range(len(society)):
        out_old=fitness_function(compute_val(old_society[i]))
        out_cur=fitness_function(compute_val(society[i]))
        if(out_old<out_cur):
            new_society.append(old_society[i])
        else:
            new_society.append(society[i])
    return society

def run():
    sat=0.1
    mutation_rate=10
    society=create_random_population(64)
    z=0
    while(z<100000):
        if(z%1000==0):print(z)
        z+=1
        # print(len(society[0])," ",society[0])
        old_society=society[:]
        society=crossover(society)
        # print(len(society[0])," ",society[0])
        society=mutation(society,mutation_rate)
        # print(len(society[0])," ",society[0])
        society=natural_choose(society,old_society)
        # print(len(society[0])," ",society[0])
        (i,minn)=best_fitness(society)
        
        if(minn<sat):
            print("after ",z,"iteration")
            # print(i," ",minn)
            return (society[i],minn)


def main():
    (num,m)=run()
    
    val=compute_val(num)
    print(function(val),"   ",m,"     ",val)
    # print(val," ",m)


main()

'''
sat=0.001
after  6007 iteration
0.0008696964468981605     0.0008696964468981605       4.884765625

after  41633 iteration
0.0008696964468981605     0.0008696964468981605       4.884765625

after  23400 iteration
0.0008696964468981605     0.0008696964468981605       4.884765625

after  18446 iteration
0.0008696964468981605     0.0008696964468981605       4.884765625


sat=0.1
after  53 iteration
-0.05858195523978793     0.05858195523978793       4.806640625

after  87 iteration
0.08630498921775143     0.08630498921775143       4.93359375

after  100 iteration
-0.04678494020845392     0.04678494020845392       4.83203125

'''
