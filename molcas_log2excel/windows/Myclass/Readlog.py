class read:
    def __init__(self,path):
        self._all_data = []
        self._ras_data = []
        self._pt2_data = []
        self._occ_data = []
        self._osc_data= []
        self._dm_data = []
        self._file_path = path
        self._read()
        self._read_ras()
        self._read_pt2()
        self._read_occ()
        self._read_osc()

    #获取数据
    @property
    def ras_energy(self):
        return self._ras_data
    
    @property
    def pt2_energy(self):
        return self._pt2_data
    
    @property
    def occ(self):
        return self._occ_data
    
    @property
    def osc(self):
        return self._osc_data


    #读取ras_energy数据
    def _read_ras(self):
        for line in self._all_data:
            if 'RASSCF root number' in line:
                self._ras_data.append(line)


    #读取pt2_energy数据
    def _read_pt2(self):
        for line in self._all_data:
            if 'CASPT2 Root' in line:
                self._pt2_data.append(line)


    #读取占据轨道数据
    def _read_occ(self):
        judge = False
        for line in self._all_data:
            if 'CI-coefficients' in line:
                judge = True
            if 'Natural orbitals' in line:
                judge = False
            if judge:
                self._occ_data.append(line)


    #读取osc数据
    def _read_osc(self):
        judge = False
        count = 0
        for line in self._all_data:
            if 'osc.' in line:
                judge = True
            if judge:
                if '--' in line:
                    count += 1
                if count == 2:
                    break
                self._osc_data.append(line)


    #读取dm数据
    def _read_dm(self):
        pass


    #读取所有内容
    def _read(self):
        with open(self._file_path, 'r') as file:
            self._all_data = file.readlines()