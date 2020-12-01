with open('F:/python prog/BioPython/Genome sequencing/ggg.txt') as input_data:
    spec = map(int, input_data.read().strip().split())

# The spectrum isn't sorted, so find all differences and filter out the non-positive.
convolution = [str(i-j) for i in spec for j in spec if i-j > 0]

# Print and save the answer.
print (' '.join(convolution))
with open('Textbook_02F.txt', 'w') as output_data:
    output_data.write(' '.join(convolution))