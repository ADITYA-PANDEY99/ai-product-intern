from dataclasses import dataclass, field
from typing import Optional, List, Dict
from enum import Enum


class AuthType(Enum):
    OAUTH2 = "OAuth2"
    API_KEY = "API Key"
    BASIC_AUTH = "Basic Auth"
    BEARER_TOKEN = "Bearer Token"
    JWT = "JWT"
    CUSTOM = "Custom"
    NONE = "None"


@dataclass
class ApplicationResearch:
    name: str
    category: str
    one_line_description: str
    authentication: List[str]
    credential_availability: str
    public_api: str
    rest: str
    graphql: str
    webhook_support: str
    api_breadth: str
    mcp_availability: str
    toolkit_buildability: str
    primary_blocker: str
    evidence_url: str
    confidence: float  # 0-100 (This acts as explainable buildability score)
    buildability_score: float  # Automatically computed score
    needs_human_review: bool = False
    evidence: Dict[str, str] = field(default_factory=dict)


@dataclass
class Analytics:
    total_applications: int
    applications_with_public_api: int
    applications_with_rest: int
    applications_with_graphql: int
    applications_with_webhooks: int
    applications_with_oauth2: int
    applications_with_mcp: int
    high_confidence_count: int  # >= 90%
    medium_confidence_count: int  # 70-89%
    low_confidence_count: int  # < 70%
    needs_human_review_count: int
    average_confidence: float
    confidence_distribution: dict  # buckets of 10
    category_breakdown: dict
