def mannwhitney_dfcalc(df, disp=True, alternative='greater'):
    """
    Calculates the p-values of all combinations of columns in a dataframe.
    When set to one-sided, will only return p-values in in the direction that yields proper results.
    ex. will not return a > b = 0.95, instead will calculate and return b > a

    Parameters:

    df (df): Pandas dataframe with collumns which to compute t-tests on.
    disp (bool): Whether to print results or not.
    alternative (‘two-sided’, ‘less’, or ‘greater’):
        Whether to get the p-value for the one-sided hypothesis (‘less’ or ‘greater’)
        or for the two-sided hypothesis (‘two-sided’). Defaults to two-sided on invalid input.

    Returns:
    (dict): A dictionary keyed by names of compared columns with values of mann whitney output

    """
    import pandas as pd
    import scipy.stats as stats

    # pull column names from dataframe
    names = df.columns

    # print title line
    if disp:
        print('p-value for:')

    # determine the comparator symbol, default to two-sided
    if alternative== 'greater':
        comp = '>'
    elif alternative == 'less':
        comp = '<'
    else:
        alternative = 'two-sided'
        comp = '!='

    # initialize dictionary
    out = {}

    # iterate through dataframe in a 'triangle'
    for i in range(len(names)):
        for j in range(i + 1 , len(names)):
            a = df[names[i]].tolist()
            b = df[names[j]].tolist()

            # caclulate mann whitney
            res = stats.mannwhitneyu(a, b, alternative=alternative)

            # If p-value is greater than .5, calculate in the other direction
            if res.pvalue > .5 and alternative != 'two-sided':
                res = stats.mannwhitneyu(b, a, alternative=alternative)
                # store in dictionary
                out["{} {} {}".format(names[j], comp, names[i])] = res
                # print current calculation
                if disp:
                    print("{} {} {}: {:2.3f}".format(names[j], comp, names[i], res.pvalue))
            else:
                # store in dictionary
                out["{} {} {}".format(names[j], comp, names[i])] = res
                # print current calculation
                if disp:
                    print("{} {} {}: {:2.3f}".format(names[i], comp, names[j], res.pvalue))
    return out
