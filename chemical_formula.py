first_element = input("Your first element is: ")
to_continue = True
first_parity = ""
second_parity = ""
the_first_element_type = ""
the_second_element_type = ""

match first_element:
    case "H":
        first_parity = 1
        the_first_element_type = "+"
    case "He":
        print("This element cannot enter into a chemical reaction")
        to_continue = False
    case "Li":
        first_parity = 1
        the_first_element_type = "+"
    case "Be":
        first_parity = 2
        the_first_element_type = "+"
    case "B":
        first_parity = 3
        the_first_element_type = "+"
    case "C":
        first_parity = 4
        the_first_element_type = "+"
    case "N":
        first_parity = 3
        the_first_element_type = "-"
    case "O":
        first_parity = 2
        the_first_element_type = "-"
    case "F":
        first_parity = 1
        the_first_element_type = "-"
    case "Ne":
        print("This element cannot enter into a chemical reaction")
        to_continue = False
    case "Na":
        first_parity = 1
        the_first_element_type = "+"
    case "Mg":
        first_parity = 2
        the_first_element_type = "+"
    case "Al":
        first_parity = 3
        the_first_element_type = "+"
    case "Si":
        first_parity = 4
        the_first_element_type = "+"
    case "P":
        first_parity = 3
        the_first_element_type = "-"
    case "S":
        first_parity = 2
        the_first_element_type = "-"
    case "Cl":
        first_parity = 1
        the_first_element_type = "-"
    case "Ar":
        print("This element cannot enter into a chemical reaction")
        to_continue = False
    case "K":
        first_parity = 1
        the_first_element_type = "+"
    case "Ca":
        first_element = 2
        the_first_element_type = "+"
    case "OH":
        first_parity = 1
        the_first_element_type = "-"
    case "NO3":
        first_parity = 1
        the_first_element_type = "-"
    case "NO2":
        first_parity = 1
        the_first_element_type = "-"
    case "HCO3":
        first_parity = 1
        the_first_element_type = "-"
    case "NH4":
        first_parity = 1
        the_first_element_type = "+"
    case "MnO4":
        first_parity = 1
        the_first_element_type = "-"
    case "ClO3":
        first_parity = 1
        the_first_element_type = "-"
    case "CO3":
        first_parity = 2
        the_first_element_type = "-"
    case "SO4":
        first_parity = 2
        the_first_element_type = "-"
    case "Cr2O7":
        first_parity = 2
        the_first_element_type = "-"
    case "CrO4":
        first_parity = 2
        the_first_element_type = "-"
    case "PO4":
        first_parity = 3
        the_first_element_type = "-"
    case _:
        print("Please write a correct element")
        to_continue = False

if to_continue == True:
    second_element = input("Your second element is: ")
    match second_element:
        case "H":
            second_parity = 1
            the_second_element_type = "+"
        case "He":
            print("This element cannot enter into a chemical reaction")
            to_continue = False
        case "Li":
            second_parity = 1
            the_second_element_type = "+"
        case "Be":
            second_parity = 2
            the_second_element_type = "+"
        case "B":
            second_parity = 3
            the_second_element_type = "+"
        case "C":
            second_parity = 4
            the_second_element_type = "+"
        case "N":
            second_parity = 3
            the_second_element_type = "-"
        case "O":
            second_parity = 2
            the_second_element_type = "-"
        case "F":
            second_parity = 1
            the_second_element_type = "-"
        case "Ne":
            print("This element cannot enter into a chemical reaction")
            to_continue = False
        case "Na":
            second_parity = 1
            the_second_element_type = "+"
        case "Mg":
            second_parity = 2
            the_second_element_type = "+"
        case "Al":
            second_parity = 3
            the_second_element_type = "+"
        case "Si":
            second_parity = 4
            the_second_element_type = "+"
        case "P":
            second_parity = 3
            the_second_element_type = "-"
        case "S":
            second_parity = 2
            the_second_element_type = "-"
        case "Cl":
            second_parity = 1
            the_second_element_type = "-"
        case "Ar":
            print("This element cannot enter into a chemical reaction")
            to_continue = False
        case "K":
            second_parity = 1
            the_second_element_type = "+"
        case "Ca":
            second_parity = 2
            the_second_element_type = "+"
        case "OH":
            second_parity = 1
            the_second_element_type = "-"
        case "NO3":
            second_parity = 1
            the_second_element_type = "-"
        case "NO2":
            second_parity = 1
            the_second_element_type = "-"
        case "HCO3":
            second_parity = 1
            the_second_element_type = "-"
        case "NH4":
            second_parity = 1
            the_second_element_type = "+"
        case "MnO4":
            second_parity = 1
            the_second_element_type = "-"
        case "ClO3":
            second_parity = 1
            the_second_element_type = "-"
        case "CO3":
            second_parity = 2
            the_second_element_type = "-"
        case "SO4":
            second_parity = 2
            the_second_element_type = "-"
        case "Cr2O7":
            second_parity = 2
            the_second_element_type = "-"
        case "CrO4":
            second_parity = 2
            the_second_element_type = "-"
        case "PO4":
            second_parity = 3
            the_second_element_type = "-"
        case _:
            print("Please write a correct element")
            to_continue = False

    if the_first_element_type == the_second_element_type:
        print("These elements cannot enter into a chemical reaction")
    else:
        if first_parity == second_parity:
            print(f"({first_element})({second_element})")
        else:
            print(f"({first_element}){second_parity}({second_element}){first_parity}")