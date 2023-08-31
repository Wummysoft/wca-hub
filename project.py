```python
From project_database import ProjectDatabase

Class ProjectApp:
Def __init__(self):
Self.db = ProjectDatabase()

Def run(self):
While True:
Print(“1. Add Project”)
Print(“2. View Projects”)
Print(“3. Evaluate Project”)
Print(“4. Monitor Project”)
Print(“5. Exit”)
Choice = input(“Enter your choice: “)

If choice == “1”:
Self.add_project()
Elif choice == “2”:
Self.view_projects()
Elif choice == “3”:
Self.evaluate_project()
Elif choice == “4”:
Self.monitor_project()
Elif choice == “5”:
Break
Else:
Print(“Invalid choice. Please try again.”)

Def add_project(self):
Year = input(“Enter the year of implementation: “)
Local_government = input(“Enter the local government: “)
Community = input(“Enter the community: “)
Working_conditions = input(“Enter the working conditions: “)

Self.db.add_project(year, local_government, community, working_conditions)
Print(“Project added successfully!”)

Def view_projects(self):
Projects = self.db.get_projects()
For project in projects:
Print(project)

Def evaluate_project(self):
Project_id = input(“Enter the project ID: “)
Evaluation = input(“Enter the evaluation: “)

Self.db.evaluate_project(project_id, evaluation)
Print(“Project evaluation updated!”)

Def monitor_project(self):
Project_id = input(“Enter the project ID: “)
Status = input(“Enter the status: “)

Self.db.monitor_project(project_id, status)
Print(“Project status updated!”)

If __name__ == “__main__”:
App = ProjectApp()
App.run()
```
