def t_test(sample_1, sample_2, disp=False):
    """
    Performs a student's t-test and returns relavant statistics.

    Parameters:
    sample_1 (lst): a list with values for sample 1.
    sample_2 (lst): a list with values for sample 2.
    disp (bool): determines printng of values in formated strings. Does not affect return.

    Returns:
    (tup): contains t-value, degrees of freedom, and p-value
    """
    import numpy as np
    import scipy.stats as stats

    # compute sample size
    n1 = len(sample_1)
    n2 = len(sample_2)

    # t-test
    numerator = np.mean(sample_1) - np.mean(sample_2)
    denominator_sq = (np.var(sample_1) / n1) + (np.var(sample_2) / n2)
    t = numerator / np.sqrt(denominator_sq)

    # degrees of freedom
    df = (
        ((np.var(sample_1)/n1 + np.var(sample_2)/n2)**(2.0)) /
        ((np.var(sample_1)/n1)**(2.0)/(n1 - 1) + (np.var(sample_2)/n2)**(2.0)/(n2 - 1))
    )

    # create student's t distribution
    students = stats.t(df)

    # p-value
    t_abs = abs(t)
    p = students.cdf(-t_abs) + (1 - students.cdf(t_abs))

    if disp:
        print("Welch Test Statistic: {:2.2f}".format(t))
        print("Degrees of Freedom for Welch's Test: {:2.2f}".format(df))
        print("p-value: {:2.2f}".format(p))
    return (t, df, p)
