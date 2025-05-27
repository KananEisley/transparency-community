# Contributing to Transparency

Thank you for your interest in contributing to Transparency! This guide will help you understand how to contribute effectively.

## Table of Contents

- [Feature Requests](#feature-requests)
- [Bug Reports](#bug-reports)
- [Code Contributions](#code-contributions)
- [Development Setup](#development-setup)
- [Code Standards](#code-standards)
- [Testing](#testing)
- [Documentation](#documentation)

## Feature Requests

We welcome feature requests! Here's how to submit and track them effectively:

### Before Submitting a Feature Request

1. **Check Existing Issues**: Search existing issues to see if your feature has already been requested
3. **Consider the Scope**: Ensure the feature aligns with the platform's mission of government transparency

### How to Submit a Feature Request

#### GitHub Issues

Create a new issue with the following template:

```markdown
## Feature Request: [Brief Title]

### Problem Statement
Describe the problem or need this feature would address.

### Proposed Solution
Describe your proposed solution in detail.

### Use Cases
- Use case 1: [Description]
- Use case 2: [Description]

### Benefits
- Who would benefit from this feature?
- How would it improve the platform?

### Implementation Considerations
- Technical complexity: [Low/Medium/High]
- Dependencies: [List any dependencies]
- Breaking changes: [Yes/No - explain if yes]

### Additional Context
- Screenshots, mockups, or examples
- Links to relevant documentation
- Similar features in other tools

### Priority
- [ ] Critical (blocks current functionality)
- [ ] High (significantly improves user experience)
- [ ] Medium (nice to have improvement)
- [ ] Low (minor enhancement)
```

### Feature Request Labels

We use the following labels to categorize feature requests:

- `enhancement`: New feature or improvement
- `api-integration`: New government API integration
- `ui-ux`: User interface or experience improvement
- `security`: Security-related enhancement
- `performance`: Performance improvement
- `documentation`: Documentation improvement
- `good-first-issue`: Good for new contributors
- `help-wanted`: Community help needed
- `priority-high`: High priority feature
- `priority-medium`: Medium priority feature
- `priority-low`: Low priority feature

### API Integration Requests

For new government API integrations, please provide:

1. **API Documentation**: Link to official API documentation
2. **Data Value**: Explain the transparency value of this data
3. **API Key Requirements**: Whether an API key is required
4. **Rate Limits**: Any known rate limiting
5. **Data Format**: JSON, XML, CSV, etc.
6. **Example Endpoints**: Key endpoints to implement

### Feature Request Examples

#### Example 1: New API Integration
```markdown
## Feature Request: Add Congressional Voting Records API

### Problem Statement
Users want to track how their representatives vote on legislation.

### Proposed Solution
Integrate the Congress.gov API to provide voting record searches.

### Use Cases
- Search votes by representative name
- Filter votes by bill topic or date
- View voting patterns over time

### API Details
- Documentation: https://api.congress.gov/
- Requires API key: Yes (free)
- Rate limit: 5000 requests/hour
- Data format: JSON
```

#### Example 2: UI Enhancement
```markdown
## Feature Request: Export Search Results

### Problem Statement
Users want to save search results for offline analysis.

### Proposed Solution
Add export functionality for CSV, JSON, and PDF formats.

### Use Cases
- Export contribution data for research
- Save candidate information for comparison
- Generate reports for presentations
```

## Bug Reports

### Bug Report Template

```markdown
## Bug Report: [Brief Description]

### Environment
- Platform version: [e.g., v2.1.0]
- Operating system: [e.g., macOS 14.0]
- Python version: [e.g., 3.11.0]

### Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

### Expected Behavior
What you expected to happen.

### Actual Behavior
What actually happened.

### Screenshots/Logs
Include screenshots or relevant log entries from ~/.transparency/app.log

### Additional Context
Any other relevant information.
```


## Release Process

### Version Numbering

We use Semantic Versioning (SemVer):
- **Major** (X.0.0): Breaking changes
- **Minor** (X.Y.0): New features, backward compatible
- **Patch** (X.Y.Z): Bug fixes, backward compatible

Thank you for contributing to Transparency! Your contributions help make government data more accessible to everyone. 