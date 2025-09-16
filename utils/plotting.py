# utils/plotting.py

import matplotlib.pyplot as plt

def set_plot_style():
    """Apply consistent LaTeX-like styling across all plots."""
    plt.rcParams.update({
        "text.usetex": True,                # Use LaTeX for all text
        "font.family": "serif",             # Match LaTeX font family
        "font.serif": ["New PX"],           # newpxtext/newpxmath
        "axes.labelsize": 14,               # Axis labels
        "axes.titlesize": 14,               # Subplot titles
        "xtick.labelsize": 13,
        "ytick.labelsize": 13,
        "legend.fontsize": 13,
        "figure.dpi": 300,                  # High resolution
        "savefig.bbox": "tight",            # Don't cut off labels
        "savefig.dpi": 300,
        "savefig.format": "png",
    })