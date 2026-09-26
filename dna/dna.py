import csv
import sys


def main():
    if len(sys.argv) == 3:
        file_database = open("./" + sys.argv[1])
        file_dnasequence = open("./" + sys.argv[2]).read()
        reader_data = csv.DictReader(file_database)
        #Leer cada STR del archivo csv
        STR_csv = reader_data.fieldnames[1:]
        #Crear lista con cada valor de las repeticiones del STR
        i = 0
        for STR in STR_csv:
            i += 1
        for row in reader_data:
            counter = 0
            for STR in STR_csv:
                a = longest_match(file_dnasequence, STR)
                b = int(row[STR])
                if a == b:
                    counter = counter + 1
                if counter == i:
                    print(f"{row['name']}")
                    return
        print("No match")

    else:
        print("ERROR")
        return 0

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
