"""
生成文件夹
"""

import os
from FileInformation import *

class Father:
    def __init__(self, path, NPROCSHARED=8, charge=0, multiplicity=1, title='No Title'):
        self.path = path
        if not '/' in path:
            self.file_name = path
        else:
            self.file_name = path.split('/')[-1]
        self.nprocshared = NPROCSHARED
        self.charge = charge
        self.multiplicity = multiplicity
        self.IN_HEAD = IN_HEAD(NPROCSHARED=self.nprocshared, chk_name=self.file_name)
        self.TITLE = Title(title)
        self.CHA_MUL = CHA_MUL(charge=self.charge, multiplicity=self.multiplicity)

    def creat_nomal_dir(self):
        self.creat_main_dir()
        self.creat_result_dir(self.path)
        self.IN_path = self.path + '/' + self.file_name + '.in'  # in文件路径

    def creat_main_dir(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path, exist_ok=True)
            print(f"Directory {self.path} created")
        else:
            print(f"Directory {self.path} already exists")

    def creat_result_dir(self, path):
        if not os.path.exists(path + '/result'):
            os.makedirs(path + '/result', exist_ok=True)
            print(f"Directory {path + '/result'} created")
        else:
            print(f"Directory {path + '/result'} already exists")


class DTF_gen(Father):
    def __init__(self, path, NPROCSHARED=8, charge=0, multiplicity=1, title='No Title', func='m06', basis='6-31G*', type='single', solvent=False):
        super().__init__(path, NPROCSHARED, charge, multiplicity, title)
        self.func = func
        self.basis = basis
        self.type = type
        self.solvent = solvent
        self.DFT_ROUTE = DFT_ROUTE(func=self.func, basis=self.basis, solvent=self.solvent)

    def creat_file(self):
        if self.type == 'irc':
            self.creat_irc_dir()
            for i in range(2):
                with open(self.IN_path[i], 'w') as f:
                    f.write(self.IN_HEAD.get)
                    f.write(self.get_route[i])
                    f.write(self.TITLE.get)
                    f.write(self.CHA_MUL.get)
                    f.write('\n\n')
                    print(f"File {self.IN_path[i]} created")
        else:
            self.creat_nomal_dir()
            with open(self.IN_path, 'w') as f:
                f.write(self.IN_HEAD.get)
                f.write(self.get_route)
                f.write(self.TITLE.get)
                f.write(self.CHA_MUL.get)
                f.write('\n\n')
                print(f"File {self.IN_path} created")

    @property
    def get_route(self):
        if self.type == 'single':
            return self.DFT_ROUTE.g_single
        elif self.type == 'opt':
            return self.DFT_ROUTE.g_opt
        elif self.type == 'ts':
            return self.DFT_ROUTE.g_ts
        elif self.type == 'irc':
            return (self.DFT_ROUTE.g_irc_r, self.DFT_ROUTE.g_irc_f)
        else:  # 默认single
            return self.DFT_ROUTE.g_single

    def creat_irc_dir(self):
        self.creat_main_dir()
        sub_dir_r = self.path + '/' + self.file_name + '_r'
        sub_dir_f = self.path + '/' + self.file_name + '_f'
        if not os.path.exists(sub_dir_r) and not os.path.exists(sub_dir_f):
            os.makedirs(sub_dir_f, exist_ok=True)
            os.makedirs(sub_dir_r, exist_ok=True)
            self.creat_result_dir(sub_dir_f)
            self.creat_result_dir(sub_dir_r)
            self.IN_path = (sub_dir_f + '/' + self.file_name + '_f.in', sub_dir_r + '/' + self.file_name + '_r.in')  # in文件路径
            print(f"Directory {self.path + '/irc'} created")
        else:
            print(f"Directory {self.path + '/irc'} already exists")



class CAS_gen(Father):
    def __init__(self, path, NPROCSHARED=8, charge=0, multiplicity=1, title='No Title', ele=4, orb=4, basis='6-31G*', opt=False, chk = False, alter=False):
        super().__init__(path, NPROCSHARED, charge, multiplicity, title)
        self.ele = ele
        self.orb = orb
        self.basis = basis
        self.opt = opt
        self.chk = chk
        self.alter = alter
        self.type = self.get_type()
        self.CAS_ROUTE = CAS_ROUTE(ele=self.ele, orb=self.orb, bas=self.basis, opt=self.opt)
        self.alter = CAS_ALTER(alter=self.alter)

    def creat_file(self):
        self.creat_nomal_dir()
        with open(self.IN_path, 'w') as f:
            f.write(self.IN_HEAD.get)
            f.write(self.get_route)
            f.write(self.TITLE.get)
            f.write(self.CHA_MUL.get)
            f.write(self.alter.get)
            f.write('\n\n')
            print(f"File {self.IN_path} created")

    @property
    def get_route(self):
        if self.type == 'y_chk,n_alter':
            return self.CAS_ROUTE.g_ycna
        elif self.type == 'y_chk,y_alter':
            return self.CAS_ROUTE.g_ycya
        elif self.type == 'n_chk,n_alter':
            return self.CAS_ROUTE.g_ncna
        elif self.type == 'n_chk,y_alter':
            return self.CAS_ROUTE.g_ncya
        else:  # 默认y_chk,n_alter
            return self.CAS_ROUTE.g_ycna
    
    def get_type(self):
        s = ''
        if self.chk:
            s += 'y_chk,'
        else:
            s += 'n_chk,'
        if self.alter:
            s += 'y_alter'
        else:
            s += 'n_alter'
        return s