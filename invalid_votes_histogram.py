from __future__ import division
import matplotlib.pyplot as plt
from row import get_rows


def invalid_votes_hist(filename, election_name):
    rows = get_rows(filename)
    invalid_vote_percentages = []
    rows_without_votes = 0
    for row in rows:
        # Calculate percentage of votes that are invalid.
        # Skip if we can't calculate.
        if row.votes == 0:
            rows_without_votes += 1
        else:
            invalid_vote_percentages.append(row.invalid_votes / row.votes * 100)
    msg = 'percent of polling stations recorded no votes'
    print rows_without_votes / len(rows) * 100, msg

    plt.hist(invalid_vote_percentages, bins=100)
    plt.xlabel('[%] Votes that are invalid')
    plt.ylabel('# polling stations')
    plt.title(election_name)
    plot_filename = 'plots/' + election_name + ' invalid votes.pdf'
    plt.savefig(plot_filename)
    # plt.show()
    return plot_filename


if __name__ == '__main__':
    # TODO(agf): Do this breakdown by region
    print '*** Generating histogram for percentage of votes that are invalid'
    print '        across all polling stations.'
    plotname = invalid_votes_hist('data/20/by_polling_stations.csv',
                                  'Israel 20th Knesset Election')
    print '*** Generated', plotname
