# ============================================================================================================
# IIC.py
# lheywang on 02/01/2025
#
# Advanced file for the trigger class, specialized on IIC bus
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase
from channel import SiglentChannel
from digital import SiglentDigital

class SiglentIIC(SiglentBase):
    """
    pySDS [Files][SiglentIIC] : Class herited from SiglentBase.
                                Store all command related the control of the triggering system for the I2C bus

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (15): 

    """

    def SetTriggerOnSCL(self, Threshold):
        """
        pySDS 
        
        """