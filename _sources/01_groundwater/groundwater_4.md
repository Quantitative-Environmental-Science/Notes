<br><div style="page-break-before:always;"></div>

(groundwater_4)=
# Groundwater Chemistry

A key point from the groundwater lectures is the connection between groundwater
and surface water.
In the lecture we showed data for a hydrograph – that is the level of water in
a river – alongside the underlying {term}`water table`.
The two rise and fall together, with a small delay, because both respond to the
same rainfall and because groundwater discharging into the river (baseflow)
sustains river flow between storms.

We have discussed the importance of groundwater systems, how groundwater moves (and why it can move uphill), and how we can test for and figure out the key aspects that influence groundwater flow, which includes pumping tests.
Together these give us a good sense of how to calculate groundwater velocity and the energy required to move groundwater.
There are several environmental challenges that face Earth’s groundwater systems, not least of which is the fact that we are removing groundwater faster than it can {term}`recharge`.

```{note}
To explore the contamination of groundwater we are going to tell the story of arsenic poisoning in Nepal, why there are such high levels of arsenic in the groundwater and the various mechanisms that can help remedy this situation.
This is just a specific example of an acute groundwater contamination problem and the way the community and scientists are trying to help remedy it.
The details of this case study will be in the lecture slides.
```

## How does Groundwater Chemistry Evolve?

To explore this, we consider the case of arsenic poisoning in groundwater wells
in Nepal.
Nepal's steep topography forces monsoon air upwards (orographic lift), so
rainfall is very high on the southern slopes, while the rain shadow north of
the high Himalaya is very dry.
Annual rainfall varies by more than an order of magnitude across the country.
In Nepal, groundwater supplies around 50% of the drinking water for the capital,
Kathmandu, and 90% of the drinking water for the bulk of the population in the
flood plains (Terai).
Only 34% of the population has access to clean drinking water.

```{figure} ./figures/figure8.1.png
---
name: arsenic_nepal
figclass: margin-caption
---
Arsenic distribution in groundwater in Nepal Terai districts,
showing the widespread contamination of shallow groundwater wells.
```

We can consider what happens to the chemistry of groundwater along the flow path
to understand the chemistry of the drinking water in the flood plains
({numref}`flow_path_evolution`).

```{figure} ./figures/figure8.2.png
---
name: flow_path_evolution
figclass: margin-caption
---
Schematic showing how groundwater chemistry evolves along the flow path
from recharge to discharge zones.
```

## Chemical Evolution Along the Flow Path

How does the chemistry of groundwater change over distance?

1. **Precipitation and Atmospheric Equilibration**

   Rain is the major source of water to groundwater systems.
   Rain is in equilibrium with CO<sub>2</sub> in the atmosphere,
   and is slightly acidic (pH ≈ 5.6).

2. **Infiltration and Vadose Zone Processes**

   During {term}`infiltration`, water passes through the soil, where root and
   microbial respiration raise CO<sub>2</sub> to many times atmospheric levels.
   This CO<sub>2</sub> dissolves to form carbonic acid which, together with
   organic acids from decaying organic matter, attacks soil minerals.
   Evapotranspiration removes water but leaves solutes behind, concentrating
   them.
   The water that infiltrates through the vadose zone is therefore slightly
   acidic and with a higher concentration of ions and dissolved organic matter
   (DOM).

   ```{figure} ./figures/figure8.3.png
   ---
   name: vadose_zone_plant
   figclass: margin-caption
   width: 70%
   ---
   Schematic of the vadose zone showing plant roots, soil layers,
   and the processes affecting infiltrating water.
   ```

   ```{figure} ./figures/figure8.4.jpg
   ---
   name: vadose_geochemistry
   figclass: margin-caption
   width: 70%
   ---
   Geochemical processes in the vadose zone, including organic matter leaching,
   ion exchange, and mineral weathering.
   ```

3. **Mineral Dissolution**

   Along the groundwater flow path there is further dissolution of minerals
   which contribute ions to the groundwater.
   Ionic strength therefore increases along the flow path.
   Typical ions that are picked up are shown in {numref}`groundwater_ions`.

   ```{figure} ./figures/figure8.5.png
   ---
   name: groundwater_ions
   figclass: margin-caption
   width: 60%
   ---
   Common ions found in groundwater, including major cations (Ca<sup>2+</sup>,
   Mg<sup>2+</sup>, Na<sup>+</sup>, K<sup>+</sup>) and anions
   (HCO<sub>3</sub><sup>-</sup>, SO<sub>4</sub><sup>2-</sup>, Cl<sup>-</sup>).
   ```

   Key to this is an understanding of saturation state and where minerals are
   undersaturated or oversaturated with respect to the fluids in the groundwater
   system.
   We express this using a solubility product for a mineral or salt.

