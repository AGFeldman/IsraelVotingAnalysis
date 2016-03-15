class Row(object):
    def __init__(self, raw_row):
        self.city_name = raw_row[0]
        self.city_symbol = int(raw_row[1])
        # Most polling stations could be ints, but some are 37.1, 37.2, etc.
        self.polling_station = float(raw_row[2])
        self.registered_voters = int(raw_row[3])
        self.votes = int(raw_row[4])
        self.invalid_votes = int(raw_row[5])
        self.valid_votes = int(raw_row[6])
        assert self.valid_votes + self.invalid_votes == self.votes
        # Note that some polling stations are listed with 0 registered voters
        if self.registered_voters != 0 and self.votes > self.registered_voters:
            print 'WARNING:', self.votes, 'votes but only', self.registered_voters, 'registered voters'
        self.data = map(int, raw_row[7:])
        assert sum(self.data) == self.valid_votes

    def __getitem__(self, key):
        return self.data[key]

    def __len__(self):
        return len(self.data)


def get_rows(filename):
    with open(filename) as f:
        lines = f.readlines()
    # Strip header by considering only lines[1:]
    return [Row(line.strip().split(',')) for line in lines[1:]]


if __name__ == '__main__':
    # Quick test
    rows = get_rows('data/20/by_polling_stations.csv')
    # We should have 10414 rows of data
    assert len(rows) == 10414
    for row in rows:
        # Each row should have the vote count for each of the 26 parties
        assert len(row) == 26

    rows = get_rows('data/19/by_polling_stations.csv')
    assert len(rows) == 10109
    for row in rows:
        assert len(row) == 34

    rows = get_rows('data/18/by_polling_stations.csv')
    assert len(rows) == 9264
    for row in rows:
        assert len(row) == 34
