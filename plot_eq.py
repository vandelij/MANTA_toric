import equilibrium_process as eqdsk
eqdsk_file='ips-eqdsk.geq'
print(eqdsk_file)
eq0,fig0=eqdsk.readGEQDSK(eqdsk_file,doplot=True,dolimiter=True)
