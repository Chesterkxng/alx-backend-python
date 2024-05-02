#!/usr/bin/env python3
'''Task 10.
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Retrieves the first element  if exists.
    '''
    if lst:
        return lst[0]
    else:
        return None
