


"""Data models for the astronomy observation ."""


class Observation:
    """A single astronomical observation.

    Attributes:
        target: Name of the observed object (e.g. "Vega").
        observer: Name of the person who made the observation.
        filter_name: Name of the filter used (e.g. "V", "R").
        exposure_seconds: Exposure time in seconds.
    """

    def __init__(self, target, observer, filter_name, exposure_seconds):
        self.target = target
        self.observer = observer
        self.filter_name = filter_name
        self.exposure_seconds = exposure_seconds

    def summary(self):
        """Return a multi-line, description of the observation."""
        return (
            f"  Target   : {self.target}\n"
            f"  Observer : {self.observer}\n"
            f"  Filter   : {self.filter_name}\n"
            f"  Exposure : {self.exposure_seconds:g} s "
            f"({self.exposure_minutes():.2f} min)"
        )

    def exposure_minutes(self):
        """Return the exposure time converted from seconds to minutes."""
        return self.exposure_seconds / 60


class Spectroscopic_Observation(Observation):
    """An observation that also records the wavelength.

    Attributes:
        wavelength_nm: Observed wavelength in nanometres.
    """

    def __init__(self, target, observer, filter_name, exposure_seconds, wavelength_nm):
        super().__init__(target, observer, filter_name, exposure_seconds)
        self.wavelength_nm = wavelength_nm

    def summary(self):
        """Return the base summary with the wavelength appended."""
        return super().summary() + f"\n  Wavelength: {self.wavelength_nm:g} nm"

class Photometric_Observation(Observation):
    """An observation that also records the brightness.

    Attributes:
        brightness: Measured brightness of the target.
    """

    def __init__(self, target, observer, filter_name, exposure_seconds, brightness):
        super().__init__(target, observer, filter_name, exposure_seconds)
        self.brightness = brightness

    def summary(self):
        """Return the base summary with the brightness appended."""
        return super().summary() + f"\n  Brightness: {self.brightness:g}"


# In[ ]:




