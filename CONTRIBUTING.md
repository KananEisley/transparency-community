# Contributing to Transparency Platform

Thank you for your interest in contributing to the Transparency Platform! This guide will help you understand how to contribute effectively.

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
2. **Review the Roadmap**: Check our project roadmap to see if the feature is already planned
3. **Consider the Scope**: Ensure the feature aligns with the platform's mission of government transparency

### How to Submit a Feature Request

#### Option 1: GitHub Issues (Recommended)

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

#### Option 2: Discussion Forum

For broader feature discussions or brainstorming, use GitHub Discussions.

### Feature Request Lifecycle

1. **Submission**: Feature request is submitted via GitHub issue
2. **Triage**: Maintainers review and label the request
3. **Discussion**: Community discusses the feature
4. **Decision**: Maintainers decide whether to accept, defer, or decline
5. **Planning**: Accepted features are added to the roadmap
6. **Implementation**: Features are developed and tested
7. **Release**: Features are included in a release

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

## Code Contributions

### Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Add tests for your changes
5. Ensure all tests pass: `make check`
6. Commit your changes: `git commit -m "Add your feature"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Create a Pull Request

### Pull Request Guidelines

- **Clear Title**: Use a descriptive title
- **Description**: Explain what your PR does and why
- **Link Issues**: Reference related issues with "Fixes #123"
- **Tests**: Include tests for new functionality
- **Documentation**: Update documentation if needed
- **Changelog**: Add entry to version history if significant

### Pull Request Template

```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issues
Fixes #[issue number]

## Testing
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

## Development Setup

### Prerequisites

- Python 3.9+
- Git
- Virtual environment tool (venv, conda, etc.)

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/yourusername/transparency.git
cd transparency

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests to verify setup
make check
```

### Development Workflow

```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and test
make check

# Commit changes
git add .
git commit -m "Add new feature"

# Push and create PR
git push origin feature/new-feature
```

## Code Standards

### Python Style

- **Formatter**: Black with 100 character line length
- **Linter**: Flake8 with project configuration
- **Type Hints**: Required for all new code
- **Docstrings**: Google style docstrings

### Code Quality Checks

```bash
# Format code
make format

# Run all checks
make check

# Individual checks
make lint          # Linting
make test          # Tests
make type-check    # Type checking (if available)
```

### Naming Conventions

- **Files**: `snake_case.py`
- **Classes**: `PascalCase`
- **Functions/Variables**: `snake_case`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private**: `_leading_underscore`

## Testing

### Test Requirements

- All new features must include tests
- Bug fixes should include regression tests
- Aim for high test coverage
- Tests should be fast and reliable

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=transparency

# Run specific test file
pytest tests/test_updater.py

# Run specific test
pytest tests/test_updater.py::TestUpdateChecker::test_init
```

### Test Structure

```python
import unittest
from unittest.mock import Mock, patch

class TestNewFeature(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        pass
    
    def test_feature_functionality(self):
        """Test the main functionality."""
        # Arrange
        # Act
        # Assert
        pass
    
    def test_error_handling(self):
        """Test error conditions."""
        pass
```

## Documentation

### Documentation Requirements

- **README**: Keep README.md updated with new features
- **Docstrings**: All public functions and classes
- **Type Hints**: All function signatures
- **Examples**: Include usage examples for new features

### Documentation Style

```python
def search_contributions(self, name: str, limit: int = 10) -> Dict[str, Any]:
    """
    Search for campaign contributions by contributor name.
    
    Args:
        name: The contributor name to search for
        limit: Maximum number of results to return
        
    Returns:
        Dictionary containing search results and metadata
        
    Raises:
        APIError: If the API request fails
        ValueError: If name is empty or invalid
        
    Example:
        >>> client = FECAPIClient(api_key="your_key")
        >>> results = client.search_contributions("John Smith", limit=5)
        >>> print(f"Found {len(results['results'])} contributions")
    """
```

## Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help newcomers learn and contribute
- Maintain professional communication

### Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and brainstorming
- **Documentation**: Check README and code comments
- **Code Review**: Ask for feedback on PRs

### Recognition

Contributors are recognized in:
- Git commit history
- Release notes for significant contributions
- README contributors section (if added)

## Release Process

### Version Numbering

We use Semantic Versioning (SemVer):
- **Major** (X.0.0): Breaking changes
- **Minor** (X.Y.0): New features, backward compatible
- **Patch** (X.Y.Z): Bug fixes, backward compatible

### Release Checklist

1. Update version numbers
2. Update changelog
3. Run full test suite
4. Create release branch
5. Build and test applications
6. Create GitHub release
7. Update documentation

Thank you for contributing to the Transparency Platform! Your contributions help make government data more accessible to everyone. 