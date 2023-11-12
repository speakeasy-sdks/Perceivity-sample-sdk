"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import storyschema as components_storyschema
from typing import List, Optional


@dataclasses.dataclass
class StoriesAPIListStoriesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    response: Optional[List[components_storyschema.StorySchema]] = dataclasses.field(default=None)
    r"""OK"""
    

