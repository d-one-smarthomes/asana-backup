import json, sys

def fmt(json_path, project_name, gid, out_path):
    with open(json_path) as f:
        tasks = json.load(f)
    n = len(tasks)
    x = sum(1 for t in tasks if t.get('completed'))
    lines = []
    lines.append(f"# {project_name}")
    lines.append(f"**GID:** {gid}")
    lines.append(f"**Backed up:** 2026-07-11")
    lines.append("")
    lines.append(f"## Tasks ({n} total, {x} completed)")
    lines.append("")
    for t in tasks:
        icon = "✅" if t.get('completed') else "⬜"
        name = (t.get('name') or '').strip()
        lines.append(f"### {icon} {name}")
        assignee = t.get('assignee')
        aname = assignee['name'] if assignee else "Unassigned"
        lines.append(f"- **Assignee:** {aname}")
        due = t.get('due_on') or "None"
        lines.append(f"- **Due:** {due}")
        notes = t.get('notes') or ""
        notes = notes.strip()
        if notes:
            truncated = notes[:500]
            lines.append(f"- **Notes:** {truncated}")
        lines.append("")
    with open(out_path, 'w') as f:
        f.write("\n".join(lines))
    print(f"Wrote {out_path}: {n} total, {x} completed")

if __name__ == '__main__':
    json_path, project_name, gid, out_path = sys.argv[1:5]
    fmt(json_path, project_name, gid, out_path)
