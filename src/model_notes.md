## CHEMKIN Model Notes

To launch equations governing steady, isobaric, quasi-one-dimensional flame propagation, CHEMKIN gives a choice of two options: 
1. Premixed Laminar Burner-stabilized Flame
2. Premixed Laminar Flame-speed Calculation

The first models the flame itself, while the second is used for estimating laminar flame speed and modelling at laminar flame speed (despite inlet speeds).
Of the first model there are two options depending on whether an adiabatic or non-adiabatic flame should be modelled. If a temperature profile is known, then this can be imported instead of using a profile determined by the energy conservation equation. 
This is because the imported temperature profile will allow for the consideration of heat losses in the model. 

In this experimental set-up, the wall surface temperature is used as an input condition for Premixed Laminar Burner-Stabilized Flame Model. 
Hence the layout of the input file for this model (followingt the ANSYS example guide) would be as follows (where ! are comments and capitalised words e.g BURN are input variables):
```
! 
! problem type definition
! 
BURN   ! Burner Stabilized Flame
MIX   ! Use Mixture-averaged Transport
TDIF   ! Use Thermal Diffusion (Soret Effect)
TGIV   ! Fix Gas Temperature
VCOR   ! Use Correction Velocity Formalism
! 
! physical property
! 
FLRT 0.1   ! Mass Flow Rate (g/cm2-sec)
PRES 1.0   ! Pressure (atm)
TPRO 0.0 373.7   ! Temperature (K)
TPRO 0.125 484.5   ! Temperature (K)
TPRO 0.25 583.7   ! Temperature (K)
TPRO 0.375 672.2   ! Temperature (K)
TPRO 0.5 753.5   ! Temperature (K)
TPRO 0.75 901.4   ! Temperature (K)
TPRO 1.0 1027.0   ! Temperature (K)
TPRO 1.25 1120.0   ! Temperature (K)
TPRO 1.5 1184.0   ! Temperature (K)
TPRO 2.0 1260.0   ! Temperature (K)
TPRO 3.0 1348.0   ! Temperature (K)
TPRO 6.0 1475.0   ! Temperature (K)
TPRO 10.0 1524.0   ! Temperature (K)
! 
! reactor dimension definition
! 
CURV 0.9   ! Adaptive Grid Control Based On Solution Curvature
GRAD 0.9   ! Adaptive Grid Control Based On Solution Gradient
NPTS 6   ! Number of Uniform Grid Points
NTOT 1500   ! Maximum Number of Grid Points Allowed
XEND 2.0   ! Ending Axial Position (cm)
XSTR 0.0   ! Starting Axial Position (cm)
! 
! species property
! 
MOLE   ! Print Mole Fractions
PRMN 0.0   ! Minimum for Product Estimates (mole fraction)
REAC C3H8 0.05   ! Reactant Fraction (mole fraction)
REAC N2 0.7505   ! Reactant Fraction (mole fraction)
REAC O2 0.1995   ! Reactant Fraction (mole fraction)
! 
! solver control
! 
XIMN 1.0E-12   ! Minimum for Estimated Intermediate Fraction (mole fraction)
ATIM 1.0E-8   ! Absolute Tolerance for Pseudo Timestepping
ATOL 1.0E-9   ! Absolute Tolerance
RTIM 1.0E-8   ! Relative Tolerance for Pseudo Timestepping
RTOL 0.0001   ! Relative Tolerance
SFLR -0.001   ! Minimum Bounds on Species Fractions
SPOS 1.0E-12   ! Positive Value to Reset Species Fractions
TIM1 100.0 1.0E-6   ! Pseudo Time Steps (Fixed Temperature) (none, sec)
WDIF   ! Windward Differencing
GFAC 1.0   ! Gas Reaction Rate Multiplier
PRNT 1.0   ! Print Level Control
! 
! grid property continuation
! 
! Number of Continuation 5   ! Continuation Count
CNTN   ! Continuation
END   ! End
CURV 0.5   ! Adaptive Grid Control Based On Solution Curvature
GRAD 0.5   ! Adaptive Grid Control Based On Solution Gradient
XEND 2.0   ! Ending Axial Position (cm)
CNTN   ! Continuation
END   ! End
CURV 0.1   ! Adaptive Grid Control Based On Solution Curvature
GRAD 0.1   ! Adaptive Grid Control Based On Solution Gradient
CNTN   ! Continuation
END   ! End
CURV 0.05   ! Adaptive Grid Control Based On Solution Curvature
GRAD 0.05   ! Adaptive Grid Control Based On Solution Gradient
CNTN   ! Continuation
END   ! End
CURV 0.02   ! Adaptive Grid Control Based On Solution Curvature
GRAD 0.02   ! Adaptive Grid Control Based On Solution Gradient
CNTN   ! Continuation
END   ! End
CURV 0.01   ! Adaptive Grid Control Based On Solution Curvature
GRAD 0.01   ! Adaptive Grid Control Based On Solution Gradient
END


```