# Scripts Directory

This directory contains utility scripts for managing the Transparency development process.

## Feature Management Script

The `manage_features.py` script helps track feature requests, manage the roadmap, and generate release notes.

### Installation

No additional dependencies required - uses only Python standard library.

### Usage

```bash
# Show help
python scripts/manage_features.py --help

# Add a new feature request
python scripts/manage_features.py add \
  "export-csv" \
  "CSV Export Functionality" \
  "Allow users to export search results to CSV format" \
  --priority high \
  --type enhancement

# List all features
python scripts/manage_features.py list

# List features by status
python scripts/manage_features.py list --status planned

# List features by priority
python scripts/manage_features.py list --priority high

# Update feature status
python scripts/manage_features.py status export-csv in_progress

# Assign feature to release
python scripts/manage_features.py assign export-csv v2.2.0

# Generate release notes
python scripts/manage_features.py notes v2.2.0

# Show feature statistics
python scripts/manage_features.py stats

# Update roadmap (preview)
python scripts/manage_features.py roadmap
```

### Feature Lifecycle

1. **Add Feature**: Create new feature request with details
2. **Plan**: Assign to release and update status to "planned"
3. **Develop**: Update status to "in_progress" during development
4. **Test**: Update status to "testing" during QA
5. **Complete**: Update status to "completed" when released

### Example Workflow

```bash
# Add a new API integration request
python scripts/manage_features.py add \
  "congress-api" \
  "Congress.gov API Integration" \
  "Integrate Congress.gov API for legislative data access" \
  --priority high \
  --type api-integration

# Plan it for next release
python scripts/manage_features.py assign congress-api v2.3.0

# Start development
python scripts/manage_features.py status congress-api in_progress

# Complete development
python scripts/manage_features.py status congress-api completed

# Generate release notes
python scripts/manage_features.py notes v2.3.0
```

### Data Storage

Features are tracked in `scripts/features.json` with the following structure:

```json
{
  "features": {
    "feature-id": {
      "id": "feature-id",
      "title": "Feature Title",
      "description": "Feature description",
      "priority": "high|medium|low|critical",
      "complexity": "high|medium|low",
      "type": "enhancement|api-integration|ui-ux|security|performance|bug",
      "status": "requested|planned|in_progress|testing|completed|cancelled",
      "created_date": "2024-01-01T12:00:00",
      "assigned_release": "v2.2.0",
      "github_issue": "#123",
      "implementation_notes": []
    }
  },
  "releases": {
    "v2.2.0": {
      "features": ["feature-id"],
      "target_date": "2024-03-01",
      "status": "planning"
    }
  },
  "last_updated": "2024-01-01T12:00:00"
}
```

### Integration with GitHub

While this script manages features locally, it's designed to complement GitHub Issues:

1. **GitHub Issues**: For community feature requests and discussions
2. **Feature Script**: For internal tracking and release planning
3. **Roadmap**: For public visibility of planned features

### Best Practices

1. **Consistent IDs**: Use kebab-case for feature IDs (e.g., "csv-export")
2. **Clear Titles**: Use descriptive titles that explain the feature
3. **Detailed Descriptions**: Include enough detail for implementation
4. **Regular Updates**: Keep status current throughout development
5. **Release Planning**: Assign features to releases early in planning

### Extending the Script

The script is designed to be extensible. You can add new commands by:

1. Adding a new subparser in `main()`
2. Implementing the corresponding method in `FeatureManager`
3. Adding any new data fields to the JSON structure

Example extensions:
- GitHub integration (create/update issues)
- Time tracking (estimate vs actual development time)
- Dependency tracking (feature dependencies)
- Contributor assignment
- Automated roadmap updates 