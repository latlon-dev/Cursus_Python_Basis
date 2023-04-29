import datetime

nu = datetime.date.today()
gebortedag = datetime.date(1986, 11, 11)

leeftijd_dagen = nu - gebortedag 

print(f"Ik ben vandag {leeftijd_dagen.days} dagen oud")
