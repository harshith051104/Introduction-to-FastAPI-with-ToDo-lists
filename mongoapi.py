from fastapi import FastAPI, APIRouter, HTTPException
from configuration import collection
from database.schemas import all_data
from database.models import Todo
from bson.objectid import ObjectId
from datetime import datetime

app =FastAPI()
router = APIRouter()

@router.get("/")
async def get_all_todos():
    data = collection.find({"is_deleted":False})
    return all_data(data)

@router.post("/")
async def create_task(new_task: Todo):
    try:
        resp = collection.insert_one(dict(new_task))
        return {"status_code":200, "id":str(resp.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"some error occured {e}")
    
@router.put("/{task_id}")

async def update_task(task_id:str, updated_task:Todo):
    try:
        id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id":id, "is_deleted":False})
        if not existing_doc:
            return HTTPException(status_code=404, details="Task doesnt exists")
        updated_task.updated_at = datetime.timestamp(datetime.now())
        resp = collection.update_one({"_id":id}, {"$set":dict(updated_task)})
        return {"status_code":200, "message": "Task Updated Successfully"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"some error occured {e}")

@router.delete("/{task_id}")
async def delete_task(task_id:str):
    try:
        id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id":id, "is_deleted":False})
        if not existing_doc:
            return HTTPException(status_code=404, detail=f"Task does not exits")
        resp = collection.update_one({"_id":id}, {"$set":{"is_deleted":True}})
        return {"status_code":200, "message": "Task Deleted Successfully"}
 
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")
app.include_router(router)