from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.elastoplastic_marc_material_behavior import ElastoplasticMarcMaterialBehavior
from simscale_sdk_v1.models.simulation.hyperelastic_marc_material_behavior import HyperelasticMarcMaterialBehavior
from simscale_sdk_v1.models.simulation.linear_elastic_marc_material_behavior import LinearElasticMarcMaterialBehavior
from simscale_sdk_v1.models.simulation.viscoplastic_marc_material_behavior import ViscoplasticMarcMaterialBehavior

# Linear elastic: This behavior assumes a linear relationship between stress and strain according to Hooke's Law, where the material returns to its original shape upon unloading. It is defined by constant values for Young's modulus and Poisson's ratio and is typically used for materials experiencing small deformations below their yield point.Hyperelastic: Hyperelastic models describe materials like rubber or elastomers that can undergo very large, recoverable (elastic) strains. These models are defined through strain energy functions (e.g., Mooney-Rivlin or Ogden) to capture non-linear elastic behavior and near-incompressibility.Elastoplastic: This behavior models materials that deform elastically until a specific yield stress is reached, after which permanent (plastic) deformation occurs. It utilizes a yield criterion (such as von Mises) and a hardening rule to define how the material's strength increases with continued plastic straining. This behavior is typically used to model materials like metals or structural alloys.Viscoplastic: This multi-network model utilizes a parallel combination of hyperelastic, viscoelastic, and viscoplastic elements to capture the complex, rate-dependent response of polymers like thermoplastics and elastomers. It is specifically designed to simulate phenomena such as creep, stress relaxation, and stiffness degradation (damage) under cyclic loading conditions. It is the ideal choice for thermoplastics and elastomers.
_ONE_OF__MARC_MATERIAL_MARC_MATERIAL_BEHAVIOR_VARIANTS: dict[str, type] = {
    "LINEAR_ELASTIC_MARC": LinearElasticMarcMaterialBehavior,
    "HYPERELASTIC_MARC": HyperelasticMarcMaterialBehavior,
    "ELASTOPLASTIC_MARC": ElastoplasticMarcMaterialBehavior,
    "VISCOPLASTIC_MARC": ViscoplasticMarcMaterialBehavior,
}

OneOf_MarcMaterialMarcMaterialBehavior = Annotated[
    Union[
        LinearElasticMarcMaterialBehavior,
        HyperelasticMarcMaterialBehavior,
        ElastoplasticMarcMaterialBehavior,
        ViscoplasticMarcMaterialBehavior,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_MATERIAL_MARC_MATERIAL_BEHAVIOR_VARIANTS,
        )
    ),
]
