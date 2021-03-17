#normalde bi function define edildiginde ve icine
# gonderdigin argumentlerin sirasi onemlidi, parameter
# sirasi neyse ona gore argument gondermen gerekir.
#Ama Keyword="argument" ile siralamaya uymasan da olur

def greeting(name,lastname):
    print(f'Hi, how are you {name} {lastname}!')



greeting(lastname="Aksit",name="Irfan")#argumentlerin sirasini degistirdik ama
#keyword kullanarak da yapabiliyoruz
#keyword kullanmanin bi yarari su; diyelim ki parameter larin hepsi number,
#bu durumda hangi argument hangi number diye kafa karisikligina sebep olabilir
#bu durumda siralamayi dikkat etmeden keywork kullanarak function call edebiliriz