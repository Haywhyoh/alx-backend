def index_range(page: int, page_size: int) -> tuple:
    last_index = page_size * page
    first_index = last_index - page_size
    return (first_index, last_index)
