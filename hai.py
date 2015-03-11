# Tkinter displaying terminal output
# grab the output of the program and insert it into the text widget with something like
p = sub.Popen('./script',stdout=sub.PIPE,stderr=sub.PIPE)
output, errors = p.communicate()
self.text.insert("end", output)
