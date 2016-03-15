from __future__ import division
import matplotlib.pyplot as plt
from row import get_rows


def analyze(filename, election_name):
    rows = get_rows(filename)
    nparties = len(rows[0])
    dist_registered = [0] * nparties
    dist_no_registered = [0] * nparties
    for row in rows:
        sorted_row = sorted(row.data, reverse=True)
        if row.registered_voters > 0:
            for i in xrange(nparties):
                dist_registered[i] += sorted_row[i]
        else:
            for i in xrange(nparties):
                dist_no_registered[i] += sorted_row[i]
    filenames = []
    plt.clf()
    plt.bar(range(nparties), dist_registered)
    title = election_name + 'Station-Sorted Distribution: >0 registered voters'
    plt.title(title)
    plt.ylabel('# Votes')
    filename = 'plots/' + title + '.pdf'
    filenames.append(filename)
    plt.savefig(filename)
    # plt.show()
    plt.clf()
    plt.bar(range(nparties), dist_no_registered)
    title = election_name + 'Station-Sorted Distribution: 0 registered voters'
    plt.title(title)
    plt.ylabel('# Votes')
    filename = 'plots/' + title + '.pdf'
    filenames.append(filename)
    plt.savefig(filename)
    # plt.show()
    return filenames


if __name__ == '__main__':
    print '*** Generating plots for station-sorted distributions'
    plots = analyze('data/20/by_polling_stations.csv',
                    'Israel 20th Knesset Election')
    print '*** Generated', plots[0]
    print '*** Generated', plots[1]
    plots = analyze('data/19/by_polling_stations.csv',
                    'Israel 19th Knesset Election')
    print '*** Generated', plots[0]
    print '*** Generated', plots[1]
