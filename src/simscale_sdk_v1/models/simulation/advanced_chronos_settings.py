from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AdvancedChronosSettings(SimScaleModel):
    force_fsai: bool | None = Field(
        validation_alias="forceFsai",
        serialization_alias="forceFsai",
        default=False,
        description="Force the usage of FSAI preconditioning. This can make sense for small and simple problems, because setting up the problem might be faster with FSAI than with AMG.Otherwise, Chronos selects itself the most suitable preconditioner, depending on the characteristics of the problem. In this case, AMG is preferred over FSAI.",
    )
    algorithm: Literal["FSAI_LIGHT", "FSAI_MEDIUM", "FSAI_HEAVY"] | None = Field(
        default="FSAI_LIGHT",
        description="The algorithm for the prolongation becomes more elaborate from Jacobi over light, medium to heavy FSAI. The stability increases as well as the computational cost. It is recommended to increase it when the problem has distored elements, is ill-conditioned  or has incompressible materials.",
    )
    smoother: Literal["JACOBI", "FSAI_LIGHT", "FSAI_MEDIUM", "FSAI_HEAVY"] | None = Field(
        default=None,
        description="The algorithm for the prolongation becomes more elaborate from Jacobi over light, medium to heavy FSAI. The stability increases as well as the computational cost. It is recommended to increase it when the problem has distored elements, is ill-conditioned  or has incompressible materials.",
    )
    prolongation: Literal["UNSMOOTHED", "SMOOTHED", "ENERGY_MINIMIZATION"] | None = Field(
        default="ENERGY_MINIMIZATION",
        description="The algorithm for the prolongation becomes more elaborate from unsmoothed, smoothed to energy-minimization. The stability increases as well as the computational cost. It is recommended to increase it when the problem has small number of BCs and large number of elements",
    )
    improve_test_space: bool | None = Field(
        validation_alias="improveTestSpace",
        serialization_alias="improveTestSpace",
        default=None,
        description="This should be enabled only for very complex/ill-conditioned problems, e.g. highly constrained with many BCs, incompressible/hyperelastic materials.",
    )
    test_space_iterations: int | None = Field(
        validation_alias="testSpaceIterations",
        serialization_alias="testSpaceIterations",
        default=100,
        description="Defaults to 20, can be increased to 50 for complicated cases.",
    )
    preconditioner_recycling: float | None = Field(
        validation_alias="preconditionerRecycling",
        serialization_alias="preconditionerRecycling",
        default=1.0,
        description="Specify the recycling of the preconditioner. This can have a significant impact on the performance. The input is as follows:   Never recycle the preconditioner.0.0 Recycle the preconditioner every second iteration. Recycle the preconditioner more often than the optimal way.== 1.0 recycle the preconditioner in the optimal way.> 1.0 recycle the preconditioner less often than the optimal way.",
    )
    restart_gmres: int | None = Field(
        validation_alias="restartGmres",
        serialization_alias="restartGmres",
        default=50,
        description="Choose after how many iterations the GMRES solver should be restarted.By default, Chronos uses a PCG iterative solution method. Depending on the characteristics of the problem, it might internally switch to GMRES. With GMRES, the iterations become more expensive the more they grow. Therefore, it is restarted if a certain threshold is reached. Default is 50, can be increased to 100 for complicated cases.",
    )
    distributed_matrix_storage: bool | None = Field(
        validation_alias="distributedMatrixStorage",
        serialization_alias="distributedMatrixStorage",
        default=True,
        description="Choose this parameter as true to ensure that the system matrix saving is distributed among the processors of the computation. If multiple cores are used only the relevant part for each core is saved. If it is set to false the whole matrix is saved for each processor. Enabling this can significantly reductions in memory consumption, but introduces numerical instability in rare occasions.",
    )
    num_of_threads: int | None = Field(
        validation_alias="numOfThreads",
        serialization_alias="numOfThreads",
        default=0,
        description="Sets the number of threads for Chronos to be used for shared memory parallelization.The shared memory parallelization of Chronos is independent of the shared memory parallelization of Code_Aster.Ideally, the number of threads multiplied with the number of (MPI) processes (Number of parallel processes under Simulation control) should be set to the number of cores available on the machine.Set it to 0 to automatically choose the best setting.Note that reducing the number of MPI-processes and increasing the number of threads can significantly reduce memory and disk space consumption.",
    )
    verbosity: int | None = Field(
        default=0,
        description="This is a DEVELOPER option to specify the amount of output from Chronos. Its only purpose is debugging. Don't use it for regular runs, as it will slow down the simulation a lot! 0 means no output, 1-3 means more and more output.",
    )
    write_coords_and_matrix: int | None = Field(
        validation_alias="writeCoordsAndMatrix",
        serialization_alias="writeCoordsAndMatrix",
        default=0,
        description="This is a DEVELOPER option to output the coordinates and the matrix to a file. Its only purpose is debugging. Don't use it for regular runs, as it will slow down the simulation a lot! 0 means no output, 1 means to output the latest coords/matrix, and 2 means to output the coords/matrix for every solve (aka every iteration).",
    )
