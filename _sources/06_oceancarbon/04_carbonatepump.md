(carbon:calcification)=
# The Carbonate Pump

```{highlights}
Key Points:
- Many plankton species make shells or skeletons from calcium carbonate (CaCO<sub>3</sub>).
- The process of **calcification** takes up CO<sub>3</sub><sup>2-</sup> from the surface ocean and exports it to the deep.
- Export of CO<sub>3</sub><sup>2-</sup> reduces TA and DIC in a 2:1 ratio in the surface, and increases them in the deep, in a process known as the **carbonate pump**.
- Calcification lowers ocean pH, shifting carbon speciation and causing the release of CO<sub>2</sub> to the atmosphere.
```

## Calcification

Many groups of marine organisms make shells or skeletons from calcium carbonate (CaCO<sub>3</sub>).
You are probably familiar with bivavles and gastropods that produce the shells you find on the sea shore, and corals that produce massive reef structures found in tropical coastal environments.
Some examples you may not have encountered are the planktonic organisms found throughout the surface ocean that produce microscopic CaCO<sub>3</sub> structures.
Three groups of marine plankton are responsible the majority of calcification in the open ocean ({numref}`fig:carbon:calcifiers`):

- **Coccolithophores** are small (3-50 μm) phytoplankton that produce intricate calcium carbonate plates called coccoliths. Coccolithophores are a major calcifyer in the open ocean, demonstrated by the fact that coccoliths are the main constituent of massive chalk deposits found in uplifted marine sediments (e.g. the White Cliffs of Dover). The exact purpose of these coccoliths is unclear, although hypotheses include buoyancy control, protection from grazing and light scattering.
- **Foraminifera** are slightly larger (50-500 μm) unicellular zooplankton which produce calcium carbonate shells called tests. These tests have a distinctive multi-chambered structure, which grows gradually throughout the organism's life cycle. Some species, like the one pictured below, also create long mineralised spines that are home to symbiotic algae.
- **Pteropods** are larger-still (0.5-10 mm) multicellular zooplankton who's name literally translates to 'wing foot'. Pteropods are gastropods, which (mostly) produce a recognisable calcium carbonate 'snail shell' structure, with the soft parts of the body adapted into 'wing' that allow them some limited movement through the water.

```{figure} figures/carbon-calcifiers.png
---
name: fig:carbon:calcifiers
figclass: margin-caption
width: 100%
---
The three main open-ocean calcifiers. An SEM micrograph of the coccolithophore *Emiliania huleyi*, and light micrographs of the planktic foraminifera *Orbulina universa* and a Pteropod. Images from wikimedia commons ([coccolithophore](https://commons.wikimedia.org/wiki/File:Emiliania_huxleyi.jpg), [pteropod](https://commons.wikimedia.org/wiki/File:Fis01026_(27555118153).jpg)) and Oscar Branson.
```

The shells of these organisms are formed from one of two 'polymorphs' of CaCO<sub>3</sub> that are stable at Earth surface conditions: calcite and aragonite.
Coccolithophores and foraminifera produce calcite, while pteropods produce aragonite.

The formation of these shells is actively controlled by the organism, and involves taking up dissolved Ca<sup>2+</sup> and CO<sub>3</sub><sup>2-</sup> ions from the surrounding water, and using them to build the a mineral structure.
This process is known as **calcification**, and can be written as:

```{math}
:label: eq:carbon:calcification
\mathrm{Ca^{2+} + CO_{3}^{2-} \xrightarrow{calcification} CaCO_{3}}
```

(carbon:calcification:co2)=
### Calcification and CO<sub>2</sub>

Removing CO<sub>3</sub><sup>2-</sup> from the water and trapping it in mineral form both directly removes DIC from surface water, and alters the speciation of the remaining DIC in the surface ocean, causing CO<sub>2</sub> to be released to the atmosphere, further reducing surface DIC.

