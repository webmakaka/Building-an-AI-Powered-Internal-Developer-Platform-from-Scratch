#!/usr/bin/env python3
"""
Audit Logger

Simple audit logging for platform operations.
Logs events to stdout in structured JSON format.
In production, this would write to a central logging system.
"""

import json
import logging
from datetime import datetime, timezone
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class AuditLogger:
    """Logs platform operations for compliance and debugging."""

    def __init__(self, log_file: Optional[str] = None):
        self.log_file = log_file
        self.events = []

    def log_event(
        self,
        action: str,
        actor: str = "system",
        resource_type: str = "unknown",
        resource_id: str = "",
        status: str = "success",
        details: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Record an audit event.

        Args:
            action: What happened (e.g., 'project_bootstrapped')
            actor: Who did it
            resource_type: Type of resource affected
            resource_id: Identifier for the resource
            status: 'success' or 'failure'
            details: Additional context
        """
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action": action,
            "actor": actor,
            "resource_type": resource_type,
            "resource_id": resource_id,
            "status": status,
            "details": details or {},
        }
        self.events.append(event)
        logger.info("AUDIT: %s", json.dumps(event))

        if self.log_file:
            try:
                with open(self.log_file, "a") as f:
                    f.write(json.dumps(event) + "\n")
            except OSError as e:
                logger.warning("Could not write to audit log file: %s", e)

        return event

    def get_events(
        self, action: Optional[str] = None, actor: Optional[str] = None
    ) -> list:
        """Retrieve logged events, optionally filtered."""
        results = self.events
        if action:
            results = [e for e in results if e["action"] == action]
        if actor:
            results = [e for e in results if e["actor"] == actor]
        return results
