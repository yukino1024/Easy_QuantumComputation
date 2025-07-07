class ras_ene:
    def __init__(self, energy):
        self._all_data = energy
        self._ene_data = {}
        self._get_energy()

    #读取ras根的能量
    def get(self,i):
        if self._all_data == []:
            return 'Empty'
        try:
            return self._ene_data[str(i)]
        except:
            return 'Error'

    #读取ras根个数
    @property
    def get_num(self):
        return len(self._ene_data)


    def _get_energy(self):
        if self._all_data == []:
            return
        for line in self._all_data:
            s = line.split()
            self._ene_data[s[4]] = s[7]