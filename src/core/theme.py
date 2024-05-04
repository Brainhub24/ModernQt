class ManageTheme:
    
    __theme = "dark"

    @classmethod
    def change_theme(cls, __value: str) -> None:
        cls.__theme = __value
    
    @classmethod
    def get_theme(cls) -> str:
        return cls.__theme