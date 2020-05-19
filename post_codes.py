def postcodes_generator():
    postcode1 = input("wpisz pierwszy kod pocztowy")
    postcode2 = input("wpisz drugi kod pocztowy")
    postcodes_list = []
    precinct1 = int(postcode1[0]) * 10 + int(postcode1[1])
    office1 = int(postcode1[3]) * 100 + int(postcode1[4])*10 + int(postcode1[5])
    precinct2 = int(postcode2[0])*10 + int(postcode2[1])
    office2 = int(postcode2[3]) * 100 + int(postcode2[4])*10 + int(postcode2[5])
    lesser1st= False
    if precinct1 < precinct2:
        lesser1st = True
    elif precinct1 == precinct2:
        if office1 < office2:
            lesser1st = True
        elif office1 == office2:
            exit(0)
    if lesser1st:
        starting_office = (office1 + 1)%1000
        ending_office = office2
        starting_precinct = precinct1
        ending_precinct = precinct2
    else:
        starting_office = (office2 + 1)%1000
        ending_office = office1
        starting_precinct = precinct2
        ending_precinct = precinct1
    while starting_precinct != ending_precinct or starting_office != ending_office:
        if starting_office < 10:
            office = '00' + str(starting_office)
        elif starting_office < 100:
            office = '0' + str(starting_office)
        else:
            office = str(starting_office)
        postcodes_list.append((str(starting_precinct) + '-' + office))
        starting_office += 1
        if starting_office == 999:
            starting_office = 0
            starting_precinct += 1

    print(postcodes_list)