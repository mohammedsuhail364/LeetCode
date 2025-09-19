class Spreadsheet:

    def __init__(self, rows: int):
        self.cell=defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.cell[cell]=value

    def resetCell(self, cell: str) -> None:
        self.cell[cell]=0

    def getValue(self, formula: str) -> int:

        x,y=formula.split("+")
        x1=x[1:]
        tmp1=tmp2=0
        if x1.isdigit():
            tmp1=int(x1)
        else:
            tmp1=self.cell[x1]
        if y.isdigit():
            tmp2=int(y)
        else:
            tmp2=self.cell[y]
        return tmp1+tmp2