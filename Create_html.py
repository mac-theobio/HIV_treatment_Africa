# Run a python script from another python script
# http://stackoverflow.com/questions/3781851/run-a-python-script-from-another-python-script-passing-in-args

import subprocess
cmd = 'python csv2html.py base.table.csv > base.html'

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
out, err = p.communicate() 
result = out.split('\n')
for lin in result:
	if not lin.startswith('#'):
		print(lin)

