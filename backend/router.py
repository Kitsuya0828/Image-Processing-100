from fastapi import File, UploadFile, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile

import routers


def process_image(fileb, func):
    try:
        suffix = Path(fileb.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(fileb.file, tmp)
            result: dict = func(tmp.name)
            result["status"] = 1
    except Exception as e:
        result = {
            "status": 0,
            "message": e
        }
    finally:
        fileb.file.close()
    return jsonable_encoder(result)


router = APIRouter()


@router.post("/solve/q1", tags=["solve"])
async def solve_q1(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q1)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q2", tags=["solve"])
async def solve_q2(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q2)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q3", tags=["solve"])
async def solve_q3(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q3)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q4", tags=["solve"])
async def solve_q4(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q4)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q5", tags=["solve"])
async def solve_q5(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q5)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q6", tags=["solve"])
async def solve_q6(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q6)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q7", tags=["solve"])
async def solve_q7(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q7)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q8", tags=["solve"])
async def solve_q8(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q8)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q9", tags=["solve"])
async def solve_q9(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q9)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q10", tags=["solve"])
async def solve_q10(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q10)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q11", tags=["solve"])
async def solve_q11(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q11)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q12", tags=["solve"])
async def solve_q12(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q12)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q13", tags=["solve"])
async def solve_q13(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q13)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q14", tags=["solve"])
async def solve_q14(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q14)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q15", tags=["solve"])
async def solve_q15(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q15)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q16", tags=["solve"])
async def solve_q16(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q16)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q17", tags=["solve"])
async def solve_q17(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q17)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q18", tags=["solve"])
async def solve_q18(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q18)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q19", tags=["solve"])
async def solve_q19(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q19)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q20", tags=["solve"])
async def solve_q20(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q20)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q21", tags=["solve"])
async def solve_q21(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q21)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q22", tags=["solve"])
async def solve_q22(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q22)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q23", tags=["solve"])
async def solve_q23(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q23)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q24", tags=["solve"])
async def solve_q24(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q24)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q25", tags=["solve"])
async def solve_q25(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q25)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q26", tags=["solve"])
async def solve_q26(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q26)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q27", tags=["solve"])
async def solve_q27(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q27)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q28", tags=["solve"])
async def solve_q28(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q28)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q29", tags=["solve"])
async def solve_q29(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q29)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q30", tags=["solve"])
async def solve_q30(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q30)
    return JSONResponse(content=json_compatible_results)