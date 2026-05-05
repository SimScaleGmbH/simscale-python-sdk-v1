#!/usr/bin/env python
"""Folders & Spaces example using the SimScale SDK v1."""

from simscale_sdk_v1 import SimScaleSDK, models

sdk = SimScaleSDK()

# Get info about the user Personal Space
user_spaces = sdk.spaces.get_user_spaces()
personal_space_id = user_spaces.personal_spaces[0].space_id
personal_space_info = sdk.spaces.get_space_info(personal_space_id)
print(f"Personal Space ID: {personal_space_id} - Space info: {personal_space_info}")

# Create Folders in the Space root
folder_a = sdk.folders.create_folder(personal_space_id, models.Folder(name="Folder A"))
print(f"Created a folder with ID '{folder_a.folder_id}' and name '{folder_a.name}' in the Space root")

folder_b = sdk.folders.create_folder(personal_space_id, models.Folder(name="Folder B"))
print(f"Created a folder with ID '{folder_b.folder_id}' and name '{folder_b.name}' in the Space root")

# Create a Project in the Space root
project_a = sdk.projects.create_project(
    models.Project(
        name="Project A",
        description="Project in Space root",
        measurement_system="SI",
        space_id=personal_space_id,
    ),
)
print(f"Created a project with ID '{project_a.project_id}' and name '{project_a.name}' in the Space root")

# Create a Project inside Folder A
project_b = sdk.projects.create_project(
    models.Project(
        name="Project B",
        description="Project in Folder A",
        measurement_system="SI",
        space_id=personal_space_id,
        parent_folder_id=folder_a.folder_id,
    ),
)
print(f"Created a project with ID '{project_b.project_id}' and name '{project_b.name}' inside Folder A")

# Create a Folder inside Folder A
folder_c = sdk.folders.create_folder(
    personal_space_id, models.Folder(name="Folder C", parent_folder_id=folder_a.folder_id)
)
print(f"Created a folder with ID '{folder_c.folder_id}' and name '{folder_c.name}' inside Folder A")

# Rename Folder C
folder_c = sdk.folders.update_folder(personal_space_id, folder_c.folder_id, models.Folder(name="New name for Folder C"))
print(f"Updated folder with ID '{folder_c.folder_id}'. New name: '{folder_c.name}'")

# List the contents of the Space root
folders_in_space_root = sdk.folders.list_folders_in_space_root(personal_space_id)
print(f"Folders in Space root: {folders_in_space_root.total} (e.g. {folders_in_space_root.embedded[0].name})")

projects_in_space_root = sdk.folders.list_projects_in_space_root(personal_space_id)
print(f"Projects in Space root: {projects_in_space_root.total} (e.g. {projects_in_space_root.embedded[0].name})")

# List the contents of Folder A
folders_in_folder = sdk.folders.list_folders_in_folder(personal_space_id, folder_a.folder_id)
print(f"Number of folders in Folder A: {folders_in_folder.total} - Folders: {folders_in_folder.embedded}")

projects_in_folder = sdk.folders.list_projects_in_folder(personal_space_id, folder_a.folder_id)
print(f"Number of projects in Folder A: {projects_in_folder.total} - Projects: {projects_in_folder.embedded}")

# Move content from the Space root to Folder B
sdk.folders.move_content_from_space_root(
    personal_space_id,
    models.MoveContentRequest(
        entries=[
            models.ResourceToMove(project_id=project_a.project_id),
            models.ResourceToMove(folder_id=folder_a.folder_id),
        ],
        to=models.ResourceLocation(space_id=personal_space_id, parent_folder_id=folder_b.folder_id),
    ),
)
print("Moved Project A and Folder A into Folder B")

# Move content from Folder A to the Space root
sdk.folders.move_content_from_folder(
    personal_space_id,
    folder_a.folder_id,
    models.MoveContentRequest(
        entries=[
            models.ResourceToMove(project_id=project_b.project_id),
            models.ResourceToMove(folder_id=folder_c.folder_id),
        ],
        to=models.ResourceLocation(space_id=personal_space_id),
    ),
)
print("Moved Project B and Folder C back to Space root")

# Clean up — delete everything we created
sdk.folders.delete_folder(personal_space_id, folder_c.folder_id)
print("Deleted Folder C")

# Move Project B into Folder B so we can delete everything in one go
sdk.folders.move_content_from_space_root(
    personal_space_id,
    models.MoveContentRequest(
        entries=[models.ResourceToMove(project_id=project_b.project_id)],
        to=models.ResourceLocation(space_id=personal_space_id, parent_folder_id=folder_b.folder_id),
    ),
)
sdk.folders.delete_folder(personal_space_id, folder_b.folder_id)
print("Deleted Folder B and all remaining content")

print("\nDone!")
