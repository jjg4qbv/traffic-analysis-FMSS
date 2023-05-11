import subprocess

num_sim = 200
for i in range(0, num_sim):
    cmd = ["./../prism-games/prism/bin/prism",
           "./corner.prism",
           "-simpath",
           "1000",
       #     "stdout"
           "./sims/sim" + str(i) + ".txt"
           ]
    
    subprocess.run(cmd)