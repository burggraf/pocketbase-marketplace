#!/usr/bin/env python3
"""
PocketBase Migration Generator

Helper script to generate valid PocketBase migration files.
Used by the skill to create properly formatted migration files.
"""

import os
import re
from datetime import datetime
from typing import Dict, List, Any, Optional

class MigrationGenerator:
    """Generate PocketBase migration files with proper formatting."""

    def __init__(self):
        self.field_types = {
            'text', 'email', 'url', 'number', 'bool', 'date', 'datetime',
            'select', 'relation', 'file', 'json'
        }

    def validate_collection_name(self, name: str) -> bool:
        """Validate collection name according to PocketBase conventions."""
        if not name:
            return False

        # Must start with letter, contain only lowercase letters, numbers, underscores
        pattern = r'^[a-z][a-z0-9_]*$'

        # Check against reserved names
        reserved = {'id', 'created', 'updated'}

        return (bool(re.match(pattern, name)) and
                name not in reserved and
                len(name) <= 255)

    def validate_field_name(self, name: str) -> bool:
        """Validate field name according to PocketBase conventions."""
        if not name:
            return False

        # Must start with letter, contain only lowercase letters, numbers, underscores
        pattern = r'^[a-z][a-z0-9_]*$'

        # Check against reserved names
        reserved = {'id', 'created', 'updated'}

        return (bool(re.match(pattern, name)) and
                name not in reserved and
                len(name) <= 255)

    def generate_field_id(self) -> str:
        """Generate a unique field ID."""
        return f"field_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    def generate_collection_id(self) -> str:
        """Generate a unique collection ID."""
        return f"collection_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    def create_field(self, name: str, field_type: str, required: bool = False,
                    options: Optional[Dict[str, Any]] = None, unique: bool = False,
                    presentable: bool = False) -> Dict[str, Any]:
        """Create a field definition."""
        if not self.validate_field_name(name):
            raise ValueError(f"Invalid field name: {name}")

        if field_type not in self.field_types:
            raise ValueError(f"Invalid field type: {field_type}")

        field = {
            "id": self.generate_field_id(),
            "name": name,
            "type": field_type,
            "required": required,
            "presentable": presentable,
            "unique": unique,
            "options": options or {}
        }

        # Add default options based on field type
        if field_type == 'text':
            field["options"] = {
                "min": 1,
                "max": 200,
                "pattern": ""
            }
        elif field_type == 'email':
            field["options"] = {}
        elif field_type == 'number':
            field["options"] = {
                "min": None,
                "max": None
            }
        elif field_type == 'select':
            field["options"] = {
                "maxSelect": 1,
                "values": []
            }
        elif field_type == 'relation':
            field["options"] = {
                "collectionId": "",
                "maxSelect": 1,
                "cascadeDelete": False
            }
        elif field_type == 'file':
            field["options"] = {
                "maxSelect": 1,
                "maxSize": 5242880,
                "mimeTypes": [],
                "thumbs": None
            }

        # Override with provided options
        if options:
            field["options"].update(options)

        return field

    def generate_migration_file(self, collection_name: str, fields: List[Dict[str, Any]],
                              api_rules: Dict[str, str], collection_type: str = "base",
                              existing_migration_path: Optional[str] = None,
                              migrations_dir: str = "pb_migrations") -> str:
        """Generate a complete migration file content."""
        if not self.validate_collection_name(collection_name):
            raise ValueError(f"Invalid collection name: {collection_name}")

        if existing_migration_path:
            return self._generate_modify_migration(collection_name, fields, api_rules)
        else:
            return self._generate_create_migration(collection_name, fields, api_rules, collection_type)

    def save_migration_file(self, migration_content: str, collection_name: str,
                           migrations_dir: str = "pb_migrations") -> str:
        """Save migration file to the pb_migrations directory."""
        import os

        # Ensure migrations directory exists
        if not os.path.exists(migrations_dir):
            os.makedirs(migrations_dir)

        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_create_{collection_name}.js"
        filepath = os.path.join(migrations_dir, filename)

        # Write migration file
        with open(filepath, 'w') as f:
            f.write(migration_content)

        return filepath

    def _generate_create_migration(self, collection_name: str, fields: List[Dict[str, Any]],
                                 api_rules: Dict[str, str], collection_type: str) -> str:
        """Generate a migration for creating a new collection."""
        collection_id = self.generate_collection_id()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.000Z")

        schema = ",\n".join([f"      {field}" for field in fields])

        migration = f'''/// <reference path="../pb_data/types.d.ts" />

migrate((db) => {{
  const collection = new Collection({{
    id: "{collection_id}",
    created: new Date("{timestamp}"),
    updated: new Date("{timestamp}"),
    name: "{collection_name}",
    type: "{collection_type}",
    system: false,
    schema: [
{schema}
    ],
    indexes: [],
    listRule: "{api_rules.get('list', '@request.auth.id != ""')}",
    viewRule: "{api_rules.get('view', '@request.auth.id != ""')}",
    createRule: "{api_rules.get('create', '@request.auth.id != ""')}",
    updateRule: "{api_rules.get('update', '@request.auth.id != "" && @request.auth.id = owner')}",
    deleteRule: "{api_rules.get('delete', '@request.auth.id != "" && @request.auth.id = owner')}",
    options: {{}}
  }});

  return Dao(db).saveCollection(collection);
}}, (db) => {{
  const dao = new Dao(db);
  dao.deleteCollection("{collection_name}");
}});'''

        return migration

    def _generate_modify_migration(self, collection_name: str, fields: List[Dict[str, Any]],
                                 api_rules: Dict[str, str]) -> str:
        """Generate a migration for modifying an existing collection."""
        schema = ",\n".join([f"    collection.schema.addField({field});" for field in fields])

        migration = f'''/// <reference path="../pb_data/types.d.ts" />

migrate((db) => {{
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("{collection_name}");

{schema}

  // Update API rules if provided
  collection.listRule = "{api_rules.get('list', collection.listRule)}";
  collection.viewRule = "{api_rules.get('view', collection.viewRule)}";
  collection.createRule = "{api_rules.get('create', collection.createRule)}";
  collection.updateRule = "{api_rules.get('update', collection.updateRule)}";
  collection.deleteRule = "{api_rules.get('delete', collection.deleteRule)}";

  return dao.saveCollection(collection);
}}, (db) => {{
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("{collection_name}");

  // Remove fields (rollback logic)
{self._generate_rollback_fields(fields)}

  return dao.saveCollection(collection);
}});'''

        return migration

    def _generate_rollback_fields(self, fields: List[Dict[str, Any]]) -> str:
        """Generate rollback field removal code."""
        removals = []
        for field in fields:
            field_name = field.get('name', 'unknown')
            removals.append(f'  collection.schema.removeField("{field_name}_field_id");')

        return "\n".join(removals)

    def generate_delete_migration(self, collection_name: str) -> str:
        """Generate a migration for deleting a collection."""
        migration = f'''/// <reference path="../pb_data/types.d.ts" />

migrate((db) => {{
  const dao = new Dao(db);

  // Delete the {collection_name} collection
  dao.deleteCollection("{collection_name}");
}}, (db) => {{
  // Rollback - recreate the collection
  // Note: You'll need to manually specify the collection schema for rollback
  const collection = new Collection({{
    id: "{self.generate_collection_id()}",
    created: new Date("{datetime.now().strftime('%Y-%m-%d %H:%M:%S.000Z')}"),
    updated: new Date("{datetime.now().strftime('%Y-%m-%d %H:%M:%S.000Z')}"),
    name: "{collection_name}",
    type: "base",
    system: false,
    schema: [
      // Add back your fields here
    ],
    indexes: [],
    listRule: "@request.auth.id != \\"\"",
    viewRule: "@request.auth.id != \\"\"",
    createRule: "@request.auth.id != \\"\"",
    updateRule: "@request.auth.id != \\"\" && @request.auth.id = owner",
    deleteRule: "@request.auth.id != \\"\" && @request.auth.id = owner",
    options: {{}}
  }});

  return Dao(db).saveCollection(collection);
}});'''

        return migration


def main():
    """Example usage of the migration generator."""
    generator = MigrationGenerator()

    # Example: Create a users collection
    try:
        fields = [
            generator.create_field("name", "text", required=True, options={"max": 100}),
            generator.create_field("email", "email", required=True),
            generator.create_field("age", "number", required=False, options={"min": 0, "max": 150}),
            generator.create_field("is_active", "bool", required=False)
        ]

        api_rules = {
            "list": "public",
            "view": "public",
            "create": "@request.auth.id != \"\"",
            "update": "@request.auth.id != \"\" && @request.auth.id = owner",
            "delete": "@request.auth.id != \"\" && @request.auth.id = owner"
        }

        migration = generator.generate_migration_file("users", fields, api_rules)
        filepath = generator.save_migration_file(migration, "users")
        print(f"Migration saved to: {filepath}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()