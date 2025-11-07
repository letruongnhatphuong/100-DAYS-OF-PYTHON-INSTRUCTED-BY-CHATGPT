def calculate_love_score(person1, person2):

    word1 = ["T", "R", "U", "E"]
    word2 = ["L", "O", "V", "E"]
    combine_name = (person1 + person2).upper()

    true_count = 0
    print("Counts for TRUE letters:")

    for char in word1:
        count1 = combine_name.count(char)
        print(f"{char} occurs {count1} time(s)")
        true_count += count1

    print(f"Total = {true_count}")

    love_count = 0
    print("\nCounts for LOVE letters:")

    for char in word2:
        count2 = combine_name.count(char)
        print(f"{char} occurs {count2} time(s)")
        love_count += count2
        
    print(f"Total = {love_count}")

    score = int(str(true_count) + str(love_count))
    print(f"Love score = {score}")

calculate_love_score("TRUE", "LOVE")