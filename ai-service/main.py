# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.agents.assessment_agent import analyze_assessment
from app.agents.student_agent import analyze_student_performance
from app.agents.coordinator_agent import coordinate_criterion3


# ============================================================
# 1. CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="AI Service for NBA Criterion 3",
    description="AI service for Criterion 3 assessment analysis",
    version="1.0.0"
)


# ============================================================
# 2. REQUEST MODEL
# ============================================================

class Criterion3Request(BaseModel):
    """
    Request model for Criterion 3 analysis.

    The data field is optional because the current AI service
    uses the verified Criterion 3 dataset stored in:

        data/criterion3_data.py

    Later, the backend can send verified data through this field
    when backend integration is implemented.
    """

    data: dict = Field(default_factory=dict)


# ============================================================
# 3. HOME ENDPOINT
# ============================================================

@app.get("/")
def home():
    """
    Simple health-check endpoint.
    """

    return {
        "message": "AI Service for NBA Criterion 3 is running",
        "status": "ok"
    }


# ============================================================
# 4. CRITERION 3 ANALYSIS ENDPOINT
# ============================================================

@app.post("/criterion3/analyze")
def analyze_criterion3(request: Criterion3Request):
    """
    Run the complete Criterion 3 AI analysis.

    Flow:

        Verified Criterion 3 Data
                    ↓
            Assessment Agent
                    ↓
             Student Agent
                    ↓
           Coordinator Agent
                    ↓
            Final Analysis
    """

    try:

        # ----------------------------------------------------
        # STEP 1: RUN ASSESSMENT AGENT
        # ----------------------------------------------------

        assessment_result = analyze_assessment()


        # ----------------------------------------------------
        # STEP 2: RUN STUDENT AGENT
        # ----------------------------------------------------

        student_result = analyze_student_performance()


        # ----------------------------------------------------
        # STEP 3: RUN COORDINATOR AGENT
        # ----------------------------------------------------

        final_result = coordinate_criterion3(
            assessment_analysis=assessment_result,
            student_analysis=student_result
        )


        # ----------------------------------------------------
        # STEP 4: RETURN FINAL RESULT
        # ----------------------------------------------------

        return {
            "criterion": "Criterion 3",
            "analysis": final_result
        }


    except KeyError as error:

        raise HTTPException(
            status_code=400,
            detail=f"Missing required Criterion 3 data field: {str(error)}"
        )


    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"AI analysis failed: {str(error)}"
        )