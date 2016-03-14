from __future__ import division
import matplotlib.pyplot as plt
from row import get_rows


def turnout_hist(filename, election_name):
    '''
    Make a histogram of turnout percentages from all polling stations.
    We expect this to be about normally distributed.
    '''
    rows = get_rows(filename)
    turnouts = []
    rows_without_num_registered_voters = 0
    for row in rows:
        # Calculate turnout. Skip if we can't calculate turnout.
        if row.registered_voters == 0 and row.votes > 0:
            rows_without_num_registered_voters += 1
            continue
        if row.registered_voters == 0:
            turnout = 0
        else:
            turnout = row.votes / row.registered_voters * 100
        turnouts.append(turnout)
    missing_percent = rows_without_num_registered_voters / len(rows) * 100
    msg = 'percent of polling stations did not have #registered voters'
    print missing_percent, msg

    plt.clf()
    plt.hist(turnouts, bins=50)
    plt.xlabel('[%] Voter turnout')
    plt.ylabel('# polling stations')
    plt.title(election_name)
    plot_filename = 'plots/' + election_name + ' voter turnout.pdf'
    plt.savefig(plot_filename)
    # plt.show()
    return plot_filename


if __name__ == '__main__':
    # TODO(agf): Do this breakdown by region
    print '*** Generating histogram of voter turnout across all polling stations.'
    print '***     This should bear a passing resemblance to a normal distribution...'
    print '***     But more importantly, this should not change drastically or'
    print '***     grow new spikes between years. See page 6 of'
    print '***     references/Russia2008_Lukinova_Myagokov_Ordeshook-1.doc'
    plotname = turnout_hist('data/20/by_polling_stations.csv',
                            'Israel 20th Knesset Election')
    print '*** Generated', plotname
    plotname = turnout_hist('data/19/by_polling_stations.csv',
                            'Israel 19th Knesset Election')
    print '*** Generated', plotname
    plotname = turnout_hist('data/18/by_polling_stations.csv',
                            'Israel 18th Knesset Election')
    print '*** Generated', plotname
