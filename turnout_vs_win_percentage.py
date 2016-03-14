from __future__ import division
import matplotlib.pyplot as plt
from row import get_rows


def analyze(filename, party_num, party_name, election_name):
    '''
    Make a graph that is similar to references/1201.3087.pdf
    '''
    rows = get_rows(filename)
    turnouts = []
    percentages_for_party_num = []
    rows_without_num_registered_voters = 0
    for row in rows:
        # Calculate turnout. Skip if we can't calculate turnout.
        if row.registered_voters == 0 and row.votes > 0:
            rows_without_num_registered_voters += 1
            continue
        if row.registered_voters == 0:
            turnout = 0
            percent_for_party_num = 0
        else:
            # Could instead use valid_votes / registered_voters
            turnout = row.votes / row.registered_voters * 100
            percent_for_party_num = row[party_num] / row.registered_voters * 100
        turnouts.append(turnout)
        percentages_for_party_num.append(percent_for_party_num)
    missing_percent = rows_without_num_registered_voters / len(rows) * 100
    msg = 'percent of polling stations did not have #registered voters'
    print missing_percent, msg

    plt.clf()
    plt.hist2d(turnouts, percentages_for_party_num, bins=75)
    plt.colorbar(label='# polling stations')
    plt.xlabel('[%] Voter turnout')
    plt.ylabel('[%] Votes for ' + party_name)
    plt.title(election_name)
    plot_filename = ('plots/' + election_name +
                     ' voter turnout vs votes for ' + party_name + '.pdf')
    plt.savefig(plot_filename)
    # plt.show()
    return plot_filename


if __name__ == '__main__':
    print '*** Generating plots that are similar to references/1201.3087.pdf :'
    plotname = analyze('data/20/by_polling_stations.csv', 13, 'Likud',
                       'Israel 20th Knesset Election')
    print '*** Generated', plotname
    plotname = analyze('data/19/by_polling_stations.csv', 13, 'Likud',
                       'Israel 19th Knesset Election')
    print '*** Generated', plotname
    plotname = analyze('data/18/by_polling_stations.csv', 15, 'Likud',
                       'Israel 18th Knesset Election')
    print '*** Generated', plotname
