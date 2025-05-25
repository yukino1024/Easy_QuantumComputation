from DirGeneration import *

s1 = DTF_gen(path = 'a/test_single',NPROCSHARED=8,charge=0,multiplicity=1,title='No Title',func='m06', basis='6-31G*',type='single',solvent='Water')
s1.creat_file()
s2 = DTF_gen(path = 'a/test_opt',NPROCSHARED=8,charge=0,multiplicity=1,title='No Title',func='m06', basis='6-31G*',type='opt',solvent='Water')
s2.creat_file()
s3 = DTF_gen(path = 'a/test_ts',NPROCSHARED=8,charge=0,multiplicity=1,title='No Title',func='m06', basis='6-31G*',type='ts',solvent='Water')
s3.creat_file()
s4 = DTF_gen(path = 'a/test_irc',NPROCSHARED=8,charge=0,multiplicity=1,title='No Title',func='m06', basis='6-31G*',type='irc',solvent='Water')
s4.creat_file()