from __future__ import division
from row import get_rows


def stats(filename, election_name):
    rows = get_rows(filename)
    n_0_registered = 0
    n_0_votes = 0
    n_0_either = 0
    for row in rows:
        if row.registered_voters == 0 and row.votes == 0:
            n_0_either += 1
        elif row.registered_voters == 0:
            n_0_registered += 1
        elif row.votes == 0:
            n_0_votes += 1
    print '*** Some stats for', election_name, ':'
    print '***    ', n_0_registered / len(rows) * 100, 'percent of polling'
    print '        stations reported 0 registered voters, but >0 votes'
    print '***    ', n_0_votes / len(rows) * 100, 'percent of polling'
    print '        stations reported 0 votes, but >0 registered voters'
    print '***    ', n_0_either / len(rows) * 100, 'percent of polling'
    print '        stations reported 0 votes and 0 registered voters'


if __name__ == '__main__':
    stats('data/20/by_polling_stations.csv', '20th election')
    stats('data/19/by_polling_stations.csv', '19th election')
    stats('data/18/by_polling_stations.csv', '18th election')
