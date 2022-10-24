# Column descriptions

Not all of these 121 columns will be exploited here (some of them will certainly be deleted during the data cleaning phase) but we will nevertheless try to provide a description of those that seem to us to be the most important.

**Name**
- **pl_name** : Planet name
- **hostname** : Stellar name
- **tic_id** : 	ID given by the TESS Input Catalog

**System **Composition****
- **sy_snum**: Number of stars
- **sy_pnum** : Number of planets
- **sy_mnum** : Number of moon in planetary system
- **cb_flag** :  Indicating whether the planet orbits a binary system (1=yes, 0=no)

**Planet Discovery**
- **discoverymethod** : Method by which the planet was first identified
- **disc_year** : Year the planet was discovered
- **disc_locale** : Location of observation (Ground / Space)
- **disc_facility** : Discovery facility
- **disc_telescope** : Name of telescope of observation
- **disc_instrument** : Name of instrument observation

**Detections [1=yes, 0=no]**
- **rv_flag** : By radial velocity variation (indicate if the host star exhibits radial velocity variations due to the planet)
- **pul_flag** : By Pulsar Timing Variation
- **ptv_flag** : By Pulsation Timing Variation
- **tran_flag** : By transits
- **ast_flag** : By Astrometric Variation
- **obm_flag** : By Orbital Brightness Modulations
- **micro_flag** : By microlensing
- **etv_flag** : By Eclipse Timing Variations (transit timing variations on the orbit of another another planet in the system)
- **ima_flag** : By imaging
- **dkin_flag** : By Disk Kinematics

**Planet Parameters**
- **pl_orbper** : Time the planet takes to make a complete orbit around the host star or system [*unit : days*] 
- **pl_orbsmax** : Longest radius of an eliptic orbit (for micro_flag & ima_flag :  the projected separation in the plane of the sky) [*unit : au (Astronomical Unit)*] 
- **pl_rade** : Length from the center of the planet to its surface [*unit : radius of Earth*]
- **pl_radj** : Length from the center of the planet to its surface [*unit : radius of Jupiter*]
* **Mass**
  - **pl_masse** : Mass of the planet [*unit : mass of Earth*]
  - **pl_massj** : Mass of the planet [*unit : mass of Jupiter*]
  - **pl_msinie** : Minimum mass by radial velocity [*unit : mass of Earth*]
  - **pl_msinij** : Minimum mass by radial velocity [*unit : mass of Jupiter*]
  - **pl_bmasse** : Best mass estimation [*unit : mass of Earth*]
  - **pl_bmassj** : Best mass estimation [*unit : mass of Jupier*]
- **pl_dens** : Planet density [*unit : g/cm**3*]
- **pl_orbeccen** : Amount by which the orbit of the planet deviates from a perfect circle
- **pl_insol** : Insolation flux (another way to give the equilibrium temperature) [*unit : earth flux*]
- **pl_eqt** : Equilibrium Temperature [*unit : Kelvin*]
- **pl_orbincl** : Inclination [*unit : deg*]
- **pl_tranmid** : Average of the time the planet begins to cross the stellar limb (visible surface) and the time the planet finishes crossing the stellar limb[*unit : days*]
- **pl_tsystemref** : Time system basis for temporal and orbital parameters
- **ttv_flag** : Planet orbit exhibits transit timing variations from another planet in the system [*1=yes, 0=no*].
- **pl_imppar** : The sky-projected distance between the center of the stellar disc and the center of the planet disc at conjunction, normalized by the stellar radius
- **pl_trandur** : Time from the moment the planet begins to cross the stellar limb to the moment the planet finishes crossing the stellar limb [*unit : hours*]
- **pl_ratdor** : The distance between the planet and the star at mid-transit divided by the stellar radius. For the case of zero orbital eccentricity, the distance at mid-transit is the semi-major axis of the planetary orbit.
- **pl_ratror** : Ratio of Planet to Stellar Radius
- **pl_occdep** : Depth of occultation of secondary eclipse

**Stellar Data**
- **st_teff** : Temperature of the star as modeled by a black body emitting the same total amount of electromagnetic radiation [*unit : Kelvin*]
- **st_rad** : Length of a line segment from the center of the star to its surface. [*unit : radius of the Sun*]
- **st_mass** : Amount of matter contained in the star [*unit : sun mass*]
- **st_met** : Measurement of the metal content of the photosphere of the star as compared to the hydrogen content [dex]
- **st_lum** : (luminosity) Amount of energy emitted by a star per unit time, measured in units of solar luminosities
- **st_logg** : Gravitational acceleration experienced at the stellar surface
- **st_age** : 	The age of the host star
- **st_dens** : Amount of mass per unit of volume of the star
- **st_vsin** : Rotational velocity at the equator of the star multiplied by the sine of the inclination [km/s]
- **st_radv** : Velocity of the star in the direction of the line of sight

**System Data**
- **sy_dist** : Distance to the planetary system [*unit : parsecs (pc)*]

**Position (System Data Subset)**
- **rastr** : Right Ascension of the planetary system [*unit : sexagesimal*]
- **decstr** : Declination of the planetary system [*unit : sexagesimal*]
- **ra** : 	Right Ascension of the planetary system [*unit : Decimal Degrees*]
- **dec** : Declination of the planetary system [*unit : Decimal Degrees*]
- **glat** : Galactic latitude of the planetary system [*unit : Decimal Degrees*]
- **glon** : Galactic longitude of the planetary system [*unit : Decimal Degrees*]
- **elat** : Ecliptic latitude of the planetary system [*units : decimal degrees*]
- **elon** : Ecliptic longitude of the planetary system [*units : decimal degrees*]

**Photometry**
- **sy_kmag** : Brightness of the host star as measured using the K (2MASS) band [*units : magnitudes*]
- **sy_gaiamag** : Brightness of the host star as measuring using the Gaia band in units of magnitudes. Objects matched to Gaia using the Hipparcos or 2MASS IDs provided in Gaia DR2

**Dates**
- **rowupdate** : Date of Last Update
- **pl_pubdate** : Planetary Parameter Reference Publication
- **releasedate** : release date