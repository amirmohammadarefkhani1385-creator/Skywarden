


"""Data models for the astronomy observation ."""


class Observation:
    """A single astronomical observation.

    Attributes:
        target: Name of the observed object (e.g. "Vega").
        observer: Name of the person who made the observation.
        filter_name: Name of the filter used (e.g. "V", "R").
        exposure_seconds: Exposure time in seconds.
    """
#---------------------------------------------------------------------------
    def __init__(self, target, observer, filter_name, exposure_seconds):
        self.target = target
        self.observer = observer
        self.filter_name = filter_name
        self.exposure_seconds = exposure_seconds
#------------------------------------------------------------------------------
    def summary(self):
        """Return a multi-line, description of the observation."""
        return (
            f"  Target   : {self.target}\n"
            f"  Observer : {self.observer}\n"
            f"  Filter   : {self.filter_name}\n"
            f"  Exposure : {self.exposure_seconds:g} s "
            f"({self.exposure_minutes():.2f} min)"
        )
#-----------------------------------------------------------------------------
    def exposure_minutes(self):
        """Return the exposure time converted from seconds to minutes."""
        return self.exposure_seconds / 60

#-----------------------------------------------------------------------------
class Wavelength_Observation(Observation):
    """An observation that also stores the wavelength (lambda).

    Attributes:
        lambda_nm: Wavelength in nanometres.
    """
#------------------------------------------------------------------------------
    def __init__(self, target, observer, filter_name, exposure_seconds, lambda_nm):
        super().__init__(target, observer, filter_name, exposure_seconds)
        self.lambda_nm = lambda_nm
#------------------------------------------------------------------------------
    def summary(self):
        """Return the base text and add a line for lambda."""
        return super().summary() + f"\n  Lambda: {self.lambda_nm} nm"

#-------------------------------------------------------------------------------
class Brightness_Observation(Observation):
    """An observation that also stores how bright the target is.

    Attributes:
        apparent_mag: Apparent magnitude (smaller means brighter, may be negative).
    """
#------------------------------------------------------------------------------
    def __init__(self, target, observer, filter_name, exposure_seconds, apparent_mag):
        super().__init__(target, observer, filter_name, exposure_seconds)
        self.apparent_mag = apparent_mag
#--------------------------------------------------------------------------------
    def summary(self):
        """Return the base text and add a line for the apparent magnitude."""
        return super().summary() + f"\n  Apparent magnitude: {self.apparent_mag}"



