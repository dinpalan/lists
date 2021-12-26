#! /usr/bin/env python3
#SHEBANG

def dikupalist():
    #lists
    modules = ['netmiko','scapy','socket','smtp']
    extramodules = ['paramiko','loguru']

    print("Printing list");
    print(modules)

    print("Printing append list");
    modules.append('pytube')
    print(modules)

    print("Printing sort list");
    modules.sort()
    print(modules)

    print("Printing reverse list");
    modules.reverse()
    print(modules)

    print("Printing single value from list");
    print(modules[0])

    print("Printing list after inserting new value in list");
    modules.insert(0,'beautifulsoap')
    print(modules)

    print("Printing sorted reverse list");
    modules.sort(reverse=True)
    print(modules)

    print("Printing list after removing last value");
    modules.pop()
    print(modules)

    print("Printing last removed value from list");
    pop=modules.pop()
    print(pop)

    print("Printing list after removing value in list");
    modules.remove('scapy')
    print(modules)

    print("Printing list after extending with new list");
    modules.extend(extramodules)
    print(modules)

    print("Printing specific range values from list");
    print(modules[1:3])

    print("Printing specific values from last on list");
    print(modules[-2])

    print("Checking value available in list or not");
    print('pytube' in modules)

    print("Checking position of value in list");
    print(modules.index('pytube'))

    numeric = [1,2,3]

    print("Printing sum of list");
    print(sum(numeric))

    print("Printing max of list");
    print(max(numeric))

    print("Printing min of list");
    print(min(numeric))
    

if __name__=='__main__':
       dikupalist() 