Just like organic matter in {ref}`carbon:biopump`, the CO<sub>3</sub><sup>2-</sup> trapped in shells is exported from the surface ocean as shell-bearing organisms die and sink.
The uptake and export of CO<sub>3</sub><sup>2-</sup> directly removes DIC from the surface ocean.

We also saw when considering {ref}`carbon:solubility` that the DIC species exist in an equilibrium with each other and pH.
Removing CO<sub>3</sub><sup>2-</sup> causes this speciation adjust, reducing pH because a HCO<sub>3</sub><sup>-</sup> dissociates to replace it, releasing H<sup>+</sup> into the solution.
We can re-draw DIC speciation diagram ({numref}`fig:carbon:bjerrum`) to see how the abundance of CO<sub>3</sub><sup>2-</sup> relates to the concentration of the other species ({numref}`fig:carbon:bjerrum-co3`):

```{figure} figures/carbon-bjerrum-CO3.png
---
name: fig:carbon:bjerrum-co3
figclass: margin-caption
width: 70%
---
Change in DIC speciation as a function of CO<sub>3</sub><sup>2-</sup> concentration. This equilbrium is calculated at constant DIC concentration - there is no gas exchange with the atmosphere. If gas exchange were allowed to happen CO<sub>2</sub> would be released to the atmosphere as CO<sub>3</sub><sup>2-</sup> is removed from the surface ocean. This is shown in {numref}`fig:carbon:calc-co2-release`.
```

Removing CO<sub>3</sub><sup>2-</sup> from the water causes the fraction of DIC that exists as CO<sub>2</sub> to increase (the equilibrium shifts to the left in {numref}`fig:carbon:bjerrum-co3`), causing CO<sub>2</sub> to be released to the atmosphere.
Calcification therefore removes more DIC that we would predict based solely on the uptake of CO<sub>3</sub><sup>2-</sup> from the surface ocean, because its effect on DIC speciation make it a *source* of CO<sub>2</sub> to the atmosphere ({numref}`fig:carbon:calc-co2-release`).

```{figure} figures/carbon-calc-co2-release.png
---
name: fig:carbon:calc-co2-release
figclass: margin-caption
width: 70%
---
The change in pH and DIC caused by the removal of CO<sub>3</sub><sup>2-</sup> from the surface ocean by calcification when it is equilibrating with an atmosphere at 400 ppm pCO<sub>2</sub>. We can see that DIC is reduced directly by the removal of CO<sub>3</sub><sup>2-</sup>, and indirectly by the resulting shift in DIC speciation ({numref}`fig:carbon:bjerrum-co3`), causing CO<sub>2</sub> to be released to the atmosphere.
```

The mechanism of exporting of CO<sub>3</sub><sup>2-</sup> from the surface ocean via the formation and sinking of CaCO<sub>3</sub> structures is intuitive, but how is CO<sub>3</sub><sup>2-</sup> released back into the deep ocean?
The bacterial breakdown that applies to organic matter doesn't apply here, because there is no energetic or nutritional benefit for the microbes to actively break down CaCO<sub>3</sub>.
To consider the remineralisation of CaCO<sub>3</sub>, we must briefly consider mineral solubility and saturation states.

### Saturation State

Just like the DIC speciation equations that drive {ref}`carbon:solubility` {eq}`eq:carbon:Ks`, the calcification reaction {eq}`eq:carbon:calcification` has an equilibrium point that is defined by the thermodynamic properties of the reactants and product, and is described by an equilibrium solubility product ($K_{sp}$) for the mineral phase:

```{math}
K_{sp} = (\mathrm{[Ca^{2+}][CO_{3}^{2-}]})_{eq}
```

Which is the concentration of Ca<sup>2+</sup> and CO<sub>3</sub><sup>2-</sup> at which the mineral is in equilibrium with the surrounding water, and will neither grow nor dissolve.
Note that, just like $K_1$ and $K_2$, $K_{sp}$ varies with temperature, salinity and pressure.
From this, we can define the **saturation state** of seawater with respect to CaCO<sub>3</sub>:

```{math}
\Omega = \frac{[Ca^{2+}][CO_{3}^{2-}]}{K_{sp}}
```

