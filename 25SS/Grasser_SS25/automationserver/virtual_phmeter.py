"""class simulating a pH meter"""

import random
import numpy as np

class pHMeter:
    """A simulated pHMeter.
    
    Simulates titration of 1 mol of a randomized pKa with 10% w/w NaOH.
    
    provides a `readout` property to get the current readout, and an `add()` function to simulate titration"""
    def __init__(self):
        self.pka = random.randint(1,5)
        """Initial pKa for the titration, randomized"""
        self.moles_to_titrate = 1
        """Config value - how much there is to titrate"""
        self.added_volume_mL = 0.0
        """How much titer was added"""
        self.tau = 0
        """degree of titration"""

    def add(self, volume_mL: float):
        """Simulates directing the titration apparatus to add volume"""
        self.added_volume_mL += volume_mL

    @property
    def pH(self) -> float:
        """Calculates the pH from the pkA, the added volume and the Hendersson-Hasselbach equation
                
        Returns:
            float: the current calculated pH"""

        added_moles = self.added_volume_mL * 0.10 / 40
        """Assuming titration with 10% w/w NaOH"""
        self.tau = added_moles / 1 if added_moles != 0 else 0
        """association quotient"""

        if self.tau == 0: return self.pka * 0.1
        elif self. tau > 1: return (pH := 14 - (self.pka + np.log10(np.abs(self.tau/(1-self.tau)))))
        else: return (pH:= self.pka + np.log10(np.abs(self.tau/(1-self.tau))))
    
    @property
    def readout(self) -> float:
        """Returns a slightly randomized version of the pH to simulate some readout noise
        
        Returns:
            float: the randomized pH readout"""
        
        return random.gauss(self.pH, 0.01)


if __name__ == "__main__":
    phmeter = pHMeter()
    for volume in np.linspace(0, 600, 50):
        phmeter.added_volume_mL = volume
        print("pH", phmeter.added_volume_mL, phmeter.pH, phmeter.tau)