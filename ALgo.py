def stableMatching(n, menPreferences, womenPreferences):

# Do not change the function definition line.



  # Initially, all n men are unmarried

  unmarriedMen = list(range(n))

  # None of the men has a spouse yet, we denote this by the value None

  manSpouse = [None] * n

  # None of the women has a spouse yet, we denote this by the value None

  womanSpouse = [None] * n

  # Each man made 0 proposals, which means that

  # his next proposal will be to the woman number 0 in his list

  nextManChoice = [0] * n

# While there exists at least one unmarried man:

  while unmarriedMen:

    # Pick an arbitrary unmarried man

    he = unmarriedMen[0]

    # Store his ranking in this variable for convenience

    hisPreferences = menPreferences[he]

    # Find a woman to propose to

    she = hisPreferences[nextManChoice[he]]

    # Store her ranking in this variable for convenience

    herPreferences = womenPreferences[she]

    # Find the present husband of the selected woman (it might be None)

    currentHusband = womanSpouse[she]

    //*************************************************//

    divorcedMan = None
    manProposing = 0
    while manProposing < len(unmarriedMen):
      he = unmarriedMen[manProposing]
      hisPreferences = menPreferences[he]
      she = hisPreferences[nextManChoice[he]]
      herPreferences = womenPreferences[she]
      currentHusband = womanSpouse[she]
      if currentHusband == None:
        womanSpouse[she] = he
        manSpouse[he] = she
        if (len(unmarriedMen) - nextManChoice[he]) >= 2:

            nextManChoice[he] += 1

            unmarriedMen[he] = -1

            manProposing += 1

        else:


          if herPreferences.index(he) < herPreferences.index(currentHusband):


            divorcedMan = currentHusband

            manSpouse[divorcedMan] = None


            womanSpouse[she] = he

          
            manSpouse[he] = she


            if (len(unmarriedMen) - nextManChoice[he]) >= 2:

              nextManChoice[he] += 1


            unmarriedMen[he] = -1


            manProposing += 1


        for man in unmarriedMen:

            if (unmarriedMen.index(man) == divorcedMan) and (man == -1):

              unmarriedMen[unmarriedMen.index(man)] = divorcedMan

              break

            else:
                 if (divorcedMan < man):

                    unmarriedMen.insert(unmarriedMen.index(man), divorcedMan)

                 break



            divorcedMan = None


    temp = []


    for bachelor in unmarriedMen:

      if bachelor != -1:

          temp.append(bachelor)

    unmarriedMen = temp

    return manSpouse