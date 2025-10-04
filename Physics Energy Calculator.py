import math
energytype=input("KE: Kinetic Energy\nGPE: Gravitational Potential Energy\nEPE: Elastic Potential Energy\nP: Power\nW: Work Done. \nEF: Efficiency\nEnter the short forms given of what you would like to work out/use.").lower()
if energytype=="ke":
    variable=input("Would you like to find Energy, mass or velocity² ? Enter either e, m or v2").lower()
    if variable == "e":
        print("E=½ m v²")
        m=float(input("Enter the mass of the object in Kilograms (Kg). "))
        v=float(input("Enter the velocity of the object in metres per second m/s. "))
        E=0.5*m*(v*v)
        print(f"The kinetic energy of the object is equal to {E} Joules.")
    elif variable=="m":
        print("m= E/½ v²")
        E=float(input("Enter the energy of the object in Joules (J). "))
        v=float(input("Enter the velocity of the object in metres per second (m/s)"))
        m=E/(0.5*(v*v))
        print(f"The mass of the object is equal to {m} Kilograms (Kg). ")
    else:
        print("v²=√½(E/m)")
        E=float(input("Enter the energy of the object in Joules (J). "))
        m=float(input("Enter the mass of the object in Kilograms (Kg). "))
        v=math.sqrt(E/(0.5*m))
        print(f"The velocity of the object is equal to {v} metres per second (m)")
elif energytype=="gpe":
    print("E=m g h")
    variable=input("Do you want to find Energy, mass, gravitational field strength or height ? Enter either e, m, g or h. ")
    if variable=="e":
        m=float(input("Enter the mass of the object in kilograms(Kg). "))
        g=float(input("Enter the graviational field strength acting upon the object in Newtons per Kilogram (N/kg). "))
        h=float(input("Enter the height of the object in metres (m). "))
        E=m*g*h
        print(f"The gravitational potential energy in the object is equal to {E} Joules.")
    elif variable=="m":
        E=float(input("Enter the amount of energy in the object in Joules (J). "))
        g=float(input("Enter the graviational field strength acting upon the object in Newtons per Kilogram (N/Kg)"))
        h=float(input("Enter the height of the object in metres (m). "))
        m=E/(g*h)
        print(f"The mass of the object is equal to {m} Kilograms (Kg). ")
    elif variable=="g":
        E=float(input("Enter the amount of energy in the object in Joules (J). "))
        m=float(input("Enter the mass of the object in (Kg). "))
        h=float(input("Enter the height of the object in metres (m). "))
        g=E/(m*h)
        print(f"The gravitational field strength on the object is equal to {g}  Newtons per Kilograms (N/Kg). ")
    else:
        E=float(input("Enter the amount of energy in the object in Joules (J). "))
        g=float(input("Enter the graviational field strength acting upon the object in Newtons per Kilogram (N/Kg)"))
        m=float(input("Enter themass of the object (Kg). "))
        h=E/(m*g)
        print(f"The height of the object is equal to {h} Metres (m). ")
elif energytype=="epe":
    variable=input("Would you like to find Energy, spring constant or extension² ? Enter either e, k or e2").lower()
    if variable == "e":
        print("E=½ k e²")
        k=float(input("Enter the spring constant of the object in Newtons per metre (N/m). "))
        e=float(input("Enter the extension of the object in metres (m). "))
        E=0.5*k*(e*e)
        print(f"The elastic potential energy of the object is equal to {E} Joules.")
    elif variable=="k":
        print("k= E/½ e²")
        E=float(input("Enter the energy of the object in Joules (J). "))
        e=float(input("Enter the extension of the object in metres (m). "))
        k=E/(0.5*(e*e))
        print(f"The spring constant of the object is equal to {k} Newtons per metre (Kg). ")
    else:
        print ("e²=√½(E/k)")
        E=float(input("Enter the energy stored in the object in Joules (J). "))
        k=float(input("Enter the spring constant of the objet in Newtons per metre (N/m)"))
        e=math.sqrt(E/(k*0.5))
        print(f"The extension of the object is equal to {e} metres (m).")
    energytype=input("Do you want to use kinetic, gravitational potential or elastic potential energy? Enter either KE, GPE, or EPE.").lower()
elif energytype=="p":
    variable=input("Would you like to find power, energy transfered, or time ? Enter either P, E or T ").lower()
    if variable=="p":
        print("P=E/t")
        e=float(input("Enter the energy transfered in Joules (J). "))
        t=float(input("Enter the time taken in seconds (s). "))
        p=e/t
        print(f"The power of the object is eqaul to {p} Watts (W).")
    elif variable=="e":
        print("E=Pt")
        p=float(input("Enter the power of the object in Watts (W). "))
        t=float(input("Enter the tie taken in seconds (s). "))
        e=p*t
        print(f"The Energy transfered is equal to {e} Joules (J).")
    else:
        print("t=P/e")
        p=float(input("Enter the power of the object in Watts (W). "))
        e=float(input("Enter the energy transfered in Joules (J). "))
        t=p/e
        print(f"The time taken is equal to {t} Seconds (s).")
elif energytype=="w":
    variable=input("Would you like to calculate the Work done, the force applied or the distance ? Enter either W, F or S. ").lower()
    if variable=="W":
        print("W=Fs")
        f=float(input("Enter the amount of Force applied in Newtons. "))
        s=float(input("Enter the distance travelled in metres. "))
        w=f*s
        print(f"The Work done is equal to {w} Joules (J)")
    elif variable=="f":
        print("f=W/s")
        w=float(input("Enter the work done in Joules (J). "))
        s=float(input("Enter the distance travelled in metres (m). "))
        f=w/s
        print(f"The force applied is equal to {f} Newtons (N). ")
    else:
        print("s=W/f")
        w=float(input("Enter the work done in Joules (J). "))
        f=float(input("Enter the force applied in Newtons (N). "))
        s=w/f
        print(f"The distance travelled is equal to {s} metres.")
else:
    variable=input("Would you like to get the efficiency, useful energy output or total energy input? Enter either e, u or t")
    if variable=="e":
        print("Efficiency= Useful energy output / Total energy input")
        u=float(input("Enter the useful energy output in Joules (J). "))
        t=float(input("Enter the total enrgy input in Joules (J). "))
        if u>t:
            u=float(input("Enter a value below the total energy input."))
        else:
            e=(u/t)*100
            print(f"The object is {e} % efficient.")
    elif  variable=="u":
        print("Useful Energy output= Efficiency x Total energy input")
        e=float(input("Enter the efficiency of the object as a percentage"))/100
        t=float(input("Enter the total energy input to the object in Joules (J)"))
        u=e*t
        print(f"The useful energy output is equal to {u} Joules (J).")
    else:
        e=float(input("Enter the efficiency of the object as a percentage"))/100
        u=float(input("Enter the useful energy output in Joules (J). "))
        t=e*u
        print(f"The total energy output is equal to {t} Joules (J).")
          