4. **Secondary Mineral Precipitation**

   The precipitation of secondary minerals can occur as groundwater becomes
   supersaturated as it ages and changes its chemical composition.

   The longer the flow path, the more altered the chemistry of the fluid will be.
   In the deepest flow paths you can get exceptionally saline waters that form
   from dissolution of salt ({numref}`tds_depth`).

   ```{figure} ./figures/figure8.6.jpg
   ---
   name: tds_depth
   figclass: margin-caption
   width: 70%
   ---
   Schematic summary of the distribution of Total Dissolved Solids (TDS) with
   depth in groundwater, showing increasing salinity with depth and residence
   time.
   ```

5. **Development of Anoxic Conditions**

   The longer groundwater is out of contact with the atmosphere,
   the more likely it is to become anoxic – and lose its oxygen.
   Remember that redox reactions are the ones that involve the exchange of
   electrons.
   In the subsurface there are many things that use up oxygen (respiration,
   reaction with minerals) but there is no way to make new oxygen.

This evolving chemistry becomes a real problem for arsenic.
In floodplain sediments, arsenic is mostly held sorbed onto iron(III) oxyhydroxide coatings on sediment grains.
Once groundwater becomes anoxic, microbes use these Fe(III) oxides as an electron acceptor to oxidise organic matter, dissolving them and releasing the sorbed arsenic (**reductive dissolution**).
Under these reducing conditions arsenic is also present as arsenite (As(III)), which sorbs less strongly than arsenate (As(V)) and so is more mobile.
The organic carbon that drives this reduction may be natural (buried peat and sedimentary organic matter) or anthropogenic (e.g. ponds, latrines, or surface water drawn down by irrigation pumping); the relative importance of these sources is still debated.

## Anoxia, Redox and Arsenic

We can remember why groundwater becomes anoxic if we consider the electrode potential associated with redox half reactions.  The electrode potential measures the voltage associated with the movement of electrons relative to a reference cell. Once you know the potential, you can calculate the total electrode potential ($\Delta E$) by coupling two redox reactions – one that gives up electrons and one that accepts electrons, as shown in {numref}`redox_ladder`.

```{figure} ./figures/redox_ladder_E_to_deltaG.png
---
name: redox_ladder
figclass: margin-caption
width: 100%
---
The redox ladder showing the relationship between the standard reduction
potential (E°) and the Gibbs free energy change (ΔG°) for key
redox reactions.
```

Electrode potential is related to the overall energy of the redox reaction through

```{math}
\Delta G = -n F \Delta E
```

Where $n$ is the number of moles of electrons transferred in the redox reaction. Remember that the more negative the $\Delta G$, the more energy released by that overall reaction. If you know the conditions you can use the Nernst Equation to calculate the true, in situ $\Delta G$ for a particular reaction.

What we can see is that the most energy is gained by reactions that use oxygen as the electron acceptor. Therefore, provided reactions are not kinetically limited, microbes will use oxygen first. This means in groundwater systems, where there are many electron donors (dissolved organic matter, reduced minerals such as pyrite), oxygen is depleted first, followed in turn by nitrate, Mn(IV), Fe(III), sulfate and finally CO<sub>2</sub> as we work down the redox ladder.

We can visualise the change in the chemistry of groundwater using a Pourbaix diagram ({numref}`pH_pe_As`), which shows the acid-base chemistry (pH) against the electron chemistry (pe) to determine which species are stable. As groundwater chemistry evolves you move gradually down on this diagram towards more reducing conditions, and whether you move left or right (more acidic or basic) depends on the minerals that might be dissolving or forming along the flow path.

```{figure} ./figures/pH_pe_As.png
---
name: pH_pe_As
figclass: margin-caption
width: 100%
---
A Pourbaix diagram showing the stability of arsenic species as a function of pH and pe (electron activity). The diagram illustrates how arsenic speciation changes under different redox and pH conditions.
```
