# PocketBase Skills Marketplace

A comprehensive marketplace for PocketBase development skills, providing specialized tools for database migrations, collection management, and API rule configuration.

## What You Get

- **PocketBase Migrations Skill** - Complete database schema management
- **Collection Management** - Create, modify, and delete collections
- **Field Management** - Add, remove, and configure field types
- **API Rules Configuration** - Set up secure access controls
- **Migration Generation** - Automated migration file creation

## Installation

### Via Plugin Marketplace (Recommended)

```bash
# In Claude Code
/plugin marketplace add burggraf/pocketbase-marketplace
/plugin install pocketbase-migrations@pocketbase-marketplace
```

### Verify Installation

```bash
# Check that the skill appears
/help

# You should see pocketbase-migrations in the available skills
```

## Quick Start

The pocketbase-migrations skill activates automatically when you mention:

- "Create a migration for..."
- "Add a field to collection..."
- "Modify the collection..."
- "Delete collection..."
- "Set API rules for..."
- "Generate migration files..."

### Example Usage

**Create a new collection:**
```
Create a users collection with name (text), email (email), and is_active (bool) fields
```

**Add a field to existing collection:**
```
Add a status field to the posts collection
```

**Set API rules:**
```
Set API rules for posts collection: public read, owner write
```

## What's Inside

### PocketBase Migrations Skill

Located in `skills/pocketbase-migrations/`, this skill provides:

**Migration Operations:**
- Create new collections with field definitions
- Add/remove fields from existing collections
- Delete collections with safety checks
- Update API rules for security
- Generate properly formatted migration files

**Field Types Support:**
- Text, Email, Number, Boolean
- Date, DateTime, URL, JSON
- Select, Relation, File
- Field validation and constraints

**API Rule Templates:**
- Public access
- Authenticated users
- Owner-only access
- Role-based permissions
- Security best practices

**File Structure:**
- `SKILL.md` - Complete skill documentation
- `scripts/migration_generator.py` - Migration generation script
- `references/` - Field types and API rules reference
- `assets/` - Examples and templates

## How It Works

1. **Automatic Detection** - Claude detects PocketBase-related requests
2. **Skill Activation** - pocketbase-migrations skill activates automatically
3. **Interactive Process** - Guides you through migration creation
4. **File Generation** - Creates migration files in your project's `pb_migrations/` directory
5. **Safety Checks** - Validates names, types, and API rules

## Requirements

- PocketBase project initialized
- `pb_migrations/` directory in project root
- Python 3.6+ (for migration generation script)

## Project Structure

```
pocketbase-marketplace/
├── .claude-plugin/
│   ├── marketplace.json    # Marketplace configuration
│   └── plugin.json         # Plugin metadata
├── skills/
│   └── pocketbase-migrations/
│       ├── SKILL.md        # Main skill documentation
│       ├── scripts/        # Generation scripts
│       ├── references/     # Reference documentation
│       └── assets/         # Examples and templates
└── README.md               # This file
```

## Usage Examples

### Creating Collections

```
Create a blog posts collection with:
- title (text, required, max 200 chars)
- content (text, required)
- published (bool, default false)
- author_id (relation to users collection)
- created_at (datetime)
```

### Managing Fields

```
Add a category field to the posts collection
Make it a select field with values: ["tech", "lifestyle", "business"]
```

### Setting API Rules

```
Configure API rules for posts:
- List: public
- View: public
- Create: authenticated users
- Update: author only
- Delete: author only
```

## File Locations

**IMPORTANT:** Migration files are ALWAYS created in your project's `pb_migrations/` directory, not in the skill directory.

## Contributing

To add new skills to this marketplace:

1. Fork this repository
2. Create your skill in `skills/your-skill-name/`
3. Follow the skill creation guidelines
4. Update `marketplace.json` to include your skill
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

- **Issues**: https://github.com/burggraf/pocketbase-marketplace/issues
- **PocketBase Documentation**: https://pocketbase.io/docs/

## Related Projects

- [PocketBase](https://github.com/pocketbase/pocketbase) - Open source backend
- [Superpowers](https://github.com/obra/superpowers) - Claude Code skills library