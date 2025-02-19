DFT_TYPES = {
    'single': '#p {func}/{basis} freq nosym 5d scfcyc(maxcyc=300)',
    'opt': '#p {func}/{basis} opt(maxcyc=150,modred) freq nosym 5d scfcyc(maxcyc=300)',
    'ts': '#p {func}/{basis} guess(read) geom(check) opt(ts,rcfc,noeigentest,nofreeze,maxstep=5,maxcyc=150) nosym 5d scfcyc(maxcyc=300)',
    'irc_r': '#p {func}/{basis} guess(read) geom(check) irc(rcfc,forward,Maxpoint=120,StepSize=5,MaxCyc=150) nosym 5d scfcyc(maxcyc=300)',
    'irc_f': '#p {func}/{basis} guess(read) geom(check) irc(rcfc,reverse,Maxpoint=120,StepSize=5,MaxCyc=150) nosym 5d scfcyc(maxcyc=300)'
}

CAS_TYPES = {
    'y_chk,n_alter': '#p cas({ele},{orb})/{bas} 5d scfcyc=300 geom(check) guess(read) nosym scfcon=6',
    'y_chk,y_alter': '#p cas({ele},{orb})/{bas} 5d scfcyc=300 geom(check) guess(read,alter) nosym scfcon=6',
    'n_chk,n_alter': '#p cas({ele},{orb})/{bas} 5d scfcyc=300 nosym scfcon=6',
    'n_chk,y_alter': '#p cas({ele},{orb})/{bas} 5d scfcyc=300 guess(alter) nosym scfcon=6'
}