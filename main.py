def main():
    ##################################################
    # Comlete your code here
    ##################################################

    workhours = int(input('Enter work hours'))
reg_hours = int(40)
o_hours = int(10)
reg_rate = float(18.25)
o_rate = float(27.78)
overtime_charge = ( o_hours * o_rate)
regular_charge = (reg_hours * reg_rate)
print('regular_charge: ',reg_hours * reg_rate)
print('overtime_charge: ',o_hours * o_rate)
total_wage = regular_charge + overtime_charge
print('total_wage: ',regular_charge + overtime_charge)
pass

if __name__ == '__main__':
    main()
