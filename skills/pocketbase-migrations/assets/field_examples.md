# PocketBase Field Examples

## Text Fields
```javascript
{
  name: "name",
  type: "text",
  required: true,
  presentable: false,
  unique: false,
  options: {
    min: 1,
    max: 200,
    pattern: ""
  }
}
```

## Email Field
```javascript
{
  name: "email",
  type: "email",
  required: true,
  presentable: false,
  unique: true,
  options: {}
}
```

## Number Field
```javascript
{
  name: "age",
  type: "number",
  required: false,
  presentable: false,
  unique: false,
  options: {
    min: 0,
    max: 150
  }
}
```

## Boolean Field
```javascript
{
  name: "is_active",
  type: "bool",
  required: false,
  presentable: false,
  unique: false,
  options: {}
}
```

## Date Field
```javascript
{
  name: "birth_date",
  type: "date",
  required: false,
  presentable: false,
  unique: false,
  options: {
    min: "1900-01-01",
    max: ""
  }
}
```

## DateTime Field
```javascript
{
  name: "created_at",
  type: "datetime",
  required: false,
  presentable: false,
  unique: false,
  options: {}
}
```

## Select Field
```javascript
{
  name: "status",
  type: "select",
  required: true,
  presentable: false,
  unique: false,
  options: {
    maxSelect: 1,
    values: ["active", "inactive", "pending"]
  }
}
```

## Relation Field
```javascript
{
  name: "user",
  type: "relation",
  required: true,
  presentable: false,
  unique: false,
  options: {
    collectionId: "users_collection_id",
    maxSelect: 1,
    cascadeDelete: false
  }
}
```

## File Field
```javascript
{
  name: "avatar",
  type: "file",
  required: false,
  presentable: false,
  unique: false,
  options: {
    maxSelect: 1,
    maxSize: 5242880,
    mimeTypes: ["image/jpeg", "image/png", "image/gif"],
    thumbs: null
  }
}
```

## JSON Field
```javascript
{
  name: "metadata",
  type: "json",
  required: false,
  presentable: false,
  unique: false,
  options: {}
}
```

## URL Field
```javascript
{
  name: "website",
  type: "url",
  required: false,
  presentable: false,
  unique: false,
  options: {}
}
```