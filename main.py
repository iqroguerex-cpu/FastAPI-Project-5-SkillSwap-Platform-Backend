from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SkillSwap API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SKILLS = [

    {"username": "alex", "can_teach": "python", "wants_to_learn": "spanish"},
    {"username": "maria", "can_teach": "spanish", "wants_to_learn": "python"},
    {"username": "john", "can_teach": "guitar", "wants_to_learn": "web design"},
    {"username": "emma", "can_teach": "web design", "wants_to_learn": "guitar"},
    {"username": "liam", "can_teach": "java", "wants_to_learn": "machine learning"},
    {"username": "olivia", "can_teach": "machine learning", "wants_to_learn": "java"},
    {"username": "noah", "can_teach": "photography", "wants_to_learn": "photoshop"},
    {"username": "ava", "can_teach": "photoshop", "wants_to_learn": "photography"},
    {"username": "william", "can_teach": "excel", "wants_to_learn": "data analysis"},
    {"username": "sophia", "can_teach": "data analysis", "wants_to_learn": "excel"},
    {"username": "james", "can_teach": "c++", "wants_to_learn": "game development"},
    {"username": "isabella", "can_teach": "game development", "wants_to_learn": "c++"},
    {"username": "benjamin", "can_teach": "digital marketing", "wants_to_learn": "seo"},
    {"username": "mia", "can_teach": "seo", "wants_to_learn": "digital marketing"},
    {"username": "lucas", "can_teach": "react", "wants_to_learn": "nodejs"},
    {"username": "amelia", "can_teach": "nodejs", "wants_to_learn": "react"},
    {"username": "henry", "can_teach": "cooking", "wants_to_learn": "baking"},
    {"username": "charlotte", "can_teach": "baking", "wants_to_learn": "cooking"},
    {"username": "daniel", "can_teach": "video editing", "wants_to_learn": "animation"},
    {"username": "harper", "can_teach": "animation", "wants_to_learn": "video editing"},
    {"username": "jack", "can_teach": "cybersecurity", "wants_to_learn": "cloud computing"},
    {"username": "evelyn", "can_teach": "cloud computing", "wants_to_learn": "cybersecurity"},
    {"username": "logan", "can_teach": "statistics", "wants_to_learn": "deep learning"},
    {"username": "abigail", "can_teach": "deep learning", "wants_to_learn": "statistics"},
    {"username": "sebastian", "can_teach": "ui design", "wants_to_learn": "ux research"},
    {"username": "ella", "can_teach": "ux research", "wants_to_learn": "ui design"},
    {"username": "mason", "can_teach": "linux", "wants_to_learn": "docker"},
    {"username": "scarlett", "can_teach": "docker", "wants_to_learn": "linux"},
    {"username": "ethan", "can_teach": "public speaking", "wants_to_learn": "storytelling"},
    {"username": "chloe", "can_teach": "storytelling", "wants_to_learn": "public speaking"}

]


@app.get("/")
async def root():
    return {"message": "SkillSwap API is running"}


@app.get("/skills")
async def show_skills():
    return SKILLS


@app.post("/skills/add")
async def add_skills(skill=Body()):
    SKILLS.append(skill)
    return {"message": "Skill added successfully"}


@app.get("/skills/match")
async def skill_matches():
    matches = []
    for i in range(len(SKILLS)):
        for j in range(i + 1, len(SKILLS)):
            user1 = SKILLS[i]
            user2 = SKILLS[j]
            if (
                user1["can_teach"].casefold() == user2["wants_to_learn"].casefold()
                and
                user1["wants_to_learn"].casefold() == user2["can_teach"].casefold()
            ):
                matches.append({
                    "user1": user1["username"],
                    "user2": user2["username"]
                })

    return matches


@app.get("/skills/search")
async def search_skills(skill: str):

    results = []

    for user in SKILLS:
        if user["can_teach"].casefold() == skill.casefold():
            results.append(user)

    return results


@app.get("/skills/{username}")
async def user_by_username(username: str):

    for user in SKILLS:
        if user["username"].casefold() == username.casefold():
            return user

    return {"message": "User not found"}


@app.put("/skills/update")
async def update_skill(skill=Body()):

    for i in range(len(SKILLS)):

        if SKILLS[i]["username"].casefold() == skill["username"].casefold():
            SKILLS[i] = skill
            return {"message": "User updated successfully"}

    return {"message": "User not found"}


@app.delete("/skills/delete/{username}")
async def delete_user(username: str):

    for i in range(len(SKILLS)):

        if SKILLS[i]["username"].casefold() == username.casefold():
            SKILLS.pop(i)
            return {"message": "User deleted successfully"}

    return {"message": "User not found"}


@app.get("/skills/analytics")
async def skill_analytics():
    skill_count = {}
    for user in SKILLS:
        skill = user["can_teach"]
        if skill in skill_count:
            skill_count[skill] += 1
        else:
            skill_count[skill] = 1

    return skill_count

if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.environ.get("PORT", 8000))

    uvicorn.run("main:app", host="0.0.0.0", port=port)
