def hanoi_solver(n):
    rod1= list(range(n,0,-1))
    rod2= []
    rod3=[]
    result= f'{rod1} {rod2} {rod3}'
    rods= [rod1,rod2,rod3]

    def solve(disk_move,current_rod,new_rod,temp_rod,result):
        if disk_move ==1:
            disk= current_rod.pop()
            new_rod.append(disk)
            result = result + "\n" + f'{rods[0]} {rods[1]} {rods[2]}'
            return result
        else:
            result = solve(disk_move -1,current_rod,temp_rod,new_rod,result )
            disk= current_rod.pop()
            new_rod.append(disk)
            result = result + '\n' + f'{rods[0]} {rods[1]} {rods[2]}'
            result = solve(disk_move -1, temp_rod,new_rod,current_rod,result)
            return result
            
    result = solve(n,rod1,rod3,rod2,result)
    return result


print(hanoi_solver(3))
