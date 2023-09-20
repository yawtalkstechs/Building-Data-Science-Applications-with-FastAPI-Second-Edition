from pydantic import BaseModel, field_validator


class Model(BaseModel):
    values: list[int]

    @field_validator("values", mode="before")
    def split_string_values(cls, v):
        if isinstance(v, str):
            return v.split(",")
        return v


m = Model(values="1,2,3")
print(m.values)  # [1, 2, 3]
