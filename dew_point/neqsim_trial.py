# -*- coding: utf-8 -*-
import pandas as pd
from neqsim.neqsimpython import jNeqSim
from neqsim.thermo import TPflash, dewt, fluid_df, phaseenvelope, printFrame
from neqsim import has_matplotlib
import matplotlib.pyplot as plt

def phaseenvelope_test(testSystem, display=False):
    data_dewT = list()
    data_dewP = list()
    printFrame(testSystem)
    for temp_Pressure in range(0, 1000, 10):
        testSystem.setPressure(temp_Pressure, "bara")
        #TPflash(testSystem)
        data_dewT.append(dewt(testSystem)-273.15)
        data_dewP.append(temp_Pressure)

    print(data_dewT)
    print(data_dewP)
    print("ok")
    if display:
        if has_matplotlib():

            try:
                plt.plot(data_dewT, data_dewP, label="dew point")
            except:
                pass

            plt.title('PT envelope')
            plt.xlabel('Temperature [°C]')
            plt.ylabel('Pressure [bar]')
            plt.legend()
            plt.show()
        else:
            raise Exception("Package matplotlib is not installed")
    return "ok"

naturalgas = {'ComponentName':  ["nitrogen", "CO2", "methane", "ethane", "propane", "i-butane", "n-butane", "i-pentane", "n-pentane", "2-m-C5", "3-m-C5", "n-hexane", "benzene", "c-hexane", "n-heptane", "toluene", "c-C7", "n-octane", "m-Xylene", "c-C8", "n-nonane", "m-Xylene", "nC10", "nC11", "nC12"],
              'MolarComposition[-]':  [1.192, 0.5102, 94.3303, 2.1102, 1.3217, 0.1278, 0.0846, 0.0694, 0.0340, 0.0335, 0.0109, 0.0181, 0.0017, 0.0661, 0.0207, 0.0045, 0.0530, 0.0061, 0.0033, 0.000103, 0.0032, 0.00354, 0.00597, 0.0000597, 0.000001]
              }



naturalgasdf = pd.DataFrame(naturalgas)
print("Natural Gas Fluid:\n")
#print(naturalgasdf.head(30).to_string())

naturalgasFluid = fluid_df(naturalgasdf).setModel("UMR-PRU-EoS")
naturalgasFluid.autoSelectMixingRule()
TPflash(naturalgasFluid)
printFrame(naturalgasFluid)
gasPhaseEnvelope = phaseenvelope_test(naturalgasFluid, True)

#gasPhaseEnvelope = phaseenvelope_test(naturalgasFluid, True)
#cricobar = gasPhaseEnvelope.get("cricondenbar")
#print("cricoP ",  cricobar[1], "  [bara] ", " cricoT ", cricobar[0], " °C")


#naturalgasFluid.setTemperature(-10.0, "C")
#naturalgasFluid.setPressure(10001.0, "bara")
#TPflash(naturalgasFluid)
#printFrame(naturalgasFluid)


#naturalgasFluid.setPressure(10001.0, "bara")
#dewPointT = dewt(naturalgasFluid)-273.15
#print("dew point T ", dewPointT, " °C")
print("end")