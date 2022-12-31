import json

from datetime import datetime, date

from Fate import OparateItem

class DataSync:

    def Open(self,File:str|None = None) -> dict:

        if not File is None:

            self.File=File

        with open(self.File,'r',encoding='UTF8') as f:

            self.Data = json.loads(f.read())

        return self.Data

    def Close(self,Data:dict,File:str|None = None) -> None:

        if not File is None:

            self.File=File

        self.Data=Data

        with open(self.File,"w",encoding="UTF8") as f:

            json.dump(self.Data,f,indent=4)

class OprateDate:

    def MultifyDate(self,Date:date,Money:int) -> str:

        DfDays = date.today().toordinal() - Date.toordinal()
        
        Date= date.fromordinal(DfDays)

        MFDate = (Date.year-1)*12
        
        MFDate =(MFDate + (Date.month-1))*3

        DateOfMoney = f"{-MFDate + Money}"

        return DateOfMoney

class Operatings(DataSync,OprateDate,OparateItem):

    def Looking(self,Arg:list[str])-> bool:

        Data=self.Open()

        if len(Arg) !=1:

            user=str(Arg[1]).lower()

            if not user in Data:
                
                self.err="Kayıtlarda bu isim yok"

                return False
                
            
            Data[user]["Releas"]=str(date.today())

            dt = datetime.strptime(Data[user]["Date"],'%d-%m-%Y')

            Money = self.MultifyDate(dt.date(),Data[user]["Money"])

            self.Print = user+" "+Money+"TL"

        else :

            self.Print=""

            for Users in Data:

                dt = datetime.strptime(Data[Users]["Date"],'%d-%m-%Y')

                if dt != 0 :

                    Money = self.MultifyDate(dt.date(),Data[Users]["Money"])

                    self.Print += f"{Users}:{Money} TL \n"
                
                else:

                    self.Print += f"{Users}:{Data[Users]['Money']} TL \n"
                

                Data[Users]["Releas"]=str(date.today())
            

        self.Close(Data)
        
        return True
         
    def DiscontAndWhitdraw(self,Arg:list[str]) -> bool:
        
        Data=self.Open()
        
        self.err=""

        if len(Arg)<2:

            self.err="Give veya Take kullanmadınız"

            return False

        wish:str = str(Arg[1]).lower()

        if not wish in ["give","take"]:

            self.err="girşi kısmında yazım yanlışı"
            
            return False
        
        if len(Arg) == 4 :

            UserName=str(Arg[2]).lower()

            if "give" in wish :
                
                if not UserName in Data:
                    
                    self.err="Kayıtlı kişi bulunamadı"
                    return False

                if not any(x in Arg[3] for x in ["1","2","3","4","5","6","7","8","9","0"]) :

                    self.err="para girmediniz"
                    return False

                Data[UserName]["Money"] += int(Arg[3])

                self.Print = f"bu kişiye {UserName} şukadar para girişi oldu {Arg[3]}"
            
            elif "take" in wish :

                if not UserName in Data:
                    
                    self.err="Kayıtlı kişi bulunamadı"

                    return False

                if not any(x in Arg[3] for x in ["1","2","3","4","5","6","7","8","9","0"]) :

                    self.err="para girmediniz"

                    return False

                Data[UserName]["Money"] -= int(Arg[3])

                self.Print = f"bu kişiye {UserName} şukadar para çıkışı oldu {Arg[3]}"

        elif len(Arg) == 3 :

            if "give" in wish :

                self.Print =""

                if not any(x in Arg[2] for x in ["1","2","3","4","5","6","7","8","9","0"]):

                    self.err="para girmediniz"
                    
                    return False
    
                for Users in Data:
                    
                    Data[Users]["Money"] += int(Arg[2])
                    
                    self.Print += f"bu kişiye {Users} şukadar para girişi oldu {Arg[2]} \n"

            elif "take" in wish :
                
                self.Print=""

                if not any(x in Arg[2] for x in ["1","2","3","4","5","6","7","8","9","0"]) :

                    self.err="para girmediniz"
                    
                    return False
                
                for Users in Data:
                    
                    Data[Users]["Money"] -= int(Arg[2])
                    
                    self.Print += f"bu kişiye {Users} şukadar para Çıkışı oldu {Arg[2]} \n"

        else:

            self.err="Para belirlemediniz"

            return False

        self.Close(Data)
        
        return True
    
    def Toplam(self,Arg:list[str]) -> bool:

        if len(Arg) == 2:

            if not "kayıtlar" in str(Arg[1]).lower():

                self.err ="Toplam ile yanlış kullanalım"
                
                return False

            AllMoney=0

            Data=self.Open()
            
            dt = datetime.strptime(Data[UserName]["Date"],'%d-%m-%Y')
            
            for UserName in Data:
                
                AllMoney += self.MultifyDate(dt.date(),Data[UserName]["Money"])
                
                Data[UserName]["Releas"]=str(date.today())
            
            self.Print = self.AllMoney = AllMoney
            
            self.Close(Data)
            
            return True
        
        else:

            AllMoney=0

            Data=self.Open()

            for UserName in Data:
            
                AllMoney += Data[UserName]["Money"]

            self.Print = self.AllMoney = AllMoney 

            self.Close(Data)
            
            return True

    def Inventory(self,Arg:list[str]):

        promes = Arg[2].lower()

class Outing(Operatings):
    
    def __init__(self,Arg:str,Pname:str="") -> str:

        self.Arg=Arg.split()

        self.Member="MatKing"

        self.Pname=Pname

        self.Print:str

        self.File = "Data.json"

        self.Oparte(self.Arg)

    def Oparte(self,Arg:list[str]) -> None:

        if len(Arg) == 0 :
            
            self.Print="Birşeyler yazınız"

            return

        FirstWord=(Arg[0]).lower()

        if  "kayıtlar" in FirstWord and not len(Arg) > 2 :
        
            if not self.Looking(Arg):
        
                self.Print="Kayıt sırasında hata: " +self.err
        
        elif "money" in FirstWord and not len(Arg) > 4 :

            if self.Member == self.Pname:
                self.Print="Member değilsin"

            elif not self.DiscontAndWhitdraw(Arg):
                
                self.Print="Para konusunda hatalar:" + self.err
            
        
        elif "toplam" in FirstWord and len(Arg) > 0 and len(Arg) <= 2 :

            if not self.Toplam(Arg) :
                
                self.Print="Toplanamadı" + self.err

        else:

            self.Print="Not correct answar"

if __name__ == "__main__":

    print(Outing(input("@:"),"MatKing").Print)