from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Union

from physics.kinematics.solver_1d import solve_kinematics_1d


app = FastAPI(
    title="Physics Simulator API",
    description="REST API for solving 1D kinematics problems",
    version="1.0.0",
)


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "Physics Simulator API",
        "description": "1D kinematics solver backend",
    }
    

class SolveRequest(BaseModel):
    knowns: Dict[str, float]
    target: str


class SolveResponse(BaseModel):
    result: Union[float, tuple[float, float]]
    equation: str | None = None
    rearranged_equation: str | None = None
    algebra_steps: list[str] = []
    evaluation_steps: list[str] = []


@app.post("/solve/kinematics/1d", response_model=SolveResponse)
def solve_kinematics(request: SolveRequest):
    try:
        solution = solve_kinematics_1d(
            knowns=request.knowns,
            target=request.target,
        )
        return solution
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

