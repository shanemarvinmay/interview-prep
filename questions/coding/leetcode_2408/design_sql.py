from typing import List

class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        self.schema = dict() # {name: DataFrame}
        for i in range(len(names)):
            self.schema[names[i]] = Table(names[i],columns[i])

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.schema:
            return False
        return self.schema[name].ins(row)

    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.schema:
            return
        self.schema[name].rmv(rowId)

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.schema:
            return "<null>"
        columnId -= 1
        return self.schema[name].sel(rowId, columnId)

    def exp(self, name: str) -> List[str]:
        if name not in self.schema:
            return []
        return self.schema[name].exp()

class Table:
    def __init__(self, name, cols):
        self.name = name
        self.nxt_idx = 1
        self.num_cols = cols
        self.values = dict()

    def ins(self, row):
        if len(row) != self.num_cols:
            return False
        self.values[self.nxt_idx] = row
        self.nxt_idx += 1
        return True
    def rmv(self, id):
        if id not in self.values:
            return
        del self.values[id]
    def sel(self, id, col):
        if id not in self.values:
            return "<null>"
        if col < 0 or col > self.num_cols:
            return "<null>"
        return self.values[id][col]
    def exp(self):
        rows = []
        # List of the ids sorted
        ids = sorted(list(self.values.keys()))
        for id in ids:
            row = ",".join(self.values[id])
            rows.append(f'{id},{row}')
        return rows


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)