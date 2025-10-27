import math

# can_list = can name/radius(centimeters)/height(centimeters)/Cost per Can($)
can_list = [["#1 Picnic",6.83,10.16,0.28],
            ["#1 Tall",7.78,11.91,0.43],
            ["#2",8.73,11.59,0.45],
            ["#2.5",10.32,11.91,0.61],
            ["#3 Cylinder",10.79,17.78,0.86],
            ["#5",13.02,14.29,0.83],
            ["#6Z",5.40,8.89,0.22],
            ["#8Z short",6.83,7.62,0.26],
            ["#10",15.72,17.78,1.53],
            ["#211",6.83,12.38,0.34],
            ["#300",7.62,11.27,0.38],
            ["#303",8.10,11.11,0.42]]

def main():
    best_store = ["",0]
    best_cost = ["",0]
    for i in range(0,len(can_list)):
        name = can_list[i][0]
        radius = can_list[i][1]
        height = can_list[i][2]
        cost = can_list[i][3]
        volume = can_volume(radius,height)
        area = surface_area(radius,height)
        eff = compute_storage_efficiency(radius, height)
        if best_store[1] < eff:
            best_store = [name,eff]
        cost_eff = cost_efficiency(cost, volume)
        if best_cost[1] < cost_eff:
            best_cost = [name,cost_eff]
        print(f"{name:12} volume={volume:9.2f}   area={area:8.2f}   Efficiency={eff:5.2f}  Cost Efficiency={cost_eff:8.2f}")
       
    print() 
    print(f"Best can size in storage efficiency: {best_store[0]}")
    print(f"Best can size in cost efficiency: {best_cost[0]}")

def cost_efficiency(cost, volume):
    return volume/cost
    
def compute_storage_efficiency(radius, height):
    return (can_volume(radius, height)/surface_area(radius, height))  

def can_volume(radius, height):
    return (math.pi * height * (radius**2))

def surface_area(radius, height):
    return (2 * math.pi * radius * (radius + height))
    
main()