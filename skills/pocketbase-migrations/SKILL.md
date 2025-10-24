---
name: pocketbase-migrations
description: This skill should be used when the user mentions creating, modifying, or managing PocketBase collections, migrations, or database schema changes. It handles creating new collections, adding/removing fields, managing API rules, and generating proper migration files for PocketBase projects.
---

# PocketBase Migrations

## Overview

This skill enables comprehensive management of PocketBase database migrations, allowing you to create new collections, modify existing ones, manage fields, and configure API access rules. It generates properly formatted JavaScript migration files that can be executed with `pocketbase migrate`.

## Quick Start

Use this skill when you hear phrases like:
- "Create a migration for..."
- "Add a field to collection..."
- "Modify the collection..."
- "Delete collection..."
- "Set API rules for..."
- "Generate migration files..."

## Migration Operations

### 1. Create New Collection

To create a new collection:
1. Validate collection name follows PocketBase conventions
2. Define fields with appropriate types and validation
3. Set API rules for CRUD operations
4. Generate migration file with proper schema
5. Save to pb_migrations directory

**Example Request**: "Create a users collection with name (text), email (email), and is_active (bool) fields"

### 2. Add Fields to Existing Collection

To add fields to an existing collection:
1. Locate existing collection in pb_migrations directory
2. Define new fields with types and validation
3. Generate modify migration with field additions
4. Preserve existing API rules or update as needed

**Example Request**: "Add a status field to the posts collection"

### 3. Remove Fields from Collection

To remove fields from an existing collection:
1. Identify collection and target fields
2. Generate modify migration with field removals
3. Include rollback logic to restore fields
4. Test migration safely

**Example Request**: "Remove the old_category field from the articles collection"

### 4. Delete Collection

To delete a collection:
1. Verify collection exists and can be safely deleted
2. Warn about potential data loss
3. Generate delete migration with rollback capability
4. Confirm deletion with user

**Example Request**: "Delete the deprecated_comments collection"

### 5. Update API Rules

To modify collection API rules:
1. Understand access requirements (public, authenticated, owner, admin)
2. Define rules for list, view, create, update, delete operations
3. Generate migration with updated rule configuration
4. Follow security best practices

**Example Request**: "Set API rules for posts collection: public read, owner write"

## Field Types and Validation

### Supported Field Types
- **Text**: Basic text with min/max length and pattern validation
- **Email**: Email format validation
- **Number**: Numeric values with min/max constraints
- **Boolean**: True/false values
- **Date**: Date fields (YYYY-MM-DD)
- **DateTime**: Date and time fields
- **URL**: URL format validation
- **JSON**: Structured JSON data
- **Select**: Single or multiple selection from predefined values
- **Relation**: Foreign key relationships to other collections
- **File**: File uploads with size and type restrictions

### Field Validation Patterns
- Required fields: `{"required": true}`
- Text constraints: `{"min": 1, "max": 100}`
- Number ranges: `{"min": 0, "max": 1000}`
- Select options: `{"values": ["option1", "option2"]}`

## API Rule Templates

### Common Rule Patterns
- **Public Access**: `"public"`
- **Authenticated Users**: `"@request.auth.id != \"\""`
- **Owner Only**: `"@request.auth.id != \"\" && @request.auth.id = owner"`
- **Admin Only**: `"@request.auth.role = \"admin\""`
- **Role-Based**: `"@request.auth.role in [\"admin\", \"editor\"]"`

### Security Best Practices
1. Apply principle of least privilege
2. Use owner checks for user-generated content
3. Separate read/write permissions when appropriate
4. Always include rollback logic in migrations

## Migration File Structure

### Create Collection Template
```javascript
/// <reference path="../pb_data/types.d.ts" />

migrate((db) => {
  const collection = new Collection({
    // Collection configuration
  });
  return Dao(db).saveCollection(collection);
}, (db) => {
  // Rollback logic
});
```

### Modify Collection Template
```javascript
/// <reference path="../pb_data/types.d.ts" />

migrate((db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("collection_name");

  // Add fields, update rules
  return dao.saveCollection(collection);
}, (db) => {
  // Rollback modifications
});
```

## Validation and Safety Checks

### Before Creating Migrations
1. **Check pb_migrations directory exists** - If not, ask user for correct location
2. **Validate collection/field names** - Follow PocketBase naming conventions
3. **Check for existing migrations** - Prevent conflicts and overwrites
4. **Validate field types and options** - Ensure compatibility with PocketBase
5. **Review API rules** - Verify security implications

### Naming Conventions
- Collections: lowercase, snake_case, start with letter
- Fields: lowercase, snake_case, start with letter
- Avoid reserved names: `id`, `created`, `updated`
- Maximum length: 255 characters

## File Management

### Migration File Location
- **ALWAYS** use: `pb_migrations/` directory in PocketBase project root
- If directory doesn't exist, create it or ask user for correct path
- Generate files with descriptive names and timestamps (e.g., `20251024_143022_create_people.js`)

### Migration Workflow
1. **Verify pb_migrations directory exists** in project root
2. Generate migration file in pb_migrations directory
3. Review generated file for accuracy
4. Run migration with `pocketbase migrate`
5. Verify changes in PocketBase admin panel

### IMPORTANT: File Location Rules
- **NEVER** create migration files inside the skill directory
- **ALWAYS** use the project's `pb_migrations/` directory
- Migration files should be at the same level as `pb_data/` directory
- Follow PocketBase's standard migration file naming convention

## Resources

### scripts/migration_generator.py
Python script for generating properly formatted PocketBase migration files. Contains field validation, ID generation, and migration file creation logic.

### references/field_types.md
Comprehensive reference for all PocketBase field types, their configuration options, and validation patterns.

### references/api_rules.md
Detailed guide for PocketBase API rules including common patterns, security best practices, and rule syntax.

### assets/example_migrations.md
Collection of complete migration examples showing create, modify, and delete operations with real-world scenarios.

### assets/field_examples.md
Field definition examples for all supported field types with configuration options.

### assets/create_collection_template.js
Template for creating new collections with proper structure and placeholder values.