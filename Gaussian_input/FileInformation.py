'''
文件具体信息
'''

from custom_types import DFT_TYPES, CAS_TYPES

class IN_HEAD:  # .in文件头
    def __init__(self, NPROCSHARED=8, chk_name=False):
        self.NPROCSHARED = str(NPROCSHARED)
        self.mem = str(NPROCSHARED * 8) + 'GB'
        if chk_name:
            self.chk = str(chk_name) + '.chk'
        else:
            self.chk = False

    @property
    def get(self):
        if self.chk:
            return '%NPROCSHARED=' + self.NPROCSHARED + '\n%mem=' + self.mem + '\n%chk=' + self.chk + '\n'
        else:
            return '%NPROCSHARED=' + self.NPROCSHARED + '\n%mem=' + self.mem + '\n'


class DFT_ROUTE:  # DFT计算路线
    def __init__(self, func='m06', basis='6-31G*', solvent=False):  # 需要加溶剂请直接输入溶剂名
        self.func = str(func)
        self.basis = str(basis)
        self.TYPE = DFT_TYPES.copy()
        if solvent != 'False':  # 溶剂
            for key in self.TYPE:
                self.TYPE[key] += ' scrf=(PCM,solvent=' + solvent + ')'

    # 拿到各种ROUTE
    @property
    def g_single(self):
        return self.TYPE['single'].format(func=self.func, basis=self.basis) + '\n\n'

    @property
    def g_opt(self):
        return self.TYPE['opt'].format(func=self.func, basis=self.basis) + '\n\n'

    @property
    def g_ts(self):
        return self.TYPE['ts'].format(func=self.func, basis=self.basis) + '\n\n'

    @property
    def g_irc_r(self):
        return self.TYPE['irc_r'].format(func=self.func, basis=self.basis) + '\n\n'

    @property
    def g_irc_f(self):
        return self.TYPE['irc_f'].format(func=self.func, basis=self.basis) + '\n\n'


class CAS_ROUTE:  # CAS计算路线
    def __init__(self, ele=4, orb=4, bas='6-31G*', opt=False):  # 需要优化请直接输入优化步数
        self.ele = str(ele)
        self.orb = str(orb)
        self.bas = str(bas)
        self.TYPE = CAS_TYPES.copy()
        if opt != 'False':
            for key in self.TYPE:
                self.TYPE[key] += ' opt(maxcyc=' + str(opt) + ',modred)'

    # 拿到各种ROUTE
    @property
    def g_ycna(self):
        return self.TYPE['y_chk,n_alter'].format(ele=self.ele, orb=self.orb, bas=self.bas) + '\n\n'

    @property
    def g_ycya(self):
        return self.TYPE['y_chk,y_alter'].format(ele=self.ele, orb=self.orb, bas=self.bas) + '\n\n'

    @property
    def g_ncna(self):
        return self.TYPE['n_chk,n_alter'].format(ele=self.ele, orb=self.orb, bas=self.bas) + '\n\n'

    @property
    def g_ncya(self):
        return self.TYPE['n_chk,y_alter'].format(ele=self.ele, orb=self.orb, bas=self.bas) + '\n\n'


class Title:  # 标题
    def __init__(self, title='No Title'):
        self.title = title

    @property
    def get(self):
        return 'Title: ' + self.title + '\n\n'


class CHA_MUL:  # 电荷和自旋
    def __init__(self, charge=0, multiplicity=1):
        self.charge = str(charge)
        self.multiplicity = str(multiplicity)

    @property
    def get(self):
        return self.charge + ' ' + self.multiplicity + '\n'



class CAS_ALTER:
    def __init__(self, alter=False):
        self.alter = alter

    @property
    def get(self):
        if self.alter:
            s = '\n'
            for i in self.alter:
                s += str(i) + '\n'
            return s
        else:
            return ''