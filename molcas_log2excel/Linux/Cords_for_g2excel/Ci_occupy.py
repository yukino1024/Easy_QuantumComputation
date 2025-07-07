class ci_coo:
    def __init__(self,data):
        self._all_data = data
        self._occ_data = {}
        self._all_occ = {}
        self._get_allocc()
        self._get_maxocc()

    #读取ci根的占据
    def get(self, i):
        if self._all_data == []:
            return 'Empty'
        try:
            return self._occ_data[str(i)]
        except:
            return 'Error'

    #读取ci根个数
    def get_num(self):
        return len(self._occ_data)



    #读取ci根的最大权重占据
    def _get_maxocc(self):
        if self._all_data == []:
            return
        for i in self._all_occ:
            s = self._all_occ[i]
            s.sort(key=lambda x: float(x[1]), reverse=True)
            self._occ_data[i] = s[0][0]

    #读取ci根的所有占据
    def _get_allocc(self):
        if self._all_data == []:
            return
        i= False
        judge1 = False
        judge2 = False
        for line in self._all_data:
            if 'root' in line:
                kk = line.split()
                i = kk[8]
                self._all_occ[i] = []
                judge1 = True
            if 'conf/sym' in line:
                judge2 = True
                continue
            if judge1 and judge2:
                if line == '\n':
                    judge1 = False
                    judge2 = False
                    continue
                self._all_occ[str(i)].append([line.split()[1],line.split()[3]])