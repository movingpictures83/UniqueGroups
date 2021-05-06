
class UniqueGroupsPlugin:
    def input(self, filename):
       self.infile = open(filename, 'r')

    def run(self):
       self.groups = set()
       self.infile.readline()
       for line in self.infile:
          group = line.strip().split(',')
          self.groups.add(group[1])

    def output(self, filename):
        outfile = open(filename, 'w')
        for group in self.groups:
           outfile.write(group+"\n")
