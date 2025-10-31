""" 
    Author: Brady Burgener
    
    Write a Python program that asks the user for five numbers:

    tower_height
    tank_height
    length of supply pipe from tank to lot
    quantity 90degree angles
    Length of pipe from supply to house
    
    return the pressure at the house
    
    Enhancements:
    Added constants WATER_DENSITY, EARTH_GRAVITY, and WATER_VISCOSITY
    function to convert kPa to psi
    test function to convert kPa to psi
    loop to ask if the user would like to do another calculation
"""
PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
WATER_DENSITY=998.2                  # density of water (998.2 kilogram / meter^3)
EARTH_GRAVITY=9.80665                # acceleration from Earths gravity 9.80665 (meter / second2)
WATER_VISCOSITY=0.0010016            # dynamic viscosity of water (0.0010016 Pascal seconds)

def main():
    calculate = 'yes'
    while calculate[0] == 'y':
        calculate = ''
        tower_height = float(input("\nHeight of water tower (meters): "))
        tank_height = float(input("Height of water tank walls (meters): "))
        length1 = float(input("Length of supply pipe from tank to lot (meters): "))
        quantity_angles = int(input("Number of 90° angles in supply pipe: "))
        length2 = float(input("Length of pipe from supply to house (meters): "))
        
        water_height = water_column_height(tower_height, tank_height)
        pressure = pressure_gain_from_water_height(water_height)
        diameter = PVC_SCHED80_INNER_DIAMETER
        friction = PVC_SCHED80_FRICTION_FACTOR
        velocity = SUPPLY_VELOCITY
        reynolds = reynolds_number(diameter, velocity)
        loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
        pressure += loss
        loss = pressure_loss_from_fittings(velocity, quantity_angles)
        pressure += loss
        loss = pressure_loss_from_pipe_reduction(diameter,
                velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
        pressure += loss
        diameter = HDPE_SDR11_INNER_DIAMETER
        friction = HDPE_SDR11_FRICTION_FACTOR
        velocity = HOUSEHOLD_VELOCITY
        loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
        pressure += loss
        pressure_psi = kpa_psi(pressure)
        print(f"\nPressure at house: {pressure:.1f} kilopascals or {pressure_psi:.1f} psi\n")
        while calculate == '' or calculate[0] != 'y':
            calculate = input("Would you like to do another calculation (yes/no): ")
            if calculate[0] == 'n':
                print("Have a nice day\n")
                break

def kpa_psi(pressure):
    return pressure * 0.1450377377

def water_column_height(tower_height, tank_height):
    return tower_height + 3 * tank_height / 4

def pressure_gain_from_water_height(height):
    return WATER_DENSITY * EARTH_GRAVITY * height / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    numerator = -friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2
    denominator = 2000 * pipe_diameter
    return numerator / denominator

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    return -.04 * WATER_DENSITY * (fluid_velocity ** 2) * quantity_fittings / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
      return WATER_DENSITY * hydraulic_diameter * fluid_velocity / WATER_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    k=(.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    return -k * WATER_DENSITY * fluid_velocity ** 2 / 2000

if __name__ == "__main__":
    main()