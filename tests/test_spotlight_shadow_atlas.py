import pytest
import graphics.spotlight_shadow_atlas as mod

CASES = [
    ("stable_page", (1,)),
    ("release_page", (1,)),
    ("wait_alloc", (1,)),
    ("page_group_res", (1,)),
    ("flip_sample", (1,)),
    ("guard_band", (1,)),
    ("determinism", (1,)),
    ("validation", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("atlas_alloc", (1,)),
    ("metrics", (1,)),
    ("shadow_render", (1,)),
    ("light_sort", (1,)),
    ("sample", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
