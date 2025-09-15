# utils/plotting.py

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def plot_correlation_heatmap(df, figsize=(8, 6), cmap="coolwarm"):
    """
    Plot a heatmap of the correlation matrix for a DataFrame.
    """
    correlation_matrix = df.corr()

    plt.figure(figsize=figsize)
    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap=cmap,
        fmt=".2f",
        linewidths=0.5
    )
    plt.title("Correlation Matrix Heatmap")
    plt.show()


def plot_regression_line(df, feature, target, theta, color="red", ax=None):
    """
    Plot scatter of data and regression line given coefficients.
    
    Parameters
    ----------
    df : pd.DataFrame
        Data containing feature and target columns.
    feature : str
        Column name of the independent variable (x).
    target : str
        Column name of the dependent variable (y).
    theta : list or tuple
        [intercept, slope] for the regression line.
    color : str
        Line color.
    ax : matplotlib.axes.Axes, optional
        Axis to plot on. If None, a new figure is created.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 4))

    # Scatter plot
    ax.scatter(df[feature], df[target], alpha=0.5, label="Data")

    # Regression line
    x_vals = np.linspace(df[feature].min(), df[feature].max(), 100)
    y_vals = theta[0] + theta[1] * x_vals
    ax.plot(x_vals, y_vals, color=color, label="Fit line")

    ax.set_xlabel(feature.capitalize())
    ax.set_ylabel(target.capitalize())
    ax.set_title(f"Predicting {target.capitalize()} from {feature.capitalize()}")
    ax.legend()


def plot_side_by_side_regressions(df, feature_target_theta_list, figsize=(10, 4)):
    """
    Plot multiple regression fits side by side for comparison.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset with feature and target columns.
    feature_target_theta_list : list of tuples
        Each tuple is (feature, target, theta, color).
    figsize : tuple
        Size of the whole figure.
    """
    n = len(feature_target_theta_list)
    fig, axes = plt.subplots(1, n, figsize=figsize)

    if n == 1:
        axes = [axes]  # make iterable if only one subplot

    for ax, (feature, target, theta, color) in zip(axes, feature_target_theta_list):
        plot_regression_line(df, feature, target, theta, color=color, ax=ax)

    plt.tight_layout()
    plt.show()