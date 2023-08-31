```python
Import sqlite3

Class ProjectDatabase:
Def __init__(self):
Self.conn = sqlite3.connect(‘project_data.db’)
Self.cursor = self.conn.cursor()
Self.create_table()

Def create_table(self):
Self.cursor.execute(‘’’
CREATE TABLE IF NOT EXISTS projects (
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Year INTEGER,
Local_government TEXT,
Community TEXT,
Working_conditions TEXT,
Evaluation TEXT,
Status TEXT
)
‘’’)
Self.conn.commit()

Def add_project(self, year, local_government, community, working_conditions):
Self.cursor.execute(‘’’
INSERT INTO projects (year, local_government, community, working_conditions)
VALUES (?, ?, ?, ?)
‘’’, (year, local_government, community, working_conditions))
Self.conn.commit()

Def get_projects(self):
Self.cursor.execute(‘SELECT * FROM projects’)
Projects = self.cursor.fetchall()
Return projects

Def evaluate_project(self, project_id, evaluation):
Self.cursor.execute(‘’’
UPDATE projects
SET evaluation = ?
WHERE id = ?
‘’’, (evaluation, project_id))
Self.conn.commit()

Def monitor_project(self, project_id, status):
Self.cursor.execute(‘’’
UPDATE projects
SET status = ?
WHERE id = ?
‘’’, (status, project_id))
Self.conn.commit()

Def __del__(self):
Self.conn.close()
```
