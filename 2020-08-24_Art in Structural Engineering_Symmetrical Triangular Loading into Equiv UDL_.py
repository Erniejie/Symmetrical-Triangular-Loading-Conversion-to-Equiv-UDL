import math


print("Conversion of Symmetrical Triangular Loading into Equiv UDL-Beam")

################################INPUT DATA################################

DL_load = float(input("Unfactored Dead Load: "))        ## in [kN/m]
IL_load = float(input("Unfactored Imposed Load: "))     ## in [kN/m]

TotalLoad = DL_load + IL_load
print ("Total Load at SLS = ")
print(TotalLoad)

       
L_Span = float(input("Beam Span: "))                    ## in [m]
E_Modulus  = float(input("Material Young Modulus: "))   ## in [N/mm^2]
I_Inertia = float(input("Moment of Inertia: "))         ## in [cm^4]

############################### WRITING FUNCTIONS###################################
Equivalent_UDL = input("Convert Triangular Load into an Equivalent UDL? (yes/no): ")

if Equivalent_UDL == "yes":

    SF = round(L_Span*(DL_load + IL_load)/3,2)
    BM = round((DL_load + IL_load)*L_Span**2 /12,2)
    D= "%.2f"%(5e12*(DL_load + IL_load)*L_Span**4/(5760000*E_Modulus*I_Inertia))
    

    
    
else:                                         ### (Triangular Load-Actual Conditions)

    SF = "%.2f"%(L_Span*(DL_load + IL_load)/4)
    BM = round((DL_load + IL_load)*L_Span**2 /12,2)
    D= "%.3f"%(1e12*(DL_load + IL_load)*L_Span**4/(1200000*E_Modulus*I_Inertia))


    
###################################OUTPUT DATA################################

print("Maximum Shear Load = ")                             ## in [kN]
print(SF)
print("Maximum Bending Moment = ")                         ## in [kN.m]
print(BM)
print("Maximum Vertical Deflection = ")                    ## in [mm]
print(D)
                     
 
