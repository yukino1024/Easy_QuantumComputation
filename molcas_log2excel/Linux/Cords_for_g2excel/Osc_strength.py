class osc_str:
    def __init__(self, data):
        self._all_data = data
        self._str_data = {'1':""}
        self._get_str()


    def get(self, i):
        if self._all_data == []:
            return 'Empty'
        try:
            return self._str_data[str(i)]
        except:
            return 'Error'


    #读取osc根的强度
    def _get_str(self):
        if self._all_data == []:
            return
        judge = False
        for line in self._all_data:
            if '---' in line:
                judge = True
                continue
            if judge:
                s = line.split()
                if s[0] == '1':
                    self._str_data[s[1]] = s[2]
                if s[0] == '2':
                    break