from collections import OrderedDict



periods = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']

tableElements =[['H ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'He'], 
                ['Li', 'Be', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'B ', 'C ', 'N ', 'O ', 'F ', 'Ne'], 
                ['Na', 'Mg', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'Al', 'Si', 'P ', 'S ', 'Cl', 'Ar'],
                ['K ', 'Ca', 'Sc', 'Ti', 'V ', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr'],
                ['Rb', 'Sr', 'Y ', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I ', 'Xe'], 
                ['Cs', 'Ba', ' ↓', 'Hf', 'Ta', 'W ', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn'], 
                ['Fr', 'Ra', ' ↓', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og'],
                ['  ', '  ', ' ↓', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['  ', '  ', '→|', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu'],
                ['  ', '  ', '→|', 'Ac', 'Th', 'Pa', 'U ', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']
                ]



chemInfo= ['',
          'Press l to locate, and n to cycle results.',
          'Press G to jup to bottom, press g to jump to top',
          '',
          '########################',
          '## Table of Contents ###',
          '########################',
          ' ',
          'Table Info',
          'Element Facts',
          'Conversions and Constants',
          'Other Info',
          ' ',
          '-- Table Info --',
          ' ',
          '- Trends -',
          '→Left to Right→',
          '    Atomic Radius Decreases',
          '    Ionization Energy Increases',
          '    Electronegativity Increases',
          '    Electron Affinity Increases',
          ' ',
          '↓Top to Bottom↓',
          '    Atomic Radius Increases',
          '    Ionization Energy Decreases',
          '    Electronegativity Decreases',
          '    Electron  Affinity Decreases',
          ' ',
          ' - Groups - ',
          'Group 1: Alkali Metals',
          'Group 2: Alkaline Earth Metals',
          'Group 11: Coinage Metals (not an IUPAC approved name)',
          'Group 15: Pnictogens (not an IUPAC approved name)',
          'Group 16: Chalcogens',
          'Group 17: Halogens',
          'Group 18: Noble Gases',
          ' ',
          ' ',
          '-- Element Info --',
          ' ',
          'Diatomic Elements: H₂, N₂, O₂, F₂, Cl₂, Br₂, I₂',
          '',
          '-- Conversions and Constants --',
          ' ',
          'Kelvin = ˚C + 273.15',
          'Celsius = (˚F -32) × (5/9)',
          'Speed of Light = 3x10⁸ or 300,000,000 m/s',
          'Plankc\'s Constant = 6.62607004 × 10⁻³⁴ J⋅s',
          'Avagadros Number = 6.0221409 × 10²³',
          ' ',
          '-- Other Info --',
          ' ',
          'Solid → Liquid: Melting',
          'Solid → Gas: Sublimation',
          'Liquid → Gas: Vaporization',
          'Liquid → Solid: Fusion',
          'Gas → Liquid: Condensation',
          'Gas → Solid: Deposition']




elementStats = {'H': OrderedDict([('Name:', 'Hydrogen'),
        ('Atomic Number:', 1),
        ('Group:', 1),
        ('Period:', 1),
        ('Block:', 's'),
        ('Category:', 'Reactive Nonmetal'),
        ('Atomic Mass (u):', 1.00794),
        ('Electronegativity:', 2.20),
        ('Electron Configuration:', '1s¹'),
        ('Valence Electrons:', 1),
        ('Phase at STP:', 'Gas'), 
        ('Melting Point (K):', 13.99),
        ('Boiling Point (K):', 20.271),
        ('Density at STP (g/L):', 0.08988),
        ('Triple Point (K):', 13.8033),
        ('Critical Point (K):', 32.938),
        ('Heat Capacity (J/(mol·K)):', 28.836),
        ('Oxidation States:', '-1, +1'),
        ('Covalent Radius (pm):', '31±5'),
        ('Van Der Waals Radius (pm):', 120),
        ('Crystal Structure:', 'Hexagonal'),
        ('Speed of Sound (gas, 27˚C, m/s)', 1310),
        ('Thermal Conductivity (W/(m·K))', 0.1805),
        ('Magnetic Ordering:', 'Diamagnetic')]),
    
    'He': OrderedDict([('Name:', 'Helium'),
        ('Atomic Number:', 2),
        ('Group:', 18),
        ('Period:', 1),
        ('Block:', 's'),
        ('Category:', 'Noble Gas'),
        ('Atomic Mass (u):', 4.002602),
        ('Electronegativity:', 'No Data'),
        ('Electron Configuration:', '1s²'),
        ('Valence Electrons:', 0),
        ('Phase at STP:', 'Gas'),
        ('Melting Point (K):', 0.95),
        ('Boiling Point (K):', 4.222),
        ('Density at STP (g/L):', 0.1786),
        (' → at Melting Point (g/cm³):', 0.145),
        ('Triple Point (K):', 2.117),
        ('Critical Point (K):', 5.1953),
        ('Heat Capacity (J/(mol·K)):', 20.78),
        ('Oxidation States:', '0'),
        ('Covalent Radius (pm):', '28'),
        ('Van Der Waals Radius (pm):', 140),
        ('Crystal Structure:', 'Hexagonal Close-Packed'),
        ('Thermal Conductivity (W/(m·K))', 0.1513),
        ('Magnetic Ordering:', 'Diamagnetic')]),


    'Li': OrderedDict([('Name:', 'Lithium'),
        ('Atomic Number:', 3),
        ('Group:', 1),
        ('Period:', 2),
        ('Block:', 's'),
        ('Category:', 'Alkali Metal'),
        ('Atomic Mass (u):', 6.94),
        ('Electronegativity:', 0.98), 
        ('Valence Electrons:', 1),
        ('Electron Configuration:', '[He]2s¹'),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 453.65),
        ('Boiling Point (K):', 1603),
        ('Density at RT (g/cm³):', 0.534),
        (' → at Melting Point (g/cm³):', 0.512),
        ('Critical Point (K):', 3220),
        ('Heat of Fusion (kJ/mol):', 3.00 ),
        ('Heat of Vaporization (kJ/mol):', 136),
        ('Heat Capacity (J/(mol·K)):', 24.860),
        ('Oxidation States:', '+1'),
        ('Atomic Radius (pm):', 152),
        ('Covalent Radius (pm):', '128±7'),
        ('Van Der Waals Radius (pm):', 182),
        ('Crystal Structure:', 'Body-Centric Cubic'),
        ('Thermal Expansion at 25˚C: (µm/(m·K))', 46),
        ('Thermal Conductivity (W/(m·K))', 84.8),
        ('Electrical Resistivity at 25˚C (nΩ·m)', 98.2),
        ('Magnetic Ordering:', 'Paramagnetic')]),
        
            
    'Be': OrderedDict([('Name:', 'Beryllium'),
        ('Atomic Number:', 4),
        ('Group:', 2),
        ('Period:', 2),
        ('Block:', 's'),
        ('Category:', 'Alkaline Earth Metal'),
        ('Atomic Mass (u):', 9.012),
        ('Electronegativity:', 1.57),
        ('Valence Electrons:', 2),
        ('Electron Configuration:', '[He]2s²'),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 1560),
        ('Boiling Point (K):', 2742),
        ('Density at RT (g/cm³):', 1.85),
        (' → at Melting Point (g/cm³):', 1.690),
        ('Critical Point (K):', 5205),
        ('Heat of Fusion (kJ/mol):', 12.2 ),
        ('Heat of Vaporization (kJ/mol):', 292),
        ('Heat Capacity (J/(mol·K)):', 16.443),
        ('Oxidation States:', '+2, +1'),
        ('Atomic Radius (pm):', 112),
        ('Covalent Radius (pm):', '96±3'),
        ('Van Der Waals Radius (pm):', 153),
        ('Crystal Structure:', 'Hexagonal Closed-Packed'),
        ('Thermal Expansion at 25˚C: (µm/(m·K))', 11.3),
        ('Thermal Conductivity (W/(m·K))', 200),
        ('Electrical Resistivity at 25˚C (nΩ·m)', 36),
        ('Magnetic Ordering:', 'Diamagnetic')]),

    'B': OrderedDict([('Name:', 'Boron'),
        ('Atomic Number:', 5),
        ('Group:', 13),
        ('Period:', 2),
        ('Block:', 'p'),
        ('Category:', 'Metalloid'),
        ('Atomic Mass (u):', 10.81),
        ('Electronegativity:', 2.04),
        ('Valence Electrons:', 3),
        ('Electron Configuration:', '[He]2s²2p¹'),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 2349),
        ('Boiling Point (K):', 4200),
        ('Density at Melting Point (g/cm³):', 2.08),
        ('Heat of Fusion (kJ/mol):', 50.2 ),
        ('Heat of Vaporization (kJ/mol):', 508),
        ('Heat Capacity (J/(mol·K)):', 11.087),
        ('Oxidation States:', '+3, +2, +1, -1, -5'),
        ('Atomic Radius (pm):', 90),
        ('Covalent Radius (pm):', '84±3'),
        ('Van Der Waals Radius (pm):', 192),
        ('Crystal Structure:', 'Rhombohedral'),
        ('Thermal Expansion at 25˚C: (µm/(m·K))', 6),
        ('Thermal Conductivity (W/(m·K))', 27.4),
        ('Electrical Resistivity at 20˚C (Ω·m)', '10⁶'),
        ('Magnetic Ordering:', 'Diamagnetic')]),
            
        
    'C': OrderedDict([('Name:', 'Carbon'),
        ('Atomic Number:', 6),
        ('Group:', 14),
        ('Period:', 2),
        ('Block:', 'p'),
        ('Category:', 'Reactive Nonmetal/Metalloid'),
        ('Atomic Mass (u):', 12.011),
        ('Electron Configuration:', '[He]2s²2p²'), 
        ('Valence Electrons:', 4),
        ('Phase at STP:', 'Solid'),
        ('Sublimation Point (K):', 3915),
        ('Triple Point (K):', 4600),
        ('Density at RT (g/cm³):', '1.8-2.1'),
        ('Heat of Fusion (kJ/mol):', 117),
        ('Heat of Vaporization (kJ/mol):', 508),
        ('Heat Capacity (J/(mol·K)):', '8.517 Graphite, 6.155 Diamond'),
        ('Oxidation States:', '+4, +3, +2, +1, 0, -1, -2, -3, -4'),
        ('Atomic Radius (pm):', 70),
        ('Covalent Radius (pm):', '69-77'),
        ('Van Der Waals Radius (pm):', 170),
        ('Crystal Structure:', 'Simple Hexagonal'),
        ('Thermal Expansion at 25˚C: (µm/(m·K))', 0.8),
        ('Thermal Conductivity (W/(m·K))', '119-165 Graphite, 900-2300 Diamond'),
        ('Electronegativity:', 2.55),
        ('Electrical Resistivity at 20˚C (µΩ·m)', 7.837),
        ('Magnetic Ordering:', 'Diamagnetic')]),
    

    'N': OrderedDict([('Name:', 'Nitrogen'),
        ('Atomic Number:', 7),
        ('Group:', 15),
        ('Period:', 2),
        ('Block:', 'p'),
        ('Category:', 'Reactive Nonmetal'),
        ('Atomic Mass (u):', 14.007),
        ('Electron Configuration:', '[He]2s²2p³'),
        ('Valence Electrons:', 5),
        ('Phase at STP:', 'Gas'),
        ('Melting Point (K):', 63.15),
        ('Boiling Point (K):', 77.377),
        ('Triple Point (K):', '63.151 at 12.52 kPa'),
        ('Critical Point (K):', '126.192 at 3.3958 MPa'),
        ('Density at STP (g/L):', '1.2504 at 0˚C, 1013 mbar'),
        ('Heat of Fusion (kJ/mol):', 0.72),
        ('Heat of Vaporization (kJ/mol):', 5.56),
        ('Heat Capacity (J/(mol·K)):', 29.124),
        ('Oxidation States:', '+5, +4, +3, +2, +1, -1, -2, -3'),
        ('Covalent Radius (pm):', '71±1'),
        ('Van Der Waals Radius (pm):', 155),
        ('Crystal Structure:', 'Hexagonal'),
        ('Thermal Conductivity (W/(m·K))', '25.83x10⁻³'),
        ('Electronegativity:', 3.04),
        ('Magnetic Ordering:', 'Diamagnetic')]),
    
    'O': OrderedDict([('Name:', 'Oxygen'),
        ('Atomic Number:', 8),
        ('Group:', 16),
        ('Period:', 2),
        ('Block:', 'p'),
        ('Category:', 'Reactive Nonmetal'),
        ('Atomic Mass (u):', 15.999),
        ('Electron Configuration:', '[He]2s²2p⁴'),
        ('Valence Electrons:', 6),
        ('Phase at STP:', 'Gas'),
        ('Melting Point (K):', 54.36),
        ('Boiling Point (K):', 90.188),
        ('Triple Point (K):', '54.361 at 0.1463 kPa'),
        ('Critical Point (K):', '154.581 at 5.043 MPa'),
        ('Density at STP (g/L):', 1.429),
        ('Heat of Fusion (kJ/mol):', 0.444),
        ('Heat of Vaporization (kJ/mol):', 6.82),
        ('Heat Capacity (J/(mol·K)):', 29.378),
        ('Oxidation States:', '+2, +1, -1, -2'),
        ('Covalent Radius (pm):', '66±2'),
        ('Van Der Waals Radius (pm):', 152),
        ('Crystal Structure:', 'Cubic'),
        ('Thermal Conductivity (W/(m·K))', '26.53x10⁻³'),
        ('Electronegativity:', 3.44),
        ('Magnetic Ordering:', 'Paramagnetic')]),
    
    'F': OrderedDict([('Name:', 'Fluorine'),
        ('Atomic Number:', 9),
        ('Group:', 17),
        ('Period:', 2),
        ('Block:', 'p'),
        ('Category:', 'Reactive Nonmetal'),
        ('Atomic Mass (u):', 18.998),
        ('Electron Configuration:', '[He]2s²2p⁵'),
        ('Valence Electrons:', 7),
        ('Phase at STP:', 'Gas'),
        ('Melting Point (K):', 53.48),
        ('Boiling Point (K):', 85.03),
        ('Triple Point (K):', '53.48 at 90 kPa'),
        ('Critical Point (K):', '144.41 at 5.1724 MPa'),
        ('Density at STP (g/L):', 1.696),
        ('Heat of Fusion (kJ/mol):', 0.2552),
        ('Heat of Vaporization (kJ/mol):', 6.51),
        ('Heat Capacity (J/(mol·K)):', '31 or 23 at 21.1˚C'),
        ('Oxidation States:', '-1'),
        ('Covalent Radius (pm):', 64),
        ('Van Der Waals Radius (pm):', 135),
        ('Crystal Structure:', 'Cubic'),
        ('Thermal Conductivity (W/(m·K))', 0.02591),
        ('Electronegativity:', 3.98),
        ('Magnetic Ordering:', 'Diamagnetic')]),
    
    'Ne': OrderedDict([('Name:', 'Neon'),
        ('Atomic Number:', 10),
        ('Group:', 18),
        ('Period:', 2),
        ('Block:', 'p'),
        ('Category:', 'Noble Gas'),
        ('Atomic Mass (u):', 20.1797),
        ('Electron Configuration:', '[He]2s²2p⁶'),
        ('Valence Electrons:', 0),
        ('Phase at STP:', 'Gas'),
        ('Melting Point (K):', 24.56),
        ('Boiling Point (K):', 27.104),
        ('Triple Point (K):', '24.556 at 43.37 kPa'),
        ('Critical Point (K):', '44.4918 at 2.7686 MPa'),
        ('Density at STP (g/L):', 0.9002),
        ('Heat of Fusion (kJ/mol):', 0.335),
        ('Heat of Vaporization (kJ/mol):', 1.71),
        ('Heat Capacity (J/(mol·K)):', 1.71),
        ('Oxidation States:', '0'),
        ('Covalent Radius (pm):', 58),
        ('Van Der Waals Radius (pm):', 154),
        ('Crystal Structure:', 'Face-Centered Cubic'),
        ('Thermal Conductivity (W/(m·K))', '49.1x10⁻³'),
        ('Electronegativity:', 'None'),
        ('Magnetic Ordering:', 'Diamagnetic')]),

    
    'Na': OrderedDict([('Name:', 'Sodium'),
        ('Atomic Number:', 11),
        ('Group:', 1),
        ('Period:', 3),
        ('Block:', 's'),
        ('Category:', 'Alkali Metal'),
        ('Atomic Mass (u):', 22.989),
        ('Electron Configuration:', '[Ne]3s¹'),
        ('Valence Electrons:', 1),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 370.944),
        ('Boiling Point (K):', 1156.090),
        ('Critical Point (K):', '2573 K, 35 MPa (extrapolated)'),
        ('Density at RT (g/cm³):', 0.968),
        ('Density at Melting Point (g/cm³):', 0.927),
        ('Heat of Fusion (kJ/mol):', 2.60),
        ('Heat of Vaporization (kJ/mol):', 97.42),
        ('Heat Capacity (J/(mol·K)):', 28.230),
        ('Oxidation States:', '+1, −1 (a strongly basic oxide)'),
        ('Covalent Radius (pm):', '166±9'),
        ('Van Der Waals Radius (pm):', 227),
        ('Crystal Structure:', 'Body-Centered Cubic'),
        ('Thermal Conductivity (W/(m·K))', 142),
        ('Electronegativity:', 0.93),
        ('Electrical Resistivity  (nΩ·m):', '47.7 at 20˚C' ),
        ('Magnetic Ordering:', 'Paramagnetic')]),
        
    'Mg': OrderedDict([('Name:', 'Magnesium'),
        ('Atomic Number:', 12),
        ('Group:', 2),
        ('Period:', 3),
        ('Block:', 's'),
        ('Category:', 'Alkaline Earth Metal'),
        ('Atomic Mass (u):', 24.305),
        ('Electron Configuration:', '[Ne]3s²'),
        ('Valence Electrons:', 2),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 923),
        ('Boiling Point (K):', 1363),
        ('Density at RT (g/cm³):', 1.738),
        ('Density at Melting Point (g/cm³):', 1.584),
        ('Heat of Fusion (kJ/mol):', 8.48),
        ('Heat of Vaporization (kJ/mol):', 128),
        ('Heat Capacity (J/(mol·K)):', 24.869),
        ('Oxidation States:', '+2, +1 (a strongly basic oxide)'),
        ('Covalent Radius (pm):', '141±7'),
        ('Van Der Waals Radius (pm):', 173),
        ('Crystal Structure:', 'Hexagonal Closed-Packed'),
        ('Thermal Conductivity (W/(m·K))', 156),
        ('Electronegativity:', 1.31),
        ('Electrical Resistivity  (nΩ·m):', '43.9 at 20˚C' ),
        ('Magnetic Ordering:', 'Paramagnetic')]),
        

        'Al': OrderedDict([('Name:', 'Aluminium'),
        ('Atomic Number:', 13),
        ('Group:', 13),
        ('Period:', 3),
        ('Block:', 'p'),
        ('Category:', 'Post-Transition Metal'),
        ('Atomic Mass (u):', 26.981),
        ('Electron Configuration:', '[Ne]3s²3p¹'),
        ('Valence Electrons:', 3),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 933.47),
        ('Boiling Point (K):', 2743),
        ('Density at RT (g/cm³):', 2.70),
        ('Density at Melting Point (g/cm³):', 2.375),
        ('Heat of Fusion (kJ/mol):', 10.71),
        ('Heat of Vaporization (kJ/mol):', 284),
        ('Heat Capacity (J/(mol·K)):', 24.20),
        ('Oxidation States:', '+3, +2, +1, −1, −2 (an amphoteric oxide)'),
        ('Covalent Radius (pm):', '121±4'),
        ('Atomic Radius (pm):', 143),
        ('Van Der Waals Radius (pm):', 184),
        ('Crystal Structure:', 'Face Centered-Cubic'),
        ('Thermal Conductivity (W/(m·K))', 237),
        ('Electronegativity:', 1.61),
        ('Electrical Resistivity  (nΩ·m):', '26.5 at 20˚C' ),
        ('Magnetic Ordering:', 'Paramagnetic')]),


        'Si': OrderedDict([('Name:', 'Silicon'),
        ('Atomic Number:', 14),
        ('Group:', 14),
        ('Period:', 3),
        ('Block:', 'p'),
        ('Category:', 'Metalloid'),
        ('Atomic Mass (u):', 28.085),
        ('Electron Configuration:', '[Ne]3s²3p²'),
        ('Valence Electrons:', 4),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 1687),
        ('Boiling Point (K):', 3538),
        ('Density at RT (g/cm³):', 2.3290),
        ('Density at Melting Point (g/cm³):', 2.57),
        ('Heat of Fusion (kJ/mol):', 50.21),
        ('Heat of Vaporization (kJ/mol):', 383),
        ('Heat Capacity (J/(mol·K)):', 19.789),
        ('Oxidation States:', '+4, +3, +2, +1, −1, −2, -3, -4'),
        ('Covalent Radius (pm):', 111),
        ('Atomic Radius (pm):', 111),
        ('Van Der Waals Radius (pm):', 210),
        ('Crystal Structure:', 'Face-Centered Diamond-Cubic'),
        ('Thermal Conductivity (W/(m·K))', 149),
        ('Electronegativity:', 1.90),
        ('Electrical Resistivity  (Ω·m):', '2.3 x 10⁻³ at 20˚C' ),
        ('Magnetic Ordering:', 'Diamagnetic')]),

        
        'P': OrderedDict([('Name:', 'Phosphorus'),
        ('Atomic Number:', 15),
        ('Group:', 15),
        ('Period:', 3),
        ('Block:', 'p'),
        ('Category:', 'Reactive Nonmetal'),
        ('Atomic Mass (u):', 30.973),
        ('Electron Configuration:', '[Ne]3s²3p³'),
        ('Valence Electrons:', 5),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 'White: 317.3, Red: ∼860'),
        ('Boiling Point (K):', 'white: 553.7'),
        ('Density at RT (g/cm³):', 'White: 1.823, Red: ≈2.2–2.34, Violet: 2.36, Black: 2.69'),
        ('Heat of Fusion (kJ/mol):', 0.66),
        ('Heat of Vaporization (kJ/mol):', 51.9),
        ('Heat Capacity (J/(mol·K)):', 23.824),
        ('Oxidation States:', '+5, +4, +3, +2, +1, −1, −2, -3  (a mildly acidic oxide)'),
        ('Covalent Radius (pm):', '107ٍٍ±3'),
        ('Van Der Waals Radius (pm):', 180),
        ('Crystal Structure:', 'Body-Centered Cubic'),
        ('Thermal Conductivity (W/(m·K))', 149),
        ('Electronegativity:', 2.19),
        ('Magnetic Ordering:', 'Diamagnetic')]),

        'S': OrderedDict([('Name:', 'Sulfur'),
        ('Atomic Number:', 16),
        ('Group:', 16),
        ('Period:', 3),
        ('Block:', 'p'),
        ('Category:', 'Reactive Nonmetal'),
        ('Atomic Mass (u):', 32.06),
        ('Electron Configuration:', '[Ne]3s²3p⁴'),
        ('Valence Electrons:', 6),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 388.36),
        ('Boiling Point (K):', 717.8),
        ('Density at RT (g/cm³):', 'Alpha: 2.07, Beta: 1.96, Gamma: 1.92'),
        ('Density at MP (g/cm³):', 1.819),
        ('Heat of Fusion (kJ/mol):', 1.727),
        ('Heat of Vaporization (kJ/mol):', 45),
        ('Heat Capacity (J/(mol·K)):', 22.75),
        ('Oxidation States:', '+6, +5, +4, +3, +2, +1, −1, −2,  (a strongly acidic oxide)'),
        ('Covalent Radius (pm):', '105±3'),
        ('Van Der Waals Radius (pm):', 180),
        ('Crystal Structure:', 'Orthorhombic'),
        ('Thermal Conductivity (W/(m·K))', 0.205),
        ('Electronegativity:', 2.58),
        ('Electrical Resistivity  (Ω·m):', '2 x 10¹⁵ at 20˚C' ),
        ('Magnetic Ordering:', 'Diamagnetic')]),
        


        'Cl': OrderedDict([('Name:', 'Chlorine'),
        ('Atomic Number:', 17),
        ('Group:', 17),
        ('Period:', 3),
        ('Block:', 'p'),
        ('Category:', 'Reactive Nonmetal'),
        ('Atomic Mass (u):', 35.45),
        ('Electron Configuration:', '[Ne]3s²3p⁵'),
        ('Valence Electrons:', 7),
        ('Phase at STP:', 'Gas'),
        ('Melting Point (K):', 171.6),
        ('Boiling Point (K):', 239.11),
        ('Density at STP (g/L):', 3.2),
        ('Density at BP (g/cm³):', 1.5625),
        ('Heat of Fusion (kJ/mol):', '(Cl2) 6.406'),
        ('Heat of Vaporization (kJ/mol):', '(Cl2) 20.41'),
        ('Heat Capacity (J/(mol·K)):', '(Cl2) 33.949'),
        ('Oxidation States:', '+7 ,+6, +5, +4, +3, +2, +1, −1  (a strongly acidic oxide)'),
        ('Covalent Radius (pm):', '102±4'),
        ('Van Der Waals Radius (pm):', 175),
        ('Crystal Structure:', 'Orthorhombic'),
        ('Thermal Conductivity (W/(m·K))', '8.9 x 10⁻³'),
        ('Electronegativity:', 3.16),
        ('Electrical Resistivity  (Ω·m):', '> 10 at 20˚C' ),
        ('Magnetic Ordering:', 'Diamagnetic')]),

        'Ar': OrderedDict([('Name:', 'Argon'),
        ('Atomic Number:', 18),
        ('Group:', 18),
        ('Period:', 3),
        ('Block:', 'p'),
        ('Category:', 'Noble Gas'),
        ('Atomic Mass (u):', 39.948),
        ('Electron Configuration:', '[Ne]3s²3p⁶'),
        ('Valence Electrons:', 0),
        ('Phase at STP:', 'Gas'),
        ('Melting Point (K):', 83.81),
        ('Boiling Point (K):', 87.302),
        ('Density at STP (g/L):', 1.784),
        ('Density at BP (g/cm³):', 1.3954),
        ('Heat of Fusion (kJ/mol):', 1.18),
        ('Heat of Vaporization (kJ/mol):', 6.52),
        ('Heat Capacity (J/(mol·K)):', 20.85),
        ('Oxidation States:', 0),
        ('Covalent Radius (pm):', '106±10'),
        ('Van Der Waals Radius (pm):', 188),
        ('Crystal Structure:', 'Face Centered-Cubic'),
        ('Thermal Conductivity (W/(m·K))', '17.72 x 10⁻³'),
        ('Electronegativity:', 'No Data'),
        ('Magnetic Ordering:', 'Diamagnetic')]),

        'K': OrderedDict([('Name:', 'Potassium'),
        ('Atomic Number:', 19),
        ('Group:', 1),
        ('Period:', 4),
        ('Block:', 's'),
        ('Category:', 'Alkali Metal'),
        ('Atomic Mass (u):', 39.0983),
        ('Electron Configuration:', '[Ar]4s¹'),
        ('Valence Electrons:', 1),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 336.7),
        ('Boiling Point (K):', 1032),
        ('Density at Room Temp (g/cm³):', 0.862),
        ('Density at MP (g/cm³):', 0.828),
        ('Heat of Fusion (kJ/mol):', 2.44),
        ('Heat of Vaporization (kJ/mol):', 76.9),
        ('Heat Capacity (J/(mol·K)):', 29.6),
        ('Oxidation States:', '+1, -1'),
        ('Atomic Radius (pm):', 227),
        ('Covalent Radius (pm):', '203±12'),
        ('Van Der Waals Radius (pm):', 275),
        ('Crystal Structure:', 'Body-Centered Cubic'),
        ('Thermal Conductivity (W/(m·K))', 102.5),
        ('Electrical Resistivity  (nΩ·m):', '72 at 20˚C' ),
        ('Electronegativity:', 0.82),
        ('Magnetic Ordering:', 'Paramagnetic')]),
        
        'Ca': OrderedDict([('Name:', 'Calcium'),
        ('Atomic Number:', 20),
        ('Group:', 2),
        ('Period:', 4),
        ('Block:', 's'),
        ('Category:', 'Alkaline Earth Metal'),
        ('Atomic Mass (u):', 40.078),
        ('Electron Configuration:', '[Ar]4s²'),
        ('Valence Electrons:', 2),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 1115),
        ('Boiling Point (K):', 1757),
        ('Density at Room Temp (g/cm³):', 1.55),
        ('Density at MP (g/cm³):', 1.378),
        ('Heat of Fusion (kJ/mol):', 8.54),
        ('Heat of Vaporization (kJ/mol):', 154.7),
        ('Heat Capacity (J/(mol·K)):', 25.929),
        ('Oxidation States:', '+2, +1'),
        ('Atomic Radius (pm):', 197),
        ('Covalent Radius (pm):', '176±10'),
        ('Van Der Waals Radius (pm):', 231),
        ('Crystal Structure:', 'Face-Centered Cubic'),
        ('Thermal Conductivity (W/(m·K))', 201),
        ('Electrical Resistivity  (nΩ·m):', '33.6 at 20˚C' ),
        ('Electronegativity:', 1.00),
        ('Magnetic Ordering:', 'Diamagnetic')]),
        
        'Sc': OrderedDict([('Name:', 'Scandium'),
        ('Atomic Number:', 21),
        ('Group:', 3),
        ('Period:', 4),
        ('Block:', 'd'),
        ('Category:', 'Transition Metal'),
        ('Atomic Mass (u):', 44.955),
        ('Electron Configuration:', '[Ar]4s²3d¹'),
        ('Valence Electrons:', 3),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 1814),
        ('Boiling Point (K):', 3109),
        ('Density at Room Temp (g/cm³):', 2.985),
        ('Density at MP (g/cm³):', 2.80),
        ('Heat of Fusion (kJ/mol):', 14.1),
        ('Heat of Vaporization (kJ/mol):', 332.7),
        ('Heat Capacity (J/(mol·K)):', 25.52),
        ('Oxidation States:', '+3, +2, +1'),
        ('Atomic Radius (pm):', 162),
        ('Covalent Radius (pm):', '170±7'),
        ('Van Der Waals Radius (pm):', 211),
        ('Crystal Structure:', 'Hexagonal Closed-Packed'),
        ('Thermal Conductivity (W/(m·K))', 15.8),
        ('Electrical Resistivity  (nΩ·m):', 'α, poly: 562 at RT' ),
        ('Electronegativity:', 1.36),
        ('Magnetic Ordering:', 'Paramagnetic')]),

        'Ti': OrderedDict([('Name:', 'Titanium'),
        ('Atomic Number:', 22),
        ('Group:', 4),
        ('Period:', 4),
        ('Block:', 'd'),
        ('Category:', 'Transition Metal'),
        ('Atomic Mass (u):', 47.867),
        ('Electron Configuration:', '[Ar]4s²3d²'),
        ('Valence Electrons:', 4),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 1941),
        ('Boiling Point (K):', 3560),
        ('Density at Room Temp (g/cm³):', 4.506),
        ('Density at MP (g/cm³):', 4.11),
        ('Heat of Fusion (kJ/mol):', 14.15),
        ('Heat of Vaporization (kJ/mol):', 425),
        ('Heat Capacity (J/(mol·K)):', 25.060),
        ('Oxidation States:', '-2, -1, +1, +2, +3, +4'),
        ('Atomic Radius (pm):', 147),
        ('Covalent Radius (pm):', '160±8'),
        ('Crystal Structure:', 'Hexagonal Closed-Packed'),
        ('Thermal Conductivity (W/(m·K))', 21.9),
        ('Electrical Resistivity  (nΩ·m):', '420 at 20˚C' ),
        ('Electronegativity:', 1.54),
        ('Magnetic Ordering:', 'Paramagnetic')]),
        
        'V': OrderedDict([('Name:', 'Vanadium'),
        ('Atomic Number:', 23),
        ('Group:', 5),
        ('Period:', 4),
        ('Block:', 'd'),
        ('Category:', 'Transition Metal'),
        ('Atomic Mass (u):', 50.9415),
        ('Electron Configuration:', '[Ar]4s²3d³'),
        ('Valence Electrons:', 5),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 2183),
        ('Boiling Point (K):', 3680),
        ('Density at Room Temp (g/cm³):', 6.0),
        ('Density at MP (g/cm³):', 5.5),
        ('Heat of Fusion (kJ/mol):', 21.5),
        ('Heat of Vaporization (kJ/mol):', 444),
        ('Heat Capacity (J/(mol·K)):', 24.89),
        ('Oxidation States:', '-3, -1, +1, +2, +3, +4, +5'),
        ('Atomic Radius (pm):', 134),
        ('Covalent Radius (pm):', '158±8'),
        ('Crystal Structure:', 'Body-Centered Cubic'),
        ('Thermal Conductivity (W/(m·K))', 30.7),
        ('Electrical Resistivity  (nΩ·m):', '197 at 20˚C' ),
        ('Electronegativity:', 1.63),
        ('Magnetic Ordering:', 'Paramagnetic')]),
        
        'Cr': OrderedDict([('Name:', 'Chromium'),
        ('Atomic Number:', 24),
        ('Group:', 6),
        ('Period:', 4),
        ('Block:', 'd'),
        ('Category:', 'Transition Metal'),
        ('Atomic Mass (u):', 51.9961),
        ('Electron Configuration:', '[Ar]3d⁵4s¹'),
        ('Valence Electrons:', 6),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 2180),
        ('Boiling Point (K):', 2944),
        ('Density at Room Temp (g/cm³):', 7.19),
        ('Density at MP (g/cm³):', 6.3),
        ('Heat of Fusion (kJ/mol):', 21.0),
        ('Heat of Vaporization (kJ/mol):', 347),
        ('Heat Capacity (J/(mol·K)):', 23.35),
        ('Oxidation States:', '-4, -2, -1, +1, +2, +3, +4, +5, +6'),
        ('Atomic Radius (pm):', 128),
        ('Covalent Radius (pm):', '139±5'),
        ('Crystal Structure:', 'Body-Centered Cubic'),
        ('Thermal Conductivity (W/(m·K))', 93.3),
        ('Electrical Resistivity  (nΩ·m):', '125 at 20˚C' ),
        ('Electronegativity:', 1.66),
        ('Magnetic Ordering:', 'Antiferromagnetic')]),
        
        'Mn': OrderedDict([('Name:', 'Manganese'),
        ('Atomic Number:', 25),
        ('Group:', 7),
        ('Period:', 4),
        ('Block:', 'd'),
        ('Category:', 'Transition Metal'),
        ('Atomic Mass (u):', 54.938),
        ('Electron Configuration:', '[Ar]3d⁵4s²'),
        ('Valence Electrons:', 7),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 1519),
        ('Boiling Point (K):', 2334),
        ('Density at Room Temp (g/cm³):', 7.21),
        ('Density at MP (g/cm³):', 5.95),
        ('Heat of Fusion (kJ/mol):', 12.91),
        ('Heat of Vaporization (kJ/mol):', 221),
        ('Heat Capacity (J/(mol·K)):', 26.32),
        ('Oxidation States:', '-3, -2, -1, +1, +2, +3, +4, +5, +6, +7'),
        ('Atomic Radius (pm):', 127),
        ('Covalent Radius (pm):', '139±5'),
        ('Crystal Structure:', 'Body-Centered Cubic'),
        ('Thermal Conductivity (W/(m·K))', 7.81),
        ('Electrical Resistivity  (µΩ·m):', '1.44 at 20˚C' ),
        ('Electronegativity:', 1.55),
        ('Magnetic Ordering:', 'Paramagnetic')]),
        
        'Fe': OrderedDict([('Name:', 'Iron'),
        ('Atomic Number:', 26),
        ('Group:', 8),
        ('Period:', 4),
        ('Block:', 'd'),
        ('Category:', 'Transition Metal'),
        ('Atomic Mass (u):', 55.845),
        ('Electron Configuration:', '[Ar]3d⁶4s²'),
        ('Valence Electrons:', 2),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 1811),
        ('Boiling Point (K):', 3134),
        ('Density at Room Temp (g/cm³):', 7.874),
        ('Density at MP (g/cm³):', 6.98),
        ('Heat of Fusion (kJ/mol):', 13.81),
        ('Heat of Vaporization (kJ/mol):', 340),
        ('Heat Capacity (J/(mol·K)):', 25.10),
        ('Oxidation States:', '-4, -2, -1, +1, +2, +3, +4, +5, +6, +7'),
        ('Atomic Radius (pm):', 126),
        ('Covalent Radius (pm):', '132±3'),
        ('Crystal Structure:', 'Body-Centered Cubic'),
        ('Thermal Conductivity (W/(m·K))', 80.4),
        ('Electrical Resistivity  (nΩ·m):', '96.1 at 20˚C' ),
        ('Electronegativity:', 1.83),
        ('Magnetic Ordering:', 'Ferromagnetic')]),

        'Co': OrderedDict([('Name:', 'Cobalt'),
        ('Atomic Number:', 27),
        ('Group:', 9),
        ('Period:', 4),
        ('Block:', 'd'),
        ('Category:', 'Transition Metal'),
        ('Atomic Mass (u):', 58.933),
        ('Electron Configuration:', '[Ar]3d⁷4s²'),
        ('Valence Electrons:', '2 or 9'),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 1768),
        ('Boiling Point (K):', 3200),
        ('Density at Room Temp (g/cm³):', 8.908),
        ('Density at MP (g/cm³):', 8.86),
        ('Heat of Fusion (kJ/mol):', 16.06),
        ('Heat of Vaporization (kJ/mol):', 377),
        ('Heat Capacity (J/(mol·K)):', 24.87),
        ('Oxidation States:', '-3, -1, +1, +2, +3, +4 +5'),
        ('Atomic Radius (pm):', 125),
        ('Covalent Radius (pm):', '126±3'),
        ('Crystal Structure:', 'Hexagonal Closed Packed'),
        ('Thermal Conductivity (W/(m·K))', 100),
        ('Electrical Resistivity  (nΩ·m):', '62.4 at 20˚C' ),
        ('Electronegativity:', 1.88),
        ('Magnetic Ordering:', 'Ferromagnetic')]),
        
        'Ni': OrderedDict([('Name:', 'Nickel'),
        ('Atomic Number:', 28),
        ('Group:', 10),
        ('Period:', 4),
        ('Block:', 'd'),
        ('Category:', 'Transition Metal'),
        ('Atomic Mass (u):', 58.6934),
        ('Electron Configuration:', '[Ar]3d⁸4s²'),
        ('Valence Electrons:', '2 or 10'),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 1728),
        ('Boiling Point (K):', 3003),
        ('Density at Room Temp (g/cm³):', 8.908),
        ('Density at MP (g/cm³):', 7.81),
        ('Heat of Fusion (kJ/mol):', 17.48),
        ('Heat of Vaporization (kJ/mol):', 379),
        ('Heat Capacity (J/(mol·K)):', 26.07),
        ('Oxidation States:', '-2, -1, +1, +2, +3, +4'),
        ('Atomic Radius (pm):', 124),
        ('Covalent Radius (pm):', '124±4'),
        ('Van Der Waals Radius (pm):', 163),
        ('Crystal Structure:', 'Face-Centered Cubic'),
        ('Thermal Conductivity (W/(m·K))', 90.9),
        ('Electrical Resistivity  (nΩ·m):', '69.3 at 20˚C' ),
        ('Electronegativity:', 1.91),
        ('Magnetic Ordering:', 'Ferromagnetic')]),

        'Cu': OrderedDict([('Name:', 'Copper'),
        ('Atomic Number:', 29),
        ('Group:', 11),
        ('Period:', 4),
        ('Block:', 'd'),
        ('Category:', 'Transition Metal'),
        ('Atomic Mass (u):', 63.546),
        ('Electron Configuration:', '[Ar]3d¹⁰4s¹'),
        ('Valence Electrons:', 2),
        ('Phase at STP:', 'Solid'),
        ('Melting Point (K):', 1357.77),
        ('Boiling Point (K):', 2835),
        ('Density at Room Temp (g/cm³):', 8.96),
        ('Density at MP (g/cm³):', 8.02),
        ('Heat of Fusion (kJ/mol):', 13.26),
        ('Heat of Vaporization (kJ/mol):', 300.4),
        ('Heat Capacity (J/(mol·K)):', 24.440),
        ('Oxidation States:', '-2, +1, +2, +3, +4'),
        ('Atomic Radius (pm):', 128),
        ('Covalent Radius (pm):', '132±4'),
        ('Van Der Waals Radius (pm):', 140),
        ('Crystal Structure:', 'Face-Centered Cubic'),
        ('Thermal Conductivity (W/(m·K))', 401),
        ('Electrical Resistivity  (nΩ·m):', '16.78 at 20˚C' ),
        ('Electronegativity:', 1.90),
        ('Magnetic Ordering:', 'Diamagnetic')]),

        }
