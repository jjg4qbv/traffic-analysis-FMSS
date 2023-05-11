import subprocess

num_sim = 200
for i in range(0, num_sim):
    cmd = ["C:/Program Files/prism-games-3.1/bin/prism.bat",
           "./corner.prism",
           "-simpath",
           "1000",
           "./sims/sim" + str(num_sim) + ".txt"]
    subprocess.run(cmd, shell=True)