#!/usr/bin/env python3
"""
Feature Request Management Script

This script helps manage feature requests and roadmap updates for the Transparency Platform.
It can be used to:
- Analyze feature request trends
- Generate roadmap updates
- Track feature implementation status
- Create release notes

Usage:
    python scripts/manage_features.py --help
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


class FeatureManager:
    """Manages feature requests and roadmap planning."""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.roadmap_file = project_root / "ROADMAP.md"
        self.features_data = project_root / "scripts" / "features.json"

    def load_features_data(self) -> Dict[str, Any]:
        """Load features data from JSON file."""
        if self.features_data.exists():
            with open(self.features_data, 'r') as f:
                return json.load(f)
        return {
            "features": {},
            "releases": {},
            "last_updated": None
        }

    def save_features_data(self, data: Dict[str, Any]) -> None:
        """Save features data to JSON file."""
        data["last_updated"] = datetime.now().isoformat()
        self.features_data.parent.mkdir(exist_ok=True)
        with open(self.features_data, 'w') as f:
            json.dump(data, f, indent=2)

    def add_feature(self, feature_id: str, title: str, description: str, 
                   priority: str = "medium", complexity: str = "medium",
                   feature_type: str = "enhancement") -> None:
        """Add a new feature to tracking."""
        data = self.load_features_data()
        
        feature = {
            "id": feature_id,
            "title": title,
            "description": description,
            "priority": priority,
            "complexity": complexity,
            "type": feature_type,
            "status": "requested",
            "created_date": datetime.now().isoformat(),
            "assigned_release": None,
            "github_issue": None,
            "implementation_notes": []
        }
        
        data["features"][feature_id] = feature
        self.save_features_data(data)
        print(f"✅ Added feature: {title}")

    def update_feature_status(self, feature_id: str, status: str) -> None:
        """Update the status of a feature."""
        data = self.load_features_data()
        
        if feature_id not in data["features"]:
            print(f"❌ Feature {feature_id} not found")
            return
        
        valid_statuses = ["requested", "planned", "in_progress", "testing", "completed", "cancelled"]
        if status not in valid_statuses:
            print(f"❌ Invalid status. Valid options: {', '.join(valid_statuses)}")
            return
        
        data["features"][feature_id]["status"] = status
        data["features"][feature_id]["last_updated"] = datetime.now().isoformat()
        
        self.save_features_data(data)
        print(f"✅ Updated {feature_id} status to: {status}")

    def assign_to_release(self, feature_id: str, release_version: str) -> None:
        """Assign a feature to a specific release."""
        data = self.load_features_data()
        
        if feature_id not in data["features"]:
            print(f"❌ Feature {feature_id} not found")
            return
        
        data["features"][feature_id]["assigned_release"] = release_version
        data["features"][feature_id]["status"] = "planned"
        
        # Add to release tracking
        if release_version not in data["releases"]:
            data["releases"][release_version] = {
                "features": [],
                "target_date": None,
                "status": "planning"
            }
        
        if feature_id not in data["releases"][release_version]["features"]:
            data["releases"][release_version]["features"].append(feature_id)
        
        self.save_features_data(data)
        print(f"✅ Assigned {feature_id} to release {release_version}")

    def list_features(self, status_filter: str = None, priority_filter: str = None) -> None:
        """List features with optional filtering."""
        data = self.load_features_data()
        
        features = data["features"].values()
        
        if status_filter:
            features = [f for f in features if f["status"] == status_filter]
        
        if priority_filter:
            features = [f for f in features if f["priority"] == priority_filter]
        
        if not features:
            print("No features found matching criteria")
            return
        
        print(f"\n📋 Features ({len(features)} found):")
        print("-" * 80)
        
        for feature in sorted(features, key=lambda x: x["created_date"], reverse=True):
            status_emoji = {
                "requested": "📝",
                "planned": "📋",
                "in_progress": "🔄",
                "testing": "🧪",
                "completed": "✅",
                "cancelled": "❌"
            }.get(feature["status"], "❓")
            
            priority_emoji = {
                "low": "🔵",
                "medium": "🟡",
                "high": "🔴",
                "critical": "🚨"
            }.get(feature["priority"], "⚪")
            
            print(f"{status_emoji} {priority_emoji} {feature['id']}: {feature['title']}")
            print(f"   Status: {feature['status']} | Priority: {feature['priority']} | Type: {feature['type']}")
            if feature["assigned_release"]:
                print(f"   Release: {feature['assigned_release']}")
            print()

    def generate_release_notes(self, release_version: str) -> None:
        """Generate release notes for a specific version."""
        data = self.load_features_data()
        
        if release_version not in data["releases"]:
            print(f"❌ Release {release_version} not found")
            return
        
        release = data["releases"][release_version]
        feature_ids = release["features"]
        
        print(f"\n# Release Notes - {release_version}\n")
        
        # Group features by type
        features_by_type = {}
        for feature_id in feature_ids:
            if feature_id in data["features"]:
                feature = data["features"][feature_id]
                feature_type = feature["type"]
                if feature_type not in features_by_type:
                    features_by_type[feature_type] = []
                features_by_type[feature_type].append(feature)
        
        # Generate notes by type
        type_headers = {
            "api-integration": "🔗 New API Integrations",
            "enhancement": "✨ New Features",
            "ui-ux": "🎨 User Interface Improvements",
            "security": "🔒 Security Enhancements",
            "performance": "⚡ Performance Improvements",
            "bug": "🐛 Bug Fixes"
        }
        
        for feature_type, features in features_by_type.items():
            header = type_headers.get(feature_type, f"📋 {feature_type.title()}")
            print(f"## {header}\n")
            
            for feature in features:
                print(f"- **{feature['title']}**: {feature['description']}")
            print()

    def update_roadmap(self) -> None:
        """Update the roadmap file with current feature status."""
        data = self.load_features_data()
        
        print("🔄 Updating roadmap...")
        
        # This is a simplified version - in practice, you might want to
        # parse the existing roadmap and update specific sections
        
        roadmap_updates = []
        
        # Get features by status
        for status in ["planned", "in_progress"]:
            features = [f for f in data["features"].values() if f["status"] == status]
            if features:
                status_name = "In Progress" if status == "in_progress" else "Planned"
                roadmap_updates.append(f"\n### {status_name} Features\n")
                
                for feature in features:
                    emoji = "🔄" if status == "in_progress" else "📋"
                    roadmap_updates.append(f"- {emoji} **{feature['title']}**: {feature['description']}")
                    if feature["assigned_release"]:
                        roadmap_updates.append(f"  - Target: {feature['assigned_release']}")
        
        if roadmap_updates:
            print("Roadmap updates:")
            for update in roadmap_updates:
                print(update)
        else:
            print("No roadmap updates needed")

    def feature_stats(self) -> None:
        """Display feature statistics."""
        data = self.load_features_data()
        features = data["features"].values()
        
        if not features:
            print("No features tracked yet")
            return
        
        # Count by status
        status_counts = {}
        priority_counts = {}
        type_counts = {}
        
        for feature in features:
            status = feature["status"]
            priority = feature["priority"]
            feature_type = feature["type"]
            
            status_counts[status] = status_counts.get(status, 0) + 1
            priority_counts[priority] = priority_counts.get(priority, 0) + 1
            type_counts[feature_type] = type_counts.get(feature_type, 0) + 1
        
        print(f"\n📊 Feature Statistics (Total: {len(features)})\n")
        
        print("By Status:")
        for status, count in sorted(status_counts.items()):
            print(f"  {status}: {count}")
        
        print("\nBy Priority:")
        for priority, count in sorted(priority_counts.items()):
            print(f"  {priority}: {count}")
        
        print("\nBy Type:")
        for feature_type, count in sorted(type_counts.items()):
            print(f"  {feature_type}: {count}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Manage feature requests and roadmap")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add feature command
    add_parser = subparsers.add_parser("add", help="Add a new feature")
    add_parser.add_argument("feature_id", help="Unique feature ID")
    add_parser.add_argument("title", help="Feature title")
    add_parser.add_argument("description", help="Feature description")
    add_parser.add_argument("--priority", choices=["low", "medium", "high", "critical"], 
                           default="medium", help="Feature priority")
    add_parser.add_argument("--complexity", choices=["low", "medium", "high"], 
                           default="medium", help="Implementation complexity")
    add_parser.add_argument("--type", default="enhancement", help="Feature type")
    
    # Update status command
    status_parser = subparsers.add_parser("status", help="Update feature status")
    status_parser.add_argument("feature_id", help="Feature ID")
    status_parser.add_argument("status", choices=["requested", "planned", "in_progress", 
                                                 "testing", "completed", "cancelled"],
                              help="New status")
    
    # Assign to release command
    assign_parser = subparsers.add_parser("assign", help="Assign feature to release")
    assign_parser.add_argument("feature_id", help="Feature ID")
    assign_parser.add_argument("release", help="Release version (e.g., v2.2.0)")
    
    # List features command
    list_parser = subparsers.add_parser("list", help="List features")
    list_parser.add_argument("--status", help="Filter by status")
    list_parser.add_argument("--priority", help="Filter by priority")
    
    # Release notes command
    notes_parser = subparsers.add_parser("notes", help="Generate release notes")
    notes_parser.add_argument("release", help="Release version")
    
    # Update roadmap command
    subparsers.add_parser("roadmap", help="Update roadmap")
    
    # Statistics command
    subparsers.add_parser("stats", help="Show feature statistics")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Find project root
    project_root = Path(__file__).parent.parent
    manager = FeatureManager(project_root)
    
    # Execute command
    if args.command == "add":
        manager.add_feature(args.feature_id, args.title, args.description,
                           args.priority, args.complexity, args.type)
    elif args.command == "status":
        manager.update_feature_status(args.feature_id, args.status)
    elif args.command == "assign":
        manager.assign_to_release(args.feature_id, args.release)
    elif args.command == "list":
        manager.list_features(args.status, args.priority)
    elif args.command == "notes":
        manager.generate_release_notes(args.release)
    elif args.command == "roadmap":
        manager.update_roadmap()
    elif args.command == "stats":
        manager.feature_stats()


if __name__ == "__main__":
    main() 