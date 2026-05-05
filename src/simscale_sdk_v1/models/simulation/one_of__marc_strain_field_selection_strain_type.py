from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.marc_elastic_strain_type import MarcElasticStrainType
from simscale_sdk_v1.models.simulation.marc_equivalent_elastic_strain_type import MarcEquivalentElasticStrainType
from simscale_sdk_v1.models.simulation.marc_equivalent_plastic_strain_type import MarcEquivalentPlasticStrainType
from simscale_sdk_v1.models.simulation.marc_plastic_strain_type import MarcPlasticStrainType
from simscale_sdk_v1.models.simulation.marc_principal_elastic_strain_type import MarcPrincipalElasticStrainType
from simscale_sdk_v1.models.simulation.marc_principal_plastic_strain_type import MarcPrincipalPlasticStrainType
from simscale_sdk_v1.models.simulation.marc_principal_total_strain_type import MarcPrincipalTotalStrainType
from simscale_sdk_v1.models.simulation.marc_total_strain_type import MarcTotalStrainType

# Total strain: Represents the sum of all strain components (elastic, plastic, and thermal) relative to the original configuration. It describes the complete deformation state of the material. Tensor quantity.Elastic strain: The recoverable portion of the strain that disappears upon unloading, calculated using the material's elastic constitutive laws. Tensor quantity.Plastic strain: The permanent, non-recoverable deformation that occurs once the material exceeds its yield point. Tensor quantity.Principal strain (total): The strains oriented along the axes where shear strain is zero. These represent the maximum, intermediate, and minimum normal strains in the material. Derived from the total strain tensor field.Principal strain (elastic): The strains oriented along the axes where shear strain is zero. These represent the maximum, intermediate, and minimum normal strains in the material. Derived from the elastic strain tensor field.Principal strain (plastic): The strains oriented along the axes where shear strain is zero. These represent the maximum, intermediate, and minimum normal strains in the material. Derived from the plastic strain tensor field.Equivalent elastic strain: A scalar value derived from the elastic strain tensor components, used to represent the magnitude of elastic deformation in a single value.Equivalent plastic strain: A scalar measure (the von Mises equivalent) representing the accumulation of plastic deformation, often used for assessing material failure or hardening.
_ONE_OF__MARC_STRAIN_FIELD_SELECTION_STRAIN_TYPE_VARIANTS: dict[str, type] = {
    "TOTAL": MarcTotalStrainType,
    "ELASTIC": MarcElasticStrainType,
    "PLASTIC": MarcPlasticStrainType,
    "PRINCIPAL_TOTAL": MarcPrincipalTotalStrainType,
    "PRINCIPAL_ELASTIC": MarcPrincipalElasticStrainType,
    "PRINCIPAL_PLASTIC": MarcPrincipalPlasticStrainType,
    "EQUIVALENT_ELASTIC": MarcEquivalentElasticStrainType,
    "EQUIVALENT_PLASTIC": MarcEquivalentPlasticStrainType,
}

OneOf_MarcStrainFieldSelectionStrainType = Annotated[
    Union[
        MarcTotalStrainType,
        MarcElasticStrainType,
        MarcPlasticStrainType,
        MarcPrincipalTotalStrainType,
        MarcPrincipalElasticStrainType,
        MarcPrincipalPlasticStrainType,
        MarcEquivalentElasticStrainType,
        MarcEquivalentPlasticStrainType,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_STRAIN_FIELD_SELECTION_STRAIN_TYPE_VARIANTS,
        )
    ),
]
