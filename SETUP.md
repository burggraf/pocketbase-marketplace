# Setup Guide

This guide will help you set up your PocketBase marketplace repository on GitHub and make it available for others to install.

## Prerequisites

- GitHub account
- Git installed locally
- GitHub CLI (recommended) or SSH keys configured

## Step 1: Update Configuration

Before publishing, update the following files with your information:

### 1. Update marketplace.json

Edit `.claude-plugin/marketplace.json`:

```json
{
  "name": "pocketbase-marketplace",
  "description": "Marketplace for PocketBase development skills...",
  "owner": {
    "name": "Your Name",
    "email": "your.email@example.com"
  },
  "plugins": [
    {
      "name": "pocketbase-migrations",
      "description": "...",
      "version": "1.0.0",
      "source": "./skills/pocketbase-migrations",
      "author": {
        "name": "Your Name",
        "email": "your.email@example.com"
      }
    }
  ]
}
```

### 2. Update plugin.json

Edit `.claude-plugin/plugin.json`:

```json
{
  "name": "pocketbase-migrations",
  "description": "...",
  "version": "1.0.0",
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com"
  },
  "homepage": "https://github.com/yourusername/pocketbase-marketplace",
  "repository": "https://github.com/yourusername/pocketbase-marketplace",
  "license": "MIT",
  "keywords": ["pocketbase", "migrations", "database", "collections", "api-rules", "schema"]
}
```

### 3. Update README.md

Replace `yourusername` with your actual GitHub username in the README.md file.

## Step 2: Create GitHub Repository

### Option A: Using GitHub CLI (Recommended)

```bash
# Navigate to your marketplace directory
cd pocketbase-marketplace

# Create repository on GitHub
gh repo create yourusername/pocketbase-marketplace --public --source=. --push

# Or create private first, then make public
gh repo create yourusername/pocketbase-marketplace --private --source=. --push
gh repo edit yourusername/pocketbase-marketplace --visibility public
```

### Option B: Using GitHub Web UI

1. Go to https://github.com/new
2. Repository name: `pocketbase-marketplace`
3. Description: `Marketplace for PocketBase development skills`
4. Choose Public (important for marketplace)
5. Don't initialize with README (we already have one)
6. Click "Create repository"
7. Follow the git commands shown to push your existing code

## Step 3: Verify Repository Structure

Your repository should look like this:

```
pocketbase-marketplace/
├── .claude-plugin/
│   ├── marketplace.json
│   └── plugin.json
├── skills/
│   └── pocketbase-migrations/
│       ├── SKILL.md
│       ├── scripts/
│       ├── references/
│       └── assets/
├── README.md
├── LICENSE
└── SETUP.md
```

## Step 4: Test Installation

Once your repository is public, test the installation:

```bash
# In Claude Code
/plugin marketplace add yourusername/pocketbase-marketplace
/plugin install pocketbase-migrations@pocketbase-marketplace
```

If everything works correctly, you should see the pocketbase-migrations skill available when you type `/help`.

## Step 5: Share Your Marketplace

You can now share your marketplace with others:

### Installation Commands for Users:

```bash
/plugin marketplace add yourusername/pocketbase-marketplace
/plugin install pocketbase-migrations@pocketbase-marketplace
```

### Share via:

1. **GitHub Repository Link**: Direct users to your repository
2. **Documentation**: Include installation commands in your README
3. **Community**: Share in PocketBase or Claude Code communities

## Step 6: Maintenance

### Updating Skills

When you update your pocketbase-migrations skill:

1. Update the version in `plugin.json`
2. Commit and push changes
3. Users can update with: `/plugin update pocketbase-migrations`

### Adding New Skills

To add more skills to your marketplace:

1. Create skill in `skills/your-new-skill/`
2. Update `marketplace.json` to include the new skill
3. Update README.md to document the new skill
4. Commit and push changes

## Troubleshooting

### "Plugin not found" Error

- Ensure your repository is public
- Check that the marketplace.json file is correct
- Verify the repository name matches what users are trying to install

### "Skill not activating" Error

- Check that SKILL.md has proper YAML frontmatter
- Ensure skill directory structure is correct
- Verify skill content in SKILL.md

### Permission Issues

- Make sure all files have correct permissions
- Check that scripts are executable if needed
- Verify repository is accessible

## Best Practices

1. **Semantic Versioning**: Use semantic versioning (1.0.0, 1.0.1, 1.1.0, 2.0.0)
2. **Changelog**: Keep a CHANGELOG.md file to track changes
3. **Testing**: Test skills thoroughly before publishing
4. **Documentation**: Keep README.md and skill documentation up to date
5. **Community**: Respond to issues and pull requests promptly

## Next Steps

Once your marketplace is set up:

1. Consider creating additional PocketBase-related skills
2. Solicit feedback from users
3. Watch for PocketBase updates that might affect your skills
4. Share your marketplace in PocketBase communities