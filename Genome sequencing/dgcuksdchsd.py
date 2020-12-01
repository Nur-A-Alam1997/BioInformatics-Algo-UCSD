def read_data_from(fileName):
    with open(fileName) as file:
#         peptide = file.readline().strip()
        spectrum = file.readline().strip().split()

    for i in range(len(spectrum)):
        spectrum[i] = int(spectrum[i])

    return spectrum

print(read_data_from("F:/python prog/BioPython/Genome sequencing/spect.txt"))