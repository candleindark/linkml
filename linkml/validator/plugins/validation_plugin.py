from abc import ABC, abstractmethod
from typing import Any, Iterator, NamedTuple

from linkml.validator.report import ValidationResult
from linkml.validator.validation_context import ValidationContext


class ValidationResultWithSource(NamedTuple):
    result: ValidationResult
    source: Any  # The source from which the `ValidationResult` was generated


class ValidationPlugin(ABC):
    """Abstract base class for validation plugins.

    Subclasses must implement a ``process`` method.
    """

    def pre_process(self, context: ValidationContext) -> None:
        """A hook that will be called before instances are processed.

        :param context: A `ValidationContext` instance which provides
            access to the schema, target class, and artifacts generated
            from the schema
        """
        pass

    def post_process(self, context: ValidationContext) -> None:
        """A hook that will be called after instances are processed.

        :param context: A `ValidationContext` instance which provides
            access to the schema, target class, and artifacts generated
            from the schema
        """
        pass

    @abstractmethod
    def process(self, instance: dict, context: ValidationContext) -> Iterator[ValidationResultWithSource]:
        """Lazily yield validation results for an instance according to
        the validation context.

        :param instance: The instance to validate
        :param context: A `ValidationContext` instance which provides
            access to the schema, target class, and artifacts generated
            from the schema
        :return: Iterator over validation results
        :rtype: Iterator[ValidationResultWithSource]
        """
        pass
