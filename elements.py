from collections import OrderedDict
from mendeleev import *

def elementStats(badelement):
    Myelement = element(badelement)
    data = OrderedDict([
        ('Name:', Myelement.name),
        ('Symbol:', Myelement.symbol),
        ('Period:', Myelement.period),
        ('Block:', Myelement.block),
        ('Atomic Number:', Myelement.atomic_number),
        ('Number of Neutrons:', Myelement.neutrons),
        ('Number of Protons:', Myelement.protons),
        ('Atomic Radius (pm):', Myelement.atomic_radius),
        ('Atomic Volume(cm³/mol):', Myelement.atomic_volume),
        ('Atomic Weight:', Myelement.atomic_weight),
        ('Density (g/gm³ @ 295K):', Myelement.density),
        ('Dipole polarizability:', Myelement.dipole_polarizability),
        ('Discoverers:', Myelement.discoverers),
        ('Electron Affinity (eV):', Myelement.electron_affinity),
        ('Electrons:', Myelement.electrons),
        ('Electronegativity (eV):', Myelement.en_pauling),
        ('Electron configuration:', Myelement.econf),
        ('Thermal conductivity @25 C (W/(m K)):', Myelement.thermal_conductivity),
        ('Specific heat @ 20 C, (J/(g mol)):', Myelement.specific_heat),
        ('Heat of Evaporation (kJ/mol):', Myelement.evaporation_heat),
        ('Heat of Fusion (kJ/mol):', Myelement.fusion_heat),
        ('Heat of Formation (kJ/mol):', Myelement.heat_of_formation),
        ('Heat of Melting (kJ/mol):', Myelement.melting_point),
        ('Heat of Boiling (K):', Myelement.boiling_point),
        ('Gas Basicity:', Myelement.gas_basicity),
        ('Geochemical classification:', Myelement.geochemical_class),
        ('Group:', Myelement.group),
        ('Monoisotopic?:', Myelement.is_monoisotopic),
        ('Radioactive?:', Myelement.is_radioactive),
        ('Isotopes:', Myelement.isotopes),
        ('Mass Number:', Myelement.mass_number),
        ('Oxidation States:', Myelement.oxistates),
        ('Proton Affinity', Myelement.proton_affinity),
        ('CAS Number:', Myelement.cas),
        ('Covalent Radius (pm):', Myelement.covalent_radius_bragg),
        ('Van der Waals radius (pm):', Myelement.vdw_radius),
        ])
    return(data)


