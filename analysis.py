import pylhe
import math
import matplotlib.pyplot as plt

#file: generate p p > mu+ vm & launch 50.000 events
file = "/mnt/c/Users/bukec/pp_muvm/Events/run_01/unweighted_events.lhe.gz"

muon_pT = []
muon_phi = []
neutrino_pT = []
neutrino_phi = []
mT_list = []

for event in pylhe.read_lhe_with_attributes(file):
	for particle in event.particles:
		if particle.id == -13:
			px = particle.px
			py = particle.py
			pT = (px**2 + py**2)**0.5
			phi = math.atan2(py, px)
			muon_pT.append(pT)
			muon_phi.append(phi)
		elif particle.id == 14:
			px = particle.px
			py = particle.py
			pT = (px**2 + py**2)**0.5
			phi = math.atan2(py, px)
			neutrino_pT.append(pT)
			neutrino_phi.append(phi)
	mT = (2*muon_pT[-1]*neutrino_pT[-1]*(1-math.cos(muon_phi[-1]-neutrino_phi[-1])))**0.5
	mT_list.append(mT)
print(f"anti-muons: {len(muon_pT)}")
print(f"neutrinos: {len(neutrino_pT)}")
print(f"First 5 mT values: {[round(x,2) for x in mT_list[:5]]}")

plt.xlabel("mT (GeV)")
plt.ylabel("Number of events")
plt.hist(mT_list, bins = 100, range=(0, 150))
plt.savefig("mT.png")
plt.show()
