library(readr)
#library(doParallel)

download.file("http://www.gutenberg.org/cache/epub/2000/pg2000.txt", "quijote.txt")
raw = read_file_raw(file = "quijote.txt")
