


"""Charts for the astronomy observation ."""

import matplotlib.pyplot as plt


def show_exposure_chart(observations):
    """Show a bar chart of exposure time for each target.

    Args:
        observations: List of Observation objects to plot.
    """
    if not observations:
        print("\n  No observations to plot.")
        return

    target_names = [obs.target for obs in observations]
    exposure_times = [obs.exposure_seconds for obs in observations]

    figure, axis = plt.subplots(figsize=(8, 5))
    bars = axis.bar(target_names, exposure_times, color="#4C72B0", edgecolor="black")

    axis.bar_label(bars, fmt="%g s", padding=3)
    axis.set_xlabel("Target name")
    axis.set_ylabel("Exposure time (seconds)")
    axis.set_title("Target vs exposure time")

    plt.tight_layout()
    plt.show()

