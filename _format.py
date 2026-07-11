import json, sys

batch_file = sys.argv[1]
body_file = sys.argv[2]

with open(batch_file, 'r', encoding='utf-8') as f:
    tasks = json.load(f)

lines = []
for t in tasks:
    name = t.get('name') or '(untitled)'
    completed = t.get('completed', False)
    icon = '✅' if completed else '⬜'
    assignee = t.get('assignee')
    assignee_name = assignee.get('name') if assignee else 'Unassigned'
    due = t.get('due_on') or 'None'
    notes = t.get('notes') or ''
    notes = notes.strip()
    lines.append(f"### {icon} {name}")
    lines.append(f"- **Assignee:** {assignee_name}")
    lines.append(f"- **Due:** {due}")
    if notes:
        truncated = notes[:500]
        # keep notes on one logical block, escape nothing (markdown raw)
        lines.append(f"- **Notes:** {truncated}")
    lines.append("")

with open(body_file, 'a', encoding='utf-8') as f:
    f.write("\n".join(lines))
    f.write("\n")

print(f"Appended {len(tasks)} tasks. Total lines written: {len(lines)}")
