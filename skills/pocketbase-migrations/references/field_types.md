# PocketBase Field Types Reference

## Basic Field Types

### Text (`text`)
- Basic text field for storing strings
- Options: `required`, `min`, `max`, `pattern`
- Example validation: `{ "required": true, "min": 3, "max": 100 }`

### Number (`number`)
- Numeric field for integers and decimals
- Options: `required`, `min`, `max`
- Example validation: `{ "required": true, "min": 0, "max": 1000 }`

### Boolean (`bool`)
- True/false field
- Options: `required`
- Example validation: `{ "required": true }`

### Date (`date`)
- Date field (YYYY-MM-DD format)
- Options: `required`, `min`, `max`
- Example validation: `{ "required": true, "min": "2024-01-01" }`

### DateTime (`datetime`)
- Date and time field
- Options: `required`, `min`, `max`
- Example validation: `{ "required": true }`

### Email (`email`)
- Email field with automatic validation
- Options: `required`
- Example validation: `{ "required": true }`

### URL (`url`)
- URL field with automatic validation
- Options: `required`
- Example validation: `{ "required": false }`

### JSON (`json`)
- JSON field for storing structured data
- Options: `required`
- Example validation: `{ "required": false }`

## Special Field Types

### File (`file`)
- File upload field
- Options: `required`, `maxSize`, `allowedTypes`
- Example validation: `{ "required": false, "maxSize": 5242880, "allowedTypes": ["image/jpeg", "image/png"] }`

### Relation (`relation`)
- Foreign key relationship to another collection
- Options: `required`, `maxSelect`, `collectionId`
- Example validation: `{ "required": true, "maxSelect": 1, "collectionId": "users_collection_id" }`

### Select (`select`)
- Single select from predefined options
- Options: `required`, `values`
- Example validation: `{ "required": true, "values": ["active", "inactive", "pending"] }`

## Common Validation Patterns

### Required Fields
```javascript
{
  "required": true
}
```

### Text Length Validation
```javascript
{
  "required": true,
  "min": 2,
  "max": 50
}
```

### Email Pattern
```javascript
{
  "required": true,
  "pattern": "^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$"
}
```

### Number Range
```javascript
{
  "required": true,
  "min": 0,
  "max": 100
}
```

### Date Range
```javascript
{
  "required": true,
  "min": "2024-01-01",
  "max": "2025-12-31"
}
```

## Field Naming Conventions

- Use lowercase letters, numbers, and underscores only
- Start with a letter
- Avoid PocketBase reserved names: `id`, `created`, `updated`
- Use snake_case for multi-word names
- Examples: `first_name`, `user_id`, `created_at`, `is_active`