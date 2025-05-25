class ras_ene:
    def __init__(self, energy):
        self.all_data = energy
        self.ene_data = {}
        self._get_energy()

    #读取ras根的能量
    def get(self,i):
        if self.all_data == []:
            return 'Empty'
        try:
            return self.ene_data[str(i)]
        except:
            return 'Error'

    #读取ras根个数
    @property
    def get_num(self):
        return len(self.ene_data)


    def _get_energy(self):
        if self.all_data == []:
            return
        for line in self.all_data:
            s = line.split()
            self.ene_data[s[4]] = s[7]