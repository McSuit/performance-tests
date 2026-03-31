from fastapi import FastAPI, APIRouter, HTTPException, status
from pydantic import BaseModel, RootModel

app = FastAPI()

courses_router = APIRouter(
    prefix="/api/v1/courses",
    tags=["courses-service"]
)


class CourseIn(BaseModel):
    """ Входная модель курса (без id) """
    title: str
    max_score: int
    min_score: int
    description: str


class CourseOut(CourseIn):
    """ Выходная модель курса (с id) """
    id: int


class CoursesStore(RootModel):
    root: list[CourseOut]

    def find(self, course_id: int) -> CourseOut | None:
        """ Поиск курса по ID """
        for course in self.root:
            if course.id == course_id:
                return course
        return None

    def create(self, course: CourseIn) -> CourseOut:
        """ Создание курса с автогенерацией ID """
        new_id = len(self.root) + 1
        new_course = CourseOut(id=new_id, **course.model_dump())
        self.root.append(new_course)
        return new_course

    def update(self, course_id: int, course_in: CourseIn) -> CourseOut | None:
        """ Обновление данных существующего курса """
        for i, course in enumerate(self.root):
            if course.id == course_id:
                updated_course = CourseOut(id=course_id, **course_in.model_dump())
                self.root[i] = updated_course
                return updated_course
        return None

    def delete(self, course_id: int) -> bool:
        """ Удаление курса из списка """
        for i, course in enumerate(self.root):
            if course.id == course_id:
                self.root.pop(i)
                return True
        return False


store = CoursesStore(root=[])


@courses_router.get("", response_model=list[CourseOut])
async def get_courses():
    """ Получение списка всех курсов """
    return store.root


@courses_router.get("/{course_id}", response_model=CourseOut)
async def get_course(course_id: int):
    """ Получение курса по ID или 404 """
    course = store.find(course_id)
    if not course:
        raise HTTPException(
            detail=f"Course with id {course_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )
    return course


@courses_router.post("", response_model=CourseOut, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseIn):
    """ Создание нового курса """
    return store.create(course)


@courses_router.put("/{course_id}", response_model=CourseOut)
async def update_course(course_id: int, course: CourseIn):
    """ Обновление курса или 404 """
    updated = store.update(course_id, course)
    if not updated:
        raise HTTPException(
            detail=f"Course with id {course_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )
    return updated


@courses_router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int):
    """ Удаление курса или 404 """
    if not store.delete(course_id):
        raise HTTPException(
            detail=f"Course with id {course_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )


app.include_router(courses_router)
