library(readr)
#library(doParallel)

#download.file("http://www.gutenberg.org/cache/epub/2000/pg2000.txt", "quijote.txt")
# system("tr '\r\n' ' '<quijote.txt>quijote.sed.txt
#       sed -i 's/\\s\\+/ /ig;s/[^a-zA-Z ]*//g;y/ABCDEFGHIJKLMNOPQRSTUVWXYZ/abcdefghijklmnopqrstuvwxyz/' quijote.sed.txt
#       tr ' ' '\n'<quijote.sed.txt>quijote.nl.txt;
#       sort -u<quijote.nl.txt>quijote.nl.tmp;
#       mv quijote.nl.tmp quijote.nl.txt")
raw = read_file_raw(file = "quijote.sed.txt")
raw = rawToChar(raw)
raw = tolower(raw)
raw = substr(raw, 0, 500)
print(raw)
ds = NULL
raw = read_lines("quijote.nl.txt")
long = length(raw)
for(i in 1:long) {
  #ds = data.frame(raw[i])
  ds = rbind(ds, c(raw[i], i))
  if((i %% 10000) == 0) {
    print(paste("Loading ", i, " out of ", long))
  }
  # if((i %% 15000) == 0) {
  #   ds = rbind(ds, c("erizados", i+1))
  #   break
  # }
}
#print(ds)
rm(raw, long, i)