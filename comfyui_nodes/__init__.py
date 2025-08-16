"""ComfyUI custom node bundle for the AI storyboard generator pipeline.

This package exposes nodes that wrap the existing
Python scripts in this repository so they can be executed as part of a
ComfyUI workflow.
"""

from .storyboard_nodes import (
    DreamUpStoryNode,
    BuildChaptersNode,
    SummarizeChaptersNode,
    CreateImagesNode,
    CreateUniqueCharacterNode,
    CreateMovieNode,
    CreateMosaicNode,
    ZoomPanMovieNode,
    AddSubtitlesNode,
    CreateVoiceoverNode,
    PreviewAndUploadNode,
)

NODE_CLASS_MAPPINGS = {
    "DreamUpStory": DreamUpStoryNode,
    "BuildChapters": BuildChaptersNode,
    "SummarizeChapters": SummarizeChaptersNode,
    "CreateImages": CreateImagesNode,
    "CreateUniqueCharacter": CreateUniqueCharacterNode,
    "CreateMovie": CreateMovieNode,
    "CreateMosaic": CreateMosaicNode,
    "ZoomPanMovie": ZoomPanMovieNode,
    "AddSubtitles": AddSubtitlesNode,
    "CreateVoiceover": CreateVoiceoverNode,
    "PreviewAndUpload": PreviewAndUploadNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DreamUpStory": "Dream Up Story",
    "BuildChapters": "Build Chapters",
    "SummarizeChapters": "Summarize Chapters & Prompts",
    "CreateImages": "Create Images",
    "CreateUniqueCharacter": "Create Unique Character",
    "CreateMovie": "Create Movie",
    "CreateMosaic": "Create Mosaic",
    "ZoomPanMovie": "Add Zoom/Pan",
    "AddSubtitles": "Add Subtitles",
    "CreateVoiceover": "Create Voiceover",
    "PreviewAndUpload": "Preview & Upload",
}
