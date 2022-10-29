print('Dobrodosli u kviz znanja!')
pitanje=input('Da li zelite da igrate:')

if pitanje.lower()!='da':
    quit()
else:
    print('Pocnimo')
    score = 0

pitanje=input('Koja je najduza reka na svetu:')
if pitanje.lower()=='nil':
    print('Pogodili ste,krenimo na drugo pitanje!')
    score += 1
else:
    print('Niste pogodili')
    
pitanje=input('Kako se zove pisac koji je napisao trilogiju Gospodar prstenova:')
if pitanje=='tolkin':
    print('Pogodili ste,krenimo na trece pitanje')
    score += 1
else:
    print('Niste pogodili')
    

pitanje=input('Koje je godine Kristifor Kolumbo otkrio Ameriku:')
if pitanje=='1492':
    print('Pogodili ste,krenimo na cetvrto pitanje')
    score += 1
else:
    print('Niste pogodili')

pitanje=input('Franc Ferdinand je bio predstolonaslednik koje drzave:')

if pitanje.lower()=='austrougarske':
    print('Pogodili ste,krenimo na peto pitanje')
    score += 1
else:
    print('Niste pogodili')

pitanje=input('Koji je najveci sisar na svetu:')

if pitanje.lower()=='plavi kit':
    print('Pogodili ste,krenimo na sesto pitanje')
    score +=1
else:
    print('Niste pogodili')
    
pitanje=input('Koji slikar je naslikao Mona Lisu:')

if pitanje.lower()=='leonardo da vinci':
    print('Pogodili ste,krenimo na sedmo pitanje')
    score +=1
else:
    print('Niste pogodili')

pitanje=input('Italija okruzuje dve mikrodrzave,koje su to mikrodrzave:')

if pitanje.lower()=='vatikan i san marino':
    print('Pogodili ste,krenimo na osmo pitanje')
    score +=1
else:
    print('Niste pogodili')

pitanje=input('Kako se zove dogadjaj gde su u psr srbi morali da beze preko albanija :')

if pitanje.lower()=='albanska golgota':
    print('Pogodili ste,krenimo na deveto pitanje')
    score +=1
else:
    print('Niste pogodili')

pitanje=input('Ko je bio premijer engleske tokom dsr:')

if pitanje.lower()=='vinston cercil':
    print('Pogodili ste,krenimo na deseto pitanje')
    score +=1
else:
    print('Niste pogodili')

pitanje=input('Ko je bila kraljica Francuske tokom Francuske revolucije:')

if pitanje.lower()=='marija antoaeneta':
    print('Pogodili ste i zavrsili ste sa kvizom')
    score +=1
else:
    print('Niste pogodili i zavrsili ste sa kvizom')

print('Pogodili ste' + str(score) + 'pitanja tacno')


