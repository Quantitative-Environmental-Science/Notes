<br><div style="page-break-before:always;"></div>

(groundwater_5)=
# Contaminant Transport and Pollution in Rivers

Another major challenge in groundwater systems is the transport of contaminants, that is something (potentially toxic) is released into the subsurface and travels with the groundwater, appearing in the water supply at some point later in time (depending on the {term}`hydraulic conductivity` of the aquifer, and the {term}`hydraulic head` difference driving the flow).
In some respects we have learned the tools you would need to determine how long before a contaminant released into the groundwater would be seen at some point downstream.
You could figure out the lines of equipotential, and the {term}`hydraulic conductivity`, and then calculate the flow velocity, and this would yield time (with some knowledge of the distance travelled).

## Control Volumes and Dispersion

One way to think about this is using the 'control volume' and thinking that flow
through advection moves the control volume along the X axis but flow through
dispersion (molecular diffusion and mechanical or hydrodynamic dispersion) also
moves the flow along in the Y and Z direction ({numref}`control_volume`).

```{admonition} A brief primer on diffusion
:class: dropdown

**Diffusion** is the spontaneous movement of particles from regions of high
concentration to regions of low concentration.
At the molecular level,
this occurs due to random thermal motion of molecules.
In groundwater,
contaminants diffuse through pore water even in the absence of flow.

Diffusion is governed by **Fick's First Law**,
which states that the diffusive flux is proportional to the concentration
gradient:

$$J = -D \frac{\partial C}{\partial x}$$

where $J$ is the diffusive flux, $D$ is the diffusion coefficient,
and $\frac{\partial C}{\partial x}$ is the concentration gradient.
The negative sign indicates that diffusion occurs down the concentration gradient
(from high to low concentration).

```{figure} ./figures/figure7.12.png
---
name: diffusion_timeseries
width: 90%
---
Time series showing the spreading of dye through diffusion at four successive
time steps, illustrating how concentration gradients diminish over time.
```

```{figure} ./figures/figure7.5.png
---
name: control_volume
figclass: margin-caption
width: 80%
---
A diagram showing how advection moves the control volume along the X axis while
dispersion causes movement in the Y and Z directions.
```

In beadpacks in the Institute for Energy and Environmental Flows you can see the
stretching along the flowpath of an injection of dye ({numref}`beadpack_dye`).

```{figure} ./figures/figure7.6.png
---
name: beadpack_dye
figclass: margin-caption
width: 80%
---
Dye injection in a beadpack showing stretching along the flowpath.
```

## The Peclet Number

Determining the relative importance of advection versus dispersion
(so the growing shape of the contaminant plume during subsurface transport) is
often done using the dimensionless **Peclet Number** ({numref}`peclet_number`).

```{figure} ./figures/figure7.7.png
---
name: peclet_number
figclass: margin-caption
width: 80%
---
The Peclet Number characterizes the relative importance of advection and
dispersion in contaminant transport.
```

```{figure} ./figures/figure7.8.png
---
name: dispersion_peclet
figclass: margin-caption
width: 70%
---
Normalized dispersion coefficient plotted against Péclet number.
```

## Contaminant Plume Modeling

If we assume that the contaminant spreads out in all directions as it moves along
the flow of the groundwater,
then we can track the shape of the contaminant plume away from the point source.
Here the relative movement in the X direction versus the Y and Z direction is a
function of the magnitude of the movement due to molecular diffusion versus that
due to advective velocity and mechanical dispersion.
With a series of simplifying assumptions (isotropic media, flow in the x direction
etc.) we can use a gaussian model to track plume movement over time
({numref}`plume_diagram`).

```{figure} ./figures/figure7.9.png
---
name: plume_diagram
figclass: margin-caption
width: 80%
---
Diagram showing the development of a contaminant plume in groundwater,
tracking movement in three dimensions over time.
```

This is similar to the maths behind following a plume of smoke in the atmosphere
({numref}`smoke_plume`, {numref}`plume_model`).

```{figure} ./figures/figure7.10.png
---
name: smoke_plume
figclass: margin-caption
width: 70%
---
A smoke plume in the atmosphere showing similar dispersion patterns.
```

```{figure} ./figures/figure7.11.png
---
name: plume_model
figclass: margin-caption
width: 80%
---
Plume model diagram illustrating the mathematical framework for tracking
dispersion.
```

## Contaminant Transport Models

However, like most things, it is more complicated than this.
The contaminant is not just subject to advection with the flow of the groundwater, but also diffusion (the process by which things move from high concentration to low concentration) and possibly chemical reaction with the porous media.
This leads to an entirely different class of equations and models known as advective diffusive transport models.
We wont go through the mathematics of these models but the standard formula is:

```{margin} Units!
:class: units
$$
C &= \mathrm{amount~m^{-3}} \\
D &= \mathrm{m^2~s^{-1}} \\
v &= \mathrm{m~s^{-1}} \\
R &= \mathrm{amount~m^{-3}~s^{-1}} \\
$$
```

```{math}
:label: advection
D \frac{\delta^2 C}{\delta x^2} - v \frac{\delta C}{\delta x} = R \left( \frac{\delta C}{\delta t} \right)
```

Where $C$ is a contaminant, and I am curious how its concentration changes with time $\left( \frac{\delta C}{\delta t} \right)$ and with distance $\left( \frac{\delta C}{\delta x} \right)$.
Because there are changes with time and with difference, we need to use a partial differential equation.
In the partial differential equation above, $D$ is the diffusion coefficient for the contaminant in water, $v$ is the flow velocity $\left( \frac{-K}{\rho} \dv{h}{x} \right)$ (can you figure out why this is the flow velocity from Darcy’s Law?), and $R$ represents the chemical reactions that change the concentration with time.
In the lecture we’ll talk through each of these terms, and how diffusion can be molecular diffusion or mechanical dispersion, and the types of chemical reactions that change the concentration of common contaminants.


Pollution in rivers has been a growing concern.
In general, pollution in rivers is from the release of sewage,
chemicals and nutrients into the rivers.
The River Trust has a bunch of maps that track pollution levels in rivers across
the UK, including the amount of 'forever chemicals'
(e.g., chemicals that are very hard to degrade so will stay in rivers for a very
long time) and the rate of release of sewage.
However, the largest source of pollution to rivers is through nutrients from
agriculture.

## Nutrients and Eutrophication

Nutrients refer largely to nitrate and phosphate,
which are key macronutrients that are needed for photosynthesis.
Nitrogen (in the form of ammonium or nitrate) is used in amino acids and proteins
while phosphorus is used for DNA and cell walls and lipids.
To get plants to grow you need a source of CO<sub>2</sub>,
water, light, nitrogen and phosphorus.
This is why nitrogen and phosphorus are often added to soils in the form of
fertilizers to maximize plant growth.
Currently UK farmers are not penalised for overfertilizing their land,
so it is just the cost of the fertilisers that limits the amount that would be
used to stimulate growth.

As you add nitrogen and phosphorus run-off from agriculture to rivers you get
growth of algae in the rivers,
often measured as the chlorophyll abundance ({numref}`chlorophyll_growth`).

```{figure} ./figures/figure9.1.png
---
name: chlorophyll_growth
figclass: margin-caption
width: 70%
---
The addition of nitrate and phosphate leads to exceptional algal growth,
shown by chlorophyll abundance.
```

And we know that more algal production leads to more respiration which depletes
the water in oxygen.
This is **{term}`eutrophication`**.

```{figure} ./figures/figure9.2.png
---
name: eutrophication_diagram
figclass: margin-caption
width: 80%
---
The process of eutrophication:
excess nutrients lead to algal blooms,
which increase respiration and deplete oxygen levels in the water.
```

In the lecture we discussed the particular challenge of the River Wye,
where intensification of chicken farming has led to mass eutrophication and fish
kills along the river.
Focusing on cleaning up rivers often focuses on stemming the tide of runoff into
the river.
But much of the waste is seeping into the groundwater.
We can start to ask ourselves how long until it reaches the rivers and the
challenges with eutrophication might be over?

## Transit Time and Groundwater

The transit time simply might be considered:

```{math}
:label: eq:transit_time
\text{Time} = \frac{\text{Length to travel}}{\text{velocity of fluid}}
```

Where the length might be how far a farm is from the river of interest and the
velocity could be the rate of flow of a stream or the rate of flow of the
groundwater derived from Darcy's Law.
It has long been thought that time scales with length.
Next week in Andy's lectures,
he is going to show us why -- when it comes to groundwater systems -- time
scales with length<sup>2</sup>
(due to the flowpaths in the subsurface and the impact of dispersion).

```{margin} Units!
:class: units
$$
\text{Time} &= \mathrm{s~or~yr} \\
\text{Length} &= \mathrm{m} \\
\text{velocity} &= \mathrm{m~s^{-1}}
$$
```

## Groundwater and Surface Water Interactions

The take home from groundwater is the importance it plays in the overall surface
water system!

```{figure} ./figures/figure9.3.png
---
name: groundwater_surface_water
figclass: margin-caption
width: 80%
---
Diagram showing the network of interactions between groundwater and surface
water systems.
```
