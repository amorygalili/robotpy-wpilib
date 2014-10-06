#----------------------------------------------------------------------------
# Copyright (c) FIRST 2008-2012. All Rights Reserved.
# Open Source Software - may be modified and shared by FRC teams. The code
# must be accompanied by the FIRST BSD license file in the root directory of
# the project.
#----------------------------------------------------------------------------

import hal

from .digitalsource import DigitalSource

class DigitalInput(DigitalSource):
    """Class to read a digital input. This class will read digital inputs and
    return the current value on the channel. Other devices such as encoders,
    gear tooth sensors, etc. that are implemented elsewhere will automatically
    allocate digital inputs and outputs as required. This class is only for
    devices like switches etc. that aren't implemented anywhere else.
    """

    def __init__(self, channel):
        """Create an instance of a Digital Input class. Creates a digital
        input given a channel.

        :param channel: the port for the digital input
        """
        super().__init__(channel, True)

        hal.HALReport(hal.HALUsageReporting.kResourceType_DigitalInput,
                      channel)

    def get(self):
        """Get the value from a digital input channel. Retrieve the value of
        a single digital input channel from the FPGA.

        :returns: the stats of the digital input
        """
        if self.port is None:
            raise ValueError("operation on freed port")
        return hal.getDIO(self.port)

    def getChannel(self):
        """Get the channel of the digital input

        :returns: The GPIO channel number that this object represents.
        """
        return self.channel

    def getAnalogTriggerForRouting(self):
        return False

    # Live Window code, only does anything if live window is activated.
    def getSmartDashboardType(self):
        return "Digital Input"

    def initTable(self, subtable):
        self.table = subtable
        self.updateTable()

    def updateTable(self):
        table = getattr(self, "table", None)
        if table is not None:
            table.putBoolean("Value", self.get())

    def getTable(self):
        return getattr(self, "table", None)

    def startLiveWindowMode(self):
        pass

    def stopLiveWindowMode(self):
        pass