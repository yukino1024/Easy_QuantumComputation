class pt2_ene:
    def __init__(self, energy):
        self._all_data = energy
        self._ene_data = {}
        self._get_energy()


    #读取pt2根的能量
    def get(self, i):
        if self._all_data == []:
            return 'Empty'
        try:
            return self._ene_data[str(i)]
        except:
            return 'Error'

    #读取pt2根个数
    def get_num(self):
        return len(self._ene_data)
    



    def _get_energy(self):
        if self._all_data == []:
            return
        i = 1
        for line in self._all_data:
            s = line.split()
            self._ene_data[str(i)] = s[6]
            i += 1