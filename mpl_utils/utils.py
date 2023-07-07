import typing as T

import matplotlib as mpl
import matplotlib.pyplot as plt


def make_axis_limits_equal(ax: plt.Axes, lower_limit: float = None, upper_limit: float = None) -> plt.Axes:
    """
    Make the axes of a plot have equal limits.

    Args:
        ax: Plot axis to modify
        lower_limit: Lower limit of axes (optional).
        upper_limit: Upper limit of axes (optional).
    Returns:
        Plot with modified axis limits.
    """
    xlims = ax.get_xlim()
    ylims = ax.get_ylim()
    # Find  minimum and maximum values
    limits = [i for j in (xlims, ylims) for i in j]
    low = min(limits)
    upp = max(limits)
    # Use user-defined limits if given
    low = low if lower_limit is None else lower_limit
    upp = upp if upper_limit is None else upper_limit
    lims = (low, upp)
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    return ax


def draw_diagonal_line(
    ax: plt.Axes, ls: str = "--", color: str = "k", lw: float = 1, alpha: float = 1, label: str = None, **kwargs
) -> plt.Axes:
    """
    Draw a diagonal line from the lower left to the upper right of a plot. Useful to show
    the 45 degree line when the axes limits are equal (see make_axis_limits_equal).

    Args:
        ax: Axis in which to draw the line.
        ls: Line style.
        color: Color of line.
        lw: Line width.
        alpha: Alpha value of line.
        label: Line label.
        **kwargs: Any other kwarg to pass to plt.plot

    Returns:
        Original axes with line.
    """
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    low = min(xlim[0], ylim[0])
    upp = max(xlim[1], ylim[1])
    ax.plot([low, upp], [low, upp], ls=ls, color=color, lw=lw, alpha=alpha, label=label, **kwargs)
    return ax


def setup_legend(
    ax: mpl.axes.Axes,
    linewidth: float = None,
    markersize: float = None,
    labels: T.Iterable = None,
    loc: T.Union[int, str] = None,
    bbox_to_anchor: T.Tuple = None,
    **kwargs
) -> mpl.axes.Axes:
    """
    Convenience function to change properties of an axis legend, with the ability to change the size of
    lines and markers to improve readability, optionally change the label text, and optionally use a custom
    location for the legend.
    Adds a legend to an axis if it doesn't already exist.

    Args:
        ax: Plot axis with a legend
        linewidth: Width of lines in legend
        markersize: Size of markers in Legend
        labels: List of labels to use to replace existing text in legend
        loc: Location of legend. Can be number or string (same as normal) with custom location of 'outside right'
        bbox_to_anchor: Tuple for anchor point of legend (see matplotlib documentation for details)
        kwargs: Any other keyword arguments to pass to ax.legend()

    Returns:
        Original axis with modified legend
    """
    handles, old_labels = ax.get_legend_handles_labels()
    if labels is None:
        labels = old_labels

    # Custom position to put the legend on the outside of the plot on the center right
    if loc == "outside right":
        loc = "center left"
        bbox_to_anchor = (1, 0.5)
    leg = ax.legend(handles, labels, loc=loc, bbox_to_anchor=bbox_to_anchor, **kwargs)

    # Setup lines
    if linewidth is not None:
        leg_lines = leg.get_lines()
        plt.setp(leg_lines, linewidth=linewidth)

    # Setup markers
    if markersize is not None:
        for handle in leg.legendHandles:
            handle._legmarker.set_markersize(markersize)
    return ax
