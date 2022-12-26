class OparateItem:

    def __init__(self) -> None:
        self.Item:dict
        
    def Item(self,Arg:list[str],Data:dict):
        
        self.Item = Data

        Arg.pop(0)

        Path = str.join("",Arg)

        PISize = Path.count(">")

        Arg = Path.split(">")
            
