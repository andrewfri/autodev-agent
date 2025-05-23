"""
Base class for all project generators.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any

class BaseGenerator(ABC):
    """Abstract base class for all project generators."""
    
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        
    @abstractmethod
    def generate(self, prompt: str) -> Dict[str, Any]:
        """
        Generate a project based on the given prompt.
        
        Args:
            prompt: The natural language prompt describing the project
            
        Returns:
            Dict containing metadata about the generated project
        """
        pass
    
    @abstractmethod
    def validate_prompt(self, prompt: str) -> bool:
        """
        Validate if the prompt is suitable for this generator.
        
        Args:
            prompt: The natural language prompt to validate
            
        Returns:
            bool indicating if the prompt is valid
        """
        pass