Values of $\Omega > 1$ will favour the formation of CaCO<sub>3</sub>, while values of $\Omega < 1$ will favour dissolution.

Ca is relatively abundant and constant in seawater (~10.2 mmol kg<sup>-1</sup>) compared to CO<sub>3</sub><sup>2-</sup> (0.1-0.3 mmol kg<sup>-1</sup> at normal ocean surface conditions).
This means that the formation and dissolution of CaCO<sub>3</sub> is predominantly controlled by the concentration of CO<sub>3</sub><sup>2-</sup> in the water.

The majority of the modern surface ocean is **saturated** (i.e. $\Omega > 1$) with respect to CaCO<sub>3</sub>, and so calcification is favoured.
For CaCO<sub>3</sub> to dissolve in the deep ocean, the deep ocean must be **undersaturated** (i.e. $\Omega < 1$) with respect to CaCO<sub>3</sub>.

### CaCO<sub>3</sub> Dissolution

The dissolution of CaCO<sub>3</sub> is driven by a combination of changes in **pressure** and the impact of the **biological pump**.

#### Pressure

The CaCO<sub>3</sub> minerals become more soluble at higher pressure; $K_{sp}$ increases with depth.
The two polymorphs of CaCO<sub>3</sub>, calcite and aragonite, also have different $K_{sp}$ values - calcite is more stable than aragonite, so has a lower $K_{sp}$.
The speciation of DIC is also sensitive to pressure, which causes [CO<sub>3</sub><sup>2-</sup>] to decrease with depth.
In combination, this means that as a CaCO<sub>3</sub> particle sinks through the ocean it will become less stable as pressure increases, while [CO<sub>3</sub><sup>2-</sup>] in the surrounding water simultaneously decreases.
This causes the mineral to dissolve when it sinks below the depth at which [CO<sub>3</sub><sup>2-</sup>] is lower than $\frac{K_{sp}}{[Ca^{2+}]}$ ({numref}`fig:carbon:co3-sat`).
Thus, changes in pressure alone are sufficient to dissolve a large fraction of the CaCO<sub>3</sub> in the deep ocean.

```{figure} figures/carbon-CO3-sat.png
---
name: fig:carbon:co3-sat
figclass: margin-caption
width: 70%
---
The concentration of CO<sub>3</sub><sup>2-</sup> in seawater at which the CaCO<sub>3</sub> minerals calcite and aragonite are in equilibrium with seawater across a range of water depths. The shaded regions are supersaturated with respect to each mineral. The horizontal dashed line shows the [CO<sub>3</sub><sup>2-</sup>] for typical deep ocean water. The equilibrium [CO<sub>3</sub><sup>2-</sup>] for each mineral both increase with depth, while [CO<sub>3</sub><sup>2-</sup>] decreases with depth. The mineral will begin to dissolve below where the dashed line intersects with the solid lines. Calculated at 4 °C and salinity of 35.
```

#### Biological Pump

The effects of pressure on solubility and speciation then combine with the biological pump to make CaCO<sub>3</sub> dissolution occur at shallower depths than would be expected from pressure alone.
The uptake of CO<sub>2</sub> by photosynthesis in surface waters raises pH and [CO<sub>3</sub><sup>2-</sup>], and the release of CO<sub>2</sub> by remineralisation in the deep ocean causes pH and [CO<sub>3</sub><sup>2-</sup>] to decrease.
In combination with the pressure effects on CaCO<sub>3</sub> solubility, this causes CaCO<sub>3</sub> dissolution to occur at shallower depths ({numref}`fig:carbon:co3-sat-real`)}).

```{figure} figures/carbon-CO3-sat-real.png
---
name: fig:carbon:co3-sat-real
figclass: margin-caption
width: 70%
---
Similar to {numref}`fig:carbon:co3-sat`, but showing a real [CO<sub>3</sub><sup>2-</sup>] profile for the Southern Atlantic. The action of the biological pump causes [CO<sub>3</sub><sup>2-</sup>] to be elevated in surface waters, where CO<sub>2</sub> is being removed by photosynthesis, and elevated at depth, where CO<sub>2</sub> is being released by remineralistion.
```

