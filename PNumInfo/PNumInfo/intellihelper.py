try:
    def intellihelper(NumberOrCountry,event=None,porr=False):
        number = str(NumberOrCountry)
        prefix = {"+1" : "USA","+90" : "TUR","USA":"+1","TUR":"+90"}
        for i in prefix:
                if number.startswith(str(i)):
                    if porr==True:
                        print(prefix.get(i))
                    else:
                        return prefix.get(i)
except:
    print("Sory!.Please Try Agian")
finally:
    a =1