import subprocess

# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 -c 4

proc = subprocess.run(
    #  ['ping', '127.0.0.1', '-c', '4'], #  linux
    ['ping', '127.0.0.1'],    # windows
    capture_output=True,
    text=True
)

saida = proc.stdout
print(saida)
