'''
Day 2: Red-Nosed Reports

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:


'''

def is_safe_report(report):
    if len(report) == 1:
        return True
    
    # Determine if the report is increasing or decreasing
    increasing = report[0] < report[1]
    
    for i in range(len(report) - 1):
        # Check if the sequence is consistent (either all increasing or all decreasing)
        if (increasing and report[i] >= report[i + 1]) or (not increasing and report[i] <= report[i + 1]):
            return False
        # Check if adjacent levels differ by at least 1 and at most 3
        if abs(report[i + 1] - report[i]) > 3 or abs(report[i + 1] - report[i]) < 1:
            return False
            
    return True

def main():
    #file = 'example2.txt'
    file = 'input.txt'
    with open(file) as f:
        reports = [list(map(int, line.strip().split())) for line in f]
    safe_reports = [report for report in reports if is_safe_report(report)]
    print(len(safe_reports))



# Part 2 
'''
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:


'''


def is_safe_report2(report):
    def check_safe(report):
        if len(report) == 1:
            return True
        
        increasing = report[0] < report[1]
        
        for i in range(len(report) - 1):
            # Check if the sequence is consistent (either all increasing or all decreasing)
            if (increasing and report[i] >= report[i + 1]) or (not increasing and report[i] <= report[i + 1]):
                return False
            # Check if adjacent levels differ by at least 1 and at most 3
            if abs(report[i + 1] - report[i]) > 3 or abs(report[i + 1] - report[i]) < 1:
                return False
        return True

    # First, check if the report is already safe
    if check_safe(report):
        return True

    # Otherwise, check if removing one level makes it safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]  # Remove the i-th level
        if check_safe(modified_report):
            return True

    return False

def main2():
    #file = 'example2.txt'
    file = 'input.txt'
    with open(file) as f:
        reports = [list(map(int, line.strip().split())) for line in f]
    safe_reports = [report for report in reports if is_safe_report2(report)]
    print(len(safe_reports))


if __name__ == '__main__':
    main()
    main2()
