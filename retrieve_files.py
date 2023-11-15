import os, sys
#these shenanigans relate to vscode not having the working directory as the directory of the file it runs
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

host = 'perlmutter.nersc.gov'
username = 'vandelij'
# rwdir = open("remoteDirectory.txt", "r").readlines()[0].strip()
# shotNum = rwdir.split('/')[-1].split('_')[1]

# os.system(f'scp {username}@{host}:/pscratch/sd/v/vandelij/manta_baseline/simulation_results/100.000/components/rf_ic_toric_3/fort.21 .')

os.system(f'scp {username}@{host}:/pscratch/sd/v/vandelij/manta_baseline/simulation_results/100.000/components/rf_ic_toric_3/cql3d.nc .')
os.system(f'scp {username}@{host}:/pscratch/sd/v/vandelij/manta_baseline/simulation_results/100.000/components/rf_ic_toric_3/fort.21 .')