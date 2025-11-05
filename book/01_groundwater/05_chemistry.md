(groundwater:chemistry)=
# Groundwater Chemistry

```{tip} Key Concepts
- Chemical evolution of groundwater
- Mineral dissolution and precipitation
- Redox conditions in groundwater
- Contaminant transport mechanisms
```

A key point from the groundwater lectures is the connection between groundwater
and surface water - that groundwater levels reflect changes in surface water.
In the lecture we showed data for a hydrograph - that is the level of water in
a river - and the underlying {term}`water table`.
There is a small delay, but the {term}`water table` follows changes in the flow
of the local river.

## How does Groundwater Chemistry Evolve?

To explore this, we consider the case of arsenic poisoning in groundwater wells
in Nepal.
There is tremendous elevation change in Nepal, and this leads to temperature
gradients from the high Himalaya to the low plains, which in turn leads to
nearly an order-of-magnitude difference in annual rainfall.
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
   and is slightly acidic (pH ~5.5-6.5).

2. **Infiltration and Vadose Zone Processes**

   During {term}`infiltration`, chemical reactions occur with soil minerals due
   to leaching of organic carbon, and there is evapotranspiration which leads to
   concentration of ions.
   The water that infiltrates through the vadose zone is therefore slightly
   acidic and with a higher concentration of ions and dissolved organic matter
   (DOM).

   ```{figure} ./figures/figure8.3.png
   ---
   name: vadose_zone_plant
   figclass: margin-caption
   ---
   Schematic of the vadose zone showing plant roots, soil layers,
   and the processes affecting infiltrating water.
   ```

   ```{figure} ./figures/figure8.4.jpg
   ---
   name: vadose_geochemistry
   figclass: margin-caption
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
   ---
   Schematic summary of the distribution of Total Dissolved Solids (TDS) with
   depth in groundwater, showing increasing salinity with depth and residence
   time.
   ```

5. **Development of Anoxic Conditions**

   The longer groundwater is out of contact with the atmosphere,
   the more likely it is to become anoxic - and lose its oxygen.
   Remember that redox reactions are the ones that involve the exchange of
   electrons.
   In the subsurface there are many things that use up oxygen (respiration,
   reaction with minerals) but there is no way to make new oxygen.

This evolving chemistry becomes a real problem for arsenic.
Arsenic-bearing minerals are easily weathered (chemically dissolved) in anoxic
conditions, and in particular when there is a lot of dissolved organic matter
which binds to the arsenate ions.
Increased human waste at the surface is increasing the flux of organic matter
into the subsurface and creating increasingly anoxic conditions that are
accelerating the weathering of arsenic.

## Contaminant Transport in Groundwater

Having understood a bit about how the chemistry of groundwater evolves along the
flow path, we can consider what happens when we add a contaminant to groundwater
and how it is likely to travel and disperse through the groundwater system.

```{figure} ./figures/figure8.7.png
---
name: control_volume_transport
figclass: margin-caption
---
A control volume in groundwater showing solute transport by advection and
dispersion, with possible chemical reactions within the box.
```

If we consider a control volume in the groundwater where we have flow of a
contaminant (or molecule or element - here we will call it a 'solute', meaning
a component dissolved in groundwater) through that volume, we can apply mass
conservation to this box.
Solute can move into the box or out of the box, and chemical reactions can
create or destroy solute within the box (e.g. mineral dissolution or
precipitation).
This allows us to consider the net rate of change of the concentration of the
solute within the box.

So how does the solute, or contaminant, move through the control volume?

It moves by advection, and by dispersion.

### Advection

**Advection** causes the wholesale movement of the solute with the flow field at
the same velocity as the flow field.
So if we have a solute (like a contaminant) in groundwater, and the groundwater
is moving at a velocity of 5 meters per year, then if we return one year later,
we expect the contaminant to have moved 5 meters away.

```{figure} ./figures/figure8.8.png
---
name: advection_diagram
figclass: margin-caption
width: 50%
---
The effect of advection on contaminant movement over time from t0 to t2,
showing the displacement of the solute plume with the groundwater flow.
```

{numref}`advection_diagram` shows the effect of advection on the movement of a
contaminant over time from t0 to t2.

In reality what we find is that over this time we often get more than just the
movement of the contaminant in the flow field but also the spreading out of the
concentration.
This is the effect of diffusion and hydrodynamic dispersion.

### Dispersion

