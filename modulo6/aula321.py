import subprocess
import sys

# mac or linux
cmd = ['ping', '127.0.0.1', '-c', '4']
enconding = 'utf-8'

if sys.platform == 'win32':
    cmd = ['ping', '127.0.0.1']
    enconding= 'cp850'

proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding=enconding
)
print()
# print(proc.args)
# print(proc.stderr)
# print(proc.stdout.decode('cp850'))
print(proc.stdout)
# print(proc.returncode)
