import re
import csv

def parse_markdown_file_to_csv(file_path, output_csv_path):
    # Regex for matching categories and extracting topics
    category_patterns = {
        1: re.compile(r'^=([^=]+)=$'),
        2: re.compile(r'^==([^=]+)==$'),
        3: re.compile(r'^===([^=]+)===$'),
        4: re.compile(r'^====([^=]+)====$'),
        5: re.compile(r'^=====([^=]+)=====$'),
    }
    link_pattern = re.compile(r'\[\[([^]]+)\]\]')

    # Initialize variables
    category_chain = []
    topic_chain = [''] * 6
    results = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            # Check for category changes
            for level, pattern in sorted(category_patterns.items()):
                match = pattern.match(line)
                if match:
                    category_name = match.group(1).strip()
                    category_chain = category_chain[:level-1] + [category_name]
                    topic_chain = [''] * 6
                    break
            else:
                # Process topic lines
                topic_match = re.search(link_pattern, line)
                if topic_match:
                    topic_name = topic_match.group(1)
                    topic_level = len(re.match(r'^(#+)', line).group(0))
                    topic_chain[topic_level] = topic_name
                    parent_chain = category_chain + [name for name in topic_chain[1:topic_level] if name]
                    results.append((topic_name, ' > '.join(parent_chain)))

    # Write to CSV
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Topic', 'Parent Chain'])
        for topic, chain in results:
            writer.writerow([topic, chain])


# Parse the Wikipedia pages from the markdown file and write to a CSV file
file_path = "../../data/raw/wikipedia_pages.md"
output_csv_path = "../../data/interim/pages.csv"
parse_markdown_file_to_csv(file_path, output_csv_path)