```{figure} ./figures/figure8.9.png
---
name: dispersion_diagram
figclass: margin-caption
width: 60%
---
Illustration of dispersion processes showing how a contaminant plume spreads
due to molecular diffusion and mechanical dispersion.
```

**Dispersion** comprises molecular diffusion and hydrodynamic or mechanical
dispersion.

- **Molecular Diffusion** describes the spread of particles through **random**
  motion from regions of higher concentration to regions of lower concentration.
  It is governed by Fick's First law, where the overall flux due to molecular
  diffusion is given by a diffusion coefficient (determined in the lab) and the
  concentration gradient:

  ```{math}
  :label: eq:ficks_law
  J = -D \pdv{C}{x}
  ```

  where $J$ is the diffusive flux, $D$ is the diffusion coefficient,
  and $\pdv{C}{x}$ is the concentration gradient.

- **Mechanical Dispersion** reflects the fact that not everything in the porous
  medium travels at the average water flow speed.
  Some paths are faster, some slower, some longer, some shorter.
  This results in a net spreading of the solute plume that looks very much like
  a diffusive behavior.

  ```{figure} ./figures/figure8.10.jpg
  ---
  name: mechanical_dispersion
  figclass: margin-caption
  ---
  Modelling of the mechanical dispersion in porous media,
  showing variations in flow paths through the pore structure.
  ```

  Since mechanical dispersion depends on the flow, it is expected to increase
  with increasing flow speed.
  The most common expression for mechanical dispersion is given by:

  ```{math}
  :label: eq:mechanical_dispersion
  D = \alpha v
  ```

  where $D$ is the mechanical dispersion coefficient, $\alpha$ is the dynamic
  dispersivity, and $v$ is the average linear velocity.

**Note that given the very slow rate of molecular diffusion, advection and
hydrodynamic dispersion tend to dominate contaminant transport in groundwater.**

```{figure} ./figures/figure8.11.png
---
name: transport_processes
figclass: margin-caption
---
Summary diagram showing the combined effects of advection, dispersion,
and chemical reactions on contaminant transport in groundwater.
```

### Chemical Reactions

- When solutes flow through a porous medium they can interact with the solid
  phase.
  In particular they can sorb and desorb, or precipitate into mineral phases.
  The net result is a process called retardation that effectively slows the
  transport of a solute through a porous medium.

- The amount of these chemical reactions and how they impact the overall
  chemical transport depends on the solute, water chemistry, and geochemical
  makeup of the porous medium.

### The Advection-Diffusion-Reaction Equation

Having discussed advection, dispersion, and chemical reactions individually,
we can now consider how they combine in a mathematical framework.
In previous lectures, we learned the tools needed to determine how long before a
contaminant released into the groundwater would be seen at some point downstream.
We could figure out the lines of equipotential and the {term}`hydraulic
conductivity`, and then calculate the flow velocity, which would yield time
(with some knowledge of the distance travelled).

However, like most things, it is more complicated than this.
The contaminant is not just subject to advection with the flow of the
groundwater, but also diffusion (the process by which things move from high
concentration to low concentration) and possibly chemical reaction with the
porous media.
This leads to an entirely different class of equations and models known as
advective-diffusive transport models.
We will not go through the mathematics of these models in detail, but the
standard formula is:

```{margin} Units!
:class: units
$$
C &= \mathrm{amount~m^{-3}} \\
D &= \mathrm{m^2~s^{-1}} \\
v &= \mathrm{m~s^{-1}} \\
R &= \mathrm{amount~m^{-3}~s^{-1}}
$$
```

```{math}
:label: eq:advection_diffusion_reaction
D \frac{\partial^2 C}{\partial x^2} - v \frac{\partial C}{\partial x} = R \left( \frac{\partial C}{\partial t} \right)
```

Where $C$ is the contaminant concentration, and we are interested in how its
concentration changes with time $\left( \frac{\partial C}{\partial t} \right)$
and with distance $\left( \frac{\partial C}{\partial x} \right)$.
Because there are changes with time and with distance, we need to use a partial
differential equation.
In the partial differential equation above, $D$ is the diffusion coefficient for
the contaminant in water, $v$ is the flow velocity
$\left( \frac{-K}{\rho} \dv{h}{x} \right)$ (can you figure out why this is the
flow velocity from Darcy's Law?), and $R$ represents the chemical reactions that
change the concentration with time.
Diffusion can be molecular diffusion or mechanical dispersion, and the types of
chemical reactions that change the concentration vary depending on the
contaminant and the geochemical environment.
