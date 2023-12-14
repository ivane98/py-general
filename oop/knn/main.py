from typing import Optional, List
import weakref
import datetime
from collections.abc import Iterable


class Sample:
    def __init__(self, sepal_length: float, sepal_width: float, petal_length: float, petal_width: float, species: Optional[str] = None) -> None:
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species
        self.classification: Optional[str] = None

    def __repr__(self) -> str:
        if self.species is None:
            known_unknown = "UnknownSample"
        else:
            known_unknown = "KnownSample"
        if self.classification is None:
            classification = ""
        else:
            classification = f"{self.classification}"

        return (
            f"{known_unknown}("
            f"sepal_length={self.sepal_length}, "
            f"sepal_width={self.sepal_width}, "
            f"petal_length={self.petal_length}, "
            f"petal_width={self.petal_width}, "
            f"species={self.species!r}, "
            f"classification={classification}"
            f")"
        )
    
    def classify(self, classification: str) -> None:
        self.classification = classification

    def matches(self)-> bool:
        return self.species == self.classification
    
s2 = Sample(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species="Iris-setosa")
s2.classification = "Wrong"


class Hyperparameter:
    """A hyperparameter value and the overall quality of the
classification."""

    def __init__(self, k: int, training: "TrainingData") -> None:
        self.k = k
        self.data: weakref.ReferenceType["TrainingData"] = weakref.ref(training)
        self.quality: float

    def test(self):
        """Run the entire test suite."""
        training_data: Optional["TrainingData"] = self.data()

        if not training_data:
            raise RuntimeError("Broken Weak Reference")

        pass_count, fail_count = 0, 0
        for sample in training_data.testing:
            sample.classification = self.classify(sample)
        
        if self.matches():
            pass_count += 1
        else:
            fail_count += 1

        self.quality = pass_count / (pass_count + fail_count)


class TrainingData:
    """A set of training data and testing data with methods to load and
test the samples."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.uploaded: datetime.datetime
        self.tested: datetime.datetime
        self.training: List[Sample] = []
        self.testing: List[Sample] = []
        self.tuning: List[Hyperparameter] = []

    def load(self, raw_data_source: Iterable[dict[str, str]]) -> None:
        """Load and partition the raw data"""
        for n, row in enumerate(raw_data_source):
            sample = Sample(
                sepal_length=float(row["sepal_length"]),
                sepal_width=float(row["sepal_width"]),
                petal_length=float(row["petal_length"]),
                petal_width=float(row["petal_width"]),
                species=row["species"],
            )
            if n % 5 == 0:
                self.testing.append(sample)
            else:
                self.training.append(sample)
        self.uploaded = datetime.datetime.now(tz=datetime.timezone.utc)


    
    def test(self, parameter: Hyperparameter) -> None:
        """Test this Hyperparameter value."""
        parameter.test()
        self.tuning.append(parameter)
        self.testing = datetime.datetime.now(tz=datetime.timezone.utc)


    def classify(self, parameter: Hyperparameter, sample: Sample) -> Sample:
        """Test this Hyperparameter value."""
        classification = parameter.classify(sample)
        sample.classify(classification)
        return sample
    
    

    




    
    

