title = "|" + "{:^51}".format("Cereal Yields(kg/ha)")+"|"
line = "+" + "-"*15 + "+" + ("-"*8 + "+")*4
row = "| {:<13} |" + "{:6,d} |"*4
header = "| {:^13s} |".format("Country") + (" {:^6d} |"*4).format(1980, 1990, 2000, 2010)

print("+" + "-" * (len(title)-2)) + "+",
    title,
    line,
    header,
    line,
    row.format("China", 2937, 4321, 4752, 5527),
    row.format("Germany", 4225, 5411, 6453, 6718),
    row.format("United States", 3772, 4755, 5854, 6988),
    line,
    sep = "\n")
