import re

# Customize your target locations and keywords here
TARGET_LOCATIONS = ["New York", "Remote", "Boston", "NJ", "Canada"]
TARGET_KEYWORDS = ["Fall", "2026", "Intern", "Consulting"] 

def filter_markdown_table(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    filtered_rows = []
    header_found = False
    
    for line in lines:
        # Find the table header row
        if "| Company | Job Title | Location |" in line or "| *Company*" in line:
            header_found = True
            filtered_rows.append(line)
            continue
        
        if header_found and line.startswith("|"):
            # Keep the table formatting row (e.g., | --- | --- |)
            if "---" in line:
                filtered_rows.append(line)
                continue
                
            columns = [col.strip() for col in line.split("|")]
            if len(columns) < 5:
                continue
                
            job_title = columns[2]
            location = columns[3]
            
            # Match against your preferred locations and keywords
            match_location = any(loc.lower() in location.lower() for loc in TARGET_LOCATIONS)
            match_keyword = any(kw.lower() in job_title.lower() for kw in TARGET_KEYWORDS)
            
            if match_location and match_keyword:
                filtered_rows.append(line)
        else:
            # Keep the rest of the file structure intact
            if not header_found:
                filtered_rows.append(line)

    # Output to a new custom file
    with open('FILTERED_README.md', 'w', encoding='utf-8') as f:
        f.writelines(filtered_rows)
        
    print("Filtered list successfully saved to FILTERED_README.md!")

if __name__ == "__main__":
    filter_markdown_table('README.md')