(carbon:calcification:aggregates)=
### Aggregates and Local Environments

Another layer of complexity when considering CaCO<sub>3</sub> is the effect of particle aggregates.
Most material leaving the surface ocean is in the form of aggregates - collections of smaller particles that clump together to form larger particles.
The respiration of bacteria in these aggregates can drive very high local CO<sub>2</sub> concentrations, dramatically reducing pH and CO<sub>3</sub><sup>2-</sup> and creating a highly locally undersaturated environment.
This effectively 'concentrates' the impact of the biological pump in a way that you would not pick up from bulk water chemistry measurements.
A lot of CaCO<sub>3</sub> dissolution occurs within these local environments, which can cause a substantial fraction of CaCO<sub>3</sub> to dissolve much shallower than predicted by pressure and bulk water chemistry alone.

## The Carbonate Pump

The export of CaCO<sub>3</sub> from the surface ocean to the deep ocean is known as the **carbonate pump**.
The impact of the carbonate pump on carbon concentration and speciation considered {ref}`above <carbon:calcification:co2>` can also be described in terms of DIC and TA, which describe the concentration and speciation of carbon in the water.
The carbonate pump acts to move TA and DIC from the surface to the deep ocean in a 2:1 ratio.
This follows from our definitions of DIC and TA:

```{math}
:label: eq:carbon:carbonate-pump-dic-ta
\mathrm{DIC} &= {\color{red}\mathrm{[CO_3^{2-}]}} + \mathrm{[HCO_3^-]} + \mathrm{[CO_2^*]} \\
\mathrm{TA} &= {\color{red}\mathrm{2[CO_3^{2-}]}} + \mathrm{[HCO_3^-]} + [\dots] - \mathrm{[H^+]} \\
```

Because calcification and dissolution affect TA and DIC in different amounts, it will alter both the concentration and speciation of DIC in the water ({numref}`fig:carbon:DIC-TA`).

The carbonate pump is inextricably connected to the biological pump, because CaCO<sub>3</sub> production is driven by biological productivity.
This means that the carbonate pump also depends on the supply of nutrients to the surface ocean, which fuels biological productivity.
However, this connection is not one-way: the carbonate pump can also affect the efficiency of the biological pump by altering the density of sinking particles.

### Ballasting
We saw in {ref}`carbon:biopump` that the proportion of primary production that is exported to the deep ocean depends to a large extent on particle sinking speed, which is a function of particle density.
Seawater has a density of ~1025 kg m<sup>-3</sup>, organic matter has a typical density of ~1030-1500 kg m<sup>-3</sup>.
Calcite has a density of 2710 kg m<sup>-3</sup>.
The inclusion of CaCO<sub>3</sub> in particle aggregates will therefore act to increase their density, allowing them to sink faster and increasing the proportion of primary production that is exported to the deep ocean.
This means that, even thought calcification is an immediate source of CO<sub>2</sub> to the atmosphere, increasing the efficiency of the biological may offset this effect and make calcification a net (indirect) sink for CO<sub>2</sub>.
This feedback is known as **ballasting**, and the amount of dense CaCO<sub>3</sub> relative to organic matter in sinking particles is a critical parameter in determining the efficiency of the biological pump.

(carbon:calcification:ocean-acidification)=
### Ocean Acidification

In {ref}`carbon:solubility` we saw that pCO<sub>2</sub> and pH are inversely related, and that elevating atmospheric pCO<sub>2</sub> will cause the surface ocean to become more acidic.
This would reduce [CO<sub>3</sub><sup>2-</sup>], and therefore the saturation state (Ω) of the surface ocean ({numref}`fig:carbon:pco2-ph-omega`).
Reducing the saturation state has the potential to reduce CaCO<sub>3</sub> production, by marine organisms, and enhance CaCO<sub>3</sub> dissolution at shallow depths, thus reducing the strength of the carbonate pump.

