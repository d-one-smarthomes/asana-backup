#!/usr/bin/env python3
"""Convert Asana task JSON to formatted markdown."""
import json, sys, os
from datetime import datetime

def fmt_date(d):
    if not d: return None
    try:
        return datetime.fromisoformat(d.replace('Z','+00:00')).strftime('%Y-%m-%d')
    except:
        return d[:10] if len(d)>=10 else d

def task_to_md(task, depth=3):
    hashes = '#' * depth
    name = (task.get('name') or '').strip()
    if not name:
        return ''
    completed = task.get('completed', False)
    icon = '✅' if completed else '🔲'
    lines = [f"{hashes} {icon} {name}"]
    assignee = task.get('assignee') or {}
    if assignee.get('name'):
        lines.append(f"**Assignee:** {assignee['name']}")
    due = fmt_date(task.get('due_on'))
    if due:
        lines.append(f"**Due:** {due}")
    comp_at = fmt_date(task.get('completed_at'))
    if comp_at:
        lines.append(f"**Completed:** {comp_at}")
    notes = (task.get('notes') or '').strip()
    if notes:
        lines.append('')
        lines.append(notes)
    subtasks = task.get('subtasks', []) or []
    for st in subtasks:
        st_md = task_to_md(st, depth+1)
        if st_md:
            lines.append('')
            lines.append(st_md)
    return '\n'.join(lines)

def tasks_to_md(project_name, project_notes, tasks, export_date='2026-07-03'):
    sections = {}
    section_order = []
    for task in tasks:
        memberships = task.get('memberships', []) or []
        section = '(no section)'
        if memberships:
            sec = memberships[0].get('section', {})
            section = (sec.get('name') or '(no section)') if sec else '(no section)'
        if section not in sections:
            sections[section] = []
            section_order.append(section)
        sections[section].append(task)
    
    lines = [f"# {project_name}", f"*Exported: {export_date}*"]
    if project_notes:
        lines.append('')
        lines.append('## Project Notes')
        lines.append('')
        lines.append(project_notes.strip())
    
    for section in section_order:
        lines.append('')
        label = section if section != '(no section)' else 'General'
        lines.append(f"## {label}")
        for task in sections[section]:
            lines.append('')
            md = task_to_md(task, 3)
            if md:
                lines.append(md)
            lines.append('')
            lines.append('---')
    
    return '\n'.join(lines)

if __name__ == '__main__':
    json_file = sys.argv[1]
    out_file = sys.argv[2]
    project_name = sys.argv[3]
    notes_file = sys.argv[4] if len(sys.argv) > 4 else None
    project_notes = ''
    if notes_file and os.path.exists(notes_file):
        with open(notes_file) as f:
            project_notes = f.read()
    
    with open(json_file) as f:
        tasks = json.load(f)
    
    md = tasks_to_md(project_name, project_notes, tasks)
    with open(out_file, 'w') as f:
        f.write(md)
    print(f"Written {len(tasks)} tasks -> {out_file} ({os.path.getsize(out_file):,} bytes)")
