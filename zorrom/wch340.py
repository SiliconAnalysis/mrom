from zorrom import mrom


# This is possible the CH340T-Series
class CH340(mrom.MaskROM):
    def desc(self):
        return 'CH340'

    def endian(self):
        return "big"

    def word_bits(self):
        return 14

    def nwords(self):
        return ((16 * 14 * 64) // 14)

    def txtwh(self):
        # 14 groups (16 bits in each) of 224 bits across, 64 lines down.
        return (16 * 14, 64)

    def invert(self):
        return True

    '''Given binary (word offset, bit index) return image row/col'''

    def calc_oi2cr(self, offset, maski):
        row = offset // 16
        col = (15 - (offset % 16)) + 16 * (13 - maski)
        return (col, row)
