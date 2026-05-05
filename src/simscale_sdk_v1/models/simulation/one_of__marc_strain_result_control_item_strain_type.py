from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.elastic_strain import ElasticStrain
from simscale_sdk_v1.models.simulation.equivalent_elastic_strain import EquivalentElasticStrain
from simscale_sdk_v1.models.simulation.equivalent_plastic_strain import EquivalentPlasticStrain
from simscale_sdk_v1.models.simulation.plastic_strain import PlasticStrain
from simscale_sdk_v1.models.simulation.principal_elastic_strain import PrincipalElasticStrain
from simscale_sdk_v1.models.simulation.principal_plastic_strain import PrincipalPlasticStrain
from simscale_sdk_v1.models.simulation.principal_total_strain import PrincipalTotalStrain
from simscale_sdk_v1.models.simulation.total_strain import TotalStrain

# Total strain: Represents the sum of all strain components (elastic, plastic, and thermal) relative to the original configuration. It describes the complete deformation state of the material. Tensor quantity.Elastic strain: The recoverable portion of the strain that disappears upon unloading, calculated using the material's elastic constitutive laws. Tensor quantity.Plastic strain: The permanent, non-recoverable deformation that occurs once the material exceeds its yield point. Tensor quantity.Principal strain (total): The strains oriented along the axes where shear strain is zero. These represent the maximum, intermediate, and minimum normal strains in the material. Derived from the total strain tensor field.Principal strain (elastic): The strains oriented along the axes where shear strain is zero. These represent the maximum, intermediate, and minimum normal strains in the material. Derived from the elastic strain tensor field.Principal strain (plastic): The strains oriented along the axes where shear strain is zero. These represent the maximum, intermediate, and minimum normal strains in the material. Derived from the plastic strain tensor field.Equivalent elastic strain: A scalar value derived from the elastic strain tensor components, used to represent the magnitude of elastic deformation in a single value.Equivalent plastic strain: A scalar measure (the von Mises equivalent) representing the accumulation of plastic deformation, often used for assessing material failure or hardening.
_ONE_OF__MARC_STRAIN_RESULT_CONTROL_ITEM_STRAIN_TYPE_VARIANTS: dict[str, type] = {
    "TOTAL": TotalStrain,
    "ELASTIC": ElasticStrain,
    "PLASTIC": PlasticStrain,
    "PRINCIPAL_TOTAL": PrincipalTotalStrain,
    "PRINCIPAL_ELASTIC": PrincipalElasticStrain,
    "PRINCIPAL_PLASTIC": PrincipalPlasticStrain,
    "EQUIVALENT_ELASTIC": EquivalentElasticStrain,
    "EQUIVALENT_PLASTIC": EquivalentPlasticStrain,
}

OneOf_MarcStrainResultControlItemStrainType = Annotated[
    Union[
        TotalStrain,
        ElasticStrain,
        PlasticStrain,
        PrincipalTotalStrain,
        PrincipalElasticStrain,
        PrincipalPlasticStrain,
        EquivalentElasticStrain,
        EquivalentPlasticStrain,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_STRAIN_RESULT_CONTROL_ITEM_STRAIN_TYPE_VARIANTS,
        )
    ),
]