```{figure} figures/carbon-pCO2-pH.png
---
name: fig:carbon:pco2-ph-omega
figclass: margin-caption
width: 70%
---
The impact of ocean acidification on surface ocean $\Omega$ at 0 and 30 °C. Because of the influence of temperature on solubility and DIC speciation, the high latitudes are much more affected by ocean acidification than the tropics. The polar waters may become undersaturated with respect to aragonite as soon as ~2050.
```

In the immediate term, this could act as a negative feedback on atmospheric pCO<sub>2</sub>, because reductions in calcification will reduce the rate of associated CO<sub>2</sub> release from the surface ocean.
However, when the effect of CaCO<sub>3</sub> production on ballasting the biological pump is considered, it is less clear whether impact of ocean acidification on the carbonate pump will have a net postitive or negative effect on atmospheric pCO<sub>2</sub>.
The interaction between ballasting and ocean acidification is a significant source of uncertainty in our predictions of the uptake of CO<sub>2</sub> by the ocean in future.

## Modelling the Carbonate Pump

Calcification is biologically-mediated, and takes up CO<sub>3</sub><sup>-2</sup> from the surface ocean and exports it to the deep.
We will therefore model calcification as a function of biological productivity in the surface ocean, assuming that some fraction of biological carbon export ($f_{calc}$) is accompanied by calcification:

```{math}
f_{calc} = \frac{CO_{3,calc}^{2-}}{DIC_{org}}
```

The amount of CO<sub>3</sub><sup>2-</sup> exported from a surface box is therefore given by:

```{math}
\dv{CO_{3,i}^{2-}}{t} = f_{calc,i} \underbrace{106 \frac{V_i}{\tau^P_i} P_i}_{biological~C~export}
```

From our definitions of TA and DIC {eq}`eq:carbon:carbonate-pump-dic-ta`, this modifies TA and DIC in our model in a 2:1 ratio.
We therefore model the impact of calcification on DIC as:

```{math}
:label: eq:3box:dic:calc
\dv{DIC_L}{t} &= \begin{bmatrix} \mathrm{transport} \\ \mathrm{CO_2~exch.} \\ \mathrm{bio.~pump.} \end{bmatrix} - f_{calc,L} 106 \frac{1}{\tau^P_L} P_L \\
\dv{DIC_H}{t} &= \begin{bmatrix} \mathrm{transport} \\ \mathrm{CO_2~exch.} \\ \mathrm{bio.~pump.} \end{bmatrix} - f_{calc,H} 106 \frac{1}{\tau^P_H} P_H \\
\dv{DIC_D}{t} &= \begin{bmatrix} \mathrm{transport} \\ \mathrm{bio.~pump.} \end{bmatrix} + \left(f_{calc,L} 106 \frac{V_L}{\tau^P_L} P_L + f_{calc,H} 106 \frac{V_H}{\tau^P_H} P_H \right) / V_D
```

where the terms in square brackets represents the transport {eq}`eq:3box:conservative`, gas exchange {eq}`eq:3box:dic:solubility` and biological pump {eq}`eq:3box:dic:biopump` terms.  For TA, the expression is included as:

```{math}
:label: eq:3box:ta:calc
\dv{TA_L}{t} &= \begin{bmatrix} \mathrm{transport} \\ \mathrm{bio.~pump.} \end{bmatrix} - 2 f_{calc,L} 106 \frac{1}{\tau^P_L} P_L \\
\dv{TA_H}{t} &= \begin{bmatrix} \mathrm{transport} \\ \mathrm{bio.~pump.} \end{bmatrix} - 2 f_{calc,H} 106 \frac{1}{\tau^P_H} \\
\dv{TA_D}{t} &= \begin{bmatrix} \mathrm{transport} \\ \mathrm{bio.~pump.} \end{bmatrix} + \left( 2 f_{calc,L} 106 \frac{V_L}{\tau^P_L} P_L + 2 f_{calc,H} 106 \frac{V_H}{\tau^P_H} P_H \right) / V_D
```
