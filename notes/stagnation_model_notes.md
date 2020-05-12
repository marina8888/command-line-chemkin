##Burner Stabilized Stagnation Models
To run the burner-stabilized stagnation flame model can be used to plot strain stabilized flat flames.
Take product gases at the XEND position. In the template file included below, the key parameters that need to be modified for every run are: 

PRES = (room pressure converted into atm)
TINL StagPlane = (stagnation plate temperature converted to K)
TMAX = (adiabatic Tmax temperature (from conditions calcs) +200 degrees to K)

TINL C1_Inlet1 = (inlet temperature as T1 in K)
UINL C1_Inlet1  = (inlet velocity in cm/s)
REAC C1_Inlet1 NH3  = (molar fraction NH3)
REAC C1_Inlet1 CH4  = (molar fraction CH4)
REAC C1_Inlet1 O2 = (molar fraction O2)
REAC C1_Inlet1 N2 = (molar fraction N2)

```
! 
! problem type definition
! 
AXIS   ! Cylindrical Coordinates
ENRG  ! Solve Gas Energy Equation
FLUX   ! Flux Balance for Inlet Species
MIX   ! Use Mixture-averaged Transport
PLAT   ! Plateau Profile for Initial Guess
STAGNATION_FLAME   ! Stagnation Flame Reactor
! 
! physical property
! 
PRES 1.0   ! Pressure (atm)
TINF 297.0   ! Ambient Temperature (K) - set to 24 degrees
TINL StagPlane 700.0   ! Stagnation Plane Temperature (K)
TMAX 2800.0   ! Maximum Temperature for Initial Profile (K)
! 
! reactor dimension definition
! 
CURV 0.9   ! Adaptive Grid Control Based On Solution Curvature
GRAD 0.9   ! Adaptive Grid Control Based On Solution Gradient
NADP 10   ! Number of Adaptive Grid Points
NPTS 100   ! Number of Uniform Grid Points
NTOT 500   ! Maximum Number of Grid Points Allowed
PCAD 0.75   ! Percent of Grids for Adaptation
RGTC 1.0   ! Ratio of Gradient to Curvature Adaptation
XEND 2.0   ! Ending Axial Position (cm)
! 
! output control and other misc. property
! 
GFAC 1.0   ! Gas Reaction Rate Multiplier
PRNT 1.0   ! Print Level Control
! 
! physical property
! 
AINL C1_Inlet1 0.0   ! Radial Gradient in Inlet Velocity (1/sec)
TINL C1_Inlet1 293.0   ! Inlet Temperature (K)
UINL C1_Inlet1 90.34   ! Inlet Velocity (cm/sec)
! 
! species property
! 
REAC C1_Inlet1 NH3 0.28135   ! Reactant Fraction (mole fraction)
REAC C1_Inlet1 CH4 1   ! Reactant Fraction (mole fraction)
REAC C1_Inlet1 O2 2.21101   ! Reactant Fraction (mole fraction)
REAC C1_Inlet1 N2 8.31342   ! Reactant Fraction (mole fraction)
INLET C1_Inlet1 1   ! Inlet Stream
! 
! physical property
! 
INLET StagPlane 1
!
! grid property continuation
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
