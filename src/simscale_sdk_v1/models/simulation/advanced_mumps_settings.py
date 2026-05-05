from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__advanced_mumps_settings_mumps_acceleration import (
    OneOf_AdvancedMUMPSSettingsMumpsAcceleration,
)


class AdvancedMUMPSSettings(SimScaleModel):
    force_symmetric: bool | None = Field(
        validation_alias="forceSymmetric",
        serialization_alias="forceSymmetric",
        default=False,
        description="Choose if you want to enforce a symmetric matrix.",
    )
    enable_singularity_detection: bool | None = Field(
        validation_alias="enableSingularityDetection",
        serialization_alias="enableSingularityDetection",
        default=True,
        description="Enable the check for singularities in the model. This is helpful for debugging, to spot problems with the setup.",
    )
    precision_singularity_detection: int | None = Field(
        validation_alias="precisionSingularityDetection",
        serialization_alias="precisionSingularityDetection",
        default=9,
        description="Define the precision value for the detection of a singular matrix. Positive values enable the check, with 9 being a good starting point. Smaller values make the check more strict. This is an advanced option that should only be used to debug a model.",
    )
    stop_if_singular: bool | None = Field(
        validation_alias="stopIfSingular",
        serialization_alias="stopIfSingular",
        default=False,
        description="Choose if the calculation should be stopped if the problem turns out to be singular.",
    )
    matrix_type: Literal["ASYMMETRIC", "AUTOMATIC_DETECTION", "SYMMETRIC_POSITIVE_INDEFINITE"] | None = Field(
        validation_alias="matrixType",
        serialization_alias="matrixType",
        default="AUTOMATIC_DETECTION",
        description="Choose the type of your system matrix by directly selecting the appropriate type or using the automatic detection. With the selection automatic detection the matrix type symmetric positive indefinite is selected if a symmetric system matrix is detected, and asymmetric otherwise.",
    )
    memory_percentage_for_pivoting: float | None = Field(
        validation_alias="memoryPercentageForPivoting",
        serialization_alias="memoryPercentageForPivoting",
        default=20,
        description="Define how much additional memory should be reserved for the pivoting operations. If MUMPS estimates that the necessary space for factorising the matrix would be 100, choosing a value of 20 would mean that MUMPS allocates a memory space of 120.",
    )
    linear_system_relative_residual: float | None = Field(
        validation_alias="linearSystemRelativeResidual",
        serialization_alias="linearSystemRelativeResidual",
        default=1e-05,
        description="Set the maximum allowable numerical error in solving the linear equation system. Use -1 if you do not wish to carry out a check on the solution error (not recommended).",
    )
    matrix_filtering_threshold: float | None = Field(
        validation_alias="matrixFilteringThreshold",
        serialization_alias="matrixFilteringThreshold",
        default=-1,
        description="This parameter allows a filtration of the matrix entries that are saved and possibly passed to the nonlinear algorithm (Newton) and is similar to a relaxation mechanism. If the given threshold value is strictly positive, MUMPS only saves the matrix entries that satisfy the following condition: |Kij| value*(|Kii|+|Kjj|). Thus using this functionality might save computation time as well as memory consumption, but the effects strongly depend on the given value and is only advised for the experienced user.",
    )
    single_precision: bool | None = Field(
        validation_alias="singlePrecision",
        serialization_alias="singlePrecision",
        default=False,
        description="If this option is activated the matrix factorisation is done with single precision and thus a reduction in memory consumption (often about 50%) and computation time is gained if the problem is well conditioned. If the problem is ill-conditioned one risks that in a nonlinear computation the newton algorithm fails to converge.",
    )
    preprocessing: bool | None = Field(
        default=True,
        description="If this option is activated MUMPS performs a pre-processing on order to identify the best parameter setting for some internal parameters adapted to the current problem.",
    )
    renumbering_method: Literal["AMD", "SCOTCH", "AMF", "PORD", "QAMD", "AUTOMATIC"] | None = Field(
        validation_alias="renumberingMethod",
        serialization_alias="renumberingMethod",
        default="AUTOMATIC",
        description="Choose the renumbering method for the system matrix entries. The choice of the renumbering method has a big impact on the memory consumption and the solution time. Currently supported are:SCOTCH is a powerful renumbering tool, suited for most scenarios and the standard choice for MUMPS.PORD is a renumbering tool that comes with MUMPS.AMD uses the Approximate Minimum Degree method.AMF uses the Approximate Minimum Fill method.QAMD is a variant of AMD with automatic detection of quasi-dense matrix lines.If automatic is selected the user let MUMPS choose the renumbering tool. The methods AMD, AMF and QAMD are generally inferior to the more sophisticated methods SCOTCH and PORD but may be a better choice in some cases.",
    )
    postprocessing: str | None = Field(
        default="AUTOMATIC",
        description="With this option the user can control the iterative refinement of the linear system solution. This option only has an effect if the value of the  linear system relative residual given by the user is greater than zero, otherwise it is ignored. If it is activate MUMPS carries out at least one additional iteration of the linear system resolution and at most 10 iterations. The process is stopped if the residual isn't reduced by at least a factor of 5. If this option is set to be inactive no additional iteration is done and if automatic is chosen MUMPS automatically decides if additional iterations should be done and the maximum number of iterations is set to 4.",
    )
    mumps_acceleration: OneOf_AdvancedMUMPSSettingsMumpsAcceleration | None = Field(
        validation_alias="mumpsAcceleration", serialization_alias="mumpsAcceleration", default=None
    )
    distributed_matrix_storage: bool | None = Field(
        validation_alias="distributedMatrixStorage",
        serialization_alias="distributedMatrixStorage",
        default=True,
        description="Choose this parameter as true to ensure that the system matrix saving is distributed among the processors of the computation. If multiple cores are used only the relevant part for each core is saved. If it is set to false the whole matrix is saved for each processor. Enabling this can significantly reductions in memory consumption, but introduces numerical instability in rare occasions.",
    )
