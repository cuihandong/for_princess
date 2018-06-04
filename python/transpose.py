import click

# index method [row_idx][col_idx]


class Transposer(object):

    def __init__(self, filename, out_filename, head=1, sep=None):
        self._filename = filename
        self._head = head
        self._col_num = 0
        self._row_num = 0
        self._sep = sep
        self._data = []
        self._data_tp = []
        self._out_filename = out_filename
        if self._out_filename is None or self._out_filename == "":
            self._out_filename = self._filename + "transposition.txt"

    def readfile(self):
        file = open(self._filename, "r")
        lines = file.readlines()
        file.close()

        self._col_num = -1
        self._row_num = len(lines) - self._head

        for row in range(len(lines))[self._head:]:

            line = lines[row]
            ld = line.split(self._sep)
            l = len(ld)
            if row == self._head:
                self._col_num = l
            if self._col_num != l:
                print("the col is ", l, ", but expected", self._col_num)
                return False
            self._data.append(ld)

    def transpose(self):
        tp_col = self._row_num
        tp_row = self._col_num
        data_tp = [[self._data[c][r] for c in range(tp_col)] for r in range(tp_row)]
        self._data_tp = data_tp

    def writefile(self):
        lines = []
        for row in self._data_tp:
            sep = "\t" if self._sep is None else self._sep
            line = sep.join(row)
            line += "\n"
            lines.append(line)

        out_file_name = self._out_filename
        f = open(out_file_name, "w")
        f.writelines(lines)
        f.close()


@click.command()
@click.option('--sep', default=None, help='Using sep as the delimiter string between columns, default="\\t"')
@click.option('-o', help="the file for saving transposed data")
@click.argument('filename', type=click.Path(exists=True))
def transpose(filename, o, sep):
    ts = Transposer(filename, o, 0, sep)
    ts.readfile()
    ts.transpose()
    ts.writefile()


if __name__ == "__main__":
    transpose()
