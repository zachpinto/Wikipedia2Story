import re
import csv

def parse_markdown_file_to_csv(file_path, output_csv_path):
    # Regular expressions for matching categories and extracting topics
    category_patterns = {
        1: re.compile(r'^=([^=]+)=$'),
        2: re.compile(r'^==([^=]+)==$'),
        3: re.compile(r'^===([^=]+)===$'),
        4: re.compile(r'^====([^=]+)====$'),
        5: re.compile(r'^=====([^=]+)=====$'),
    }
    link_pattern = re.compile(r'\[\[([^]]+)\]\]')

    # Initialize the parent chain for categories and topics
    category_chain = []
    topic_chain = [''] * 6  # up to level 5 of topics (# to ####)
    results = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            # Check for category changes
            for level, pattern in sorted(category_patterns.items()):
                match = pattern.match(line)
                if match:
                    category_name = match.group(1).strip()
                    # Adjust the category chain to current category depth
                    category_chain = category_chain[:level-1] + [category_name]
                    # Reset topic chain from this level onward when category changes
                    topic_chain = [''] * 6
                    break
            else:
                # Process topic lines
                topic_match = re.search(link_pattern, line)
                if topic_match:
                    topic_name = topic_match.group(1)
                    topic_level = len(re.match(r'^(#+)', line).group(0))  # count # to determine the level
                    topic_chain[topic_level] = topic_name  # update the current level's topic name

                    # Build the parent chain using categories and applicable topics
                    parent_chain = category_chain + [name for name in topic_chain[1:topic_level] if name]
                    results.append((topic_name, ' > '.join(parent_chain)))

    # Write to CSV
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Topic', 'Parent Chain'])
        for topic, chain in results:
            writer.writerow([topic, chain])


file_path = "../../data/raw/wikipedia_pages.md"
output_csv_path = "../../data/interim/pages.csv"
parse_markdown_file_to_csv(file_path, output_csv_path)
