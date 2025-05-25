class pt2_ene:
    def __init__(self, energy):
        self.all_data = energy
        self.ene_data = {}
        self._get_energy()


    #读取pt2根的能量
    def get(self, i):
        if self.all_data == []:
            return 'Empty'
        try:
            return self.ene_data[str(i)]
        except:
            return 'Error'

    #读取pt2根个数
    def get_num(self):
        return len(self.ene_data)
    



    def _get_energy(self):
        if self.all_data == []:
            return
        i = 1
        for line in self.all_data:
            s = line.split()
            self.ene_data[str(i)] = s[6]
            i += 1