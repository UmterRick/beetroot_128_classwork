class Journal:
    def __init__(self):
        self.records = []

    def add_record(self, record_data):
        self.records.append(record_data)



class Saver:
    ...


class JournalSaver(Saver):
    def save_to_file(self, journal, file_name):
        with open(file_name, 'w') as file:
            file.write(str(journal.records))


class ResportSaver(Saver):
    ...
