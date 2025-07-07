import os
from Readlog import read
from Ras_energy import ras_ene
from Pt2_energy import pt2_ene
from Ci_occupy import ci_coo
from Osc_strength import osc_str
from Write_excel import wri_excel

def do_write(log_adress):
    excel_name = os.path.splitext(os.path.basename(log_adress))[0] + '.xlsx'
    excel_adress = os.path.join(os.path.dirname(log_adress), excel_name)
    s = read(log_adress)
    r = ras_ene(s.ras_energy)
    p = pt2_ene(s.pt2_energy)
    c = ci_coo(s.occ)
    o = osc_str(s.osc)
    w = wri_excel()
    for i in range(1, r.get_num + 1):
        w.add_data(i, r.get(i), p.get(i), o.get(i), c.get(i))
    w.wri_data()
    w.save_excel(excel_adress)
